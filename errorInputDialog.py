# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorInputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(284, 103)
        self.erroLabel = QtWidgets.QLabel(Dialog)
        self.erroLabel.setGeometry(QtCore.QRect(20, 10, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.erroLabel.setFont(font)
        self.erroLabel.setWordWrap(True)
        self.erroLabel.setObjectName("erroLabel")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 70, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(self.hide)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.erroLabel.setText(_translate("Dialog", "Input masih salah, mohon sesuaikan dengan format!"))
        self.pushButton.setText(_translate("Dialog", "OK"))
