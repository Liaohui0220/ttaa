# -*- coding: utf-8 -*-
import sys
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH']
from PIL import Image
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

number_ = 0

def path_jpg(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg'):
                path1.append(os.path.join(root, file))
    return path1
path1 = path_jpg(r"\\dtc-fs\MarkTest\tool\测试数据\2k4k8k长图\1\美女")

def show_image(image_path=path1[number_]):
    def update_img_90():
        global number_
        print("开始旋转")
        # 90
        im = Image.open(path1[number_])
        out = im.transpose(Image.ROTATE_90)
        out.save(path1[number_])
        # 调整显示
        img = Image.open(path1[number_])
        w_ = img.width
        h_ = img.height
        if h_ < w_:
            h__ = h_ * (700 / w_)
            w__ = 700
        else:
            w__ = w_ * (700 / h_)
            h__ = 700

        w.label.setFixedSize(int(w__), int(h__))
        w.label.setStyleSheet('border:2px solid red')
        jpg = QtGui.QPixmap(path1[number_]).scaled(w.label.width(), w.label.height())
        w.label.setPixmap(jpg)
        # w.setScaledContents(True)
        w.show()
        # QMessageBox.information(w, '信息提示框', "test")
        QtWidgets.QApplication.processEvents()

    def update_img_180():
        global number_
        print("开始旋转")
        # 180
        im = Image.open(path1[number_])
        out = im.transpose(Image.ROTATE_180)
        out.save(path1[number_])
        # 调整显示
        img = Image.open(path1[number_])
        w_ = img.width
        h_ = img.height
        if h_ < w_:
            h__ = h_ * (700 / w_)
            w__ = 700
        else:
            w__ = w_ * (700 / h_)
            h__ = 700

        w.label.setFixedSize(int(w__), int(h__))
        w.label.setStyleSheet('border:2px solid red')
        jpg = QtGui.QPixmap(path1[number_]).scaled(w.label.width(), w.label.height())
        w.label.setPixmap(jpg)
        # w.setScaledContents(True)  #
        w.show()
        # QMessageBox.information(w, '信息提示框', "test")
        QtWidgets.QApplication.processEvents()

    def update_img_270():
        global number_
        print("开始旋转")
        # 180
        im = Image.open(path1[number_])
        out = im.transpose(Image.ROTATE_270)
        out.save(path1[number_])
        # 调整显示
        img = Image.open(path1[number_])
        w_ = img.width
        h_ = img.height
        if h_ < w_:
            h__ = h_ * (700 / w_)
            w__ = 700
        else:
            w__ = w_ * (700 / h_)
            h__ = 700

        w.label.setFixedSize(int(w__), int(h__))
        w.label.setStyleSheet('border:2px solid red')
        jpg = QtGui.QPixmap(path1[number_]).scaled(w.label.width(), w.label.height())
        w.label.setPixmap(jpg)
        # w.setScaledContents(True)  #
        w.show()
        # QMessageBox.information(w, '信息提示框', "test")
        QtWidgets.QApplication.processEvents()

    def left_img():
        global number_
        global path1
        number_ -= 1
        print(number_)
        print("左")
        img = Image.open(path[number_])
        print(path[number_])
        w_ = img.width  # 图片的宽
        h_ = img.height  # 图片的高
        if h_ < w_:
            h__ = h_ * (700 / w_)
            w__ = 700
        else:
            w__ = w_ * (700 / h_)
            h__ = 700
        w.label.setFixedSize(w__, h__)
        w.label.setStyleSheet('border:no')
        jpg = QtGui.QPixmap(path[number_]).scaled(w.label.width(), w.label.height())
        w.label.setPixmap(jpg)
        w.show()
        QtWidgets.QApplication.processEvents()
        return number_

    def right_img():
        global number_
        global path1
        number_ += 1
        print(number_)
        print("右")
        img = Image.open(path[number_])
        print(path[number_])
        w_ = img.width  # 图片的宽
        h_ = img.height  # 图片的高
        if h_ < w_:
            h__ = h_ * (700 / w_)
            w__ = 700
        else:
            w__ = w_ * (700 / h_)
            h__ = 700
        w.label.setFixedSize(w__, h__)
        w.label.setStyleSheet('border:no')
        jpg = QtGui.QPixmap(path[number_]).scaled(w.label.width(), w.label.height())
        w.label.setPixmap(jpg)
        w.show()
        QtWidgets.QApplication.processEvents()

    app = QtWidgets.QApplication(sys.argv)

    # ShuRuKuang = QtWidgets.QLineEdit("输入", w)
    # ShuRuKuang.setGeometry(QtCore.QRect(110, 70, 171, 51))
    # ShuRuKuang.setObjectName("ShuRuKuang")

    w = QWidget()
    w.label = QLabel(w)
    w.label.setText("   显示图片")

    btn = QPushButton("旋转90°", w)
    btn.clicked.connect(update_img_90)
    btn.setGeometry(0, 0, 50, 25)

    btna = QPushButton("旋转180°", w)
    btna.clicked.connect(update_img_180)
    btna.setGeometry(0, 25, 50, 25)

    btnb = QPushButton("旋转270°", w)
    btnb.clicked.connect(update_img_270)
    btnb.setGeometry(0, 50, 50, 25)

    btn2 = QPushButton("上一张", w)
    btn2.clicked.connect(left_img)
    btn2.setGeometry(0, 100, 100, 50)
    btn2.setShortcut('A')

    btn3 = QPushButton("下一张", w)
    btn3.clicked.connect(right_img)
    btn3.setGeometry(0, 200, 100, 50)
    btn3.setShortcut('D')

    # ShuRuKuang = QtWidgets.QLineEdit(w)
    # ShuRuKuang.setGeometry(QtCore.QRect(110, 70, 171, 51))
    # self.ShuRuKuang.setObjectName("ShuRuKuang")

    img = Image.open(r"C:\Users\lh9373\Downloads\壁纸\t3.jpg",'r+b')
    w_ = img.width  # 图片的宽
    h_ = img.height  # 图片的高

    if h_ < w_:
        h__ = h_ * (700 / w_)
        w__ = 700
    else:
        w__ = w_ * (700 / h_)
        h__ = 700



    w.label.setFixedSize(w__, h__)
    w.label.move(400, 100)
    w.label.setStyleSheet("QLabel{background:white;}"
                          "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                          )

    # resize()方法调整窗口的大小。这离是250px宽150px高
    w.resize(1600, 900)
    # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
    #    w.move(300, 300)
    # 设置窗口的标题
    w.setWindowTitle('Simple')
    jpg = QtGui.QPixmap(image_path).scaled(w.label.width(), w.label.height())
    w.label.setPixmap(jpg)
    # 显示在屏幕上
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_image()
    # QApplication.processEvents()
