#!/usr/bin/env
# -*- coding: utf-8 -*-

import os
import shutil as sh

print ("** " + os.path.basename(__file__) + " **")

itaken_pc_path = "C://Users//itaken322//Documents//Experiment//Joint Action_Ladder//Data//Log_files"
dropbox_path   = "C://Users//itaken322//Dropbox//Inbox//Experiment//Joint Action_Ladder//Log_files"

############################################################
# ログファイルのバックアップ
############################################################

# 院生室のパソコンとdropboxフォルダの中身の確認
# set：重複なし、順序なしの集合、集合演算に使用する
itaken_pc_set = set(os.listdir(itaken_pc_path))
dropbox_set   = set(os.listdir(dropbox_path))

# 差集合を取ってリストにする ＝ 院生室のパソコンにあってdropboxにないものをリストに
new_files = list(itaken_pc_set.difference(dropbox_set))

# backup処理
if len(new_files) > 0:
    print(new_files)
    print("backup running")
    for fl in new_files:
        base_copy = itaken_pc_path + "//" + fl
        sh.copy2(base_copy, dropbox_path)
    print("Complete!!")
else:
    print ("No new file")
    pass
