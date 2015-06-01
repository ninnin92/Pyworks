#!/usr/bin/env python3
#coding:utf-8

from turtle import *

while True:
    forward(300)
    left(130)
    if abs(pos()) < 1:  # カーソルが中心に戻ってきたら
        break

input()
