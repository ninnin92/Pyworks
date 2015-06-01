#!/usr/bin/env python3
#coding:utf-8

year = int(input("西暦:"))  # キーボードから西暦を入力

if year == 1868:  # 明治元年かどうか
    print("明治元年")
elif year < 1912:  # 明治かどうか
    print("明治", year-1867, "年")

elif year == 1912:  # 大正元年かどうか
    print("大正元年")
elif year < 1926:  # 大正かどうか
    print("大正", year-1911, "年")

elif year == 1926:  # 昭和元年かどうか
    print("昭和元年")
elif year < 1989:  # 昭和かどうか
    print("昭和", year-1925, "年")

elif year == 1989:  # 平成元年かどうか
    print("平成元年")
else:
    print("平成", year-1988, "年")

input()
