# coding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, "タイトル付きBoxSizer", size=(300,300))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

button_1 = wx.Button(panel, wx.ID_ANY, "ボタン1")
button_2 = wx.Button(panel, wx.ID_ANY, "ボタン2")
button_3 = wx.Button(panel, wx.ID_ANY, "ボタン3")

box = wx.StaticBox(panel, wx.ID_ANY, "boxsizer_static")

layout = wx.StaticBoxSizer(box, wx.HORIZONTAL)
# layout = wx.StaticBoxSizer(box, wx.VERTICAL)

layout.Add(button_1)
layout.Add(button_2)
layout.Add(button_3)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()