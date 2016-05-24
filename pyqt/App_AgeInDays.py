#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import ui_ageindays
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import calendar as cal
from datetime import date, timedelta, datetime


class MainWindow(QMainWindow, ui_ageindays.Ui_AgeInDays):

    def __init__(self):
        super(MainWindow, self).__init__()
        # setupUi というメソッドが定義されているので実行する
        # これで設置したウィジェットなどがインスタンス化される
        self.setupUi(self)
        # 継承したので self.名前 でアクセスできる
        self.setWindowTitle("AgeInDays")
        self.pushButton_Go.clicked.connect(self.calculate)
        self.pushButton_Clear.clicked.connect(self.textBrowser.clear)
        self.switch_target_age.activated.connect(self.target_mode_change)
        self.switch_target_range.activated.connect(self.target_range_change)
        self.input_birthday.setDate(QDate.currentDate())
        self.input_research_date.setDate(QDate.currentDate())

    def age_in_days(self):
        research_date_set = self.input_research_date.date().toString("yyyy/MM/dd")
        research_date = datetime.strptime(research_date_set, "%Y/%m/%d")
        research_date = date(research_date.year, research_date.month, research_date.day)

        birthday_set = self.input_birthday.date().toString("yyyy/MM/dd")
        birthday = datetime.strptime(birthday_set, "%Y/%m/%d")
        birthday = date(birthday.year, birthday.month, birthday.day)

        # 年齢の計算（閏日補正含む）：今何歳なのか？:age
        try:
            t_year = birthday.replace(year=research_date.year)
        except ValueError:
            b += timedelta(days=1)
            t_year = birthday.replace(year=research_date.year)

        age = research_date.year - birthday.year
        if research_date < t_year:
            age -= 1

        # 月齢および何歳”何ヶ月”を計算:months, year_months
        if (research_date.day - birthday.day) >= 0:
            months = (research_date.year - birthday.year) * 12 \
            + (research_date.month - birthday.month)

            year_months = (research_date.year - birthday.year) * 12 - age * 12 \
            + (research_date.month - birthday.month)

        else: # 誕生日が来るまでは月齢も-1
            months = (research_date.year - birthday.year) * 12 \
            + (research_date.month - birthday.month) - 1

            year_months = (research_date.year - birthday.year) * 12 - age * 12 \
            + (research_date.month - birthday.month) - 1


        # 日齢および何歳何ヶ月の余り日数（何歳何ヶ月”何日”）:year_days
        if (research_date.day - birthday.day) >= 0:
            year_days = research_date.day - birthday.day
        else:
            try:
                if research_date.month == 1:
                    before = research_date.replace(year=research_date.year - 1,
                                                   month=12, day=birthday.day)
                    year_days = (research_date - before).days
                else:
                    before = research_date.replace(month=research_date.month - 1,
                                                   day=birthday.day)
                    year_days = (research_date - before).days
            except ValueError:
                year_days = research_date.day
                # 2月は1ヶ月バックするとエラーになる時がある(誕生日が29-31日の時)
                # なのでそうなった場合は、すでに前月の誕生日を迎えたことにする（setされた日が日数とイコールになる）

        # 年齢を表示
        age             = str(age)
        age_year_months = str(year_months)
        age_year_days   = str(year_days)
        age_months      = str(months)
        age_days        = str((research_date - birthday).days)

        age_details = age + "years " +age_year_months + "months " + age_year_days + "days"

        results = ["Research date  " + research_date_set,
                   "Birthday  " + birthday_set,
                   "Age  " + age,
                   "Age_months  " + age_months,
                   "Age_in_days  " + age_days,
                   "Age_details  " + age_details]

        return results

    # 対象年齢と調査予定日から誕生日を推定
    def age_to_birthday(self):
        target_mode = self.switch_target_age.currentText()
        target_range = self.switch_target_range.currentText()

        if target_range == "範囲":
            if target_mode == "月齢":
                Age1_months = int(self.input_target1_months.text())
                Age1_days = int(self.input_target1_days.text())
                Age1 = [str(Age1_months//12), str(Age1_months%12), str(Age1_days)]
                return Age1

            else:
                pass

        else:
            if target_mode == "月齢":
                pass

            else:
                pass

        """set_days = int(age[2])  # 年齢（日）
        set_months = base.month - int(age[1])  # 調査予定日の月から年齢（月）を引く

        # 引いた月の数がマイナスになる時は、年齢からもう1年引いて、月に12ヶ月足す → 再計算
        if set_months <= 0:
            set_years = base.year - int(age[0]) - 1
            set_months = 12 + set_months
        else:
            set_years = base.year - int(age[0])  # 調査予定日の年から年齢（年）を引く

        # 調査予定日を基準に年齢の年・月を引いてから日を引き算
        try:
            bd = base.replace(year=set_years, month=set_months)  # 調査予定日から年と月を計算後に変更
            bd -= timedelta(days=set_days)  # 変更後から日数を変更

        # 調査予定日が29-31日で、変更後の月が2月（29-31日）、4・6・9・11月（31日）だとエラー（存在しないため）
        except ValueError:
            # 調査予定日から年と月を計算後に変更、日は変更後の月末にとりあえず指定
            bd = base.replace(year=set_years, month=set_months,
                              day=cal.monthrange(set_years, set_months)[1])
            bd += timedelta(days=base.day - bd.day)  # とりあえず変更した日数（減らした日数分）を追加
            bd -= timedelta(days=set_days)  # 変更後から日数を変更
        bd = date(bd.year, bd.month, bd.day)
        return bd"""

    """# 対象年齢と誕生日から調査予定日を推定
    def age_to_date(self):
        set_days = int(age[2])  # 年齢（日）
        set_months = bd.month + int(age[1])  # 調査予定日の月から年齢（月）を引く

        # 引いた月の数がマイナスになる時は、年齢からもう1年引いて、月に12ヶ月足す → 再計算
        if set_months > 12:
            set_years = bd.year + int(age[0]) + 1
            set_months = set_months - 12
        else:
            set_years = bd.year + int(age[0])  # 調査予定日の年から年齢（年）を引く

        # 誕生日を基準に年齢の年・月を足してから日を足し算
        try:
            d = bd.replace(year=set_years, month=set_months)  # 誕生日から年と月を計算後に変更
            d += timedelta(days=set_days)  # 変更後から日数を変更

        # 誕生日が29-31日で、変更後の月が2月（29-31日）、4・6・9・11月（31日）だとエラー（存在しないため）
        except ValueError:
            # 誕生日から年と月を計算後に変更、日は変更後の月末にとりあえず指定
            d = bd.replace(year=set_years, month=set_months,
                           day=cal.monthrange(set_years, set_months)[1])
            d += timedelta(days=bd.day - d.day)  # とりあえず変更した日数（減らした日数分）を追加
            d += timedelta(days=set_days)  # 変更後から日数を変更
        d = date(d.year, d.month, d.day)
        return d"""

    def calculate(self):
        mode = int(self.change_mode.currentText()[0])
        if mode == 1:
            text = self.age_in_days()
        elif mode == 2:
            text = self.age_to_birthday()
        elif mode == 3:
            text = ["さん"]
        else:
            pass

        text.insert(0, "*******************************")
        text.append("*******************************")

        for i in text:
            self.textBrowser.append(i)

    def target_mode_change(self):
        target_mode = self.switch_target_age.currentText()
        if target_mode == "月齢":
            self.input_target1_years.setEnabled(False)
            self.input_target2_years.setEnabled(False)
        else:
            self.input_target1_years.setEnabled(True)
            self.input_target2_years.setEnabled(True)

    def target_range_change(self):
        target_mode = self.switch_target_range.currentText()
        if target_mode == "固定":
            self.input_target2_years.setEnabled(False)
            self.input_target2_months.setEnabled(False)
            self.input_target2_days.setEnabled(False)
        else:
            self.input_target2_years.setEnabled(True)
            self.input_target2_months.setEnabled(True)
            self.input_target2_days.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())