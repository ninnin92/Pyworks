#!/usr/bin/env
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
import itertools as it
# import openpyxl as opx
# import xlsxwriter as xw

print("** " + os.path.basename(__file__) + " **")

# データ入力設定
############################################################
# 新しくサマリーを作る必要のあるIDを抽出
log  = os.listdir("Log_files/")
data = os.listdir("data_files/")

# set内包表記 { } = 内包表記 + setで返してくれる
ID_log  = {id_l[0:6] for id_l in log}
ID_data = {id_d[0:6] for id_d in data}
# 新しいIDを探して、リストを作成
new_ID = list(ID_log.difference(ID_data))
###########################################################

# 自作関数
############################################################


def overlap(ls):  # 重複する要素を検出する関数(リスト)
    r = []
    for x in ls:
        if x not in r:
            r.append(x)
    return r


def press(C, series):  # LとRのターン数を分類する関数（左右、Series）
    # 分類を決めておく
    L_list = ["0.L", "1.XL", "2.XLR", "3.XRL"]
    R_list = ["2.XLR", "3.XRL", "4.XR", "5.R"]

    turns_list = []

    # 引数で渡されるSeriesから分類コードと一致するものを別リストに
    if C == "L":
        for e in L_list:
            if e in series:
                turns_list.append(series[e])
            else:
                pass
    elif C == "R":
        for e in R_list:
            if e in series:
                turns_list.append(series[e])
            else:
                pass

    return sum(turns_list)


def errors(series):  # エラーのSeriesから、エラー数とエラーしたStepのリストを返す関数
    errors_list = []
    for i in series:
        errors_list.append(i)
    else:
        pass

    errors_len = len(errors_list)  # エラー数をカウント
    exclude_list = list(set(errors_list))  # 重複を除外（順番は無視される）

    return(errors_len, exclude_list)


def exclude(df, series):  # エラーした次のStepを除外する関数
    for n in series:
        df = df[df.step != n + 1]  # データフレームから該当Stepを除外→更新を1つずつやる
    else:
        pass

    return(df)

# 分析
############################################################

