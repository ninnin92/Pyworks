#!/usr/bin/env python
# coding:utf-8
# env: Python3.3
# python2系でも動くように調整済み

from datetime import date, timedelta, datetime


# y年における誕生日（閏日補正含む）
def count_years(b, t):
    try:
        this_year = b.replace(year=t.year)
    except ValueError:
        b += timedelta(days=1)
        this_year = b.replace(year=t.year)

    age = t.year - b.year
    if today < this_year:
        age -= 1

    return age


# 月齢の計算
def count_months(b, t):
    if (t.day - b.day) >= 0:
        months = (t.year - b.year)*12 + (t.month - b.month)
    else:
        months = (t.year - b.year)*12 + (t.month - b.month) - 1  # 誕生日が来るまでは月齢も-1
    return months


# 何歳”何ヶ月”を計算
def count_year_months(b, t):
    months = t.month - b.month  # 月の引き算
    return months


# 月齢および何歳何ヶ月の余り日数（何歳何ヶ月”何日”）
def count_days(b, t):
    if (t.day - b.day) >= 0:
        days = t.day - b.day
    else:
        before = t.replace(month=t.month-1, day=b.day)
        days = (t - before).days
    return days


# 日付設定(今日)
today = date.today()

# 入力待ち(exceptでPython2系にも対応)
try:
    bd = input('Please enter your birthday (e.g. "2015/06/04")  ')
except:
    def input(text):
        return raw_input(text)  # python2ではraw_input
    bd = input('Please enter your birthday (e.g. "2015/06/04")  ')
    pass

# 誕生日をdatetime型に設定
bd = datetime.strptime(bd, "%Y/%m/%d")
birthday = date(bd.year, bd.month, bd.day)

# 年齢を表示
age = str(count_years(birthday, today))
age_months = str(count_months(birthday, today))
age_in_days = str((today - birthday).days)
age_year_months = str(count_year_months(birthday, today))
age_days = str(count_days(birthday, today))

age_details = age + "years " + age_year_months + "months " + age_days + "days"


print ("********************************************")  # python2では()なし
print ("Age  " + age)
print ("Age_months  " + age_months)
print ("Age_in_days  " + age_in_days)
print ("Age_details  " + age_details)
print ("********************************************")
