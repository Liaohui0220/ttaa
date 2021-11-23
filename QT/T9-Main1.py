from QT import T9_1
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class CamShow(QMainWindow, T9_1.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())