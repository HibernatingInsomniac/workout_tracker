from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow,\
    QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sqlite_utils.sqlTable as sl3_util
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
        self.pbLocateSl3.clicked.connect(self.locate_sl3)
        self.pbLoadTables.clicked.connect(self.load_tables)
        self.show()
        
    def locate_sl3(self):
        filepath = QFileDialog.getOpenFileName(self)
        self.leSl3Location.setText(filepath[0])
        
    def load_tables(self):
        sl3_util.load_db_tables(self.leSl3Location.text())
        

app = QApplication(sys.argv)
window = UI()
app.exec_()