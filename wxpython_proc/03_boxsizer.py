# coding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, "Boxsizer", size=(400, 200))

# 親をframeとしてpanelを初期化
panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF") # 灰色

# 親をpanelとしてbutton_1,2,3を初期化
button_1 = wx.Button(panel, wx.ID_ANY, "ボタン1")
button_2 = wx.Button(panel, wx.ID_ANY, "ボタン2")
button_3 = wx.Button(panel, wx.ID_ANY, "ボタン3")

# 横方向にボタンを羅列
layout = wx.BoxSizer(wx.HORIZONTAL)
# 縦方向にボタンを羅列
# layout = wx.BoxSizer(wx.VERTICAL)
#要素を追加、proportionでフレームサイズに応じて連動
layout.Add(button_1, proportion=1)
layout.Add(button_2, proportion=1)
layout.Add(button_3, proportion=1)

# パネルへBoxSizerをセット
panel.SetSizer(layout)

frame.Show()
app.MainLoop()