# coding: utf-8

import wx

app=wx.App()
frame = wx.Frame(None, wx.ID_ANY, "余白設定", size=(300,300))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

button_1 = wx.Button(panel, wx.ID_ANY, "1")
button_2 = wx.Button(panel, wx.ID_ANY, "2")
button_3 = wx.Button(panel, wx.ID_ANY, "3")
button_4 = wx.Button(panel, wx.ID_ANY, "4")

layout = wx.GridSizer(2)
layout.Add(button_1, flag=wx.EXPAND | wx.TOP,   border=10)
layout.Add(button_2, flag=wx.EXPAND | wx.LEFT,  border=10)
layout.Add(button_3, flag=wx.EXPAND | wx.RIGHT, border=10)
layout.Add(button_4, flag=wx.EXPAND | wx.ALL,   border=10)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()