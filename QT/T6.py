#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *

import base64
import io
from PIL import Image


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        pix = QPixmap('test_img.jpg')

        btn1 = QPushButton("按钮1", self)
        btn1.setGeometry(0, 0, 100, 50)
        btn1.clicked.connect(update_img)

        btn2 = QPushButton("按钮2", self)
        btn2.setGeometry(100, 0, 100, 50)
        btn2.clicked.connect(update_img)

        btn3 = QPushButton("按钮3", self)
        btn3.setGeometry(200, 0, 100, 50)
        btn3.clicked.connect(update_img)

        lb1 = QLabel(self)
        lb1.setGeometry(0, 50, 500, 210)
        lb1.setStyleSheet("border: 2px solid red")
        lb1.setPixmap(pix)

        lb2 = QLabel(self)
        lb2.setGeometry(0, 250, 500, 210)
        lb2.setPixmap(pix)
        lb2.setStyleSheet("border: 2px solid red")
        lb2.setScaledContents(True)  # 自适应QLabel大小

        self.lb3 = QLabel(self)
        self.lb3.setGeometry(0, 500, 500, 210)
        self.lb3.setPixmap(pix)
        self.lb3.setStyleSheet("border: 2px solid red")
        self.lb3.setScaledContents(True)  # 自适应QLabel大小


def set_img_on_label(lb, img_b64):
    img_b64decode = base64.b64decode(img_b64)  # [21:]
    img_io = io.BytesIO(img_b64decode)
    img = Image.open(img_io)
    pix = img.toqpixmap()
    lb.setScaledContents(True)  # 自适应QLabel大小
    lb.setPixmap(pix)


def update_img(self):
    lb2 = QLabel(self)
    lb2.setGeometry(250, 250, 500, 210)
    lb2.setPixmap(QPixmap('test_img.jpg'))
    lb2.setStyleSheet("border: 2px solid red")
    lb2.setScaledContents(True)  # 自适应QLabel大小


if __name__ == '__main__':
    app = QApplication([])  # argv)
    # icon = QIcon("logo.ico")
    # app.setWindowIcon(icon)
    win = Demo()
    win.show()
    sFile = open("test_img.jpg", "rb").read()
    img_b64 = base64.b64encode(sFile)
    set_img_on_label(win.lb3, img_b64)
    sys.exit(app.exec_())
