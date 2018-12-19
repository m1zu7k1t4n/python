# coding:utf-8

import wx

caption = ("都道府県", "男女計", "男", "女")

data = [
    ("北海道", "5,570", "2,638", "2,933"),
    ("青森県", "1,407", "663", "744"),
    ("岩手県", "1,364", "652", "712"),
    ("宮城県", "2,347", "1,140", "1,208"),
    ("秋田県", "1,121", "527", "593"),
    ("山形県", "1,198", "575", "623"),
    ("福島県", "2,067", "1,004", "1,063"),
    ("茨城県", "2,969", "1,477", "1,492"),
    ("栃木県", "2,014", "1,001", "1,013"),
    ("群馬県", "2,016", "993", "1,024"),
    ("埼玉県", "7,090", "3,570", "3,520"),
    ("千葉県", "6,098", "3,047", "3,051"),
    ("東京都", "12,758", "6,354", "6,405"),
    ("神奈川県", "8,880", "4,484", "4,396"),
]


class MyTable(wx.ListCtrl):
    def __init__(self, parent):
        wx.ListCtrl.__init__(
            self, parent, -1, style=wx.LC_REPORT | wx.LC_HRULES)

        for col, v in enumerate(caption):
            self.InsertColumn(col, v)

        for line in range(len(data)):
            self.InsertStringItem(line, data[line][0])
            for col in range(1, 4):
                self.SetStringItem(line, col, data[line][col])


class MyWindow(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "MyTitle", size=(300, 200))
        MyTable(self)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyWindow(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
