
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMainWindow,QApplication,QPushButton,QTextEdit
from PyQt5.uic import loadUi
import sys
import sqlite3
import shutil
import test
import re

class Ui_Details(QMainWindow):
    def __init__(self):

        super(Ui_Details, self).__init__()
        loadUi("details.ui",self)

        self.Browsefile.clicked.connect(self.Browse)

        self.browsefolder.clicked.connect(self.Browsefolder)

        self.Submit.clicked.connect(self.insertData)

    def warning(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def Browse(self):
        print("button pressed")
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "JPEG (*.jpg)")
        if files:
            print(files)
            self.Imagetext.setText('{}'.format(files))

    def _set_text(self, text):
        return text




        #with open(path, 'rb') as f:
         #   m = f.read()
          #  print(m)
    def Browsefolder(self):
        global file
        file = QFileDialog.getExistingDirectory(self,"Select Directory")
        print(file)

        # test.FileCopyProgress(src=filename, dest='C:\\Users\Hega\Desktop\\New_Folder_2')
    def insertData(self):
        name = self.nameEdit.text()
        records = self.recordEdit.text()
        picture = self.surnameEdit.text()

        conn = sqlite3.connect('FaceNetdb.db')
        conn.execute("INSERT INTO Suspects(NAME , CRIMINAL_RECORDS, PICTURE) VALUES(?,?,?)", (name, records, picture))
        conn.commit()

        conn.close()
        self.warning("Warning", "Correct details entered")
        src = file
        dest = "D:\AI\Face\ImageGUI"
        destination = shutil.copytree(src, dest, copy_function=shutil.copy)
        print(destination)
app = QtWidgets.QApplication(sys.argv)
UIDetails = Ui_Details()
UIDetails.show()
sys.exit(app.exec_())
