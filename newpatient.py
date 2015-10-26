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

from decimal import Decimal
from PySide.QtGui import QDialog, QMessageBox
import ui_newpatient
from db_queries import PatientQueries


class NewPatientForm(QDialog,
                     ui_newpatient.Ui_Dialog):

    def __init__(self, parent=None):
        super(NewPatientForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()

    def uiConnect(self):
        # Map button clicked events to appropriate methods
        self.btnCalculateBmi.clicked.\
            connect(self.btnCalculateBmiClicked)
        self.btnReset.clicked.connect(self.btnResetClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.btnSaveAddNew.clicked.\
            connect(self.btnSaveAddNewClicked)
        self.spnWeight.setMinimum(0)
        self.spnHeight.setMinimum(0)
        self.spnHeight.setMaximum(220)
        self.spnWeight.setMaximum(300)
        self.spnWeight.setDecimals(0)

    def btnCalculateBmiClicked(self):
        # Calculate BMI using weight and height data
        weight = Decimal(self.spnWeight.value())
        height = Decimal(self.spnHeight.value()) / 100
        # Return 0 if weight or height is 0
        if weight == 0 or height == 0:
            self.txtBmi.setText("0")
            return
        bmi = weight / (height * height)
        # Give answer in BMI textbox to 2 dp
        self.txtBmi.setText(str(round(bmi, 2)))

    def btnResetClicked(self):
        # Clear all fields
        self.clearFields()

    def btnSaveClicked(self):
        q_status, q_error = self.insertPatient()
        if q_status:
            QMessageBox.information(self, "Success", "New patient record added successfully")
            self.close()
        else:
            QMessageBox.warning(self, "Failure", "Could not add new patient! Error: {}".format(
                q_error))
            self.clearFields()  # Clear all fields

    def btnSaveAddNewClicked(self):
        success, error = self.insertPatient()
        if success:
            QMessageBox.information(self, "Success", "New patient record added successfully")
            self.clearFields()
        else:
            QMessageBox.warning(self, "Failure", "Could not add new patient! Error: {}".format(
                error))
            self.clearFields()

    def insertPatient(self):
        # Insert new patient and return query status
        # TODO Add form data validation?
        db_patients = PatientQueries()
        q_status, q_error = db_patients.insert(patientid=self.txtPatientId.text(),
                                               name=self.txtName.text(),
                                               surname=self.txtSurname.text(),
                                               sex=self.cbxSex.currentText(),
                                               dob=self.dateDob.text(),
                                               phone=self.txtPhone.text(),
                                               height=self.spnHeight.text(),
                                               weight=self.spnWeight.text(),
                                               bmi=self.txtBmi.text(),
                                               epsworth=self.spnEpsworth.text(),
                                               assessment=str(self.txtBriefAssessment.document().toPlainText()))
        return q_status, q_error

    def clearFields(self):
        self.txtPatientId.clear()
        self.txtName.clear()
        self.txtSurname.clear()
        self.txtPhone.clear()
        self.txtBriefAssessment.clear()
        self.txtBmi.clear()
        self.spnWeight.minimum()
        self.spnHeight.minimum()
        self.dateDob.minimumDate()
        self.cbxSex.clear()
        self.spnEpsworth.minimum()
        self.txtPatientId.setFocus()
