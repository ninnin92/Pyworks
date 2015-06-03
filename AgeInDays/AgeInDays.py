#!/usr/bin/env python
# coding:utf-8

from datetime import date, timedelta, datetime


def count_years(b, t):
    # y年における誕生日（閏日補正含む）
    try:
        this_year = b.replace(year=t.year)
    except ValueError:
        b += timedelta(days=1)
        this_year = b.replace(year=t.year)

    age = t.year - b.year
    if today < this_year:
        age -= 1

    return age


def count_months(b, t):
    if (t.day - b.day) >= 0:
        months = (t.year - b.year)*12 + (t.month - b.month)
    else:
        months = (t.year - b.year)*12 + (t.month - b.month) - 1  # 誕生日が来るまでは月齢も-1
    return months


def count_days(b, t):
    if (t.day - b.day) >= 0:
        days = t.day - b.day
    else:
        before = t.replace(month=t.month-1, day=b.day)
        days = (t - before).days
    return days


# 日付設定
today = date.today()
# birthday = date(1992, 2, 28)
bd = input("Please enter your birthday   ")  # python2ではraw_input
bd = datetime.strptime(bd, "%Y/%m/%d")
birthday = date(bd.year, bd.month, bd.day)

# 年齢を表示
age_in_days = (today - birthday).days
age = count_years(birthday, today)
age_months = count_months(birthday, today)
age_days = count_days(birthday, today)


print (age_in_days, age, age_months, age_days)  # python2では()なし
