#!/usr/bin/env
# -*- coding: utf-8 -*-

import os
import pandas as pd

outpath = "Log/time-analysis_py.xlsx"
writer = pd.ExcelWriter(outpath)
time_set = pd.DataFrame()

data_list = os.listdir("data/")
for dt in data_list:

    ID = dt[0:6]  # ID名を取得
    dt = "data/" + dt

    df = pd.read_csv(dt)
    df = df.dropna(axis=0, how='all')  # 欠損値を削除

    id_len = df["trial_Num"].count()  # 列数をカウント
    ID_colm = [ID for id in range(0, id_len)]  # 列数分のIDのリストを作成（リスト内包表記）

    df["ID"] = ID_colm  # データフレームに追加

    df = df[df["step"] > 2]
    df = df[df["step"] < 43]
    time_set = pd.concat([time_set, df], ignore_index=True)  # indexを無視してデータフレームを合体

time_set = time_set.dropna(axis=1, how='all')  # 空の列を削除

time_set.to_excel(writer, "time")
writer.save()  # エクセルに書き込み
print("Completed!")
