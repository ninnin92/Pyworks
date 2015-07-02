#!/usr/bin/env python
# coding:utf-8
# env: Python2.7

import sys
import git
import pandas as pd

if sys.platform == "win32":
    ref_path = "C:\Users\itaken322\Documents\Reserch\Rstudio"
else:
    ref_path = "hogehoge"

g = git.Git(ref_path)
commit = g.log("--date=short", "--pretty=format:%ad,%s").encode('utf_8')

data = []
commit = commit.split(",")
print(commit[0])
for i in range(0, 100, 2):
    try:
        data.append([commit[i], commit[i + 1]])
    except IndexError:
        break

print(data)

fp = open("commit_ref.csv", "w")
for x in data:
    fp.write("%s, %s\n" % tuple(x))
fp.close
