#!/usr/bin/env
# -*- coding: utf-8 -*-

import os
import pandas as pd
import openpyxl as opx

print ("** " + os.path.basename(__file__) + " **")

outpath = "time_analysis.xlsx"
writer  = pd.ExcelWriter(outpath)

drop_path = "C:/Users/itaken322/Dropbox/Inbox/Experiment/Joint Action_Ladder/Analyze_R/time_analysis.xlsx"
# ログファイルの読み込み
log_list = os.listdir("Log_files/")

# 元ファイルの読み込み
base    = pd.ExcelFile("time_analysis.xlsx")
df_base = base.parse('time')

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
    print ("Full Output")
    write_list = log_list

if len(write_list) > 0:
    print ("Run Process")
    time_set = pd.DataFrame()
    for wt in write_list:
        if "demo" not in wt:
            ID = wt[0:6]  # ID名を取得
            print ("Begin  " + ID)
            wt = "Log_files/" + wt

            df = pd.read_csv(wt)
            df = df.dropna(axis=0, how='all')  # 欠損値を削除

            id_len  = df["trial_Num"].count()  # 列数をカウント
            ID_colm = [ID for id in range(0, id_len)]  # 列数分のIDのリストを作成（リスト内包表記）

            df["ID"] = ID_colm  # データフレームに追加

            df = df[df["step"] > 2]
            df = df[df["step"] < 43]
            time_set = pd.concat([time_set, df], ignore_index=True)  # indexを無視してデータフレームを合体
            print ("End  " + ID)
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

    print("Completed!")

else:
    print("No new file")