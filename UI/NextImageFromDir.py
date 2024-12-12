from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtWidgets import QFileDialog

class ImageLoader(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        layout = QtWidgets.QGridLayout(self)

        self.label = QtWidgets.QLabel()
        layout.addWidget(self.label, 0, 0, 1, 2)
        self.label.setMinimumSize(200, 200)
        # the label alignment property is always maintained even when the contents
        # change, so there is no need to set it each time
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.loadImageButton = QtWidgets.QPushButton('Load image')
        layout.addWidget(self.loadImageButton, 1, 0)

        self.nextImageButton = QtWidgets.QPushButton('Next image')
        layout.addWidget(self.nextImageButton)

        self.loadImageButton.clicked.connect(self.loadImage)
        self.nextImageButton.clicked.connect(self.nextImage)

        self.dirIterator = None
        self.fileList = []

    def loadImage(self):
        filename, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "", "JPEG (*.jpg)")
        if filename:
            pixmap = QtGui.QPixmap(filename).scaled(self.label.size(),
                QtCore.Qt.KeepAspectRatio)
            if pixmap.isNull():
                return
            self.label.setPixmap(pixmap)
            dirpath = os.path.dirname(filename)
            self.fileList = []
            for f in os.listdir(dirpath):
                fpath = os.path.join(dirpath, f)
                if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg')):
                    self.fileList.append(fpath)
            self.fileList.sort()
            self.dirIterator = iter(self.fileList)

            while True:
                # cycle through the iterator until the current file is found
                if next(self.dirIterator) == filename:
                    break

    def nextImage(self):
        # ensure that the file list has not been cleared due to missing files
        if self.fileList:
            try:
                filename = next(self.dirIterator)
                pixmap = QtGui.QPixmap(filename).scaled(self.label.size(),
                    QtCore.Qt.KeepAspectRatio)
                if pixmap.isNull():
                    # the file is not a valid image, remove it from the list
                    # and try to load the next one
                    self.fileList.remove(filename)
                    self.nextImage()
                else:
                    self.label.setPixmap(pixmap)
            except:
                # the iterator has finished, restart it
                self.dirIterator = iter(self.fileList)
                self.nextImage()
        else:
            # no file list found, load an image
            self.loadImage()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    imageLoader = ImageLoader()
    imageLoader.show()
    sys.exit(app.exec_())