from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys


class MyQLabel(QLabel):
    # 自定义信号, 注意信号必须为类属性
    button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)


class Winform(QWidget):
    # button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('自定义信')
        self.resize(330, 200)
        label = MyQLabel(self)
        label.resize(330, 200)
        label.connect_customized_slot(self.Printss)

        # link_槽函数
        # label.clicked.MyQLabel(self.btn_clicked)
        # getLink_槽
        # self.button_clicked_signal.connect(self.Printss)

    def Printss(self):
        print('aaabbb')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
