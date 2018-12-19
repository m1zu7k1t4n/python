# coding: UTF-8

import Tkinter
import os
import tkMessageBox
import tkFileDialog
import csv
import sys
import urllib
def input_file():
    root = Tkinter.Tk()
    root.withdraw()
    iDir = '/mnt/d/HDDdownload/CACHE/'
    fTyp = [('txtFile','*.txt')]
    filenames = tkFileDialog.askopenfilenames(filetypes=fTyp,initialdir=iDir)
    return filenames

def select_extension(filename,extension):
    fin = open(filename, 'r')
    Allf = fin.read()

    outfilename = filename
    outfilename = outfilename.replace('.txt','_out.txt')
    fout = open(outfilename, 'w')
    text = Allf.replace('doujinantena.com','cdn.doujinantena.com')
    text = text.replace('page.php?id=', extension + '/')
    text = text.replace('\r\n','.' + extension + '\n')
    fout.write(text)
    print extension.upper() + " File Downloading Now..."
    os.system('xargs -P 20 -n 1 wget -q -nc -P /mnt/d/!Dropbox/Dropbox/個人用途/antena/ < ' + outfilename)
    print extension.upper() + " File Download Complete!"
    end_option(outfilename)
    fout.close()
    fin.close()

def del_space(filename):
    os.system('''rename 's/ /_/' ''' + filename)

def down(filename):
    os.system('xargs -P 20 -n 1 wget -q -nc $1 -P /mnt/d/!Dropbox/Dropbox/個人用途/antena/ < ' + filename)

def end_option(removefile):
    if os.system("rm -rf " + removefile) == True:
        print u"enderror"

def main():
    args = sys.argv
    filepaths = input_file()
    if len(args) > 1:
        for path in filepaths:
            select_extension(path, args[1])
        if len(args) > 2:
            for path in filepaths:
                select_extension(path, args[2])
    else:
        for path in filepaths:
            select_extension(path, "pdf")
    print "Process Complete!"

if __name__ == '__main__':
    main()