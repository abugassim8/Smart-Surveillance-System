from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QPushButton,QTextEdit,QLabel
from PyQt5 import uic
import sys
import os
import cv2
import datetime
import time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage ,QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import identify_face_video
import Simple_Camera
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QMovie


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450,450)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)

        self.movie = QMovie('giphy_12.gif')
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(3000,self.stopAnimation)

        self.show()
    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()



class Ui_Main(QMainWindow):

    def __init__(self):

        super().__init__()
        uic.loadUi("grid main.ui",self)
        self.logic =0
        self.showMaximized()
        self.start.clicked.connect(self.startClicked)
        #self.start.clicked.connect(identify_face_video.main())
        #self.record.clicked.connect(self.recordClicked)
        self.loading_screen = LoadingScreen()
    @pyqtSlot()

    def startClicked(self):

        self.logic = 1
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        date = datetime.datetime.now()
        out = cv2.VideoWriter('C:/Users/Hega/Desktop/GUI/videos/video_%s%s%sT%s%s%s.mp4' %(date.year ,date.month ,date.day ,date.hour,date.minute,date.second),-1, 20.0, (640, 480))
        print('Yeah')
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                #identify_face_video.main()
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
        self.start.setEnabled(False)
        time.sleep(30)
        return frame
    def recordClicked(self):
        print("hi")
        #identify_face_video.main()

        image = Simple_Camera.camera_function()
        self.displayImage(image, 1)
        #Simple_Camera.camera_function()


    def displayImage(self, img,window = 1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:

            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()

        self.imglabel.setPixmap(QPixmap.fromImage(img))
        return
from images import main_source_rc


def main1():
    app = QtWidgets.QApplication(sys.argv)
    UIWindow = Ui_Main()
    UIWindow.show()
    sys.exit(app.exec_())

main1()