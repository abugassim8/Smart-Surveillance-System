# importing libraries
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
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
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import winsound         # for sound
import time             # for sleep


from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QPushButton,QTextEdit,QFileDialog,QCompleter ,QMessageBox
from PyQt5 import uic
import sys
import os
import cv2
import shutil
import datetime
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage ,QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import tensorflow as tf
from scipy import misc
import cv2
import numpy as np
import facenet
import detect_face
import os
import time
from datetime import datetime, date
import pickle
import sqlite3
from preprocess import preprocesses
import classifier
#from profileDialog import Ui_Dialog2
from LoadProfile import Ui_Profile
#from faceresult import Ui_Dialog
from LoadFaceresult import Ui_Faceresult
#from faceresult import Ui_Dialog
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget,QMainWindow,QLabel
import sys
from classifier import training
import copy2
import time
from PyQt5 import QtSql
from PyQt5 import QtWidgets

# IMPORT QSS CUSTOM
from ui_styles import Style


QtWidgets.QApplication.setAtrribute(QtCore.Qt.AA_EnableHighDpiScaling,True)

## ==> GLOBALS
counter = 0

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1
from UI_functionsPyqt5 import *
from people_counter_camera import *
from close_window import *
from Login_UI_fun import  *

input_http_url = "http://192.168.43.1:8080/video"
modeldir = './model/20180402-114759.pb'
classifier_filename = './class/classifier.pkl'
npy = './npy'
train_img = "./train_img"
font = cv2.FONT_HERSHEY_SIMPLEX


