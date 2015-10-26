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
import ui_appointmentdates
import pickle
import os.path
import datetime

fname = 'pickled_dates.data'


class AppointmentDatesForm(QDialog,
                           ui_appointmentdates.Ui_Dialog):

    def __init__(self, parent=None):
        super(AppointmentDatesForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        # Set to store appointment dates
        self.dates = set()
        self.showDates()

    def uiConnect(self):
        # Connects form's buttons to appropriate events
        self.btnAddDate.clicked.connect(self.btnAddDateClicked)
        self.btnRemoveDate.clicked.\
            connect(self.btnRemoveDateClicked)
        self.btnBack.clicked.connect(self.close)
        self.chkShowLegacy.clicked.connect(self.showDates)

    def btnAddDateClicked(self):
        # Fetch date selected from calendar widget
        selected_date = self.calendarDatesSelect.selectedDate()
        # Convert to python datetime format
        py_date = selected_date.toPython()
        # Add to dates set
        self.dates.add(py_date)
        self.storeDates()  # Method to store dates set
        self.showDates()  # Method to display dates set in list widget

    def btnRemoveDateClicked(self):
        # Fetch selection from list widget as string
        selected_date = self.listAllDates.currentItem().text()
        # Convert string to datetime object and remove from dates set
        self.dates.remove(datetime.datetime.strptime(selected_date, "%d/%m/%y").date())
        self.storeDates()
        self.showDates()

    def showDates(self):
        # Fetch dates from pickle
        self.retrieveDates()
        # Clear list widget to avoid duplication
        self.listAllDates.clear()
        for date in sorted(self.dates):
            # Check if user wants to see legacy dates
            if not self.chkShowLegacy.isChecked():
                # Fetch today and future dates
                if date >= datetime.date.today():
                    # Convert to string, then dump to list widget
                    self.listAllDates.addItem(datetime.date.strftime(date, "%d/%m/%y"))
            else:
                self.listAllDates.addItem(datetime.date.strftime(date, "%d/%m/%y"))

    def retrieveDates(self):
        # Check if file exists before opening
        if os.path.isfile(fname):
            # 'with' handles closing of file
            with open(fname, 'rb') as handle:
                # Load dates from pickle to instance variable
                self.dates = pickle.load(handle)

    def storeDates(self):
        # Store dates instance variable
        with open(fname, 'wb') as handle:
            pickle.dump(self.dates, handle)
