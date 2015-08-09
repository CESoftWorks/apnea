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


class AppointmentViewForm(QDialog, ui_appointmentview.Ui_Dialog):

    def __init__(self, appointment_id, patient_id, parent=None):
        super(AppointmentViewForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.fetch_appointment(appointment_id)
        self.fetch_patient(patient_id)

    def uiConnect(self):
        self.buttonAttachDocReport.clicked.connect(self.buttonAttachDocReportClicked)
        self.buttonAttachPsgReport.clicked.connect(self.buttonAttachPsgReportClicked)
        self.buttonEditPatient.clicked.connect(self.buttonEditPatientClicked)
        self.buttonOpenPsgReport.clicked.connect(self.buttonOpenPsgReportClicked)
        self.buttonOpenDocReport.clicked.connect(self.buttonOpenDocReportClicked)
        self.buttonSave.clicked.connect(self.buttonSaveClicked)
        self.buttonSaveAndAdd.clicked.connect(self.buttonSaveAndAddClicked)
        self.buttonViewPreviousAppointments.clicked.connect(self.buttonViewPreviousAppointmentsClicked)

    def buttonEditPatientClicked(self):
        return

    def buttonViewPreviousAppointmentsClicked(self):
        return

    def buttonSaveClicked(self):
        return

    def buttonSaveAndAddClicked(self):
        return

    def buttonAttachPsgReportClicked(self):
        return

    def buttonOpenPsgReportClicked(self):
        return

    def buttonAttachDocReportClicked(self):
        return

    def buttonOpenDocReportClicked(self):
        return

    def fetch_appointment(self, appointment_id):
        return

    def fetch_patient(self, patient_id):
        return