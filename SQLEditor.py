import mysql.connector
from PySide2 import QtWidgets

class SQLEditor:
    def __init__(self, mydb, ui):

        access_level = 0
        self.mydb = mydb
        self.cursor = self.mydb.cursor()
        self.ui = ui
        self.cursor.execute("SELECT CURRENT_USER()")
        self.user = str(self.cursor.fetchone()[0])


        if self.user == "owner@localhost":  # właściciel

            self.ui.logged_person.setText("Zalogowano: Właściciel")

            self.initialize_employee()
            self.initialize_cars()
            self.initialize_clients()
            # initialize_office
            # initialize_factory
            # initialize_payment
            # initialize_order
            # initialize_part
            # initialize_supplier


        elif self.user == "seller@localhost":  # sprzedawcy

            self.ui.logged_person.setText("Zalogowano: Sprzedawca")

            self.initialize_clients()
            self.initialize_cars()
            # initialize_order

        elif self.user == "production@localhost":  # produkcja

            self.ui.logged_person.setText("Zalogowano: Produkcja")

            self.initialize_cars()
            # initialize_part
            # initialize_supplier

        elif self.user == "accountant@localhost":  # księgowość

            self.ui.logged_person.setText("Zalogowano: Księgowość")

            # initialize_payment
            # initialize_order

    def initialize_employee(self):
        query = "SELECT * FROM employee"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.ui.table_employees.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.table_employees.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.table_employees.setItem(row_number,
                                                column_number,
                                                QtWidgets.QTableWidgetItem(str(data)))

    def initialize_cars(self):
        query = "SELECT * FROM Car"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.ui.table_cars.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.table_cars.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.table_cars.setItem(row_number,
                                           column_number,
                                           QtWidgets.QTableWidgetItem(str(data)))

    def initialize_clients(self):
        query = "SELECT * FROM Client_"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.ui.table_clients.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.table_clients.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.table_clients.setItem(row_number,
                                              column_number,
                                              QtWidgets.QTableWidgetItem(str(data)))
