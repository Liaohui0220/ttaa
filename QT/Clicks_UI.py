from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QDialog, QApplication


# from demoMouseClicks import*

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 382)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(101, 31, 255, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 255, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 110, 255, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "当鼠标按下或者释放时，显示坐标位置"))


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            x = event.x()
            y = event.y()

            if 0 < x < 100:
                text = "1"
            else:
                text = "x: {0},y: {1}".format(x, y)
            self.ui.label_2.setText('鼠标按下：' + text)

    def mouseReleaseEvent(self, event):
        x = event.x()
        y = event.y()
        text = "x: {0},y: {1}".format(x, y)
        self.ui.label_3.setText("鼠标释放：" + text)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
