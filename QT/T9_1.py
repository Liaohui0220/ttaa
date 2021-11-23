# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T9.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from package import Path_list


class Ui_MainWindow(object):
    list_ = []
    number_ = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rotating_90_1 = QtWidgets.QPushButton(self.centralwidget)
        self.rotating_90_1.setGeometry(QtCore.QRect(20, 40, 41, 41))
        self.rotating_90_1.setObjectName("rotating_90")
        self.rotating_90_1.clicked.connect(self.rot_90)
        self.rotating_180_1 = QtWidgets.QPushButton(self.centralwidget)
        self.rotating_180_1.setGeometry(QtCore.QRect(80, 40, 41, 41))
        self.rotating_180_1.setObjectName("rotating_180")
        self.rotating_270_1 = QtWidgets.QPushButton(self.centralwidget)
        self.rotating_270_1.setGeometry(QtCore.QRect(140, 40, 41, 41))
        self.rotating_270_1.setObjectName("rotating_270")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 151, 151))
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 90, 151, 151))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 90, 151, 151))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 90, 151, 151))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(750, 90, 151, 151))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(920, 90, 151, 151))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setObjectName("label_6")
        self.hou = QtWidgets.QPushButton(self.centralwidget)
        self.hou.setGeometry(QtCore.QRect(860, 10, 75, 23))
        self.hou.setObjectName("hou")
        self.qian = QtWidgets.QPushButton(self.centralwidget)
        self.qian.setGeometry(QtCore.QRect(770, 10, 75, 23))
        self.qian.setObjectName("qian")
        self.qian.clicked.connect(self.update_img_up)
        self.qian.clicked.connect(self.open_path)
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(240, 10, 75, 23))
        self.open.setObjectName("open")
        self.open.clicked.connect(self.open_path)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 211, 21))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rotating_90_1.setText(_translate("MainWindow", "90°"))
        self.rotating_180_1.setText(_translate("MainWindow", "180°"))
        self.rotating_270_1.setText(_translate("MainWindow", "270°"))
        self.label.setText(_translate("MainWindow", "图片1"))
        self.label_2.setText(_translate("MainWindow", "图片1"))
        self.label_3.setText(_translate("MainWindow", "图片1"))
        self.label_4.setText(_translate("MainWindow", "图片1"))
        self.label_5.setText(_translate("MainWindow", "图片1"))
        self.label_6.setText(_translate("MainWindow", "图片1"))
        self.hou.setText(_translate("MainWindow", "下一张"))
        self.qian.setText(_translate("MainWindow", "上一张"))
        self.open.setText(_translate("MainWindow", "open"))


    def open_path(self):
        global list_
        global number_
        number_ = 0
        path = self.lineEdit.text()
        list_ = Path_list.path_jpg(path)

        imgs = Image.open(list_[number_])
        w = imgs.width
        h = imgs.height
        # try:
        jpg = QtGui.QPixmap(list_[number_]).scaled(151, h * (150 / w))
        self.label.setPixmap(jpg)

        imgs = Image.open(list_[number_ + 1])
        w = imgs.width
        h = imgs.height

        jpg = QtGui.QPixmap(list_[number_ + 1]).scaled(151, h * (150 / w))
        self.label_2.setPixmap(jpg)

        imgs = Image.open(list_[number_ + 2])
        w = imgs.width
        h = imgs.height

        jpg = QtGui.QPixmap(list_[number_ + 2]).scaled(151, h * (150 / w))
        self.label_3.setPixmap(jpg)

        imgs = Image.open(list_[number_ + 3])
        w = imgs.width
        h = imgs.height

        jpg = QtGui.QPixmap(list_[number_ + 3]).scaled(151, h * (150 / w))
        self.label_4.setPixmap(jpg)

        imgs = Image.open(list_[number_ + 4])
        w = imgs.width
        h = imgs.height

        jpg = QtGui.QPixmap(list_[number_ + 4]).scaled(151, h * (150 / w))
        self.label_5.setPixmap(jpg)

        imgs = Image.open(list_[number_ + 5])
        w = imgs.width
        h = imgs.height

        jpg = QtGui.QPixmap(list_[number_ + 5]).scaled(151, h * (150 / w))
        self.label_6.setPixmap(jpg)


    def update_img_up(self):
        global number_
        number_ += 6

    def rot_90(self):
        global list_

        im = Image.open(list_[0])
        out = im.transpose(Image.ROTATE_90)
        out.save(list_[0])
        # 调整显示
        img = Image.open(list_[0])
        w_ = img.width
        h_ = img.height
        if h_ < w_:
            h__ = h_ * (700 / w_)
            w__ = 700
        else:
            w__ = w_ * (700 / h_)
            h__ = 700

        # self.rotating_90_1 = QtWidgets.QPushButton(self.centralwidget)
        # self.rotating_90_1.setGeometry(QtCore.QRect(20, 40, 41, 41))
        # self.rotating_90_1.setObjectName("rotating_90")
        # self.rotating_90_1.clicked.connect(self.rot_90)

        path = self.lineEdit.text()
        list_ = Path_list.path_jpg(path)

        imgs = Image.open(list_[0])
        w = imgs.width
        h = imgs.height
        # try:
        jpg = QtGui.QPixmap(list_[0]).scaled(151, h * (150 / w))
        self.label.setPixmap(jpg)

        w.label.setStyleSheet('border:2px solid red')
        jpg = QtGui.QPixmap(list_[0]).scaled(w.label.width(), w.label.height())
        w.label.setPixmap(jpg)
        # w.setScaledContents(True)
        w.show()
        # QMessageBox.information(w, '信息提示框', "test")
        QtWidgets.QApplication.processEvents()
