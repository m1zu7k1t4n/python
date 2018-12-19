# coding: utf-8

import wx


# トップレベルウィンドウクラス
class CalcFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "電卓レイアウト", size=(300, 280))
        # ステータスバーの初期化
        self.CreateStatusBar()
        self.SetStatusText("python-izm study wxpython")
        self.GetStatusBar().SetBackgroundColour(None)

        # メニューバーの初期化
        self.SetMenuBar(CalcMenu())

        # 本体部分の構築
        root_panel = wx.Panel(self, wx.ID_ANY)

        text_panel = TextPanel(root_panel)
        cmdbutton_panel = CommandButtonPanel(root_panel)
        calcbutton_panel = CalcButtonPanel(root_panel)

        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(text_panel, 0, wx.GROW | wx.ALL, border=10)
        root_layout.Add(cmdbutton_panel, 0, wx.GROW | wx.LEFT | wx.RIGHT, border=20)
        root_layout.Add(calcbutton_panel, 0, wx.GROW | wx.ALL, border=10)
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)


# メニューバークラス
class CalcMenu(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self)

        menu_file = wx.Menu()
        menu_file.Append(wx.ID_ANY, "保存")
        menu_file.Append(wx.ID_ANY, "終了")
        menu_edit = wx.Menu()
        menu_edit.Append(wx.ID_ANY, "コピー")
        menu_edit.Append(wx.ID_ANY, "ペースト")

        self.Append(menu_file, "ファイル")
        self.Append(menu_edit, "編集")


# テキスト部分
class TextPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        calc_text = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_RIGHT)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(calc_text, 1)
        self.SetSizer(layout)


# 中央ボタン部分
class CommandButtonPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        button_ce = wx.Button(self, wx.ID_ANY, "CE")
        button_c = wx.Button(self, wx.ID_ANY, "C")
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(button_ce, flag=wx.GROW)
        layout.Add(button_c, flag=wx.GROW)
        self.SetSizer(layout)


# 下部ボタン部分
class CalcButtonPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        button_collection = ("7", "8", "9", "+",
                             "4", "5", "6", "-",
                             "1", "2", "3", "*",
                             "0", ".", "=", "/")

        layout = wx.GridSizer(4, 4, 3, 3)
        for i in button_collection:
            layout.Add(wx.Button(self, wx.ID_ANY, i,
                                 size=(30, 25)), 1, wx.GROW)

        self.SetSizer(layout)


# アプリケーション開始
if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    frame.Show()
    app.MainLoop()
