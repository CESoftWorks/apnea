__author__ = 'Constantinos Eleftheriou'

"""
Copyright (C) 2015 Constantinos Eleftheriou
    
    This file is part of Apnea.

    Apnea is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Apnea is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Apnea.  If not, see <http://www.gnu.org/licenses/>.
"""

from PySide.QtGui import QDialog, QAbstractItemView
from PySide.QtCore import *
import uidlg_selectpatient
from db_data import PatientData
from newpatient import NewPatientForm


class DialogSelectPatient(QDialog, uidlg_selectpatient.Ui_Dialog):

    def __init__(self, parent=None):
        super(DialogSelectPatient, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.loadAllPatients()
        self.selectedPatientId = None

    def uiConnect(self):
        self.buttonAddNewPatient.clicked.connect(self.buttonAddNewPatientClicked)
        self.buttonSelectPatient.clicked.connect(self.buttonSelectPatientClicked)
        self.tablePatients.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePatients.setSelectionMode(QAbstractItemView.SingleSelection)
        #self.buttonSelectPatient.setEnabled(False)

    def buttonAddNewPatientClicked(self):
        newpatientform = NewPatientForm()
        newpatientform.show()
        newpatientform.exec_()
        self.loadAllPatients()

    def buttonSelectPatientClicked(self):
        index = self.tablePatients.selectionModel().currentIndex()
        row = index.row()
        self.selectedPatientId = index.sibling(row, 0).data()
        self.close()

    def selectedPatient(self):
        return self.selectedPatientId

    def loadAllPatients(self):
        patients = PatientData().returnAll()
        self.tablePatients.setModel(patients)

    @staticmethod
    def getSelectedPatient(parent=None):
        """This function initializes the form and returns the
        selected patient id"""
        dialog = DialogSelectPatient(parent)
        result = dialog.exec_()
        patientid = dialog.selectedPatientId
        return patientid, result == dialog.Accepted
