# -*- coding: utf-8 -*-
import sys
import natsort
import sys, os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH']
from PIL import Image
from PyQt5.QtWidgets import *
from package import Path_list
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

number_ = 0

aaaa = r'\\dtc-fs\MarkTest\tool\测试数据\2k4k8k长图\2\动漫\5'
print(aaaa)
path1 = Path_list.path_jpg(aaaa)
path2 = Path_list.path_jpg(aaaa)
path3 = Path_list.path_jpg(aaaa)
path4 = Path_list.path_jpg(aaaa)
path5 = Path_list.path_jpg(aaaa)


def show_image():
    def size_img(path):
        # 获取屏幕分辨率
        desktop = QApplication.desktop()
        screenRect = desktop.screenGeometry()
        height = screenRect.height() - 0.15 * screenRect.height()
        height_ = screenRect.height()
        width = screenRect.width()
        # 图片
        img = Image.open(path)
        w = img.width  # 图片的宽
        h = img.height  # 图片的高
        print(w, h)
        if w > h:
            h = ((width / 3) / w) * h
            w = width / 3
        if h > w:
            w = ((height / 2) / h) * w
            h = height / 2
        di = [w, h]
        print(w, h)
        return di

    def update_img(paths):
        global number_
        global path1, path2, path3, path4, path5

        # path
        size_I = size_img(paths[0])
        size_II = size_img(paths[1])
        size_III = size_img(paths[2])
        size_IV = size_img(paths[3])
        size_V = size_img(paths[4])

        print(size_I, size_II, size_III, size_IV, size_V)

        # 写入
        jpg = QtGui.QPixmap(path[number_]).scaled(size_I[0], size_I[1])
        jpg2 = QtGui.QPixmap(path2[number_]).scaled(size_II[0], size_II[1])
        jpg3 = QtGui.QPixmap(path3[number_]).scaled(size_III[0], size_III[1])
        jpg4 = QtGui.QPixmap(path4[number_]).scaled(size_IV[0], size_IV[1])
        jpg5 = QtGui.QPixmap(path5[number_]).scaled(size_V[0], size_V[1])

        # 更新
        w.label1.setPixmap(jpg)
        w.label2.setPixmap(jpg2)
        w.label3.setPixmap(jpg3)
        w.label4.setPixmap(jpg4)
        w.label5.setPixmap(jpg5)

        name_1_text = str(len(path)) + "/" + str(number_ + 1) + '  ' + str(path[number_]).rsplit('\\', 1)[-1]
        name_2_text = str(len(path2)) + "/" + str(number_ + 1) + '  ' + str(path2[number_]).rsplit('\\', 1)[-1]
        name_3_text = str(len(path3)) + "/" + str(number_ + 1) + '  ' + str(path3[number_]).rsplit('\\', 1)[-1]
        name_4_text = str(len(path4)) + "/" + str(number_ + 1) + '  ' + str(path4[number_]).rsplit('\\', 1)[-1]
        name_5_text = str(len(path5)) + "/" + str(number_ + 1) + '  ' + str(path5[number_]).rsplit('\\', 1)[-1]

        name_1.setText(name_1_text)
        name_2.setText(name_2_text)
        name_3.setText(name_3_text)
        name_4.setText(name_4_text)
        name_5.setText(name_5_text)

        w.show()
        QtWidgets.QApplication.processEvents()

    def left_img():
        global number_
        global path1

        if number_ == 0:
            msg_box = QMessageBox(QMessageBox.Warning, '提示', '已经是第一张了！')
            msg_box.exec_()
        elif 0 < number_ + 1:
            number_ -= 1
        print("左")

        print(path[number_])
        print(path2[number_])
        print(path3[number_])
        print(path4[number_])
        print(path5[number_])

        update_img([path[number_], path2[number_], path3[number_], path4[number_], path5[number_]])

    def right_img():
        global number_
        global path1
        if \
                len(path) == number_ + 1 or \
                        len(path2) == number_ + 1 or \
                        len(path3) == number_ + 1 or \
                        len(path4) == number_ + 1 or \
                        len(path5) == number_ + 1:
            msg_box = QMessageBox(QMessageBox.Warning, '提示', '已经是最后一张了！')
            msg_box.exec_()
        elif \
                len(path) > number_ + 1 and \
                        len(path2) > number_ + 1 and \
                        len(path3) > number_ + 1 and \
                        len(path4) > number_ + 1 and \
                        len(path5) > number_ + 1:
            number_ += 1
        print("右")

        print(path[number_])
        print(path2[number_])
        print(path3[number_])
        print(path4[number_])
        print(path5[number_])

        update_img([path[number_], path2[number_], path3[number_], path4[number_], path5[number_]])

    def aaa():
        global aaaa
        global path1, path2, path3, path4, path5
        p_a = dialog.line1.text()
        p_b = dialog.line2.text()
        p_c = dialog.line3.text()
        p_d = dialog.line4.text()
        p_e = dialog.line5.text()

        print(p_a)
        print(p_b)
        print(p_c)
        print(p_d)
        print(p_e)

        path = Path_list.path_jpg(p_a)
        path2 = Path_list.path_jpg(p_b)
        path3 = Path_list.path_jpg(p_c)
        path4 = Path_list.path_jpg(p_d)
        path5 = Path_list.path_jpg(p_e)

        dialog.close()

    def open_img():
        def bbb():
            global aaaa, number_
            global path1, path2, path3, path4, path5

            number_ = 0

            p_a = dialog.line1.text()
            p_b = dialog.line2.text()
            p_c = dialog.line3.text()
            p_d = dialog.line4.text()
            p_e = dialog.line5.text()

            print(p_a)
            print(p_b)
            print(p_c)
            print(p_d)
            print(p_e)

            path = Path_list.path_jpg(p_a)
            path2 = Path_list.path_jpg(p_b)
            path3 = Path_list.path_jpg(p_c)
            path4 = Path_list.path_jpg(p_d)
            path5 = Path_list.path_jpg(p_e)

            update_img([path[number_], path2[number_], path3[number_], path4[number_], path5[number_]])

            dialog.close()

        # 对话框
        dialog = QDialog()
        dialog.line1 = QLineEdit(dialog)  # 单行编辑框
        dialog.line1.move(20, 20)
        dialog.line1.resize(500, 20)
        dialog.line2 = QLineEdit(dialog)  # 单行编辑框
        dialog.line2.move(20, 60)
        dialog.line2.resize(500, 20)
        dialog.line3 = QLineEdit(dialog)  # 单行编辑框
        dialog.line3.move(20, 100)
        dialog.line3.resize(500, 20)
        dialog.line4 = QLineEdit(dialog)  # 单行编辑框
        dialog.line4.move(20, 140)
        dialog.line4.resize(500, 20)
        dialog.line5 = QLineEdit(dialog)  # 单行编辑框
        dialog.line5.move(20, 180)
        dialog.line5.resize(500, 20)
        btn = QPushButton('Openg', dialog)
        btn.move(230, 220)
        btn.clicked.connect(bbb)
        dialog.setWindowTitle('打开路径中的jpg')
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    app = QtWidgets.QApplication(sys.argv)

    desktop = QApplication.desktop()
    screenRect = desktop.screenGeometry()
    height = screenRect.height() - 100
    height_ = screenRect.height()
    width = screenRect.width()

    # 对话框
    dialog = QDialog()
    dialog.line1 = QLineEdit(dialog)  # 单行编辑框
    dialog.line1.move(20, 20)
    dialog.line1.resize(500, 20)
    dialog.line2 = QLineEdit(dialog)  # 单行编辑框
    dialog.line2.move(20, 60)
    dialog.line2.resize(500, 20)
    dialog.line3 = QLineEdit(dialog)  # 单行编辑框
    dialog.line3.move(20, 100)
    dialog.line3.resize(500, 20)
    dialog.line4 = QLineEdit(dialog)  # 单行编辑框
    dialog.line4.move(20, 140)
    dialog.line4.resize(500, 20)
    dialog.line5 = QLineEdit(dialog)  # 单行编辑框
    dialog.line5.move(20, 180)
    dialog.line5.resize(500, 20)
    btn = QPushButton('Openg', dialog)
    btn.move(230, 220)
    # btn.resize()
    btn.clicked.connect(aaa)
    # btn.clicked.connect(dialog.close)
    dialog.setWindowTitle('打开路径中的jpg')
    dialog.setWindowModality(Qt.ApplicationModal)
    dialog.exec_()

    w = QWidget()
    # w.label = QLabel(w)
    # w.label.setText("   显示图片")

    w.label1 = QLabel(w)
    w.label1.setText('xianshi1')

    w.label2 = QLabel(w)
    w.label2.setText('xianshi2')

    w.label3 = QLabel(w)
    w.label3.setText('xianshi3')

    w.label4 = QLabel(w)
    w.label4.setText('xianshi4')

    w.label5 = QLabel(w)
    w.label5.setText('xianshi5')

    w.pant1 = QtWidgets.QLabel()
    w.pant1.setGeometry(QtCore.QRect(530, 84, 61, 21))
    font = QtGui.QFont()
    font.setPointSize(12)
    w.pant1.setFont(font)
    w.pant1.setObjectName("pant1")

    w.pant2 = QtWidgets.QLabel()
    w.pant2.setGeometry(QtCore.QRect(530, 124, 61, 21))
    font = QtGui.QFont()
    font.setPointSize(12)
    w.pant2.setFont(font)
    w.pant2.setObjectName("pant2")

    w.pant3 = QtWidgets.QLabel()
    w.pant3.setGeometry(QtCore.QRect(530, 164, 61, 21))
    font = QtGui.QFont()
    font.setPointSize(12)
    w.pant3.setFont(font)
    w.pant3.setObjectName("pant3")

    btn2 = QPushButton("上一张(A)", w)
    btn2.clicked.connect(left_img)
    btn2.setGeometry(0, 100, 100, 50)
    # btn2.setShortcut('Left')
    btn2.setShortcut('A')
    btn2.move(0, height / 2 + 50)

    btn3 = QPushButton("下一张(D)", w)
    btn3.clicked.connect(right_img)
    btn3.setGeometry(0, 200, 100, 50)
    btn3.setShortcut('Right')
    btn3.setShortcut('D')
    btn3.move(0, height / 2 + 100)

    btn4 = QPushButton("Open（Ctrl+O)", w)
    btn4.clicked.connect(open_img)
    btn4.setGeometry(0, 200, 80, 30)
    btn4.setStyleSheet('background-color:#000000;color:#ffffff')
    btn4.setShortcut('Ctrl+O')
    btn4.move(0, height / 2 + 150)

    img = Image.open(r"\\dtc-fs\MarkTest\tool\测试数据\2k4k8k长图\1\美女\1\Emma黑色旗袍黑色丝袜美腿壁纸.jpg")
    w_ = img.width  # 图片的宽
    h_ = img.height  # 图片的高

    # 获取屏幕分辨率
    desktop = QApplication.desktop()
    screenRect = desktop.screenGeometry()
    height = screenRect.height() - 0.08 * screenRect.height()
    height_ = screenRect.height()
    width = screenRect.width()

    # 窗口设置
    # resize()方法调整窗口的大小。这离是250px宽150px高
    w.resize(width, height_)
    # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标
    # w.move(300, 300)
    # 设置窗口的标题
    w.setWindowTitle('5图查看')

    # 载入图片
    jpg1 = QtGui.QPixmap(path1[number_]).scaled(size_img(path1[number_])[0], size_img(path1[number_])[1])
    jpg2 = QtGui.QPixmap(path2[number_]).scaled(size_img(path2[number_])[0], size_img(path2[number_])[1])
    jpg3 = QtGui.QPixmap(path3[number_]).scaled(size_img(path3[number_])[0], size_img(path3[number_])[1])
    jpg4 = QtGui.QPixmap(path4[number_]).scaled(size_img(path4[number_])[0], size_img(path4[number_])[1])
    jpg5 = QtGui.QPixmap(path5[number_]).scaled(size_img(path5[number_])[0], size_img(path5[number_])[1])

    # 上1
    w.label1.setPixmap(jpg1)
    w.label1.resize(width / 3, height / 2 - 20)
    w.label1.setAlignment(Qt.AlignCenter)

    # 上2
    w.label2.move(width / 3, 0)
    w.label2.setPixmap(jpg2)
    w.label2.resize(width / 3, height / 2 - 20)
    w.label2.setAlignment(Qt.AlignCenter)

    # 上3
    w.label3.move((width / 3) * 2, 0)
    w.label3.setPixmap(jpg3)
    w.label3.resize(width / 3, height / 2 - 20)
    w.label3.setAlignment(Qt.AlignCenter)

    # 下1
    w.label4.move(width / 3 / 2, height / 2 + 20)
    w.label4.setPixmap(jpg4)
    w.label4.resize(width / 3, height / 2 - 20)
    w.label4.setAlignment(Qt.AlignCenter)

    # 下2
    w.label5.move(width / 3 * 1.5 + 5, height / 2 + 20)
    w.label5.setPixmap(jpg5)
    w.label5.resize(width / 3, height / 2 - 20)
    w.label5.setAlignment(Qt.AlignCenter)

    # 名称
    name_1 = QtWidgets.QLabel(w)
    name_1.setGeometry(QtCore.QRect(80, 80, 371, 391))
    name_1.setAlignment(QtCore.Qt.AlignJustify)
    name_1.setAlignment(QtCore.Qt.AlignTop)
    font = QtGui.QFont()
    font.setPointSize(12)
    name_1.setFont(font)
    name_1.setObjectName("ts")
    name_1.move(20, height / 2)

    name_2 = QtWidgets.QLabel(w)
    name_2.setGeometry(QtCore.QRect(80, 80, 371, 391))
    name_2.setAlignment(QtCore.Qt.AlignJustify)
    name_2.setAlignment(QtCore.Qt.AlignTop)
    font = QtGui.QFont()
    font.setPointSize(12)
    name_2.setFont(font)
    name_2.setObjectName("ts")
    name_2.move(width / 3, height / 2)

    name_3 = QtWidgets.QLabel(w)
    name_3.setGeometry(QtCore.QRect(80, 80, 371, 391))
    name_3.setAlignment(QtCore.Qt.AlignJustify)
    name_3.setAlignment(QtCore.Qt.AlignTop)
    font = QtGui.QFont()
    font.setPointSize(12)
    name_3.setFont(font)
    name_3.setObjectName("ts")
    name_3.move(width / 3 * 2, height / 2)

    name_4 = QtWidgets.QLabel(w)
    name_4.setGeometry(QtCore.QRect(80, 80, 371, 391))
    name_4.setAlignment(QtCore.Qt.AlignJustify)
    name_4.setAlignment(QtCore.Qt.AlignTop)
    font = QtGui.QFont()
    font.setPointSize(12)
    name_4.setFont(font)
    name_4.setObjectName("ts")
    name_4.move(width / 6, height)

    name_5 = QtWidgets.QLabel(w)
    name_5.setGeometry(QtCore.QRect(80, 80, 371, 391))
    name_5.setAlignment(QtCore.Qt.AlignJustify)
    name_5.setAlignment(QtCore.Qt.AlignTop)
    font = QtGui.QFont()
    font.setPointSize(12)
    name_5.setFont(font)
    name_5.setObjectName("ts")
    name_5.move(width / 2, height)

    # 显示在屏幕上
    w.showMaximized()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_image()
