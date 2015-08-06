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
import uidlg_selectpatient



class DialogSelectPatient(QDialog, uidlg_selectpatient.Ui_Dialog):

    def __init__(self, parent=None):
        super(DialogSelectPatient, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()
        self.loadPatients()

    def uiConnect(self):
        self.buttonAddNewPatient.clicked().connect(self.buttonAddNewPatientClicked)
        self.buttonSelectPatient.clicked().connect(self.buttonSelectPatientClicked)

    def buttonAddNewPatientClicked(self):
        return

    def buttonSelectPatientClicked(self):
        return

    def loadPatients(self):
        return