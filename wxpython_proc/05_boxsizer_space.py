# coding: utf-8

import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY,"テストフレーム", size=(300,200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

inner_panel_1 = wx.Panel(panel, wx.ID_ANY)
inner_panel_2 = wx.Panel(panel, wx.ID_ANY)
inner_panel_3 = wx.Panel(panel, wx.ID_ANY)

inner_panel_1.SetBackgroundColour("#FF0000")
inner_panel_2.SetBackgroundColour("#00FF00")
inner_panel_3.SetBackgroundColour("#0000FF")

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(inner_panel_1, proportion=1, flag=wx.EXPAND | wx.TOP,  border=10)
layout.Add(inner_panel_2, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=10)
layout.Add(inner_panel_3, proportion=1, flag=wx.EXPAND | wx.ALL,  border=10)

panel.SetSizer(layout)

frame.Show()
application.MainLoop()
