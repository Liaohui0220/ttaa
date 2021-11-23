# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T8.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 180, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.ShuRuKuang = QtWidgets.QLineEdit(Dialog)
        self.ShuRuKuang.setGeometry(QtCore.QRect(110, 70, 171, 51))
        self.ShuRuKuang.setObjectName("ShuRuKuang")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "开始"))
