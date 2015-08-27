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
import ui_allappointments
from db_data import AppointmentData
from appointmentview import AppointmentViewForm

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

    def updateTable(self):
        appointments = AppointmentData()
        records = None
        if self.radioAll.isChecked():
             records = appointments.returnAll()
        if self.radioUpcoming.isChecked():
            records = appointments.returnUpcoming()
        if self.radioWaitingList.isChecked():
            return
        if self.radioPrevious.isChecked():
            return
        self.tableAppointments.setModel(records)
        self.hideIrrelevantColumns()

    def hideIrrelevantColumns(self):
        #  Pretty self explanatory, hide shit user doesn't need at this stage
        for col in [4,5,6,7,8,9,10]:
            self.tableAppointments.hideColumn(col)

    def btnViewAppointmentClicked(self):
        index = self.tableAppointments.selectionModel().currentIndex()
        row = index.row()
        appointment_id = index.sibling(row, 0).data()
        patient_id = index.sibling(row, 11).data()
        if appointment_id is not None:
            app_view = AppointmentViewForm(appointment_id, patient_id)
            app_view.show()
            app_view.exec_()

    def btnChangeDateClicked(self):
        return

    def btnDeleteAppointmentClicked(self):
        return
