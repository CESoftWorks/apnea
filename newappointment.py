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
from PySide.QtCore import QDate
from db_queries import AppointmentQueries
import ui_newappointment
from dialog_selectpatient import DialogSelectPatient
from dialog_appointmentdatesassign import DialogSelectAppointmentDate


class NewAppointmentForm(QDialog, ui_newappointment.Ui_Dialog):
    def __init__(self, parent=None):
        super(NewAppointmentForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.appointment_date = None

    def uiConnect(self):
        self.buttonAssignDate.clicked.connect(self.buttonAssignDateClicked)
        self.buttonBookWithoutDate.clicked.connect(self.buttonBookWithoutDateClicked)
        self.buttonPatientSelect.clicked.connect(self.buttonPatientSelectClicked)
        self.buttonProceed.clicked.connect(self.buttonProceedClicked)
        self.buttonCancel.clicked.connect(self.buttonCancelClicked)
        self.dateEdit.setDate(QDate.currentDate())  # Default regdate to today's date
        self.dateEdit.setCalendarPopup(True)  # That's useful, right?

    def buttonPatientSelectClicked(self):
        selectedpatient, result = DialogSelectPatient.getSelectedPatient()
        self.labelPatientID.setText(str(selectedpatient))

    def buttonAssignDateClicked(self):
        # Check if patient was selected / default label value was changed
        patientid = self.labelPatientID.text()
        if patientid == "" or patientid == "Please select a patient" or patientid == "None":
            QMessageBox.warning(self, "Warning", "No patient selected!")
            return
        # Disable button to disallow dialog duplication
        self.buttonAssignDate.setEnabled(False)
        self.appointment_date = DialogSelectAppointmentDate.getDate(patientid)
        if self.appointment_date is not None:
            self.label.setText("Appointment date: " + str(self.appointment_date))
            # Disable book without date button
            self.buttonBookWithoutDate.setEnabled(False)
            # Chance cancel button to Book and Close button
            self.buttonCancel.setText("Book && Close")
            return
        # If no date was set, turn the button back on
        self.buttonAssignDate.setEnabled(True)

    def buttonBookWithoutDateClicked(self):
        patient = self.labelPatientID.text()
        if patient == "" or patient == "Please select a patient" or patient == "None":
            QMessageBox.warning(self, "Warning", "No patient selected!")
            return
        ok = QMessageBox.question(self, "No date set",
                                  "Are you sure you want to book an appointment with no test date?"
                                  "\nPlease note that you can set a test date at a later stage.",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ok == QMessageBox.No:
            # Give 'em another chance
            return
        success, error = self.insertAppointment()
        if success:
            QMessageBox.information(self, "Success", "New appointment booked with no test date!")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Could not add new appointment! Error: {}".format(error))

    def buttonProceedClicked(self):
        return

    def buttonCancelClicked(self):
        if self.appointment_date is not None:
            # If an appointment date has been selected, this is now Book and Close button
            success, error = self.insertAppointment()
            if success:
                QMessageBox.information(self, "Success", "New appointment booked!")
                self.close()
                return
            QMessageBox.warning(self, "Error", "Could not add new appointment! Error: {}".format(error))
            return
        self.close()

    def insertAppointment(self):
        # Parse form data
        testdate = self.appointment_date
        patientid = int(self.labelPatientID.text())
        regdate = self.dateEdit.text()
        refdoctor = self.txtRefDoc.text()
        # Set appointment priority
        if self.cbxPriority.currentText() == "Urgent":
            priority = 1
        elif self.cbxPriority.currentText() == "Medium":
            priority = 2
        else:
            priority = 3
        notes = str(self.txtNotes.document().toPlainText())
        # Connect to database and add appointment
        db_appointments = AppointmentQueries()
        q_status, q_error = db_appointments.insert(patientid=patientid,
                                                   regdate=regdate,
                                                   refdoctor=refdoctor,
                                                   priority=priority,
                                                   testdate=testdate,
                                                   notes=notes)
        return q_status, q_error
