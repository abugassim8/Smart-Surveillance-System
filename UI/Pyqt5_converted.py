# importing libraries
from PyQt5 import uic
import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import cv2
import datetime
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage ,QPixmap

# IMPORT QSS CUSTOM
from ui_styles import Style

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1
from UI_functionsPyqt5 import *

# YOUR APPLICATION
class FlatGui(QMainWindow):
    def __init__(self):

        super().__init__()
        uic.loadUi("gui_base_old.ui",self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())
        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################


        ## REMOVE ==> STANDARD TITLE BAR
        UIPYQT5Functions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Main Window - Python Base')
        UIPYQT5Functions.labelTitle(self, 'Main Window - Python Base')
        UIPYQT5Functions.labelDescription(self, 'Set text')
        ## ==> END ##

        ## REMOVE ==> STANDARD TITLE BAR
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.btn_toggle_menu.clicked.connect(lambda: UIPYQT5Functions.toggleMenu(self, 220, True))
        ## ==> END ##




        ## ==> ADD CUSTOM MENUS
        self.stackedWidget.setMinimumWidth(20)
        UIPYQT5Functions.addNewMenu(self, "Home Page", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIPYQT5Functions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)

        ## ==> END ##

        # START MENU => SELECTION
        UIPYQT5Functions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.stackedWidget.setCurrentWidget(self.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIPYQT5Functions.userIcon(self, "WM", "url(:/16x16/icons/16x16/cil-user.png)", True)
        ## ==> END ##




        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIPYQT5Functions.returStatus() == 1:
                UIPYQT5Functions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIPYQT5Functions.uiDefinitions(self)
        ## ==> END ##

       # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.show()
        ## ==> END ##



    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.stackedWidget.setCurrentWidget(self.page_home)
            UIPYQT5Functions.resetStyle(self, "btn_home")
            UIPYQT5Functions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIPYQT5Functions.selectMenu(btnWidget.styleSheet()))


        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.stackedWidget.setCurrentWidget(self.page_settings)
            UIPYQT5Functions.resetStyle(self, "btn_new_user")
            UIPYQT5Functions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIPYQT5Functions.selectMenu(btnWidget.styleSheet()))



    ## ==> END ##



    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(FlatGui, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################





    def startClicked(self):
        self.logic = 1
        cap = cv2.VideoCapture(0)
        date = datetime.datetime.now()
        out = cv2.VideoWriter('C:/Users/Hega/Desktop/GUI/videos/video_%s%s%sT%s%s%s.mp4' %(date.year ,date.month ,date.day ,date.hour,date.minute,date.second),-1, 20.0, (640, 480))
        print('Yeah')
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                self.displayImage(frame, 1)
                cv2.waitKey()

                if(self.logic == 1):
                    out.write(frame)

                if(self.logic == 0):

                    break
            else:
                print('return not found')
        cap.release()
        cv2.destroyAllWindows()


    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:

            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()

        self.imglabel.setPixmap(QPixmap.fromImage(img))





import files_rc

if __name__ =="__main__":


    App = QApplication(sys.argv)
    window = FlatGui()
    window.show()
    sys.exit(App.exec())
