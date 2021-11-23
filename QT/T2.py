from PyQt5.QtWidgets import *
import sys

app = QApplication([])
widget = QWidget()


def showMsg():
    QMessageBox.information(widget, '信息提示框', "ok,弹出测试信息")


QMessageBox.information(widget, '信息提示框', "ok,弹出测试信息")

btn = QPushButton("按钮1", widget)
btn.clicked.connect(showMsg)

widget.show()
sys.exit(app.exec_())

