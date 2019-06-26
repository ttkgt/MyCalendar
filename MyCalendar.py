# -*- coding:utf-8 -*-

import tkinter as tk

# カレンダーを作成するフレームクラス
class mycalendar(tk.Frame):
    def __init__(self,master=None,cnf={},**kw):
        "初期化メソッド"
        import datetime
        tk.Frame.__init(self,master,cnf,**kw)


