#!/usr/bin/env python
# coding:utf-8
# env: Python2.7

import sys
import git
import pandas as pd

if sys.platform == "win32":
    ref_path = "C:\\Users\\itaken322\\Dropbox\\Inbox\\Python\\test_repo"
else:
    ref_path = "hogehoge"

g = git.Git(ref_path)
commit = g.log("--date=short", "--pretty=format:%ad,%s").encode('utf_8')

print(commit)

fp = open("commit_ref.csv", "w")
fp.write(commit)
fp.close
