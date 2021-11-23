import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

global sec
sec = 0


class WorkThread(QThread):
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        for i in range(2000000000):
            pass

        # 结束
        self.trigger.emit()


def countTime():
    global sec
    sec += 1
    # 显示+1
    lcdNumber.display(sec)


def work():
    timer.start(1000)
    workThread.start()

    workThread.start()


def timeStop():
    timer.stop()
    print("运行结束用时", lcdNumber.value())
    global sec
    sec = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)

    # 垂直布置
    layout = QVBoxLayout(top)
    # add Window
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("test")
    layout.addWidget(button)

    timer = QTimer()
    workThread = WorkThread()

    button.clicked.connect(work)
    timer.timeout.connect(countTime)

    top.show()
    sys.exit(app.exec_())
