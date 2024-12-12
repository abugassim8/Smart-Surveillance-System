################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################
from PyQt5 import QtCore
## ==> GUI FILE
from Pyqt5_program import *


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
