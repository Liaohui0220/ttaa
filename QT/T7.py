from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp

import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("test1")

        flo = QFormLayout()
        pIntLineEdit = QLineEdit()
        pDoubleLineEdit = QLineEdit()
        pValidatorLineEdit = QLineEdit()

        flo.addRow("整", pIntLineEdit)
        flo.addRow("浮点", pDoubleLineEdit)
        flo.addRow("字母+数字", pValidatorLineEdit)

        pIntLineEdit.setPlaceholderText('整')
        pDoubleLineEdit.setPlaceholderText('浮点')
        pValidatorLineEdit.setPlaceholderText('字母+数字')

        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(1, 99)

        pDoubleValidator = QDoubleValidator(self)
        pDoubleValidator.setRange(-360, 360)
        pDoubleValidator.setNotation
        (QDoubleValidator.StandardNotation)
        pDoubleValidator.setDecimals(2)

        reg = QRegExp("[a-zA-Z0-9]+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)

        pIntLineEdit.setValidator(pIntValidator)
        pDoubleLineEdit.setValidator(pDoubleValidator)
        pValidatorLineEdit.setValidator(pValidator)

        self.setLayout(flo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())
