# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faceresult.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(654, 484)
        self.resultlabel = QtWidgets.QLabel(Dialog)
        self.resultlabel.setGeometry(QtCore.QRect(70, 60, 161, 151))
        self.resultlabel.setScaledContents(True)
        self.resultlabel.setObjectName("resultlabel")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 310, 20, 16))
        self.label_2.setObjectName("label_2")
        self.resultID_Edit = QtWidgets.QLineEdit(Dialog)
        self.resultID_Edit.setGeometry(QtCore.QRect(260, 310, 113, 20))
        self.resultID_Edit.setObjectName("resultID_Edit")
        self.resultname_Edit = QtWidgets.QLineEdit(Dialog)
        self.resultname_Edit.setGeometry(QtCore.QRect(260, 350, 113, 20))
        self.resultname_Edit.setObjectName("resultname_Edit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 350, 31, 16))
        self.label_3.setObjectName("label_3")
        self.accuracy_Edit = QtWidgets.QLineEdit(Dialog)
        self.accuracy_Edit.setGeometry(QtCore.QRect(260, 430, 113, 20))
        self.accuracy_Edit.setObjectName("accuracy_Edit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 430, 51, 16))
        self.label_4.setObjectName("label_4")
        self.resultrace_Edit = QtWidgets.QLineEdit(Dialog)
        self.resultrace_Edit.setGeometry(QtCore.QRect(260, 390, 113, 20))
        self.resultrace_Edit.setObjectName("resultrace_Edit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 390, 31, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 420, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.resultID_Edit_2 = QtWidgets.QLineEdit(Dialog)
        self.resultID_Edit_2.setGeometry(QtCore.QRect(500, 310, 113, 20))
        self.resultID_Edit_2.setObjectName("resultID_Edit_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(419, 310, 61, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 31, 16))
        self.label_7.setObjectName("label_7")
        self.resultID_Edit_3 = QtWidgets.QLineEdit(Dialog)
        self.resultID_Edit_3.setGeometry(QtCore.QRect(60, 310, 113, 20))
        self.resultID_Edit_3.setObjectName("resultID_Edit_3")
        self.resultID_Edit_4 = QtWidgets.QLineEdit(Dialog)
        self.resultID_Edit_4.setGeometry(QtCore.QRect(60, 350, 113, 20))
        self.resultID_Edit_4.setObjectName("resultID_Edit_4")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 350, 31, 16))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.resultlabel.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "ID"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.label_4.setText(_translate("Dialog", "Accuracy"))
        self.label_5.setText(_translate("Dialog", "Race"))
        self.pushButton.setText(_translate("Dialog", "previous"))
        self.pushButton_2.setText(_translate("Dialog", "next"))
        self.label_6.setText(_translate("Dialog", "Match value"))
        self.label_7.setText(_translate("Dialog", "Date"))
        self.label_8.setText(_translate("Dialog", "Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
