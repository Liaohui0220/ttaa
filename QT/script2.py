# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'script.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
import os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import shutil

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("20201130-V2")
        MainWindow.resize(1124, 600)
        MainWindow.setAutoFillBackground(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.xz = QtWidgets.QComboBox(self.centralwidget)
        self.xz.setGeometry(QtCore.QRect(80, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.xz.setFont(font)
        self.xz.setObjectName("xz")
        self.xz.addItem("")
        self.xz.addItem("")
        self.xz.currentIndexChanged[str].connect(self.start)

        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(730, 210, 101, 31))
        self.start.setObjectName("start")
        self.start.clicked.connect(self.startup)

        self.pant11 = QtWidgets.QLineEdit(self.centralwidget)
        self.pant11.setGeometry(QtCore.QRect(600, 80, 451, 31))
        self.pant11.setObjectName("pant11")

        self.Neir = QtWidgets.QTextBrowser(self.centralwidget)
        self.Neir.setGeometry(QtCore.QRect(530, 260, 521, 241))
        self.Neir.setObjectName("Neir")

        self.pant22 = QtWidgets.QLineEdit(self.centralwidget)
        self.pant22.setGeometry(QtCore.QRect(600, 120, 451, 31))
        self.pant22.setObjectName("pant22")
        self.pant33 = QtWidgets.QLineEdit(self.centralwidget)
        self.pant33.setGeometry(QtCore.QRect(600, 160, 451, 31))
        self.pant33.setObjectName("pant33")
        self.ts = QtWidgets.QLabel(self.centralwidget)
        self.ts.setGeometry(QtCore.QRect(80, 80, 371, 391))
        self.ts.setAlignment(QtCore.Qt.AlignJustify)
        self.ts.setAlignment(QtCore.Qt.AlignTop)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ts.setFont(font)
        self.ts.setObjectName("ts")
        self.pant1 = QtWidgets.QLabel(self.centralwidget)
        self.pant1.setGeometry(QtCore.QRect(530, 84, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pant1.setFont(font)
        self.pant1.setObjectName("pant1")
        self.pant2 = QtWidgets.QLabel(self.centralwidget)
        self.pant2.setGeometry(QtCore.QRect(530, 124, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pant2.setFont(font)
        self.pant2.setObjectName("pant2")
        self.pant3 = QtWidgets.QLabel(self.centralwidget)
        self.pant3.setGeometry(QtCore.QRect(530, 164, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pant3.setFont(font)
        self.pant3.setObjectName("pant3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 23))
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
        self.xz.setItemText(0, _translate("MainWindow", "移动同名文件"))
        self.xz.setItemText(1, _translate("MainWindow", "新数据转老数据"))
        self.start.setText(_translate("MainWindow", "开始"))
        self.ts.setText(_translate("MainWindow",
                                   "用于移动同名文件的，会根据后缀进行移动\n"
                                   "需要一个原始路径做比对\n"
                                   "可忽略大小写 20201130 V2 \n"
                                   " 参数1：源数据目录 \n"
                                   " 参数2：需要移动的数据目录 \n"
                                   " 参数3：需要移动的文件后缀，用|隔开 如 jpg|png|bmp"))
        self.pant1.setText(_translate("MainWindow", "参数1："))
        self.pant2.setText(_translate("MainWindow", "参数2："))
        self.pant3.setText(_translate("MainWindow", "参数3："))

    def start(self, i):
        global state
        # state = i
        state = i
        if state == '移动同名文件':
            self.ts.setText(
                '用于移动同名文件的，会根据后缀进行移动\n'
                '需要一个原始路径做比对\n'
                '可忽略大小写 20201130 V2 \n'
                ' 参数1：源数据目录 \n'
                ' 参数2：需要移动的数据目录 \n'
                ' 参数3：需要移动的文件后缀，用|隔开 如 jpg|png')
        if state == '新数据转老数据':
            self.ts.setText('未完成功能')
        print(i)

    def startup(self):

        global state
        path11 = self.pant11.text()
        path22 = self.pant22.text()
        path33 = self.pant33.text()
        if state == '移动同名文件':
            values_updates = path33.split('|')
            path1 = []
            for root, dirs, files in os.walk(path11):
                for file in files:
                    path1.append(os.path.join(root, file))
            path2 = []
            for root, dirs, files in os.walk(path22):
                for file in files:
                    path2.append(os.path.join(root, file))

            for a in path1:
                for b in path2:
                    if a.rsplit('\\', 1)[-1].split('.')[-2] == b.rsplit('\\', 1)[-1].split('.')[-2]:
                        for values_update in values_updates:
                            if b.rsplit('.', 1)[-1].lower() == values_update.lower():
                                print(a.replace(a.split('.')[-1], b.split('.')[-1]))
                                shutil.copy(b, a.replace(a.split('.')[-1], b.split('.')[-1]))
                self.Neir.append(a)  # 追加写入到信息栏
                print('查找：', a)
            return 'End'
        # if state == '新数据转老数据':


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    state = '移动同名文件'
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
