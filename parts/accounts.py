import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QWidget,QMainWindow,QApplication,QPushButton,QTextEdit
from PyQt5.uic import loadUi
import sys
import sqlite3


class Ui_Accounts(QDialog):
    def __init__(self):

        super(Ui_Accounts, self).__init__()
        loadUi("accounts.ui",self)

        self.createButton.clicked.connect(self.insertData)
        self.deleteButton.clicked.connect(self.deleteData)

    def deleteData(self):
        user = self.UlineEdit.text()
        passu = self.PlineEdit.text()

        conn = sqlite3.connect('logindata.db')

        conn.execute("DELETE FROM USERS WHERE USERNAME=user and PASSWORD=passu")
        conn.commit()


    def insertData(self):
        username = self.UlineEdit.text()
        password = self.PlineEdit.text()

        conn = sqlite3.connect('logindata.db')
        conn.execute("INSERT INTO USERS VALUES(?,?)", (username, password))
        conn.commit()
        result = conn.execute("SELECT * FROM USERS")

        for data in result:
            print("username :", data[0])
            print("password :", data[1])

            conn.execute("DELETE FROM users WHERE USERNAME=username and PASSWORD=password")

        conn.close()



app = QtWidgets.QApplication(sys.argv)
UIAccounts = Ui_Accounts()
UIAccounts.show()
sys.exit(app.exec_())
