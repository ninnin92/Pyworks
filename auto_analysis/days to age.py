#!/usr/bin/env
# -*- coding: utf-8 -*-

import pandas as pd
from datetime import date, timedelta, datetime

################################################
#  宣言
################################################

s_data = pd.read_csv("subject_age.csv")

################################################
#  処理関数
################################################
# 年齢の計算（閏日補正含む） ：今何歳何ヶ月なのか？


def count_years(b, s):
    try:
        this_year = b.replace(year=s.year)
    except ValueError:
        b += timedelta(days=1)
        this_year = b.replace(year=s.year)

    age = s.year - b.year
    if s < this_year:
        age -= 1

# 何歳”何ヶ月”を計算
    if (s.day - b.day) >= 0:
        year_months = (s.year - b.year) * 12 - age * 12 + (s.month - b.month)
    else:
        year_months = (s.year - b.year) * 12 - age * 12 + (s.month - b.month) - 1  # 誕生日が来るまでは月齢も-1

    return age, year_months


# 月齢の計算
def count_months(b, s):
    if (s.day - b.day) >= 0:
        months = (s.year - b.year) * 12 + (s.month - b.month)
    else:
        months = (s.year - b.year) * 12 + (s.month - b.month) - 1  # 誕生日が来るまでは月齢も-1
    return months


# 月齢および何歳何ヶ月の余り日数（何歳何ヶ月”何日”）
def count_days(b, s):
    if (s.day - b.day) >= 0:
        days = s.day - b.day
    else:
        try:
            before = s.replace(month=s.month - 1, day=b.day)
            days = (s - before).days
        except ValueError:
            days = s.day
            # 2月は1ヶ月バックするとエラーになる時がある(誕生日が29-31日の時)
            # なのでそうなった場合は、すでに前月の誕生日を迎えたことにする（setされた日が日数とイコールになる）
    return days

################################################
#  メイン処理
################################################

if __name__ == '__main__':

    a_months = []
    a_days = []
    a_details = []

    for i in range(0, len(s_data)):
        try:
            base = s_data.iloc[i, :]["days"]
            base = datetime.strptime(str(base), "%Y/%m/%d")
            base_day = date(base.year, base.month, base.day)

            birth = s_data.iloc[i, :]["birthday"]
            birth = datetime.strptime(str(birth), "%Y/%m/%d")
            bir_day = date(birth.year, birth.month, birth.day)

            print(base_day, bir_day)

            age             = str(count_years(bir_day, base_day)[0])
            age_year_months = str(count_years(bir_day, base_day)[1])
            age_days        = str(count_days(bir_day, base_day))
            age_months      = str(count_months(bir_day, base_day))
            age_in_days     = str((base_day - bir_day).days)
            age_details = age + "y " + age_year_months + "m " + age_days + "d"

        except:
            age_months = "NA"
            age_in_days = "NA"
            age_details = "NA"

        a_months.append(age_months)
        a_days.append(age_in_days)
        a_details.append(age_details)

    s_data = s_data.assign(age_days=a_days, age_months=a_months, age_details=a_details)
    s_data.to_csv("result_subjects_age.csv", index=False)
