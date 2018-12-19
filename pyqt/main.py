# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from ui import first_pyqt
 
class MyForm(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = first_pyqt.Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.ok_btn.clicked.connect(self.ok_btn_cliked)
 
    def ok_btn_cliked(self):
        print(type(self.ui))
        self.ui.txt_message.setText("Hello, Qt")
        
def run_app():
    app = QtWidgets.QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    run_app()