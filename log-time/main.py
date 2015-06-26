#!/usr/bin/env python
# coding:utf-8

from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
#from kivy.uix.floatlayout import FloatLayout
#from kivy.adapters.listadapter import ListAdapter
#from kivy.uix.listview import ListView, ListItemLabel
import datetime as dt

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '640')
# Config.set('graphics', 'fullscreen', 'auto')  # フルスクリーン
Config.set('graphics', 'show_cursor', '1')


class logtime(Widget):
    data = ["A"]
    pass


class MyApp(App):
    title = 'Log_Time'

    def time_get(src):
        print (src)

    def build(self):
        return logtime()

    def on_start(self):
        print ("Start!")

    def on_stop(self):
        print ("Stop!")

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':
    MyApp().run()
