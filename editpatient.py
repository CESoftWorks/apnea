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
from PySide.QtCore import QDate
from db_data import PatientData
from db_queries import PatientQueries
import ui_editpatient


class EditPatientForm(QDialog, ui_editpatient.Ui_Dialog):

    def __init__(self, patientid, parent=None):
        super(EditPatientForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.patientid = patientid
        self.fetch_patient(patientid)

    def uiConnect(self):
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.btnCalculateBmi.clicked.connect(self.btnCalculateBmiClicked)
        self.btnReset.clicked.connect(self.btnResetClicked)
        self.spnHeight.setMaximum(220)
        self.spnWeight.setMaximum(300)
        self.spnWeight.setDecimals(0)

    def btnSaveClicked(self):
        q_status, q_error = self.update_patient()
        if q_status:
            QMessageBox.information(self, "Success", "Patient record updated successfully")
            self.close()
        else:
            QMessageBox.warning(self, "Failure", "Could not update patient record! Error: {}".format(
                q_error))

    def btnCalculateBmiClicked(self):
        weight = Decimal(self.spnWeight.value())
        height = Decimal(self.spnHeight.value()) / 100
        # Return 0 if weight or height is 0
        if weight == 0 or height == 0:
            self.txtBmi.setText("0")
            return
        bmi = weight / (height * height)
        self.txtBmi.setText(str(round(bmi, 2)))

    def btnResetClicked(self):
        # Set original values
        self.fetch_patient(self.patientid)

    def fetch_patient(self, patient_id):
        patient_data = PatientData()
        patient_record = patient_data.returnSingleById(patient_id)
        self.txtPatientId.setText(str(patient_record['patientid']))
        self.txtName.setText(patient_record['name'])
        self.txtSurname.setText(patient_record['surname'])
        self.cbxSex.setCurrentIndex(self.cbxSex.findText(patient_record['sex']))
        self.dateDob.setDate(QDate.fromString(patient_record['dob']))
        self.txtPhone.setText(patient_record['phone'])
        self.spnHeight.setValue(Decimal.from_float(float(patient_record['height'])))
        self.spnWeight.setValue(Decimal.from_float(float(patient_record['weight'])))
        self.txtBmi.setText(str(patient_record['bmi']))
        self.spnEpsworth.setValue(int(patient_record['epsworth']))
        self.txtBriefAssessment.setPlainText(patient_record['assessment'])

    def update_patient(self):
        patient_record = PatientQueries()

        pid = self.patientid
        name = self.txtName.text()
        surname = self.txtSurname.text()
        sex = self.cbxSex.currentText()
        dob = self.dateDob.text()
        phone = self.txtPhone.text()
        height = self.spnHeight.text()
        weight = self.spnWeight.text()
        bmi = self.txtBmi.text()
        epsworth = self.spnEpsworth.text()
        assessment = self.txtBriefAssessment.document().toPlainText()

        q_status, q_error = patient_record.update(patientid=pid, u_name=name, u_surname=surname, u_sex=sex,
                                                  u_dob=dob, u_phone=phone, u_height=height, u_weight=weight,
                                                  u_bmi=bmi, u_epsworth=epsworth, u_assessment=assessment)

        return q_status, q_error


# TESTING
if __name__ == '__main__':
    from PySide.QtGui import QApplication
    import sys
    import db_init

    app = QApplication(sys.argv)
    db_init.DatabaseInit()

    editform = EditPatientForm(111222)
    editform.show()
    editform.exec_()

    app.exec_()
