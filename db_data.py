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

import operator
from PySide.QtSql import QSqlQuery
from PySide.QtCore import *

# The following classes assume that connection to the database
# has already been established.


class PatientData:

    def __init__(self):
        super(PatientData, self).__init__()
        self.headers = ['Patient ID', 'Name', 'Surname', 'Sex', 'Date of Birth',
                        'Phone', 'Height', 'Weight', 'BMI', 'Epsworth Score',
                        'Brief Assessment']

    def returnAll(self):
        data = self._returnAll()
        model = GenericDataModel(data, self.headers)
        return model

    def returnSearch(self, criteria):
        data = self._returnSearch(criteria)
        model = GenericDataModel(data, self.headers)
        return model

    def _returnAll(self):
        query = QSqlQuery()
        query.exec_("SELECT * FROM patients ORDER BY patientid ASC")
        print(query.lastError().text())  # Print in debug-like form if there is an error
        patients = self._parseQueryData(query)
        return patients

    def _returnSearch(self, criteria):
        query = QSqlQuery()
        # INSRT function doesn't work for some reason
        query.exec_("SELECT * "
                    "FROM patients "
                    "WHERE patientid LIKE '%{}%' ".format(criteria) +
                    "OR name LIKE '%{}%' ".format(criteria) +
                    "OR surname LIKE '%{}%'".format(criteria))
        print(query.lastError().text())
        results = self._parseQueryData(query)
        return results

    def _parseQueryData(self, query):
        parsed_data = []
        if query:
            while query.next():
                data = []  # Hold individual patient data
                data.append(query.value(0))  # patientid
                data.append(query.value(1))  # name
                data.append(query.value(2))  # surname
                data.append(query.value(3))  # sex
                data.append(query.value(4))  # dob
                data.append(query.value(5))  # phone
                data.append(query.value(6))  # height
                data.append(query.value(7))  # weight
                data.append(query.value(8))  # bmi
                data.append(query.value(9))  # epsworth
                data.append(query.value(10))  # assessment
                parsed_data.append(data)
        return parsed_data


class GenericDataModel(QAbstractTableModel):
    def __init__(self, records, header, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.records = records
        self.header = header

    def rowCount(self, parent):
        return len(self.records)

    def columnCount(self, parent):
        return len(self.header[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.records[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.records = sorted(self.records,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.records.reverse()
        self.emit(SIGNAL("layoutChanged()"))


# TESTING
if __name__ == '__main__':
    import db_init

    db_init.DatabaseInit()
    patients = PatientData()
    data = patients.returnAll()
    for row in data:
        print(str(row))
