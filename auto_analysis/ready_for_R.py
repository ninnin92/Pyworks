#!/usr/bin/env
# -*- coding: utf-8 -*-

import os
import pandas as pd
import openpyxl as opx

print("** " + os.path.basename(__file__) + " **")

############################################################
# 出力先
############################################################

main_outpath = "joint.xlsx"
demo_outpath = "joint_adult.xlsx"
main_writer = pd.ExcelWriter(main_outpath)
demo_writer = pd.ExcelWriter(demo_outpath)

drop_path = "C://Users//itaken322//Dropbox//Inbox//Experiment//Joint Action_Ladder//Analyze_R"
drop_main = drop_path + "/joint.xlsx"
drop_demo = drop_path + "/joint_adult.xlsx"

############################################################
# 各ファイルの読み込み
############################################################

# メインファイル
baseM_path = "joint.xlsx"
baseM_data = pd.ExcelFile(baseM_path)
df_baseM = baseM_data.parse('Sheet1', index_col="s")

# デモ試行（成人）用ファイル
baseD_path = "joint_adult.xlsx"
baseD_data = pd.ExcelFile(baseD_path)
df_baseD = baseD_data.parse('Sheet1', index_col="s")

# 参加者情報ファイル
sub_path = "C://Users//itaken322//Documents//Experiment//Joint Action_Ladder//Participant//subject_ladder.csv"

subject = pd.read_csv(sub_path)
subject.drop(subject.columns[[2, 4, 5]], axis=1, inplace=True)  # いらない行の削除

# サマリーファイル
data_list = os.listdir("data_files/")

############################################################
# メイン処理
############################################################

# 追加すべきファイルがあるか？
try:
    ID_list = set(df_baseM.index.tolist())  # メインファイルのIDリストを獲得して、重複削除
    write_list = []

    for dt in data_list:
        ID_name = dt[0:6]  # ファイル名からIDを獲得
        if ID_name not in ID_list:  # メインファイルにまだ記載されていないファイルをリストに追加
            write_list.append(dt)
        else:
            pass
except KeyError:
    print("Full Output")
    write_list = data_list

# データフレームの加工
if len(write_list) > 0:  # メインファイルにまだ記載されていないファイルはある？
    print("Run Process")
    for wt in write_list:
        ID_Num = wt[0:6]  # ファイル名からIDを獲得
        print("Begin  " + ID_Num)
        wt = "data_files/" + wt

        # ログファイルからサマリーのDFを作成
        Summary = pd.ExcelFile(wt)
        df_sum = Summary.parse('R')

        # 該当IDの参加者情報を獲得
        sub_ID = subject[subject["s"] == ID_Num]
        # 該当IDの参加者情報からDFを作成
        df_sub = pd.DataFrame({"sex": [sub_ID["M/F"].item()] * 10,
                               "age": [sub_ID["age_days"].item()] * 10,
                               "cb": [sub_ID["cb"].item()] * 10},
                               columns=["sex", "age", "cb"],
                               index=[sub_ID["s"].item()] * 10)

        # ログDFと参加者情報DFを結合
        df_sum = pd.concat([df_sub, df_sum], axis=1)

        # デモとメインにDFを分割
        df_demo = df_sum[df_sum["C"] == "d"]
        df_main = df_sum[df_sum["C"] != "d"]

        # メインの結合
        df_baseM = pd.concat([df_baseM, df_main])
        del df_baseM.index.name  # indexの列名を削除

        # デモの結合
        df_baseD = pd.concat([df_baseD, df_demo])
        del df_baseD.index.name  # indexの列名を削除

        print("End  " + ID_Num)

    # 書き込み
    df_baseM.to_excel(main_writer, "Sheet1", index_label=None)
    df_baseD.to_excel(demo_writer, "Sheet1", index_label=None)

    # セーブ
    main_writer.save()
    demo_writer.save()

    # バックアップとコピー
    print("complete write")

    # 後処理 先頭行がないとRがエラー出すので入力
    editsheetname = "Sheet1"
    book1 = opx.load_workbook(main_outpath)
    ws1 = book1.worksheets[book1.get_sheet_names().index(editsheetname)]
    book2 = opx.load_workbook(demo_outpath)
    ws2 = book2.worksheets[book2.get_sheet_names().index(editsheetname)]

    ws1["A1"].value = "s"
    ws2["A1"].value = "s"

    book1.save(main_outpath)
    book1.save(drop_main)
    book2.save(demo_outpath)
    book2.save(drop_demo)

    print("Exit process")

else:
    print("No add files")  # 何もない時
