import sys
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Ico(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(1000, 500)
        self.setWindowTitle('多表情')

        btn = QPushButton('test1', self)
        btn.clicked.connect(QCoreApplication.instance().quit())
        btn.resize(60, 20)
        btn.move(50, 50)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())

# class OldDog():
#     def __init__(self):
#         print('I am an old dog !')
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print('I eat it !')
#             self.hungry = False
#         else:
#             print('No thanks!')
#
#
# class NewDog(OldDog):
#     def __init__(self):
#         super().__init__()
#         print('I am a new dog!')
#
#
# olddog = OldDog()
# olddog.eat()
# olddog.eat()
# olddog.eat()
# newdog = NewDog()
# newdog.eat()
# newdog.eat()
