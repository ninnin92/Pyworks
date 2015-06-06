#!/usr/bin/env python
# coding:utf-8
# env: Python3.3
# python2系でも動くように調整済み

import sys
from datetime import date, timedelta, datetime


# 誕生日を入力させる
def get_birthday():
    # 入力待ち(exceptでPython2系にも対応)
    if sys.version_info.major > 2:  # 3系かどうかの判定
            bday = input('Please enter your birthday (e.g. 2015/06/04)  ')
    else:
            def input(text):
                return raw_input(text)  # python2ではraw_input
            bday = input('Please enter your birthday (e.g. 2015/06/04)  ')
    return bday


# 年齢の計算（閏日補正含む） ：今何歳何ヶ月なのか？
def count_years(b, t):
    try:
        this_year = b.replace(year=t.year)
    except ValueError:
        b += timedelta(days=1)
        this_year = b.replace(year=t.year)

    age = t.year - b.year
    if today < this_year:
        age -= 1

# 何歳”何ヶ月”を計算
    if (t.day - b.day) >= 0:
        year_months = (t.year - b.year)*12 - age*12 + (t.month - b.month)
    else:
        year_months = (t.year - b.year)*12 - age*12 + (t.month - b.month) - 1  # 誕生日が来るまでは月齢も-1

    return age, year_months


# 月齢の計算
def count_months(b, t):
    if (t.day - b.day) >= 0:
        months = (t.year - b.year)*12 + (t.month - b.month)
    else:
        months = (t.year - b.year)*12 + (t.month - b.month) - 1  # 誕生日が来るまでは月齢も-1
    return months


# 月齢および何歳何ヶ月の余り日数（何歳何ヶ月”何日”）
def count_days(b, t):
    if (t.day - b.day) >= 0:
        days = t.day - b.day
    else:
        before = t.replace(month=t.month-1, day=b.day)
        days = (t - before).days
    return days

if __name__ == '__main__':
    # 日付設定(今日)
    today = date.today()

    # 誕生日を入力させて、datetime型に変換（例外処理つき）
    while True:
        try:
            bd = get_birthday()
            bd = datetime.strptime(bd, "%Y/%m/%d")
            break
        except ValueError:
            print ("Error: Please one more!!")
    your_birthday = bd.strftime('%Y/%m/%d')
    birthday = date(bd.year, bd.month, bd.day)

    # 年齢を表示
    age = str(count_years(birthday, today)[0])
    age_year_months = str(count_years(birthday, today)[1])
    age_days = str(count_days(birthday, today))
    age_months = str(count_months(birthday, today))
    age_in_days = str((today - birthday).days)

    age_details = age + "years " + age_year_months + "months " + age_days + "days"

    print ("********************************************")  # python2では()なし
    print ("Your birthday  " + your_birthday)
    print ("Age  " + age)
    print ("Age_months  " + age_months)
    print ("Age_in_days  " + age_in_days)
    print ("Age_details  " + age_details)
    print ("********************************************")

# 処理のポーズ（何かしらの入力でプログラム終了）
    if sys.version_info.major > 2:
        input()
    else:
        raw_input()
