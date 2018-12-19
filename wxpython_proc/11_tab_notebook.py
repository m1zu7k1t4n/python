# coding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, "タブ作成", size=(300,150))

notebook = wx.Notebook(frame, wx.ID_ANY, wx.NB_TOP)
# notebook = wx.Notebook(frame, wx.ID_ANY, style=wx.NB_RIGHT)
# notebook = wx.Notebook(frame, wx.ID_ANY, style=wx.NB_LEFT)
# notebook = wx.Notebook(frame, wx.ID_ANY, style=wx.NB_BOTTOM)

panel_1 = wx.Panel(notebook, wx.ID_ANY)
panel_2 = wx.Panel(notebook, wx.ID_ANY)
panel_3 = wx.Panel(notebook, wx.ID_ANY)

panel_1.SetBackgroundColour("#FF0000")
panel_2.SetBackgroundColour("#00FF00")
panel_3.SetBackgroundColour("#0000FF")

#InsertPage(タグインデックス, 追加部品, タブ名称)
notebook.InsertPage(0, panel_1, "tab_1")
notebook.InsertPage(1, panel_2, "tab_2")
notebook.InsertPage(2, panel_3, "tab_3")

#ImageList(イメージファイルの縦px、横px)
image_list = wx.ImageList(32, 32)
icon = wx.Icon("wxpython.ico", wx.BITMAP_TYPE_ICO)
image_list.AddIcon(icon)
notebook.AssignImageList(image_list)

notebook.SetPageImage(2, 0)

frame.Show()
app.MainLoop()