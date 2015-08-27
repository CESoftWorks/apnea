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

    def returnSingleById(self, patientid):
        query = QSqlQuery()
        query.exec_("SELECT * "
                    "FROM patients "
                    "WHERE patientid = '{}'".format(patientid))

        if not query.isActive():
            print(query.lastError().text())
            return None

        record = self._parseToDict(query)
        return record

    def _returnAll(self):
        query = QSqlQuery()
        query.exec_("SELECT * FROM patients ORDER BY patientid ASC")

        if not query.isActive():
            print(query.lastError().text())  # Print in debug-like form if there is an error
            return None

        patients = self._parseToList(query)
        return patients

    def _returnSearch(self, criteria):
        query = QSqlQuery()
        # INSRT function doesn't work for some reason
        query.exec_("SELECT * "
                    "FROM patients "
                    "WHERE patientid LIKE '%{}%' ".format(criteria) +
                    "OR name LIKE '%{}%' ".format(criteria) +
                    "OR surname LIKE '%{}%'".format(criteria))

        if not query.isActive():
            print(query.lastError().text())
            return None

        results = self._parseToList(query)
        return results

    def _parseToList(self, query):
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

    def _parseToDict(self, query):
        parsed_dict = dict.fromkeys(['patientid', 'name', 'surname', 'sex', 'dob',
                                     'phone', 'height', 'weight', 'bmi', 'epsworth',
                                     'assessment'])

        if query:
            while query.next():
                parsed_dict['patientid'] = query.value(0)
                parsed_dict['name'] = query.value(1)
                parsed_dict['surname'] = query.value(2)
                parsed_dict['sex'] = query.value(3)
                parsed_dict['dob'] = query.value(4)
                parsed_dict['phone'] = query.value(5)
                parsed_dict['height'] = query.value(6)
                parsed_dict['weight'] = query.value(7)
                parsed_dict['bmi'] = query.value(8)
                parsed_dict['epsworth'] = query.value(9)
                parsed_dict['assessment'] = query.value(10)

        return parsed_dict


class AppointmentData():
    def __init__(self):
        self.headers = ['ID', 'Registration Date', 'Referring Doctor', 'Priority',
                        'Test Date', 'Diagnosis', 'AHI', 'Treatment', 'PSGRpath',
                        'DocRpath', 'Notes', 'Patient ID']

    def returnAll(self):
        data = self._returnAll()
        model = GenericDataModel(data, self.headers)
        return model

    def returnSingleById(self, appointmentid):
        record = self._returnSingleById(appointmentid)
        return record

    def returnAllByPatient(self, patientid):
        records = self._returnAllByPatient(patientid)
        return records

    def returnUpcoming(self):
        data = self._returnUpcoming()
        model = GenericDataModel(data, self.headers)
        return model

    def _returnAll(self):
        query = QSqlQuery()
        query.exec_("SELECT * FROM appointments ORDER BY id ASC")

        if not query.isActive():
            print(query.lastError().text())
            return None

        appointments = self._parseToList(query)
        return appointments

    def _returnSingleById(self, app_id):
        query = QSqlQuery()
        query.exec_("SELECT * "
                    "FROM appointments "
                    "WHERE id = '{}'".format(app_id))
        if not query.isActive():
            print(query.lastError().text())
            return None
        parsed_dict = self._parseToDict(query)
        return parsed_dict

    def _returnAllByPatient(self, patientid):
        query = QSqlQuery()

        query.exec_("SELECT * "
                    "FROM appointments "
                    "WHERE patientid = '{}'".format(patientid))

        if not query.isActive():
            print(query.lastError().text())
            return None

        results = self._parseToList(query)
        return results

    def _returnUpcoming(self):
        query = QSqlQuery()
        # What the fuck am I even doing here
        query.exec_("SELECT * FROM appointments "
                    "WHERE testdate >= strftime('%d/%m/') || substr(strftime('%Y'), 3, 2)")
                    # That is some seriously ugly ass shit
                    # All to fit a really shitty date system I implemented
        if not query.isActive():
            print(query.lastError().text())
            return None

        results = self._parseToList(query)
        return results

    def _parseToList(self, query):
        parsed_data = []
        if query:
            while query.next():
                data = []  # Hold individual appointment data
                data.append(query.value(0))  # id
                data.append(query.value(1))  # regdate
                data.append(query.value(2))  # refdoctor
                data.append(query.value(3))  # priority
                data.append(query.value(4))  # testdate
                data.append(query.value(5))  # diagnosis
                data.append(query.value(6))  # ahi
                data.append(query.value(7))  # treatment
                data.append(query.value(8))  # psgreport
                data.append(query.value(9))  # doctorreport
                data.append(query.value(10))  # notes
                data.append(query.value(11))  # patientid
                parsed_data.append(data)
        return parsed_data

    def _parseToDict(self, query):
        parsed_dict = dict.fromkeys(['id', 'regdate', 'refdoc', 'priority', 'testdate',
                                     'diagnosis', 'ahi', 'treatment', 'psgreport',
                                     'doctorreport', 'notes', 'patientid'])
        if query:
            while query.next():
                parsed_dict['id'] = query.value(0)
                parsed_dict['regdate'] = query.value(1)
                parsed_dict['refdoc'] = query.value(2)
                parsed_dict['priority'] = query.value(3)
                parsed_dict['testdate'] = query.value(4)
                parsed_dict['diagnosis'] = query.value(5)
                parsed_dict['ahi'] = query.value(6)
                parsed_dict['treatment'] = query.value(7)
                parsed_dict['psgreport'] = query.value(8)
                parsed_dict['doctorreport'] = query.value(9)
                parsed_dict['notes'] = query.value(10)
                parsed_dict['patientid'] = query.value(11)
        return parsed_dict


class GenericDataModel(QAbstractTableModel):
    def __init__(self, records, header, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.records = records
        self.header = header

    def rowCount(self, parent):
        return len(self.records)

    def columnCount(self, parent):
        return len(self.header)

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
        # Obligatory flux capacitor molecular signalling mechanism
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

    appointments = AppointmentData()
    data2 = appointments.returnAllByPatient(112233)
    print(data2)
    data = appointments._returnAll()
