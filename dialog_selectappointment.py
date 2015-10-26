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
import uidlg_selectappointment
from db_data import AppointmentData


class DialogSelectAppointment(QDialog,
                          uidlg_selectappointment.Ui_Dialog):

    def __init__(self, patientid, parent=None):
        super(DialogSelectAppointment, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.patientid = patientid
        self.show_appointments()
        self.selection_id = None

    def uiConnect(self):
        self.buttonSelectDate.clicked.connect(self.buttonSelectDateClicked)

    def buttonSelectDateClicked(self):
        selection = self.listAppointmentDates.currentItem().text()
        stripped_id = selection.split('(')[1].strip(")")  # Jesus fucking christ
        self.selection_id = int(stripped_id)
        self.close()

    def show_appointments(self):
        dates = self.fetch_appointments()
        self.listAppointmentDates.clear()

        for date in sorted(dates):
            self.listAppointmentDates.addItem(date)

    def fetch_appointments(self):
        app_data = AppointmentData()
        appointments = app_data.returnAllByPatient(self.patientid)

        app_dates = []
        for appointment in appointments:
            if appointment[4] is not '':  # This is the testdate field
                app_dates.append(str(appointment[4]) + ' (' + str(appointment[0]) + ')')

        return app_dates

    @staticmethod
    def getAppointment(patientid):
        dialog = DialogSelectAppointment(patientid)
        dialog.exec_()
        return dialog.selection_id
