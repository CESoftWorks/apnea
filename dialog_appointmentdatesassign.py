import os

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
import uidlg_appointmentassigndate
import pickle, os.path
import datetime

fname = 'pickled_dates.data'


class DialogSelectAppointmentDate(QDialog, uidlg_appointmentassigndate.Ui_Dialog):

    def __init__(self, patientid, parent=None):
        super(DialogSelectAppointmentDate, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.patientid = patientid
        self.dates = None
        self.showDates()
        self.selected_date = None

    def uiConnect(self):
        self.buttonSelectDate.clicked.connect(self.buttonSelectDateClicked)
        self.buttonCancel.clicked.connect(self.close)

    def buttonSelectDateClicked(self):
        # Set selection as the selected date
        self.selected_date = self.listAvailableDates.currentItem().text()
        # First, confirm
        ok = QMessageBox.question(self, "Selected Date", "You have selected the {}".format(self.selected_date) +
                                  " as the polysomnography date for the patient with ID {}".format(self.patientid) +
                                  ". Are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ok == QMessageBox.No:
            # If not, set selected date to none
            self.selected_date = None
            return
        # Well then, lets get to work
        # Get that date out of that pickle, since it's no longer available
        self.dates.remove(datetime.datetime.strptime(self.selected_date, "%d/%m/%y").date())
        self.storeDates()
        # Close this dialog, it's done with
        self.close()

    def showDates(self):
        # TODO Pickle operations could be in a separate module
        self.retrieveDates()
        self.listAvailableDates.clear()  # Avoid duplication
        if not os.path.isfile(fname):
            print("Dude, where's my pickle?")
            return
        for date in sorted(self.dates):
            if date >= datetime.date.today():
                self.listAvailableDates.addItem(datetime.date.strftime(date, "%d/%m/%y"))

    def retrieveDates(self):
        #  Check if file exists before opening
        if os.path.isfile(fname):
            # 'with' handles closing of file
            with open(fname, 'rb') as handle:
                # Load dates from pickle to instance variable
                self.dates = pickle.load(handle)

    def storeDates(self):
        with open(fname, 'wb') as handle:
            pickle.dump(self.dates, handle)

    @staticmethod
    def getDate(patientid, parent=None):
        dialog = DialogSelectAppointmentDate(patientid, parent)
        dialog.exec_()
        return dialog.selected_date
