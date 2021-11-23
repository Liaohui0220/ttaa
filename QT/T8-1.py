from QT import T8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class CamShow(QMainWindow,  T8.Ui_Dialog):
    def __init__(self, parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())