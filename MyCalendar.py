# -*- coding:utf-8 -*-

import tkinter as tk

# カレンダーを作成するフレームクラス
class mycalendar(tk.Frame):
    def __init__(self,master=None,cnf={},**kw):
        "初期化メソッド"
        import datetime
        tk.Frame.__init(self,master,cnf,**kw)

        # 現在の日付を取得
        now = datetime.datetime.now()
        # 現在の年と月を属性に追加
        self.year = now.year
        self.month = now.month

        # frame_top部分の作成
        frame_top = tk.Frame(self)
        frame_top.pack(pady=5)
        self.previous_month = tk.Label(frame_top, text = "<", font = ("",14))
        self.previous_month.pack(side = "left", padx = 10)
        self.current_year = tk.Label(frame_top, text = self.year, font = ("", 18))
        self.current_year.pack(side = "left")
        self.current_month = tk.Label(frame_top, text = self.month, font = ("",18))
        self.current_month.pack(side = "left")
        self.next_month = tk.Label(frame_top, text = ">", font = ("", 14))
        self.next_month.pack(side = "left", pack = 10)

        # frame_week部分の作成
        frame_week = tk.Frame(self)
        frame_week.pack()
        button_mon = d_button(frame_week, text = "Mon")
        button_mon.grid(column=0, row=0)
        button_mon = d_button(frame_week, text = "Tue")
        button_mon.grid(column=1, row=0)
        button_mon = d_button(frame_week, text = "Wed")
        button_mon.grid(column=2, row=0)
        button_mon = d_button(frame_week, text = "Thu")
        button_mon.grid(column=3, row=0)
        button_mon = d_button(frame_week, text = "Fri")
        button_mon.grid(column=4, row=0)
        button_mon = d_button(frame_week, text = "Sat", fg = "blue")
        button_mon.grid(column=5, row=0)
        button_mon = d_button(frame_week, text = "San", fg = "red")
        button_mon.grid(column=6, row=0)

        # frame_calendar部分の作成
        self.frame_calendar = tk.Frame(self)
        self.frame_calendar.pack()

        # 日付部分を作成するメソッドの呼び出し
        self.create_calendar(self.year, self.month)

    def create_calendar(selfself, year, month):
        "指定した年(year),月(month)のカレンダーウィジェットを作成する"

        # calendarモジュールのインスタンスを作成
        import calendar
        cal = calendar.Calendar()
        # 指定した年月のカレンダーをリストで返す
        days = cal.monthdayscalendar(year, month)

        # 日付ボタンを格納する変数をdict型で作成
        self.day = {}
        # for文を用いて、日付ボタンを生成
        for i in range(0, 42):
            c = i - (7 * int(i/7))
            r = int(i/7)
            try:
                # 日付が0でなかったら、ボタン作成
                if days[r][c] != 0:
                    self.day[i] = d_button(self.frame_calendar, text = days[r][c])

