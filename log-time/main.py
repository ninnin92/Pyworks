#!/usr/bin/env python
# coding:utf-8

from __future__ import division
from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
import datetime as dt

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'show_cursor', '1')


class logtime(Widget):
    pass


class MyApp(App):
    title = 'Log_Time'
    bt1 = "event1"
    bt2 = "event2"
    bt3 = "event3"

    data = []

    app_time = "{0:%y-%m-%d_%H-%M}".format(dt.datetime.now())
    fp = open("Log/" + "Log_" + app_time + ".csv", "w")

    def bt_release(self, bt):
        if bt == 1:
            self.root.hit1.color = [0.2, 0.70588, 0.56470, 1]
        elif bt == 2:
            self.root.hit2.color = [0.2, 0.70588, 0.56470, 1]
        else:
            self.root.hit3.color = [0.2, 0.70588, 0.56470, 1]

    def time_get(self, bt):
        if bt == 1:
            self.root.hit1.color = [0.8, 0.8, 0.8, 1]
            bt = self.bt1
        elif bt == 2:
            self.root.hit2.color = [0.8, 0.8, 0.8, 1]
            bt = self.bt2
        else:
            self.root.hit3.color = [0.8, 0.8, 0.8, 1]
            bt = self.bt3

        now = "{0:%y/%m/%d %H:%M:%S}".format(dt.datetime.now())
        self.data.append([bt] + [now])
        self.root.timel3.text = self.root.timel2.text
        self.root.timel2.text = self.root.timel1.text
        self.root.timel1.text = "*  " + bt + " | " + now

        print (self.root.timel1.text)

    def build(self):
        return logtime()

    def on_start(self):
        index = ["Event", "Time"]
        for i in index:
            self.fp.write("%s," % i)
        self.fp.write("\n")
        print ("Start!")

    def on_stop(self):
        print (self.data)
        for x in self.data:
            self.fp.write("%s, %s\n" % tuple(x))
        self.fp.flush()
        print ("Stop!")

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':
    MyApp().run()
