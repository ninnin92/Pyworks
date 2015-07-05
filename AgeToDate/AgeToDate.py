#!/usr/bin/env python
# coding:utf-8
# env: Python3.3
# python2系でも動くように調整済み

import sys
import calendar as cal
from datetime import date, timedelta, datetime

################################################
#  宣言
################################################

continue_roop = True

################################################
#  処理関数
################################################


def key_input(text=None):
    if text is None:
        if sys.version_info.major > 2:  # 3系かどうかの判定
            return input()
        else:
            return raw_input()  # python2ではraw_input
    else:
        if sys.version_info.major > 2:  # 3系かどうかの判定
            return input(text)
        else:
            return raw_input(text)  # python2ではraw_input


# モードの切替 [1] 年齢と調査日から対象の子の誕生日を推定 [2] 年齢と誕生日から調査日を推定
def mode_change():
    mode = key_input("Please enter mode number: [1] age to birthday  [2] age to date  ")
    return int(mode)


# 誕生日を入力させる
def get_age():
    while True:
        try:
            age1 = key_input('Please enter age1 (e.g. 1-1-1 = 1years 1months 1days)  ')
            age1 = age1.split("-")
            years1, months1, days1 = age1[0], age1[1], age1[2]
            print("Age1:  " + years1 + " years " + months1 + " months " + days1 + " days")
            break
        except (ValueError, IndexError):
            print("Error Age1: Please one more!!")

    while True:
        try:
            age2 = key_input('Please enter age2 (e.g. 1-1-1 = 1years 1months 1days)  ')
            age2 = age2.split("-")
            years2, months2, days2 = age2[0], age2[1], age2[2]
            op_period = True
            print("Age2:  " + years2 + " years " + months2 + " months " + days2 + " days")
            break

        except (IndexError):
            age2 = [0, 0, 0]
            op_period = False
            break

        except (ValueError):
            print("Error Age2: Please one more!!")

    print("Set age period  :" + str(age1) + "  ~  "  + str(age2))
    return age1, age2, op_period


def get_birthday():
    while True:
        try:
            bd = key_input('Please enter ones birthday (e.g. 2015/06/04)  ')
            bd = datetime.strptime(bd, "%Y/%m/%d")
            birthday = date(bd.year, bd.month, bd.day)
            break
        except ValueError:
            print("Error: Please one more!!")

    print("Birthday:  " + str(birthday))
    return birthday


def set_date():
    while True:
        try:
            bdate = key_input('Please enter research date(e.g. 2015/07/04)  ')
            bdate = datetime.strptime(bdate, "%Y/%m/%d")
            base_date = date(bdate.year, bdate.month, bdate.day)
            break
        except ValueError:
            base_date = date.today()
            break
    print("Reserch date:  " + str(base_date))
    return base_date


def calc_birthday(age, base):
    set_years = base.year - int(age[0])
    set_months = base.month - int(age[1])
    set_days = int(age[2])

    try:
        bd = base.replace(year=set_years, month=set_months)
        bd -= timedelta(days=set_days)
    except ValueError:
        bd = base.replace(year=set_years, month=set_months,
                          day=cal.monthrange(set_years, set_months)[1])
        bd += timedelta(days=base.day - bd.day)
        bd -= timedelta(days=set_days)
    bd = date(bd.year, bd.month, bd.day)
    return bd


def calc_date(age, bd):
    set_years = bd.year + int(age[0])
    set_months = bd.month + int(age[1])
    set_days = int(age[2])

    try:
        d = bd.replace(year=set_years, month=set_months)
        d += timedelta(days=set_days)
    except ValueError:
        d = bd.replace(year=set_years, month=set_months,
                       day=cal.monthrange(set_years, set_months)[1])
        d += timedelta(days=bd.day - d.day)
        d += timedelta(days=set_days)
    d = date(d.year, d.month, d.day)
    return d



################################################
#  メイン処理
################################################


if __name__ == '__main__':
    while continue_roop:
        mode = mode_change()
        if mode == 1:
            age1, age2, op_period = get_age()
            base_date = set_date()
            if op_period:
                bd1 = calc_birthday(age1, base_date)
                bd2 = calc_birthday(age2, base_date)
                print("Birthday period: " + str(bd2) + "  ~  " + str(bd1))
            else:
                bd = calc_birthday(age1, base_date)
                print("Birthday:  " + str(bd))

        elif mode == 2:
            age1, age2, op_period = get_age()
            bd = get_birthday()

            if op_period:
                d1 = calc_date(age1, bd)
                d2 = calc_date(age2, bd)
                print("Reserch period: " + str(d1) + "  ~  " + str(d2))
            else:
                d = calc_birthday(age1, base_date)
                print("Reserch date:  " + str(d))

        else:
            break

        # 処理のポーズ（y/nでループ続行 or プログラム終了）
        exit = key_input("Continue? Please input y/n (yes or no)   ")
        if exit == "y":
            continue
        else:
            break
