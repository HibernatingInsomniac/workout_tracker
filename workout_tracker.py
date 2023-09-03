from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow,\
    QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('layout.ui', self) 
        self.twDataView.setColumnCount(5)
        self.twDataView.setRowCount(1)
        for i in range(5):
            print(i)
            self.twDataView.setItem(0,i,QTableWidgetItem(str(i)))
        self.show()

app = QApplication(sys.argv)
window = UI()
app.exec_()