#!/usr/bin/env
# -*- coding: utf-8 -*-

import os
import pandas as pd
import openpyxl as opx

print("** " + os.path.basename(__file__) + " **")

outpath = "time_analysis_Adult.xlsx"
writer  = pd.ExcelWriter(outpath)

drop_path = "C://Users//itaken322//Dropbox//Inbox//Experiment//Joint Action_Ladder//Analyze_R//time_analysis_Adult.xlsx"
# ログファイルの読み込み
log_list = os.listdir("Log_files/")

# 参加者情報ファイル
sub_path = "C://Users//itaken322//Documents//Experiment//Joint Action_Ladder//Participant//subject_ladder.csv"

subject = pd.read_csv(sub_path)
subject.drop(subject.columns[[2, 4, 5]], axis=1, inplace=True)  # いらない行の削除


# 元ファイルの読み込み
base    = pd.ExcelFile("time_analysis_Adult.xlsx")
df_base = base.parse('time', index_col="s")

try:
    ID_list    = set(df_base["ID"].tolist())  # メインファイルのIDリストを獲得して、重複削除
    write_list = []

    for lg in log_list:
        ID_name = lg[0:6]  # ファイル名からIDを獲得
        if ID_name not in ID_list:  # メインファイルにまだ記載されていないファイルをリストに追加
            write_list.append(lg)
        else:
            pass

except KeyError:
    print("Full Output")
    write_list = log_list

if len(write_list) > 0:
    print("Run Process")
    time_set = pd.DataFrame()
    for wt in write_list:
        if "demo" in wt:
            ID = wt[0:6]  # ID名を取得
            print("Begin  " + ID)
            sub_ID = subject[subject["s"] == ID]  # 参加者情報
            wt = "Log_files/" + wt

            df = pd.read_csv(wt)
            df = df.dropna(axis=0, how='all')  # 欠損値を削除

            id_len  = df["trial_Num"].count()  # 列数をカウント
            ID_colm = [ID for id in range(0, id_len)]  # 列数分のIDのリストを作成（リスト内包表記）

            df["ID"] = ID_colm  # データフレームに追加

            df = df[df["step"] > 0]
            df = df[df["step"] < 43]
            df = df.assign(sex=sub_ID["M/F"].item(), age=sub_ID["age_days"].item())
            time_set = pd.concat([time_set, df], ignore_index=True)  # indexを無視してデータフレームを合体
            print("End  " + ID)
        else:
            pass

    time_set = time_set.dropna(axis=1, how='all')  # 空の列を削除
    time_set = pd.concat([df_base, time_set], ignore_index=True)

    time_set.to_excel(writer, "time")
    writer.save()  # エクセルに書き込み

    # 後処理
    editsheetname = "time"
    book = opx.load_workbook(outpath)
    ws   = book.worksheets[book.get_sheet_names().index(editsheetname)]
    ws["A1"].value = "s"
    book.save(outpath)
    book.save(drop_path)

    print("Exit Process")

else:
    print("No new file")
