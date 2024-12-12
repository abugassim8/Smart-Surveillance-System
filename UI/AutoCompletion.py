from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter


class Ui_MainWindow(object):

#    def on_button(self):
    def on_button(self, text):                                                    # +++
        nameList = text.split(', ')

        self.lineEdit_2.setText(nameList[0])
        self.lineEdit.setText(nameList[1])
       #QtCore.QTimer.singleShot(200, lambda: self.lineEdit.setText(nameList[1]))  # +++

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 254)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 180, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 90, 180, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")

        food = ["pizza, chikin", "chikin, pizza", "chikin, pizza pizza", "chikin, pizza", "fried, pizza"]

        completer = QCompleter(food)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        self.lineEdit.setCompleter(completer)

#        self.lineEdit.editingFinished.connect(lambda: self.on_button())
        completer.activated.connect(self.on_button)                                    # +++

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

