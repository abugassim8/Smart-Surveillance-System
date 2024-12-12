from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QPushButton,QTextEdit,QLabel,QDialog
from PyQt5 import uic
import sys
import sqlite3
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage ,QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Profile(QDialog):

    def __init__(self):

        super().__init__()
        uic.loadUi("profileDialog.ui",self)

        self.search.clicked.connect(self.update_suspect)





    def update_suspect(self):
        name = self.profile_name.text()
        radioBtn = self.sender()
        if radioBtn.isChecked():
            status = radioBtn.text()

        conn = sqlite3.connect('FaceNetdb.db')
        conn.execute('UPDATE Suspects SET Status = ? WHERE NAME = ?', status,name)
        conn.commit()
        conn.close()











    #@pyqtSlot()



if __name__ =="__main__":


    App = QApplication(sys.argv)
    window = Ui_Profile()
    window.show()
    sys.exit(App.exec())
