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
        self.dates = set()
        self.showDates()

    def uiConnect(self):
        self.btnAddDate.clicked.connect(self.btnAddDateClicked)
        self.btnRemoveDate.clicked.\
            connect(self.btnRemoveDateClicked)
        self.btnBack.clicked.connect(self.close)
        self.chkShowLegacy.clicked.connect(self.showDates)

    def btnAddDateClicked(self):
        selected_date = self.calendarDatesSelect.selectedDate()
        py_date = selected_date.toPython()
        self.dates.add(py_date)
        self.storeDates()
        self.showDates()

    def btnRemoveDateClicked(self):
        selected_date = self.listAllDates.currentItem().text()
        self.dates.remove(datetime.datetime.strptime(selected_date, "%d/%m/%y").date())
        self.storeDates()
        self.showDates()

    def showDates(self):
        self.retrieveDates()
        self.listAllDates.clear()
        for date in sorted(self.dates):
            if not self.chkShowLegacy.isChecked():
                if date >= datetime.date.today():
                    self.listAllDates.addItem(datetime.date.strftime(date, "%d/%m/%y"))
            else:
                self.listAllDates.addItem(datetime.date.strftime(date, "%d/%m/%y"))

    def retrieveDates(self):
        if os.path.isfile(fname):
            with open(fname, 'rb') as handle:
                self.dates = pickle.load(handle)

    def storeDates(self):
        with open(fname, 'wb') as handle:
            pickle.dump(self.dates, handle)