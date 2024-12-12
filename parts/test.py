import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QFileDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore


class FileCopyProgress(QWidget):


    def __init__(self, parent=None, src=None, dest=None):
        super(FileCopyProgress, self).__init__()

        self.src = src
        self.dest = dest
        self.build_ui()

    def build_ui(self):

        hbox = QVBoxLayout()

        lbl_src = QLabel('Source: ' + self.src)
        lbl_dest = QLabel('Destination: ' + self.dest)
        self.pb = QProgressBar()

        self.pb.setMinimum(0)
        self.pb.setMaximum(100)
        self.pb.setValue(0)

        hbox.addWidget(lbl_src)
        hbox.addWidget(lbl_dest)
        hbox.addWidget(self.pb)
        self.setLayout(hbox)

        self.setWindowTitle('File copy')
        self.auto_start_timer = QtCore.QTimer()
        self.auto_start_timer.singleShot(2000, lambda: self.copyFilesWithProgress(self.src, self.dest, self.progress, self.copydone))
        self.show()

    def progress(self, done, total):
        progress = int(round((done/float(total))*100))

        try:
            self.pb.setValue(progress)
        except:
            pass

        app.processEvents()

    def copydone(self):
        self.pb.setValue(100)
        self.close()

    def countfiles(self, _dir):
        files = []

        if os.path.isdir(_dir):
            for path, dirs, filenames in os.walk(_dir):
                files.extend(filenames)
        return len(files)

    def makedirs(self, dest):
        if not os.path.exists(dest):
            os.makedirs(dest)

    @pyqtSlot()
    def copyFilesWithProgress(self, srcc, destt, callback_progress, callback_copydone):
        numFiles = self.countfiles(srcc)
        if numFiles > 0:
            dest = os.path.join(destt, srcc.replace(BASE_DIR, '').replace('\\', ''))
            print(''.join(['Destination: ', dest]))
            self.makedirs(dest)

            numCopied = 0
            for path, dirs, filenames in os.walk(srcc):
                for directory in dirs:
                    destDir = path.replace(srcc,dest)
                    self.makedirs(os.path.join(destDir, directory))
                for sfile in filenames:
                    srcFile = os.path.join(path, sfile)
                    destFile = os.path.join(path.replace(srcc, dest), sfile)
                    shutil.copy(srcFile, destFile)

                    numCopied += 1
                    callback_progress(numCopied, numFiles)
            callback_copydone()




BASE_DIR = 'C:\\Users'

