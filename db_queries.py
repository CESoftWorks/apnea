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
from PySide.QtSql import QSqlQuery

# The following classes assume that connection to the database
# has already been established.
# All functions return True if successful or False if errors occurred


class PatientQueries():

    def insert(self, patientid, name='Unknown', surname='Unknown', sex='Unknown',
               dob='00/00/0000', phone='Unknown', height=0,
               weight=0, bmi=0, epsworth=0, assessment='N/A'):
        # Default values make data omission look a little prettier
        query = QSqlQuery()
        # Using prepared query with Oracle-style named variables
        query.prepare("INSERT INTO patients (patientid, name, "
                      "surname, sex, dob, phone, height, weight,"
                      "bmi, epsworth, assessment)"
                      "VALUES (:patientid, :name, :surname,"
                      ":sex, :dob, :phone, :height, :weight,"
                      ":bmi, :epsworth, :assessment)")
        query.bindValue(':patientid', patientid)
        query.bindValue(':name', name)
        query.bindValue(':surname', surname)
        query.bindValue(':sex', sex)
        query.bindValue(':dob', dob)
        query.bindValue(':phone', phone)
        query.bindValue(':height', height)
        query.bindValue(':weight', weight)
        query.bindValue(':bmi', bmi)
        query.bindValue(':epsworth', epsworth)
        query.bindValue(':assessment', assessment)

        query.exec_()

        # Check for errors
        if not query.isActive():
            print('Error: Could not add new patient record!')
            print(query.lastError().text())
            return False, query.lastError().text()

        print('New patient added successfully')
        return True, None

    def delete(self, patientid):
        query = QSqlQuery()
        query.exec_("DELETE FROM patients "
                    "WHERE patientid = {}".format(patientid))

        # Check for errors
        if not query.isActive():
            print('Error: Could not delete patient record!')
            print(query.lastError().text())
            return False, query.lastError().text()

        print('Patient record deleted successfully')
        return True, None

    def update(self, patientid, u_name, u_surname, u_sex, u_dob,
               u_phone, u_height, u_weight, u_bmi, u_epsworth, u_assessment):
        # Patient ID record cannot be changed through this method
        query = QSqlQuery()
        query.prepare("UPDATE patients "
                      "SET name = :name, "
                      "surname = :surname, "
                      "sex = :sex, "
                      "dob = :dob, "
                      "phone = :phone, "
                      "height = :height, "
                      "weight = :weight, "
                      "bmi = :bmi, "
                      "epsworth = :epsworth, "
                      "assessment = :assessment "
                      "WHERE patientid = :patientid")
        query.bindValue(':name', u_name)
        query.bindValue(':surname', u_surname)
        query.bindValue(':sex', u_sex)
        query.bindValue(':dob', u_dob)
        query.bindValue(':phone', u_phone)
        query.bindValue(':height', u_height)
        query.bindValue(':weight', u_weight)
        query.bindValue(':bmi', u_bmi)
        query.bindValue(':epsworth', u_epsworth)
        query.bindValue(':assessment', u_assessment)
        query.bindValue(':patientid', patientid)

        query.exec_()

        # Check for errors
        if not query.isActive():
            print('Error: Could not update patient record!')
            print(query.lastError().text())
            return False, query.lastError().text()

        print('Patient record updated successfully')
        return True, None


class AppointmentQueries():

    def insert(self, patientid, regdate='00/00/0000', refdoctor='Unknown',
               priority=0, testdate='00/00/0000', diagnosis='No data', ahi=0,
               treatment='No data', psgreport='N/A', doctorreport='N/A',
               notes='No data'):
        query = QSqlQuery()
        query.prepare("INSERT INTO appointments (regdate, refdoctor, "
                      "priority, testdate, diagnosis, ahi, treatment, "
                      "psgreport, doctorreport, notes, patientid) "
                      "VALUES (:regdate, :refdoctor, :priority, :testdate, "
                      ":diagnosis, :ahi, :treatment, :psgreport, :doctorreport, "
                      ":notes, :patientid)")
        query.bindValue(':regdate', regdate)
        query.bindValue(':refdoctor', refdoctor)
        query.bindValue(':priority', priority)
        query.bindValue(':testdate', testdate)
        query.bindValue(':diagnosis', diagnosis)
        query.bindValue(':ahi', ahi)
        query.bindValue(':treatment', treatment)
        query.bindValue(':psgreport', psgreport)
        query.bindValue(':doctorreport', doctorreport)
        query.bindValue(':notes', notes)
        query.bindValue(':patientid', patientid)

        query.exec_()

        # Check for errors
        if not query.isActive():
            print('Error: Could not add new appointment record!')
            print(query.lastError().text())
            return False, query.lastError().text()

        print('New appointment added successfully')
        return True, None

    def delete(self, appointmentid):
        query = QSqlQuery()
        query.exec_("DELETE FROM appointments "
                    "WHERE id = {}".format(appointmentid))

        # Check for errors
        if not query.isActive():
            print('Error: Could not delete appointment record!')
            print(query.lastError().text())
            return False, query.lastError().text()

        print('Appointment record deleted successfully')
        return True, None

    def update(self, appointmentid, u_regdate, u_refdoctor, u_priority,
               u_testdate, u_diagnosis, u_ahi, u_treatment, u_psgreport,
               u_doctorreport, u_notes):
        query = QSqlQuery()
        query.prepare("UPDATE appointments "
                      "SET regdate = :regdate, "
                      "refdoctor = :refdoctor, "
                      "priority = :priority, "
                      "testdate = :testdate, "
                      "diagnosis = :diagnosis, "
                      "ahi = :ahi, "
                      "treatment = :treatment, "
                      "psgreport = :psgreport, "
                      "doctorreport = :doctorreport, "
                      "notes = :notes "
                      "WHERE id = :appointmentid")
        query.bindValue(':regdate', u_regdate)
        query.bindValue(':refdoctor', u_refdoctor)
        query.bindValue(':priority', u_priority)
        query.bindValue(':testdate', u_testdate)
        query.bindValue(':diagnosis', u_diagnosis)
        query.bindValue(':ahi', u_ahi)
        query.bindValue(':treatment', u_treatment)
        query.bindValue(':psgreport', u_psgreport)
        query.bindValue(':doctorreport', u_doctorreport)
        query.bindValue(':notes', u_notes)
        query.bindValue(':appointmentid', appointmentid)

        query.exec_()

        # Check for errors
        if not query.isActive():
            print('Error: Could not update appointment record!')
            print(query.lastError().text())
            return False, query.lastError().text()

        print('Appointment record updated successfully')
        return True, None


# TESTING
if __name__ == '__main__':
    import db_init

    db_init.DatabaseInit()
    patients = PatientQueries()
    patients.insert(223344, name='John', surname='Doe')
    patients.delete(223344)
    patients.insert(112233, name='Dave', surname='Husky')
    patients.update(112233, u_name='Dave', u_surname='Husky', u_sex='Male',
                     u_phone='22334455', u_dob='14/05/1980', u_height=165,
                     u_weight=98, u_bmi=24, u_epsworth=10, u_assessment='Asshole')

    appointments = AppointmentQueries()
    appointments.insert(112233)
    appointments.delete(1)
    appointments.insert(112233)
    appointments.update(1, '12/12/2015', 'Dr. Who', 1, '14/12/2015', 'something', 12,
                        'Penicillin', 'none', 'none', 'dickpoop')