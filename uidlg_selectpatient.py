# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgselectpatient.ui'
#
# Created: Thu Aug  6 18:48:28 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 385)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tablePatients = QtGui.QTableView(Dialog)
        self.tablePatients.setObjectName("tablePatients")
        self.verticalLayout.addWidget(self.tablePatients)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.txtSearch = QtGui.QLineEdit(Dialog)
        self.txtSearch.setObjectName("txtSearch")
        self.horizontalLayout.addWidget(self.txtSearch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonSelectPatient = QtGui.QPushButton(Dialog)
        self.buttonSelectPatient.setObjectName("buttonSelectPatient")
        self.horizontalLayout_2.addWidget(self.buttonSelectPatient)
        self.buttonAddNewPatient = QtGui.QPushButton(Dialog)
        self.buttonAddNewPatient.setObjectName("buttonAddNewPatient")
        self.horizontalLayout_2.addWidget(self.buttonAddNewPatient)
        self.buttonCancel = QtGui.QPushButton(Dialog)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout_2.addWidget(self.buttonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_2.setBuddy(self.txtSearch)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonCancel, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Select an Existing Patient</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSelectPatient.setText(QtGui.QApplication.translate("Dialog", "Select Patient", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAddNewPatient.setText(QtGui.QApplication.translate("Dialog", "Add New Patient", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