if len(new_ID) > 0:
    print("Run Process")
    for ID in new_ID:
        print("Now  " + ID)
        # IDに該当する実験ログファイルを取得
        do_list = []
        file_list = os.listdir("Log_files/")

        fl = next(filter(lambda x: "demo" in x and ID in x, file_list), None)  # ラムダ式というらしい forの代わりになる
        do_list.append(fl)
        fl = next(filter(lambda x: "practice" in x and ID in x, file_list), None)
        do_list.append(fl)

        for fl in file_list:
                if ID in fl and "practice" not in fl and "demo" not in fl:
                    do_list.append(fl)

        # データ出力の準備
        outpath = "data_files/" + ID + "_py.xlsx"
        writer = pd.ExcelWriter(outpath)
        R_set = pd.DataFrame()

        for do in do_list:  # データリストから1つ選択
            do = "Log_files/" + do  # フォルダの指定
            data_base = pd.read_csv(do)  # ベースのデータフレームを作成
            data_base = data_base.dropna(axis=0, how='all')  # 欠損値の削除

            # 条件分岐のために、実験名、試行数を獲得
            exp = str(data_base["exp"][0])
            trialN = overlap(list(data_base["trial_Num"]))  # 試行数を獲得
            df_set = pd.DataFrame()

            for tN in trialN:   # 各試行ずつ分析
                data = data_base[data_base["trial_Num"] == tN]  # 各試行でデータフレームを作成

                # first turn & first pushを検出
                first_turn = data.head(1)["turn"].item()
                first_push = data.head(1)["category"].item()
                if first_push in ["0.L", "1.XL", "2.XLR", "3.XRL"]:
                    first_push = 1  # 1ならL
                elif first_push in ["2.XLR", "3.XRL", "4.XR", "5.R"]:
                    first_push = -1  # -1ならR

                # step 0-2を除外
                data = data[data["step"] > 2]

                # 遂行時間の抽出
                time = data[data["step"] == 42]
                time = time["All_Time"].min()

                # ターン数を数える

                # 各カテゴリーの数をSeriesで抽出
                count_data = data["category"].value_counts()
                # LとRでそれぞれターン数をカウント
                L_press = press("L", count_data)
                R_press = press("R", count_data)

                # エラー数のカウント、及びエラーの次の試行を除外する準備

                # LとRそれぞれのエラーのみのデータフレーム作成
                L_df = data[(data["category"] == "1.XL") | (data["category"] == "2.XLR")]
                R_df = data[(data["category"] == "3.XRL") | (data["category"] == "4.XR")]

                # エラーをしたStepをSeriesで抽出
                Le_data = L_df["step"]
                Re_data = R_df["step"]

                # エラー数と除外リストをそれぞれ返す
                L_errors, R_exd_list = errors(Le_data)
                R_errors, L_exd_list = errors(Re_data)

                # ターンエラーの算出
                L_turn_error = len(R_exd_list)
                R_turn_error = len(L_exd_list)

                # COVを計算する

                # LとRの成功試行を抽出
                Lt_df = data[data["category"] == "0.L"]
                Rt_df = data[data["category"] == "5.R"]

                # エラーの次の試行を除外
                Lt_df = exclude(Lt_df, L_exd_list)
                Rt_df = exclude(Rt_df, R_exd_list)

                # Timeのみのデータフレームに
                L_time_df = Lt_df["Time"]
                R_time_df = Rt_df["Time"]

                # それぞれの統計量計算
                L_interval = L_time_df.mean()
                L_SD       = L_time_df.std()
                L_SE       = L_SD / np.sqrt(L_time_df.count())
                L_COV      = L_SD / L_interval

                R_interval = R_time_df.mean()
                R_SD       = R_time_df.std()
                R_SE       = R_SD / np.sqrt(R_time_df.count())
                R_COV      = R_SD / R_interval

                # R用にデータを用意
                if exp == "prac":
                    t_num     = 0
                    condition = "P"

                elif exp == "indivi":
                    t_num     = tN
                    condition = "I"

                elif exp == "joint":
                    t_num     = tN
                    condition = "J"

                elif exp == "demo":
                    t_num     = 0
                    condition = "d"

                # Summaryの作成
                if exp == "prac" or exp == "joint":
                    summary = pd.DataFrame({"exp": [exp] * 8,
                                            "trialN": [tN] * 8,
                                            "Parent": [time, L_press, L_errors, L_turn_error, L_interval, L_SD, L_SE, L_COV],
                                            "Child": [time, R_press, R_errors, R_turn_error, R_interval, R_SD, R_SE, R_COV]},
                                            index=["Time", "Press", "Error", "Turn_Error", "interval", "SD", "SE", "COV"]
                                           )
                else:
                    summary = pd.DataFrame({"exp": [exp] * 8,
                                            "trialN": [tN] * 8,
                                            "Left": [time, L_press, L_errors, L_turn_error, L_interval, L_SD, L_SE, L_COV],
                                            "Right": [time, R_press, R_errors, R_turn_error, R_interval, R_SD, R_SE, R_COV]},
                                            index=["Time", "Press", "Error", "Turn_Error", "interval", "SD", "SE", "COV"]
                                           )

                R_sum = pd.DataFrame({"trial": [t_num], "C": [condition], "time": [time],
                                      "p": [R_press], "error": [R_errors], "turn_error": [R_turn_error], "interval": [R_interval],
                                      "COV": [R_COV], "p_L": [L_press], "error_L": [L_errors], "turn_error_L": [L_turn_error],
                                      "interval_L": [L_interval], "COV_L": [L_COV], "first_turn": [first_turn],
                                      "first_push": [first_push]}, index=[ID],
                                      columns=["trial", "C", "time", "p", "error", "turn_error", "COV", "interval",
                                               "p_L", "error_L", "turn_error_L", "COV_L", "interval_L", "first_turn", "first_push"])

                df_set = pd.concat([df_set, summary])
                R_set = pd.concat([R_set, R_sum])

            else:  # すべて試行を解析したら
                df_set.to_excel(writer, exp)

        else:
            R_set.to_excel(writer, "R")
            writer.save()  # エクセルに書き込み
            print("End  " + ID)

    else:
        print("Exit Process")

else:  # 新しいIDがなかった時
    print("No new ID")
