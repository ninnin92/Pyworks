#!/usr/bin/env python
# coding:utf-8

from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
import datetime as dt

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '640')
# Config.set('graphics', 'fullscreen', 'auto')  # フルスクリーン
Config.set('graphics', 'show_cursor', '1')


class logtime(Widget):
    pass


class MyApp(App):
    data = []
    title = 'Log_Time'

    def time_get(self, bt):
        now = "{0:%y/%m/%d %H:%M:%S}".format(dt.datetime.now())
        self.data.append([bt] + [now])
        self.root.timel.text = bt + " --- " + now
        print self.root.timel.text

    def build(self):
        return logtime()

    def on_start(self):
        print ("Start!")

    def on_stop(self):
        print ("Stop!")
        print (self.data)

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':
    MyApp().run()
