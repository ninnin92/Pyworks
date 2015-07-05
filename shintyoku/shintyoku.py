#!/usr/bin/env python
# coding:utf-8
# env: Python2.7

import sys
import git

#OSでPathを変更する
if sys.platform == "win32":
    ref_path = "C:\\Users\\itaken322\\Dropbox\\Inbox\\Python\\test_repo"
else:
    ref_path = "/Users/Furuhata/Dropbox/Inbox/Python/test_repo"

g = git.Git(ref_path)  # ローカルリポジトリを指定
commit = g.log("--date=short", "--pretty=format:%ad,%s")  # コミットログを取得
# オプションは元々のGitコマンドに由来、ログのフォーマットを指定している

print(commit)

# ログをCSVに
fp = open("commit_ref.csv", "w")
fp.write(commit)
fp.close