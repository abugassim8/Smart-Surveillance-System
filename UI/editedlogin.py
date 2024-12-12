from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QPushButton,QTextEdit
from PyQt5 import uic
import sys
import sqlite3
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage ,QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import platform

from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

from Login_UI_fun import  *

class Ui_Main(QMainWindow):

    def __init__(self):

        super().__init__()
        uic.loadUi("editedlogin.ui",self)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

        self.loginButton.clicked.connect(self.login)
    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        connection = sqlite3.connect("FaceNetdb.db")
        result = connection.execute ("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if(len(result.fetchall())>0):
            print ("User Found !")

        else:
            print("User Not Found !")

        connection.close()


from images import main_source_rc


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    UIWindow = Ui_Main()
    UIWindow.show()
    sys.exit(app.exec_())
