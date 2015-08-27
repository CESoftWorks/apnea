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

from PySide.QtGui import QDialog
import ui_allappointments
from db_data import AppointmentData

class AllAppointmentsForm(QDialog, ui_allappointments.Ui_Dialog):

    def __init__(self, parent=None):
        super(AllAppointmentsForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.radioUpcoming.setChecked(True)
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
        if self.radioAll.isChecked():
             data = appointments.returnAll()
             self.tableAppointments.setModel(data)

    def btnViewAppointmentClicked(self):
        return

    def btnChangeDateClicked(self):
        return

    def btnDeleteAppointmentClicked(self):
        return
