from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QPushButton,QTextEdit,QFileDialog,QCompleter
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
from datetime import datetime
import pickle
import sqlite3
from preprocess import preprocesses
import classifier
#from profileDialog import Ui_Dialog2
from LoadProfile import Ui_Profile
#from faceresult import Ui_Dialog
from LoadFaceresult import Ui_Faceresult
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget,QMainWindow,QLabel
import sys
from classifier import training
import copy2
import time
from PyQt5 import QtSql

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




input_http_url = "http://192.168.43.1:8080/video"
modeldir = './model/20180402-114759.pb'
classifier_filename = './class/classifier.pkl'
npy = './npy'
train_img = "./train_img"
font = cv2.FONT_HERSHEY_SIMPLEX

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450,450)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.label_animation = QLabel(self)

        self.movie = QMovie('GIF_Exported.gif')
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(10000,self.stopAnimation)

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

class Ui_Main(QMainWindow):


    def __init__(self):

        super().__init__()
        uic.loadUi("grid main.ui", self)

        self.logic = 0
        #self.showMaximized()
        self.loading_screen = LoadingScreen()
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
        self.exitbutton.clicked.connect(self.exit)
        #self.pushButton.clicked.connect(self.returnner)

    #def returnner(self):
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

    def on_completer(self, text):                                                    # +++
        #nameList = text.split(', ')

        #self.lineEdit_2.setText(text)
        self.lineEdit.setText(text)
       #QtCore.QTimer.singleShot(200, lambda: self.lineEdit.setText(nameList[1]))  # +++

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

    def getProfile(self,Name):


        Name = (Name,)
        conn = sqlite3.connect('FaceNetdb.db')
        cursor = conn.execute('SELECT ID,NAME,RACE,PICTURE,GUI FROM Suspects WHERE NAME = ?', Name)

        self.ui = [Ui_Faceresult() for p in range(20)]
        for p in range(20):
            for row in cursor:
                if row[4] == 0 and row[1] != 'Unknown':
                    conn.execute('UPDATE Suspects SET GUI = 1 WHERE NAME = ? ', Name)
                    conn.commit()

                    print('hrherr')
                    #self.ui[p] = Ui_Faceresult()
                    print("fsbgfgfcxg")

                    self.ui[p].show()

                    print("Data being selected")
                    resultID = row[0]
                    rID = resultID.__str__()
                    self.ui[p].resultID_Edit.setText(rID)
                    self.ui[p].resultname_Edit.setText(row[1])
                    self.ui[p].resultrace_Edit.setText(row[2])
                    print("ID name race")
                    # self.ui.accuracy_Edit.setText(best_class_probability)
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(row[3], 'jpg')

                    self.ui[p].resultlabel_2.setPixmap(pixmap)
                    print("picture 3")






        conn.close()

    def startClicked(self):

        self.pause.setEnabled(True)
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

                video_capture = cv2.VideoCapture(0)
                c = 0
                video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

                print('Start Recognition')
                prevTime = 0

                print('Yeah')
                while True:
                   print("True")
                   ret, frame = video_capture.read()
                   frame = cv2.resize(frame, (0, 0), fx=0.9, fy=0.9)

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
                       print('Number of Detected_Faces : %d' % nrof_faces)

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
                               best_class_probabilities = predictions[np.arange(len(best_class_indices)), best_class_indices]

                               #print("predictions")
                               print(best_class_indices,' with accuracy ',best_class_probabilities)

                               # print(best_class_probabilities)
                               if best_class_probabilities > 0.43:
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
                                           result_names = HumanNames[best_class_indices[0]]
                                           cv2.putText(frame, result_names, (text_x, text_y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1, (0, 0, 255), thickness=1, lineType=2)
                                           print(result_names)

                                           self.getProfile(result_names)
                                           break
                                           # if (profile != None):
                                           #     print("with id ", str(profile[0]))

                       else:
                           print('Alignment Failure')
                   self.displayImage(frame,1)
                   if cv2.waitKey(1) & 0xFF == ord('q'):
                       break

            video_capture.release()
            cv2.destroyAllWindows()

    def pauseClicked(self):
        self.pause.setEnabled(False)
        self.start.setEnabled(True)
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

    def showData(self):

        id = self.IDEdit.text()
        name = self.nameEdit_2.text()
        race = self.lineEdit_6.text()

        conn = sqlite3.connect('FaceNetdb.db')


        cursor = conn.execute('''SELECT ID,NAME,GENDER,BIRTH_YEAR,RACE,CRIMINAL_RECORDS,PICTURE
         FROM Suspects WHERE ID = ? or NAME = ? or RACE = ?''', (id,name,race))


        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Profile()
        #self.ui.setupUi(self.dialog)
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
            pixmap.loadFromData(row[6],'jpg')
            self.ui.profilelabel.setPixmap(pixmap)



        conn.close()

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
            base=os.path.basename(picture_file)
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

    def exit(self):
        conn = sqlite3.connect('FaceNetdb.db')

        conn.execute('UPDATE Suspects SET GUI = 0 ')
        conn.commit()
        conn.close()
        self.close()
        exit(0)





from images import main_source_rc

def main1():
    app = QtWidgets.QApplication(sys.argv)
    UIWindow = Ui_Main()
    UIWindow.show()
    sys.exit(app.exec_())
main1()