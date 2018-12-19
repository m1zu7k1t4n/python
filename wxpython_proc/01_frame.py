# coding: utf-8

import wx

app = wx.App()

# Frame(親ウィンドウ, 識別子, タイトル, size=フレームの大きさ, pos=表示位置の指定)
frame = wx.Frame(None, wx.ID_ANY, "テストフレーム", size=(300, 300), pos=(20, 20))

# 画面の下部にステータスバーを表示するかどうか
frame.CreateStatusBar()
# そのステータスバーに何を表示するのか
frame.SetStatusText("wxpython_enjoy")

# アイコンの割り当てを使用する
icon = wx.Icon("wxpython.ico", wx.BITMAP_TYPE_ICO)
frame.SetIcon(icon)

frame.Show()

app.MainLoop()