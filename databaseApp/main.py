################################################################################
##
## Projekt Bazy Danych 2
## Michał Droń (248832), Mateusz Bajorek (248903)
## styczeń 2021
##
################################################################################

from PySide2.QtWidgets import *

# IMPORT FUNCTIONS
import sys
import mysql.connector

# GUI FILE
import ui_main
from SQLEditor import SQLEditor


class MainWindow(QMainWindow):
    def __init__(self):

        # inicjalizacja okna
        QMainWindow.__init__(self)
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        # inicjalizacja bazy danych i kursora
        self.sql = None
        self.mydb = None
        self.cursor = None
        self.isLogged = False

        # kliknięcia przycisków
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.logout.clicked.connect(self.logout)

        self.ui.menu_cars.clicked.connect(lambda: self.set_cars())
        self.ui.menu_employees.clicked.connect(lambda: self.set_employees())
        self.ui.menu_money.clicked.connect(lambda: self.set_money())
        self.ui.menu_parts.clicked.connect(lambda: self.set_parts())
        self.ui.menu_orders.clicked.connect(lambda: self.set_orders())
        self.ui.menu_clients.clicked.connect(lambda: self.set_clients())
        self.ui.menu_houses.clicked.connect(lambda: self.set_houses())

        # pokazanie okna
        self.show()

    # logowanie
    def login(self):
        try:
            con_login = str(self.ui.login.text())
            con_password = str(self.ui.password.text())
            self.mydb = mysql.connector.connect(user=con_login,
                                                password=con_password,
                                                host='localhost',
                                                database='database_')

            self.sql = SQLEditor(self.mydb, self.ui)
            self.sql.__init__(self.mydb, self.ui)
            self.isLogged = True


        except mysql.connector.Error as ex:
            if ex.errno == 1045:
                messagebox = QMessageBox()
                messagebox.critical(self, "Błąd logowania", "Dane logowania są nieprawidłowe!")
                messagebox.setFixedSize(500, 200)

            else:
                print("Coś nie tak {}".format(ex))

    def logout(self):
        if self.isLogged:
            self.mydb.close()
            del self.sql
            self.ui.logged_person.setText("")
            self.isLogged = False
        self.ui.login.setText("")
        self.ui.password.setText("")
        self.ui.logout.clicked.connect( self.ui.pages.setCurrentWidget(self.ui.page_login))

    def no_access(self):
        if not self.isLogged:
            access_message = "Musisz najpierw się zalogować."
        else:
            access_message = "Nie masz dostępu do tej części bazy danych."
            print(self.sql.user)
            print(self.isLogged)
        messagebox = QMessageBox()
        messagebox.critical(self, "Błąd dostępu", access_message)
        messagebox.setFixedSize(500, 200)

    def set_money(self):
        if not self.isLogged:
            self.no_access()
        elif self.sql.user == "owner@localhost" or self.sql.user == "accountant@localhost":
            self.ui.pages.setCurrentWidget(self.ui.page_money)
        else:
            self.no_access()

    def set_parts(self):
        if not self.isLogged:
            self.no_access()
        elif self.sql.user == "owner@localhost" or self.sql.user == "production@localhost":
            self.ui.pages.setCurrentWidget(self.ui.page_parts)
        else:
            self.no_access()

    def set_orders(self):
        if not self.isLogged:
            self.no_access()
        elif self.sql.user == "owner@localhost" or self.sql.user == "accountant@localhost" or self.sql.user == "seller@localhost":
            self.ui.pages.setCurrentWidget(self.ui.page_orders)
        else:
            self.no_access()

    def set_cars(self):
        if not self.isLogged:
            self.no_access()
        elif self.sql.user == "owner@localhost" or self.sql.user == "production@localhost" or self.sql.user == "seller@localhost":
            self.ui.pages.setCurrentWidget(self.ui.page_cars)
        else:
            self.no_access()

    def set_clients(self):
        if not self.isLogged:
            self.no_access()
        elif self.sql.user == "owner@localhost" or self.sql.user == "seller@localhost":
            self.ui.pages.setCurrentWidget(self.ui.page_clients)
        else:
            self.no_access()

    def set_employees(self):
        if not self.isLogged:
            self.no_access()
        elif self.sql.user == "owner@localhost":
            self.ui.pages.setCurrentWidget(self.ui.page_employees)
        else:
            self.no_access()

    def set_houses(self):
        if not self.isLogged:
            self.no_access()
        elif self.sql.user == "owner@localhost":
            self.ui.pages.setCurrentWidget(self.ui.page_houses)
        else:
            self.no_access()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    exit(app.exec_())
