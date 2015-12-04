#!/usr/bin/env python
# coding:utf-8
# env: Python3.4

option = 1

if option == 1:

    # 選択肢 その１
    import tkinter
    import tkinter.filedialog as tkfd

    root = tkinter.Tk()
    root.withdraw()
    filename = tkfd.askopenfilename()
    print(filename)

else:
    # 選択肢 その２
    import os

    class tkTrickeryPulldownQuery(object):
        def __init__(self, title, values, **kw):
            import tkinter as tk
            from tkinter import ttk
            from tkinter import E, W, N, S  # for sticky
            self.root = tk.Tk()
            self.root.title(title)

            self.ent = ttk.Combobox(
                self.root, **kw)
            self.ent['values'] = values
            self.ent.current(0)  # 先頭アイテム選択

            self.ent.grid(row=0, column=0, columnspan=10, sticky=E + W)
            btno = tk.Button(
                self.root, text="OK", command=self._ok)
            btno.grid(row=1, column=0, sticky=E + W)
            btnc = tk.Button(
                self.root, text="Cancel", command=self._cancel)
            btnc.grid(row=1, column=1, sticky=E + W)
            self.root.mainloop()

        def __call__(self):
            return self.value

        def _ok(self):
            self.value = self.ent.get()  #
            self.root.destroy()

        def _cancel(self):
            self.value = "no select"
            self.root.destroy()

    if __name__ == "__main__":
        data_list = os.listdir("db/")
        print(tkTrickeryPulldownQuery(u"データベース選択", values=data_list, state='readonly')())