class FlatGui(QMainWindow):
    def __init__(self):

        super().__init__()
        uic.loadUi("gui_base_old.ui",self)
        self.logic=0

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())
        self.logic = 0
        self.showMaximized()
        #self.loading_screen = LoadingScreen()
        self.start.clicked.connect(self.startClicked)
        self.pause.setEnabled(False)
        self.pause.clicked.connect(self.pauseClicked)
        self.train_butt.setEnabled(False)
        self.align_butt.clicked.connect(self.align_image)
        self.train_butt.clicked.connect(self.train_image)
        self.CreateAccount.clicked.connect(self.insertData)
        self.deleteButton.clicked.connect(self.deleteData)
        self.imageButton.clicked.connect(self.browse)
        self.folderButton.clicked.connect(self.Browsefolder)
        self.Submit.clicked.connect(self.insertNewData)
        self.search.clicked.connect(self.showData)
        self.radioMale.toggled.connect(self.onClicked)
        self.radioFemale.toggled.connect(self.onClicked)
        self.start.clicked.connect(self.startClicked)
        #self.exitbutton.clicked.connect(self.Toexit)
        self.people_count.clicked.connect(self.People)
        self.nameEdit.setClearButtonEnabled(True)
        self.people_count_rec_btn.clicked.connect(self.recorded_people)
        self.browse_spc_btn.clicked.connect(self.browse_spc)

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################


        ## REMOVE ==> STANDARD TITLE BAR
        UIPYQT5Functions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Main Window - Python Base')
        UIPYQT5Functions.labelTitle(self, 'Main Window - Python Base')
        UIPYQT5Functions.labelDescription(self, 'Smart Surveillance System')
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
        UIPYQT5Functions.addNewMenu(self, "Show Data", "btn_show_data", "url(:/16x16/icons/16x16/cil-magnifying-glass.png)",True)
        UIPYQT5Functions.addNewMenu(self, "Train new", "btn_train", "url(:/16x16/icons/16x16/cil-briefcase.png)",True)
        UIPYQT5Functions.addNewMenu(self, "Add Account", "btn_account", "url(:/16x16/icons/16x16/cil-dialpad.png)",True)
        UIPYQT5Functions.addNewMenu(self, "People Counting", "btn_people", "url(:/16x16/icons/16x16/cil-wrap-text.png)",True)
        ## ==> END ##

        # START MENU => SELECTION
        UIPYQT5Functions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.stackedWidget.setCurrentWidget(self.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIPYQT5Functions.userIcon(self, "SSS", "url(:/16x16/icons/16x16/cil-user.png)", True)
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

        conn = sqlite3.connect('FaceNetdb.db')
        cursor = conn.execute('SELECT NAME FROM Suspects''')
        pro = []
        for row in cursor:
            row = list(row)
            pro.append(row)
        name_list = [item for sublist in pro for item in sublist]
        print(name_list)

        completer = QCompleter(name_list)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        self.nameEdit_2.setCompleter(completer)


        #        self.lineEdit.editingFinished.connect(lambda: self.on_button())
        completer.activated.connect(self.on_completer)

    def on_completer(self, text):  # +++
        # nameList = text.split(', ')

        # self.lineEdit_2.setText(text)
        self.nameEdit_2.setText(text)

    # QtCore.QTimer.singleShot(200, lambda: self.lineEdit.setText(nameList[1]))  # +++

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

        # PAGE SHOW DATA
        if btnWidget.objectName() == "btn_show_data":
            self.stackedWidget.setCurrentWidget(self.page_showdata)
            UIPYQT5Functions.resetStyle(self, "btn_show_data")
            UIPYQT5Functions.labelPage(self, "Show User")
            btnWidget.setStyleSheet(UIPYQT5Functions.selectMenu(btnWidget.styleSheet()))

        # PAGE TRAIN
        if btnWidget.objectName() == "btn_train":
            self.stackedWidget.setCurrentWidget(self.page)
            UIPYQT5Functions.resetStyle(self, "btn_train")
            UIPYQT5Functions.labelPage(self, "Train new")
            btnWidget.setStyleSheet(UIPYQT5Functions.selectMenu(btnWidget.styleSheet()))


        # PAGE ACCOUNT
        if btnWidget.objectName() == "btn_account":
            self.stackedWidget.setCurrentWidget(self.page_2)
            UIPYQT5Functions.resetStyle(self, "btn_account")
            UIPYQT5Functions.labelPage(self, "Add New Account")
            btnWidget.setStyleSheet(UIPYQT5Functions.selectMenu(btnWidget.styleSheet()))

        # PAGE People Counting
        if btnWidget.objectName() == "btn_people":
            self.stackedWidget.setCurrentWidget(self.page_3)
            UIPYQT5Functions.resetStyle(self, "btn_people")
            UIPYQT5Functions.labelPage(self, "People Counting")
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


    @pyqtSlot()
    def draw_border(self,img, pt1, pt2, color, thickness, r, d):

        x1, y1 = pt1
        x2, y2 = pt2
        #  To make anglular turn remove + r and comment out ellipse
        # Top left
        cv2.line(img, (x1, y1), (x1 + d, y1), color, thickness)
        cv2.line(img, (x1, y1), (x1, y1 + d), color, thickness)
        # cv2.ellipse(img, (x1 , y1 ), (r, r), 180, 0, 90, color, thickness)
        # Top right
        cv2.line(img, (x2, y1), (x2 - d, y1), color, thickness)
        cv2.line(img, (x2, y1), (x2, y1 + d), color, thickness)
        # cv2.ellipse(img, (x2 , y1 + r), (r, r), 270, 0, 90, color, thickness)
        # Bottom left
        cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
        cv2.line(img, (x1, y2), (x1, y2 - d), color, thickness)
        # cv2.ellipse(img, (x1 + r, y2 ), (r, r), 90, 0, 90, color, thickness)
        # Bottom right
        cv2.line(img, (x2, y2), (x2 - d, y2), color, thickness)
        cv2.line(img, (x2, y2), (x2, y2 - d), color, thickness)
        # cv2.ellipse(img, (x2 , y2 ), (r, r), 0, 0, 90, color, thickness)

    # ----------------------------------------------------------------------------------
    # def copy_and_clear(self):
    #     self.nameEdit.setText(self.lin
    def convertToBinary(filename):
        with open(filename, 'rb') as file:
            blobdata = file.read()
        return blobdata

    def getProfile(self,Name,screenshot,ui,uicounter,best_class_probability):

        Name = (Name,)
        print("Data being selected")


        conn = sqlite3.connect('FaceNetdb.db')
        cursor = conn.execute('SELECT ID,NAME,RACE,PICTURE,GUI,Status FROM Suspects WHERE NAME = ?', Name)
        best_class_probability = best_class_probability * 100


        best_class_probability_str =  best_class_probability.__str__()

        for row in cursor:
            if row[4] == 0 and row[1] != 'Unknown' and row[5] == 'Wanted':
                conn.execute('UPDATE Suspects SET GUI = 1 WHERE NAME = ? ', Name)
                conn.commit()

                cv2.imwrite("D:/AI/Face/out.png", screenshot)

                self.dialog = QtWidgets.QDialog()

                # self.ui = Ui_Faceresult()

                self.ui[uicounter].show()

                print("Data being selected")
                resultID = row[0]
                rID = resultID.__str__()
                self.ui[uicounter].resultID_Edit.setText(rID)
                self.ui[uicounter].resultname_Edit.setText(row[1])
                self.ui[uicounter].resultrace_Edit.setText(row[2])
                daytime = str(datetime.now())
                print(daytime)
                date_is = daytime[:10]
                if  len(daytime[12:16]) == 5:
                    time_is = daytime[12:16]
                else:
                    time_is = daytime[11:16]
                self.ui[uicounter].resultID_Edit_3.setText(date_is)
                self.ui[uicounter].resultID_Edit_4.setText(time_is)
                print("ID name race")
                self.ui[uicounter].accuracy_Edit.setText(best_class_probability_str)
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(row[3], 'jpg')
                self.ui[uicounter].resultlabel.setPixmap(pixmap)
                winsound.Beep(440, 250)  # frequency, duration
                time.sleep(0.25)  # in seconds (0.25 is 250ms)

                winsound.Beep(600, 250)
                time.sleep(0.25)

                # livephoto = cv2.imread('out.png',0)
                # pixmap2 = QtGui.QPixmap()
                # pixmap2.loadFromData(livephoto,'png')
                self.ui[uicounter].resultlabel_2.setPixmap(QPixmap('out.png'))
                print("picture 3")

        conn.close()

    def startClicked(self):

        self.pause.setEnabled(True)
        self.pause.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-media-pause.png"))
        self.start.setEnabled(False)
        self.logic = 1
        with tf.Graph().as_default():
            gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.6)
            sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
            with sess.as_default():
                pnet, rnet, onet = detect_face.create_mtcnn(sess, npy)

                minsize = 40  # minimum size of face
                threshold = [0.6, 0.7, 0.7]  # three steps's threshold
                factor = 0.709  # scale factor
                margin = 44
                frame_interval = 3
                batch_size = 1000
                image_size = 182
                input_image_size = 160

                HumanNames = os.listdir(train_img)
                HumanNames.sort()

                print('Loading Model')
                facenet.load_model(modeldir)
                images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
                embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
                phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
                embedding_size = embeddings.get_shape()[1]

                classifier_filename_exp = os.path.expanduser(classifier_filename)
                with open(classifier_filename_exp, 'rb') as infile:
                    (model, class_names) = pickle.load(infile)

                video_capture = cv2.VideoCapture(1)
                c = 0
                video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

                print('Start Recognition')
                prevTime = 0
                self.ui = [Ui_Faceresult() for p in range(20)]
                uicounter = 0
                print('Yeah')
                while True:
                   print("NEw Frame True")
                   ret, frame = video_capture.read()
                   frame = cv2.resize(frame, (0, 0), fx=0.8, fy=0.8)

                   curTime = time.time() + 1  # calc fps
                   timeF = frame_interval
                   #cv2.putText(frame, str(datetime.now()), (350, 15), font, 0.56, (0, 0, 0), thickness=1, lineType=1)

                   if (c % timeF == 0):
                       find_results = []

                       if frame.ndim == 2:
                           frame = facenet.to_rgb(frame)
                       frame = frame[:, :, 0:3]
                       bounding_boxes, _ = detect_face.detect_face(frame, minsize, pnet, rnet, onet, threshold, factor)
                       nrof_faces = bounding_boxes.shape[0]
                       #print('Number of Detected_Faces : %d' % nrof_faces)

                       if nrof_faces > 0:
                           det = bounding_boxes[:, 0:4]
                           img_size = np.asarray(frame.shape)[0:2]

                           cropped = []
                           scaled = []
                           scaled_reshape = []
                           bb = np.zeros((nrof_faces, 4), dtype=np.int32)

                           for i in range(nrof_faces):
                               emb_array = np.zeros((1, embedding_size))

                               bb[i][0] = det[i][0]
                               bb[i][1] = det[i][1]
                               bb[i][2] = det[i][2]
                               bb[i][3] = det[i][3]

                               # inner exception
                               # if bb[i][0] <= 0 or bb[i][1] <= 0 or bb[i][2] >= len(frame[0]) or bb[i][3] >= len(frame):
                               #     print('Face is very close!')
                               #     continue

                               cropped.append(frame[bb[i][1]:bb[i][3], bb[i][0]:bb[i][2], :])
                               cropped[i] = facenet.flip(cropped[i], False)
                               scaled.append(misc.imresize(cropped[i], (image_size, image_size), interp='bilinear'))
                               scaled[i] = cv2.resize(scaled[i], (input_image_size, input_image_size),interpolation=cv2.INTER_CUBIC)
                               scaled[i] = facenet.prewhiten(scaled[i])
                               scaled_reshape.append(scaled[i].reshape(-1, input_image_size, input_image_size, 3))
                               feed_dict = {images_placeholder: scaled_reshape[i], phase_train_placeholder: False}
                               emb_array[0, :] = sess.run(embeddings, feed_dict=feed_dict)
                               predictions = model.predict_proba(emb_array)
                               # print(predictions)
                               best_class_indices = np.argmax(predictions, axis=1)
                               global best_class_probabilities
                               best_class_probabilities = predictions[np.arange(len(best_class_indices)), best_class_indices]


                               #print("predictions")
                               #print(best_class_indices,' with accuracy ',best_class_probabilities)

                               x = bb[i][0]
                               y = bb[i][1]
                               h = bb[i][2]
                               w = bb[i][3]

                               # print(best_class_probabilities)
                               if best_class_probabilities > 0.43:
                                   screenShot = frame[y:y+h,x-w:x+w]
                                   # cv2.imwrite("D:/AI/Face/out.png",screenShot)
                                   # livephoto = cv2.imread('out.png',0)
                                   # frame = cv2.imread("D:/AI/Face/out.png",0)
                                   #cv2.imshow("current",frame)
                                   self.draw_border(frame, (bb[i][0], bb[i][1]), (bb[i][2], bb[i][3]), (255, 255, 255), 2, 5,10)
                                   #cv2.rectangle(frame, (bb[i][0], bb[i][1]), (bb[i][2], bb[i][3]), (0, 255, 0), 2)    #boxing face

                                   # plot result idx under box
                                   text_x = bb[i][0]
                                   text_y = bb[i][3] + 20
                                   # print('Result Indices: ', best_class_indices[0])
                                   # print(HumanNames)

                                   for H_i in HumanNames:
                                       if HumanNames[best_class_indices[0]] == H_i:
                                           global result_names
                                           uicounter = uicounter + 1
                                           result_names = HumanNames[best_class_indices[0]]
                                           cv2.putText(frame, result_names, (text_x, text_y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1, (0, 0, 255), thickness=1, lineType=2)
                                           print(result_names)

                                           self.getProfile(result_names,screenShot,self.ui,uicounter,best_class_probabilities[0])
                                           break

                       else:
                           print('Alignment Failure')
                   self.displayImage(frame,1)
                   cv2.waitKey()

                   if(self.logic == 0):
                        break

            video_capture.release()
            cv2.destroyAllWindows()

    def pauseClicked(self):
        self.pause.setEnabled(False)
        self.pause.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-media-play.png"))
        self.start.setEnabled(True)
        self.logic = 0
        print("hi")

    def align_image(self):
        print("Hello Emma")
        input_datadir = './train_img'
        output_datadir = './pre_img'

        obj = preprocesses(input_datadir, output_datadir)
        nrof_images_total, nrof_successfully_aligned = obj.collect_data()

        print('Total number of images: %d' % nrof_images_total)
        print('Number of successfully aligned images: %d' % nrof_successfully_aligned)
        self.warning2("Warning", "Alignment Successfully Completed")
        self.warning2("Warning", 'Total number of images: %d' % nrof_images_total)
        self.warning2("Warning", 'Number of successfully aligned images: %d' % nrof_successfully_aligned)
        self.train_butt.setEnabled(True)
        self.align_butt.setEnabled(False)

    def train_image(self):
        self.train_butt.setEnabled(False)
        self.align_butt.setEnabled(True)
        datadir = './pre_img'
        modeldir = './model/20180402-114759.pb'  # for testing the 2018 .pb file
        classifier_filename = './class/classifier.pkl'
        print("Training Start")
        obj = training(datadir, modeldir, classifier_filename)
        get_file = obj.main_train()
        print('Saved classifier model to file "%s"' % get_file)
        self.warning2("Warning", "Training Successfully Completed")

    def deleteData(self):
        user = self.lineEdit_username.text()
        passu = self.lineEdit_password.text()

        conn = sqlite3.connect('FaceNetdb.db')

        conn.execute("DELETE FROM USERS WHERE USERNAME= ? and PASSWORD= ?",(user,passu))
        conn.commit()
        result = conn.execute("SELECT * FROM USERS")
        for data in result:
            print("Current Users Username: ",data[0] +" Password: ", data[1])
        conn.close()

    def insertData(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        conn = sqlite3.connect('FaceNetdb.db')
        conn.execute("INSERT INTO USERS VALUES(?,?)", (username, password))
        conn.commit()
        result = conn.execute("SELECT * FROM USERS")

        for data in result:
            print("Current Users Username: ",data[0] +" Password: ", data[1])
        conn.close()

    def cancel(self):
        print('cancel')


    def showData(self):

        id = self.IDEdit.text()
        name = self.nameEdit_2.text()
        race = self.raceEdit.text()

        conn = sqlite3.connect('FaceNetdb.db')


        cursor = conn.execute('''SELECT ID,NAME,GENDER,BIRTH_YEAR,RACE,CRIMINAL_RECORDS,PICTURE,Status
         FROM Suspects WHERE ID = ? or NAME = ? or RACE = ?''', (id,name,race))

        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Profile()
        self.ui.show()

        for row in cursor:
            print("Data being selected")
            profileID = row[0]
            pID = profileID.__str__()
            self.ui.profile_ID.setText(pID)
            self.ui.profile_name.setText(row[1])
            self.ui.profile_gender.setText(row[2])
            self.ui.profile_BD.setText(row[3])
            self.ui.profile_race.setText(row[4])
            self.ui.profile_record.setText(row[5])
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(row[6], 'jpg')
            self.ui.profilelabel.setPixmap(pixmap)
            if row[7] == 'Wanted':
                self.ui.radioWanted.setChecked(True)
            if row[7] == 'Captured':
                self.ui.radioCaptured.setChecked(True)
            if row[7] == 'Died':
                self.ui.radioDied.setChecked(True)




        conn.close()
        self.cancel()

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

    def warning2(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def browse(self):
        print("button pressed")
        global files
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "", "JPEG (*.jpg)")

        if files:
            print(files)
            self.ImageEdit.setText('{}'.format(files))




    def browse_spc(self):
        global files_video_recorded
        #files_video_recorded, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",)
        files_video_recorded, _ = QFileDialog.getOpenFileNames(self, 'Open File', 'c\\', 'Video files ( *.mp4, *.avi, *.mp4)')



        if files_video_recorded:
            print(files_video_recorded)
            files_video_recorded = files_video_recorded[0]
            self.Video_Edit_2.setText('{}'.format(files_video_recorded))


    def copydir(src, dst):
        h = os.getcwd()
        src = r"{}".format(src)
        if not os.path.isdir(dst):
            print("\n[!] No Such directory: [" + dst + "] !!!")
            exit(1)

        if not os.path.isdir(src):
            print("\n[!] No Such directory: [" + src + "] !!!")
            exit(1)
        if "\\" in src:
            c = "\\"
            tsrc = src.split("\\")[-1:][0]
        else:
            c = "/"
            tsrc = src.split("/")[-1:][0]

        os.chdir(dst)
        if os.path.isdir(tsrc):
            print("\n[!] The Directory Is already exists !!!")
            exit(1)
        try:
            os.mkdir(tsrc)
        except WindowsError:
            print("\n[!] Error: In[ {} ]\nPlease Check Your Dirctory Path !!!".format(src))
            exit(1)
        os.chdir(h)
        files = []
        for i in os.listdir(src):
            files.append(src + c + i)
        if len(files) > 0:
            for i in files:
                if not os.path.isdir(i):
                    shutil.copy2(i, dst + c + tsrc)

        print("\n[*] Done ! :)")

    def Browsefolder(self):
        global file
        file = QFileDialog.getExistingDirectory(self,"Select Directory")
        # if file:
        self.folderEdit.setText('{}'.format(file))
        print(file)





    def onClicked(self):
        global gender
        radioBtn = self.sender()
        if radioBtn.isChecked():
            gender = radioBtn.text()
            print("clicked")

    def insertNewData(self):
        name = self.nameEdit.text()
        records = self.recordEdit.text()
        race = self.raceinEdit.text()
        birthyear = self.birthyearEdit.text()
        picture_file = files[0]

        with open(picture_file, 'rb') as input_file:
            ablob = input_file.read()
            base = os.path.basename(picture_file)
            afile, ext = os.path.splitext(base)
            conn = sqlite3.connect('FaceNetdb.db')
            sql = '''INSERT INTO Suspects (NAME, GENDER, RACE ,BIRTH_YEAR,CRIMINAL_RECORDS,PICTURE, TYPE, FILE_NAME) VALUES(?, ?, ?, ?, ?,?,?,?);'''
            conn.execute(sql, [name, gender, race, birthyear, records, sqlite3.Binary(ablob), ext, afile])
            conn.commit()
            conn.close()

            src = file
            print(src)
            dest = "D:/AI/Face/npy/"+ name
            copy2.copytree(src, dest)

            self.nameEdit.setText('')
            self.recordEdit.setText('')
            self.raceinEdit.setText('')
            self.birthyearEdit.setText('')
            self.ImageEdit.setText('')
            self.folderEdit.setText('')
            print('cleared')

            self.warning2("Warning", "Correct details entered")

    def _set_text(self, text):
        return text

    def Toexit(self):
       # conn = sqlite3.connect('FaceNetdb.db')

        #conn.execute('UPDATE Suspects SET GUI = 0 ')
        #conn.commit()
        #conn.close()
        #self.close()
        #exit(0)
        self.main = Close_window()
        self.main.show()



    def People(self):
        self.main = main_func()
        self.main.show()

    def recorded_people(self):
        #files_video_recorded = self.Video_Edit_2.text()
        #files_video_recorded = 'D:\AI\Face\\test video\library_test.mp4'
        self.main = main_func(files_video_recorded)
        self.main.show()



# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):

        super().__init__()
        uic.loadUi("splash_screen.ui",self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(50)

        # CHANGE DESCRIPTION

        # Initial Text
        self.label_description.setText("<strong>WELCOME</strong> TO OUR APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(500,lambda: self.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        QtCore.QTimer.singleShot(6000,lambda: self.label_description.setText("<strong>LOADING</strong> DATABASE"))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        ## ==> APP FUNCTIONS
        ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Login()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


class Login(QMainWindow):

    def __init__(self):

        super().__init__()
        uic.loadUi("editedlogin.ui",self)



        self.loginButton.clicked.connect(self.login)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit.setValidator(QRegExpValidator(QRegExp("[a-zA-Z]+")))


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





    def showMessageBox(self,title,message):
        msgBox =QMessageBox()
        msgBox.setStyleSheet('QMessageBox {background-color: #5b5f91; color: white; font-size: 20px;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        connection = sqlite3.connect("FaceNetdb.db")
        result = connection.execute ("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if(len(result.fetchall())>0):
            print ("User Found !")
            # SHOW MAIN WINDOW
            self.main = FlatGui()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()


        else:
            print("User Not Found !")
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.showMessageBox('Warning','Invalid Username And Password')

        connection.close()




import files_rc

if __name__ =="__main__":


    App = QApplication(sys.argv)
    window = SplashScreen()
    window.show()
    sys.exit(App.exec())



