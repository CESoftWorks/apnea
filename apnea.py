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

from PySide.QtGui import QApplication
import sys
import db_init
import ui_mainwindow


def main():
    app = QApplication(sys.argv)
    db_init.DatabaseInit()
    # mainform = MainWindow()
    # mainform.show
    app.exec_()

main()