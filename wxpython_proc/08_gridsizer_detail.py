# coding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, "詳細設定", size=(600,300))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

button_1 = wx.Button(panel, wx.ID_ANY, "1", size=(30,30))
button_2 = wx.Button(panel, wx.ID_ANY, "2", size=(30,30))
button_3 = wx.Button(panel, wx.ID_ANY, "3", size=(30,30))
button_4 = wx.Button(panel, wx.ID_ANY, "4", size=(30,30))
button_5 = wx.Button(panel, wx.ID_ANY, "5", size=(30,30))
button_6 = wx.Button(panel, wx.ID_ANY, "6", size=(30,30))
button_7 = wx.Button(panel, wx.ID_ANY, "7", size=(30,30))
button_8 = wx.Button(panel, wx.ID_ANY, "8", size=(30,30))
button_9 = wx.Button(panel, wx.ID_ANY, "9", size=(30,30))

layout = wx.GridSizer(3)
layout.Add(button_1)
layout.Add(button_2)
layout.Add(button_3, flag=wx.GROW)
layout.Add(button_4, flag=wx.SHAPED | wx.ALIGN_TOP)
layout.Add(button_5, flag=wx.SHAPED | wx.ALIGN_BOTTOM)
layout.Add(button_6, flag=wx.SHAPED | wx.ALIGN_CENTER)
layout.Add(button_7, flag=wx.SHAPED | wx.ALIGN_LEFT)
layout.Add(button_8, flag=wx.SHAPED | wx.ALIGN_RIGHT)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
