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

from PySide.QtSql import *
from PySide.QtGui import QMessageBox
import sys


class DatabaseInit():
    # Print statements are for debug output
    def __init__(self):
        self.filename = 'apneadb.sqlite'  # Editable in settings?

        print('Connecting to database...')
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.filename)

        # Test db connection
        if not self.db.open():
            QMessageBox.warning(None, "Apnea",
                                "Database Error: {}".format(self.db.lastError().text()))
            print('Failed to connect to database')
            sys.exit(1)
        print('Success!')

        print('Creating data tables if they do not exist...')
        if self.create_patients() and self.create_appointments():
            print('Done!')

        # DEBUG
        # print(str(self.db.tables()))

    def create_patients(self):
        query = QSqlQuery()
        query.exec_("""CREATE TABLE IF NOT EXISTS patients (
                        patientid INTEGER PRIMARY KEY NOT NULL,
                        name VARCHAR(40),
                        surname VARCHAR(40),
                        sex VARCHAR(10),
                        dob DATE,
                        phone VARCHAR(20),
                        height REAL,
                        weight REAL,
                        bmi REAL,
                        epsworth INTEGER,
                        assessment VARCHAR(250)
                      )""")

        # Check for errors
        if not query.isActive():  # Returns 'False' if error occured
            print('Error: Could not initialize patients table!')
            print(query.lastError().text())
            return False
        return True

    def create_appointments(self):
        query = QSqlQuery()
        query.exec_("""CREATE TABLE IF NOT EXISTS appointments(
                    id INTEGER PRIMARY KEY,
                    regdate DATE,
                    refdoctor VARCHAR(40),
                    priority INTEGER,
                    testdate DATE,
                    diagnosis VARCHAR(100),
                    ahi INTEGER,
                    treatment VARCHAR(200),
                    psgreport VARCHAR(250),
                    doctorreport VARCHAR(250),
                    notes VARCHAR(250),
                    patientid INTEGER NOT NULL,
                    FOREIGN KEY (patientid) REFERENCES patients
                    )""")

        # Check for errors
        if not query.isActive():  # Same as above
            print('Error: Could not initialize appointments table!')
            print(query.lastError().text())
            return False
        return True

    def close(self):
        # Close connection to database
        self.db.close()