# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 'q', 'p', 'o', 'n',
                 'l', 'k', 'j', 'i',
                 'h', 'g', 'f', 'e',
                 'd', 'c', 'b', 'a', ]
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            print(position, name)
            if name == '':
                continue
            button = QPushButton(name)
            print(button)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Label_test')
        self.show()

    def click_s(self):
        print('进入')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
