# coding: UTF-8

import tkinter
import tkMessageBox
import tkFileDialog

root = tkinter.Tk()
root.withdraw()
iDir = 'c:/'
fTyp = [('テキストファイル','*.txt')]
filename = tkFileDialog.askopenfilename(filetypes=fTyp,initialdir=iDir)
outfilename = filename
outfilename = outfilename.replace('.txt','')
outfilename = filename + u'_out.txt'
fin = open(filename, 'r')
fout = open(outfilename, 'w')

Allf = fin.read()

text = Allf.replace('\r\n','')
text = text.replace('.','.\r\n\r\n')
text = text.replace(',',',\r\n')

fout.write(text)
fout.close()

