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

import os.path, pickle, datetime
from PySide.QtGui import QDialog, QAbstractItemView, QMessageBox
import ui_allappointments
from db_data import AppointmentData
from db_queries import AppointmentQueries
from appointmentview import AppointmentViewForm
from dialog_selectappointment import DialogSelectAppointment
from dialog_appointmentdatesassign import DialogSelectAppointmentDate

class AllAppointmentsForm(QDialog, ui_allappointments.Ui_Dialog):

    def __init__(self, parent=None):
        super(AllAppointmentsForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.radioUpcoming.setChecked(True)  # Default appointments view
        self.tableAppointments.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableAppointments.setSelectionMode(QAbstractItemView.SingleSelection)
        self.updateTable()

    def uiConnect(self):
        self.btnViewAppointment.clicked.connect(self.btnViewAppointmentClicked)
        self.btnChangeDate.clicked.connect(self.btnChangeDateClicked)
        self.btnDeleteAppointment.clicked.connect(self.btnDeleteAppointmentClicked)
        self.radioUpcoming.toggled.connect(self.updateTable)
        self.radioWaitingList.toggled.connect(self.updateTable)
        self.radioPrevious.toggled.connect(self.updateTable)
        self.radioAll.toggled.connect(self.updateTable)

    def btnViewAppointmentClicked(self):
        index = self.tableAppointments.selectionModel().currentIndex()
        row = index.row()
        appointment_id = index.sibling(row, 0).data()
        testdate = index.sibling(row, 4).data()
        patient_id = index.sibling(row, 11).data()
        if appointment_id is not None and testdate is not '':
            app_view = AppointmentViewForm(appointment_id, patient_id)
            app_view.exec_()

    def btnChangeDateClicked(self):
        index = self.tableAppointments.selectionModel().currentIndex()
        row = index.row()
        appointment_id = index.sibling(row, 0).data()
        old_date = index.sibling(row, 4).data()
        patient_id = index.sibling(row, 11).data()
        if patient_id is '':
            return  # No point if nothing is selected, yes?
        new_date = DialogSelectAppointmentDate.getDate(patient_id)
        if new_date is None:
            return  # Again, if no date is selected, fuck everything else
        success, error = self.update_appointment(appointment_id, new_date)
        if success:
            QMessageBox.information(self, "Success", "New date set!")
            # Add the old date back to the pickle, since it's now available
            # if there is one, that is
            if old_date is not '':
                self.update_dates(old_date)
            self.updateTable()
            return
        QMessageBox.warning(self, "Error", "Could not add new appointment! Error: {}".format(error))
        return

    def btnDeleteAppointmentClicked(self):
        index = self.tableAppointments.selectionModel().currentIndex()
        row = index.row()
        appointment_id = index.sibling(row, 0).data()
        if appointment_id is None:
            return
        # Confirm first
        ok = QMessageBox.question(self, "Confirm deletion", "Are you sure you want to delete"
                        " the selected appointment?",
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ok:
            success, error = self.delete_appointment(appointment_id)
            if success:
                QMessageBox.information(self, "Success", "Appointment record deleted successfully")
                self.updateTable()
            else:
                QMessageBox.warning(self, "Failure", "Could not delete appointment! Error: {}".format(
                    error))

    def updateTable(self):
        appointments = AppointmentData()
        self.btnChangeDate.setText("Change date")
        self.btnViewAppointment.setEnabled(True)
        records = None
        if self.radioAll.isChecked():
             records = appointments.returnAll()
        if self.radioUpcoming.isChecked():
            records = appointments.returnUpcoming()
        if self.radioWaitingList.isChecked():
            records = appointments.returnWaiting()
            self.btnViewAppointment.setEnabled(False)
            self.btnChangeDate.setText("Assign date")
        if self.radioPrevious.isChecked():
            records = appointments.returnPrevious()
        self.tableAppointments.setModel(records)
        self.hideIrrelevantColumns()

    def hideIrrelevantColumns(self):
        #  Pretty self explanatory, hide shit user doesn't need at this stage
        for col in [5,6,7,8,9,10]:
            self.tableAppointments.hideColumn(col)

    def update_appointment(self, appointment_id, new_date):
        # Get all the existing appointment stuff first
        app_data = AppointmentData()
        app = app_data.returnSingleById(appointment_id)
        db_appointments = AppointmentQueries()
        q_status, q_error = db_appointments.update(appointmentid=app['id'], u_regdate=app['regdate'],
                                            u_refdoctor=app['refdoc'], u_priority=app['priority'],
                                            u_testdate=new_date, u_diagnosis=app['diagnosis'],
                                            u_ahi=app['ahi'], u_treatment=app['treatment'],
                                            u_psgreport=app['psgreport'], u_doctorreport=app['doctorreport'],
                                            u_notes=app['notes'])
        return q_status, q_error

    def delete_appointment(self, appointment_id):
        db_appointments = AppointmentQueries()
        q_status, q_error = db_appointments.delete(appointment_id)
        return q_status, q_error

    def update_dates(self, old_date):
        # Pickle file
        fname = 'pickled_dates.data'
        # Fetch dates list
        dates = set()
        if not os.path.isfile(fname):
            print("Dude, where's my pickle?")
            return
        with open(fname, 'rb') as handle:
            dates = pickle.load(handle)
        dates.add(datetime.datetime.strptime(old_date, "%d/%m/%y").date())  # Add it back yo
        with open(fname, 'wb') as handle:
            pickle.dump(dates, handle)
