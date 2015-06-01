#!/usr/bin/env python3
#coding:utf-8

from turtle import *

speed("fastest")

for i in range(40):  # 40回繰り返す
    forward(100)  # 100進む
    if i % 4 == 1:
        right(120)
    elif i % 4 == 3:
        right(40)
    else:
        right(20)

input()
