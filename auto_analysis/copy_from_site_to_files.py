#!/usr/bin/env
# -*- coding: utf-8 -*-

import os
import shutil as sh

print("** " + os.path.basename(__file__) + " **")

# 移動元・移動先のパス
from_path = "C://Users//itaken322//Documents//Experiment//Joint Action_Ladder//Data//Log_site"
to_path   = "C://Users//itaken322//Documents//Experiment//Joint Action_Ladder//Data//Log_files"

# 除外リスト
ignore = ["H27-13", "H27-33", "H27-34"]

# 差分作成の準備 + 除外リストに該当するファイルを除去
from_list = [x for x in os.listdir(from_path) if "H27" in x]
from_list = {x for x in from_list for y in ignore if y not in x}
to_list   = set(os.listdir(to_path))

# 両フォルダの差分作成
copy_list = list(from_list.difference(to_list))

# backup処理
if len(copy_list) > 0:
    print(copy_list)
    print("backup running")
    for cp in copy_list:
        from_copy = from_path + "//" + cp
        sh.copy2(from_copy, to_path)
    print("Complete!!")
else:
    print("No new file")
    pass
