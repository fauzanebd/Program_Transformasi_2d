# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogTranslasi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(280, 143)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 100, 221, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 241, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbXDist = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.lbXDist.setFont(font)
        self.lbXDist.setObjectName("lbXDist")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbXDist)
        self.inputJarakX = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.inputJarakX.setObjectName("inputJarakX")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputJarakX)
        self.lbYDist = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.lbYDist.setFont(font)
        self.lbYDist.setObjectName("lbYDist")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbYDist)
        self.inputJarakY = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.inputJarakY.setObjectName("inputJarakY")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputJarakY)
        self.lbTranslationInstruction = QtWidgets.QLabel(Dialog)
        self.lbTranslationInstruction.setGeometry(QtCore.QRect(20, 20, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.lbTranslationInstruction.setFont(font)
        self.lbTranslationInstruction.setObjectName("lbTranslationInstruction")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbXDist.setText(_translate("Dialog", "Jarak pada X"))
        self.lbYDist.setText(_translate("Dialog", "Jarak pada Y"))
        self.lbTranslationInstruction.setText(_translate("Dialog", "Masukkan detail Translasi"))