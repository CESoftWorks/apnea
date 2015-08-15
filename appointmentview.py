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

from PySide.QtGui import QDialog, QMessageBox
import ui_appointmentview
from db_data import AppointmentData, PatientData
from editpatient import EditPatientForm
from db_queries import AppointmentQueries


class AppointmentViewForm(QDialog, ui_appointmentview.Ui_Dialog):

    def __init__(self, appointment_id, patient_id, parent=None):
        super(AppointmentViewForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.fetch_appointment(appointment_id)
        self.fetch_patient(patient_id)

        self.doc_report = None
        self.psg_report = None
        self.ref_doc = None

    def uiConnect(self):
        self.buttonAttachDocReport.clicked.connect(self.buttonAttachDocReportClicked)
        self.buttonAttachPsgReport.clicked.connect(self.buttonAttachPsgReportClicked)
        self.buttonEditPatient.clicked.connect(self.buttonEditPatientClicked)
        self.buttonOpenPsgReport.clicked.connect(self.buttonOpenPsgReportClicked)
        self.buttonOpenDocReport.clicked.connect(self.buttonOpenDocReportClicked)
        self.buttonSave.clicked.connect(self.buttonSaveClicked)
        self.buttonViewPreviousAppointments.clicked.connect(self.buttonViewPreviousAppointmentsClicked)
        self.buttonAttachDocReport.setEnabled(False)
        self.buttonOpenDocReport.setEnabled(False)
        self.buttonAttachPsgReport.setEnabled(False)
        self.buttonOpenPsgReport.setEnabled(False)

    def buttonEditPatientClicked(self):
        edit_patient = EditPatientForm(self.txtPatientId.text())
        edit_patient.show()
        edit_patient.exec_()

    def buttonViewPreviousAppointmentsClicked(self):
        return

    def buttonSaveClicked(self):
        self.update_appointment()

    def buttonAttachPsgReportClicked(self):
        return

    def buttonOpenPsgReportClicked(self):
        return

    def buttonAttachDocReportClicked(self):
        return

    def buttonOpenDocReportClicked(self):
        return

    def fetch_appointment(self, appointment_id):
        app_data = AppointmentData()
        app_record = app_data.returnSingleById(appointment_id)
        self.txtAppointmentDate.setText(app_record['testdate'])
        self.txtAppointmentRegDate.setText(app_record['regdate'])
        self.txtAppointmentAhi.setText(str(app_record['ahi']))
        self.txtAppointmentDiagnosis.setPlainText(app_record['diagnosis'])
        self.txtAppointmentTreatment.setPlainText(app_record['treatment'])
        self.txtAppointmentNotes.setPlainText(app_record['notes'])

        self.psg_report = app_record['psgreport']
        self.doc_report = app_record['doctorreport']
        self.ref_doc = app_record['refdoc']

    def fetch_patient(self, patient_id):
        patient_data = PatientData()
        patient_record = patient_data.returnSingleById(patient_id)
        self.txtPatientId.setText(str(patient_record['patientid']))
        self.txtPatientName.setText(patient_record['name'])
        self.txtPatientSurname.setText(patient_record['surname'])
        self.txtPatientDob.setText(patient_record['dob'])
        self.txtPatientSex.setText(patient_record['sex'])
        self.txtPatientPhone.setText(patient_record['phone'])
        self.txtPatientHeight.setText(str(patient_record['height']))
        self.txtPatientWeight.setText(str(patient_record['weight']))
        self.txtPatientBmi.setText(str(patient_record['bmi']))
        self.txtPatientEpsworth.setText(str(patient_record['epsworth']))
        self.txtPatientAssessment.setPlainText(patient_record['assessment'])

    def update_appointment(self):
        appointment_record = AppointmentQueries()

        app_id = self.appointment_id
        test_date = self.txtAppointmentDate.text()
        reg_date = self.txtAppointmentRegDate.text()
        ref_doc = self.ref_doc
        priority = 0
        ahi = self.txtAppointmentAhi.text()
        diagnosis = self.txtAppointmentDiagnosis.document().toPlainText()
        treatment = self.txtAppointmentTreatment.document().toPlainText()
        doc_report = self.doc_report
        psg_report = self.psg_report
        notes = self.txtAppointmentNotes.document().toPlainText()

        q_status, q_error = appointment_record.update(appointmentid=app_id, u_testdate=test_date,
                                                      u_regdate=reg_date, u_refdoctor=ref_doc,
                                                      u_priority=priority, u_ahi=ahi, u_diagnosis=diagnosis,
                                                      u_treatment=treatment, u_doctorreport=doc_report,
                                                      u_psgreport=psg_report, u_notes=notes)

        if q_status:
            QMessageBox.information(self, "Success", "Appointment updated successfully")
            self.buttonCancel.setText("Close")  # Change text to close instead of cancel
        else:
            QMessageBox.warning(self, "Failure", "Could not update appointment! Error: {}".format(
                q_error))
