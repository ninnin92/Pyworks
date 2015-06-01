#!/usr/bin/env python3
#coding:utf-8

from turtle import *

# 角度に従って曲がる
curve = [10, 160, 10, 20]
speed("fastest")

for i in range(40):  # 40回繰り返す
    forward(100)  # 100進む
    degree = curve[i % len(curve)]
    right(degree)  # リストに従って曲がる

input()
