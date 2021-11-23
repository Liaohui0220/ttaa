from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys


class Winform(QWidget):
    button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('自定义信')
        self.resize(330, 50)
        btn = QPushButton('test', self)

        # link_槽函数
        btn.clicked.connect(self.btn_clicked)
        # getLink_槽
        self.button_clicked_signal.connect(self.Printss)

    def btn_clicked(self):
        self.button_clicked_signal.emit()
    def Printss(self):
        print('end```')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
