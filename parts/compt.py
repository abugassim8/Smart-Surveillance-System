from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QCompleter
from PyQt5 import uic
import sys
class Ui_Main(QMainWindow):

    def __init__(self):

        super().__init__()
        uic.loadUi("compt.ui",self)

        food = ["pizza", "chikin", "chikin", "chikin", "fried"]

        completer = QCompleter(food)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        self.lineEdit.setCompleter(completer)

        #        self.lineEdit.editingFinished.connect(lambda: self.on_button())
        completer.activated.connect(self.on_button)

    def on_button(self, text):                                                    # +++
        #nameList = text.split(', ')

        #self.lineEdit_2.setText(text)
        self.lineEdit.setText(text)
       #QtCore.QTimer.singleShot(200, lambda: self.lineEdit.setText(nameList[1]))  # +++

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Ui_Main()
    mainWin.show()
    sys.exit(app.exec_())