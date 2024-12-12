# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profileDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(655, 468)
        self.profilelabel = QtWidgets.QLabel(Dialog)
        self.profilelabel.setGeometry(QtCore.QRect(20, 30, 211, 191))
        self.profilelabel.setScaledContents(True)
        self.profilelabel.setObjectName("profilelabel")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 350, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(90, 350, 141, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.genderEdit = QtWidgets.QLineEdit(Dialog)
        self.genderEdit.setGeometry(QtCore.QRect(90, 400, 141, 20))
        self.genderEdit.setObjectName("genderEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 400, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.birthEdit = QtWidgets.QLineEdit(Dialog)
        self.birthEdit.setGeometry(QtCore.QRect(440, 310, 141, 20))
        self.birthEdit.setObjectName("birthEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 310, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.raceEdit = QtWidgets.QLineEdit(Dialog)
        self.raceEdit.setGeometry(QtCore.QRect(440, 350, 141, 20))
        self.raceEdit.setObjectName("raceEdit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(250, 350, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 400, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.recordEdit = QtWidgets.QLineEdit(Dialog)
        self.recordEdit.setGeometry(QtCore.QRect(440, 400, 141, 51))
        self.recordEdit.setObjectName("recordEdit")
        self.idEdit = QtWidgets.QLineEdit(Dialog)
        self.idEdit.setGeometry(QtCore.QRect(90, 310, 141, 20))
        self.idEdit.setObjectName("idEdit")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 310, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.profilelabel.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "NAME :"))
        self.label_3.setText(_translate("Dialog", "GENDER :"))
        self.label_4.setText(_translate("Dialog", "BIRTH YEAR :"))
        self.label_5.setText(_translate("Dialog", "RACE :"))
        self.label_6.setText(_translate("Dialog", "CRIMINAL RECORD :"))
        self.label_7.setText(_translate("Dialog", "ID :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
