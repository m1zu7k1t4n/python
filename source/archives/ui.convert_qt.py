# -*- coding: utf-8 -*-
from PyQt5 import uic

"""
fin = open('first_pyqt.ui', 'r')
fout = open('first_pyqt.py', 'w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()
"""

with open('untitled.py', 'w') as fout:
    with open('untitled.ui', 'r') as fin:
        uic.compileUi(fin, fout, execute=False)
