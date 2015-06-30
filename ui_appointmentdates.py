# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appointmentdates.ui'
#
# Created: Tue Jun 30 12:51:44 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(516, 504)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.calendarDatesSelect = QtGui.QCalendarWidget(Dialog)
        self.calendarDatesSelect.setObjectName("calendarDatesSelect")
        self.verticalLayout.addWidget(self.calendarDatesSelect)
        self.listAllDates = QtGui.QListView(Dialog)
        self.listAllDates.setObjectName("listAllDates")
        self.verticalLayout.addWidget(self.listAllDates)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btnAddDate = QtGui.QPushButton(Dialog)
        self.btnAddDate.setObjectName("btnAddDate")
        self.verticalLayout_2.addWidget(self.btnAddDate)
        self.btnRemoveDate = QtGui.QPushButton(Dialog)
        self.btnRemoveDate.setObjectName("btnRemoveDate")
        self.verticalLayout_2.addWidget(self.btnRemoveDate)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.btnBack = QtGui.QPushButton(Dialog)
        self.btnBack.setObjectName("btnBack")
        self.verticalLayout_2.addWidget(self.btnBack)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Please enter dates available <br/>for polysomnography appointments</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddDate.setText(QtGui.QApplication.translate("Dialog", "Add Date", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemoveDate.setText(QtGui.QApplication.translate("Dialog", "Remove Date", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBack.setText(QtGui.QApplication.translate("Dialog", "Back", None, QtGui.QApplication.UnicodeUTF8))

