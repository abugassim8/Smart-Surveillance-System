from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QTextEdit, QLabel, QDialog
from PyQt5 import uic
import sys
import sqlite3
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


class Ui_Profile(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("profileDialog.ui", self)

        self.Update_Status.clicked.connect(self.update_suspect)
        self.Update_Record.clicked.connect(self.update_record)

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

    def update_suspect(self):
        name = self.profile_name.text()
        conn = sqlite3.connect('FaceNetdb.db')
        if self.radioDied.isChecked() == True:
            status = self.radioDied.text()
            conn.execute('UPDATE Suspects SET Status = ? WHERE NAME = ?', (status, name))
        if self.radioCaptured.isChecked() == True:
            status = self.radioCaptured.text()
            conn.execute('UPDATE Suspects SET Status = ? WHERE NAME = ?', (status, name))
        if self.radioWanted.isChecked() == True:
            status = self.radioWanted.text()
            conn.execute('UPDATE Suspects SET Status = ? WHERE NAME = ?', (status, name))

        conn.commit()
        conn.close()


    def update_record(self):
        ID = self.profile_ID.text()
        name = self.profile_name.text()

        gender = self.profile_gender.text()

        race = self.profile_race.text()

        #BD = self.proflie_BD.text()
        rec = self.profile_record.text()



        conn = sqlite3.connect('FaceNetdb.db')
        conn.execute('UPDATE Suspects SET NAME = ?, GENDER = ?, RACE = ?, CRIMINAL_RECORDS = ? WHERE ID = ?', (name, gender, race, rec, ID))
        conn.commit()
        conn.close()

    # @pyqtSlot()


## ==> GLOBALS

GLOBAL_STATE = 0



class UIFunctions():

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE


    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # MINIMIZE
        self.btn_minimize_3.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.btn_close_3.clicked.connect(lambda: self.close())




    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Ui_Profile()
    window.show()
    sys.exit(App.exec())
