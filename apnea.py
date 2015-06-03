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

from PySide.QtGui import QApplication, QMainWindow
import sys
import db_init
import ui_mainwindow


class MainWindow(QMainWindow,
                 ui_mainwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)  # Method inherited from parent
        self.uiConnect()  # Connects form's buttons to events

    def uiConnect(self):
        return

    def buttonNewPatientClicked(self):
        print('Launching new patient form...')

    def buttonBookAppointmentClicked(self):
        print('Launching appointment booking window...')

    def buttonViewAppointmentsClicked(self):
        print('Showing all booked appointments...')

    def buttonViewPatientsClicked(self):
        print('Launching patient archive...')

    def buttonSetAvailableDatesClicked(self):
        print('Setting dates available for appointments...')

    def buttonReportsClicked(self):
        print('Launching reports faculty...')

    def buttonSettingsClicked(self):
        print('Opening settings...')

    def buttonAboutClicked(self):
        print('Showing "About" info...')

    def buttonHelpClicked(self):
        print('Opening user guide...')


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Apnea')
    app.setOrganizationName('CESoftWorks')
    db_init.DatabaseInit()
    mainform = MainWindow()
    mainform.show()
    app.exec_()

main()