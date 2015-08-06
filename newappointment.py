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


class NewAppointmentForm(QDialog, ui_newappointment.Ui_Dialog):

    def __init__(self, parent=None):
        super(NewAppointmentForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()

    def uiConnect(self):
        self.buttonAssignDate.clicked.connect(self.buttonAssignDateClicked)
        self.buttonBookWithoutDate.clicked.connect(self.buttonBookWithoutDateClicked)
        self.buttonPatientSelect.clicked.connect(self.buttonPatientSelectClicked)
        self.buttonProceed.clicked.connect(self.buttonProceedClicked)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)

    def buttonPatientSelectClicked(self):
        selectpatientdialog = DialogSelectPatient(self)
        selectpatientdialog.show()
        selectpatientdialog.exec_()
        return

    def buttonAssignDateClicked(self):
        return

    def buttonBookWithoutDateClicked(self):
        return

    def buttonProceedClicked(self):
        return
