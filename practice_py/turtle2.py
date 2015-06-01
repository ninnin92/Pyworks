#!/usr/bin/env python3
#coding:utf-8

from turtle import *

degree = 1  # 角度の初期値
distance = 50  # 距離の初期値

for i in range(40):  # 40回繰り返す
    forward(distance)  # distance分進む
    right(degree)  # degree分右に曲がる
    degree += 2  # 角度に2を足す
    distance -= 1  # 距離から1を引く

input()
