# -*- coding: utf-8 -*-

from PyQt5 import uic

with open('first_pyqt.py', 'w') as fout:
    with open('first_pyqt.ui', 'r') as fin:
        uic.compileUi(fin, fout, execute=False)
    
