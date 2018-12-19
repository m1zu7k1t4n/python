# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 223)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txt_message = QtWidgets.QPlainTextEdit(Form)
        self.txt_message.setGeometry(QtCore.QRect(10, 10, 471, 141))
        self.txt_message.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txt_message.setObjectName("txt_message")
        self.ok_btn = QtWidgets.QPushButton(Form)
        self.ok_btn.setGeometry(QtCore.QRect(400, 160, 75, 23))
        self.ok_btn.setObjectName("ok_btn")
        self.Select_btn = QtWidgets.QPushButton(Form)
        self.Select_btn.setGeometry(QtCore.QRect(20, 160, 75, 23))
        self.Select_btn.setObjectName("Select_btn")

        self.retranslateUi(Form)
        self.ok_btn.clicked.connect(self.txt_message.copy)
        self.Select_btn.clicked.connect(self.txt_message.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ok_btn.setText(_translate("Form", "OK"))
        self.Select_btn.setText(_translate("Form", "Select"))

