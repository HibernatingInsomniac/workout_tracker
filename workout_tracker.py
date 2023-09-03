from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QTableWidget
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('layout.ui', self)       
        self.show()

app = QApplication(sys.argv)
window = UI()
app.exec_()