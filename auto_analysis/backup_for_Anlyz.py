#!/usr/bin/env
# -*- coding: utf-8 -*-

import os
import datetime as dt
import shutil as sh

print ("** " + os.path.basename(__file__) + " **")

backup_path = "C://Users//itaken322//Documents//Experiment//Joint Action_Ladder//Data//Summary//"

############################################################
# サマリーファイルのバックアップ
############################################################

today = dt.datetime.today()
today = today.strftime("%Y%m%d")

# backup処理
print("backup running")

joint_backup         = backup_path + today + "_joint.xlsx"
joint_adult_backup   = backup_path + today + "_joint_adult.xlsx"
time_analysis_backup = backup_path + today + "_time_analysis.xlsx"

sh.copy2("joint.xlsx", joint_backup)
sh.copy2("joint_adult.xlsx", joint_adult_backup)
sh.copy2("time_analysis.xlsx", time_analysis_backup)

print("Complete!!")