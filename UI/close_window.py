from PyQt5 import uic
import platform
from PyQt5.QtWidgets import *
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage ,QPixmap
class Close_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("close_window.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.yes.clicked.connect(self.Testexit)
        self.no.clicked.connect(self.DoNoting)

    def Testexit(self):
        self.close()
        exit(0)

    def DoNoting(self):
        self.close()
