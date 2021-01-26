# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiYTlHMz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.Top_Bar)
        self.frame_logo.setObjectName(u"frame_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_logo.sizePolicy().hasHeightForWidth())
        self.frame_logo.setSizePolicy(sizePolicy)
        self.frame_logo.setMaximumSize(QSize(70, 40))
        self.frame_logo.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_logo.setFrameShape(QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.frame_logo)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 0))
        self.logo.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.logo)


        self.horizontalLayout.addWidget(self.frame_logo)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 20, 0)
        self.logged_person = QLabel(self.frame_top)
        self.logged_person.setObjectName(u"logged_person")
        self.logged_person.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_4.addWidget(self.logged_person, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.content)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(70, 0))
        self.left_menu.setMaximumSize(QSize(70, 16777215))
        self.left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.left_menu.setFrameShape(QFrame.NoFrame)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.buttons = QFrame(self.left_menu)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(70, 0))
        self.buttons.setFrameShape(QFrame.NoFrame)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.buttons)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_money = QPushButton(self.buttons)
        self.menu_money.setObjectName(u"menu_money")
        self.menu_money.setMinimumSize(QSize(0, 40))
        self.menu_money.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 85, 85);\n"
"}")

        self.verticalLayout_2.addWidget(self.menu_money)

        self.menu_parts = QPushButton(self.buttons)
        self.menu_parts.setObjectName(u"menu_parts")
        self.menu_parts.setMinimumSize(QSize(0, 40))
        self.menu_parts.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 85, 85);\n"
"}")

        self.verticalLayout_2.addWidget(self.menu_parts)

        self.menu_orders = QPushButton(self.buttons)
        self.menu_orders.setObjectName(u"menu_orders")
        self.menu_orders.setMinimumSize(QSize(0, 40))
        self.menu_orders.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 85, 85);\n"
"}")

        self.verticalLayout_2.addWidget(self.menu_orders)

        self.menu_cars = QPushButton(self.buttons)
        self.menu_cars.setObjectName(u"menu_cars")
        self.menu_cars.setMinimumSize(QSize(0, 40))
        self.menu_cars.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 85, 85);\n"
"}")

        self.verticalLayout_2.addWidget(self.menu_cars)

        self.menu_clients = QPushButton(self.buttons)
        self.menu_clients.setObjectName(u"menu_clients")
        self.menu_clients.setMinimumSize(QSize(0, 40))
        self.menu_clients.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 85, 85);\n"
"}")

        self.verticalLayout_2.addWidget(self.menu_clients)

        self.menu_employees = QPushButton(self.buttons)
        self.menu_employees.setObjectName(u"menu_employees")
        self.menu_employees.setMinimumSize(QSize(0, 40))
        self.menu_employees.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 85, 85);\n"
"}")

        self.verticalLayout_2.addWidget(self.menu_employees)

        self.menu_houses = QPushButton(self.buttons)
        self.menu_houses.setObjectName(u"menu_houses")
        self.menu_houses.setEnabled(True)
        self.menu_houses.setMinimumSize(QSize(0, 40))
        self.menu_houses.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 85, 85);\n"
"}")

        self.verticalLayout_2.addWidget(self.menu_houses)


        self.verticalLayout_3.addWidget(self.buttons, 0, Qt.AlignTop)

        self.logout = QPushButton(self.left_menu)
        self.logout.setObjectName(u"logout")
        self.logout.setMinimumSize(QSize(70, 70))
        self.logout.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/logout40px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon)
        self.logout.setIconSize(QSize(40, 40))
        self.logout.setFlat(True)

        self.verticalLayout_3.addWidget(self.logout)


        self.horizontalLayout_2.addWidget(self.left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_pages)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.frame_pages)
        self.pages.setObjectName(u"pages")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.horizontalLayout_8 = QHBoxLayout(self.page_login)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_login = QFrame(self.page_login)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMinimumSize(QSize(300, 531))
        self.frame_login.setMaximumSize(QSize(300, 531))
        self.frame_login.setFrameShape(QFrame.NoFrame)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_login)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 30)
        self.user_icon = QLabel(self.frame_login)
        self.user_icon.setObjectName(u"user_icon")
        self.user_icon.setPixmap(QPixmap(u":/user_white.png"))
        self.user_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.user_icon)

        self.login_label = QLabel(self.frame_login)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_6.addWidget(self.login_label)

        self.login = QLineEdit(self.frame_login)
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"QLineEdit{\n"
"	font-family: Montserrat;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	font-size: 14px;\n"
"	color: rgb(220, 220, 220);\n"
"}")

        self.verticalLayout_6.addWidget(self.login)

        self.password_label = QLabel(self.frame_login)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_6.addWidget(self.password_label)

        self.password = QLineEdit(self.frame_login)
        self.password.setObjectName(u"password")
        self.password.setStyleSheet(u"QLineEdit{\n"
"	font-family: Montserrat;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	font-size: 14px;\n"
"	color: rgb(220, 220, 220);\n"
"}")
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.password)

        self.login_filler = QFrame(self.frame_login)
        self.login_filler.setObjectName(u"login_filler")
        self.login_filler.setMaximumSize(QSize(16777215, 70))
        self.login_filler.setFrameShape(QFrame.NoFrame)
        self.login_filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.login_filler)

        self.login_btn = QPushButton(self.frame_login)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 40))
        self.login_btn.setStyleSheet(u"QPushButton {\n"
"	font-family: Montserrat;\n"
"	font-size: 16px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.login_btn)


        self.horizontalLayout_8.addWidget(self.frame_login)

        self.pages.addWidget(self.page_login)
        self.page_cars = QWidget()
        self.page_cars.setObjectName(u"page_cars")
        self.page_cars.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page_cars)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_cars = QFrame(self.page_cars)
        self.frame_cars.setObjectName(u"frame_cars")
        self.frame_cars.setFrameShape(QFrame.StyledPanel)
        self.frame_cars.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_cars)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cars_filter_frame = QFrame(self.frame_cars)
        self.cars_filter_frame.setObjectName(u"cars_filter_frame")
        self.cars_filter_frame.setMinimumSize(QSize(0, 40))
        self.cars_filter_frame.setMaximumSize(QSize(16777215, 16777215))
        self.cars_filter_frame.setFrameShape(QFrame.NoFrame)
        self.cars_filter_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.cars_filter_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cars_filter_label = QLabel(self.cars_filter_frame)
        self.cars_filter_label.setObjectName(u"cars_filter_label")
        self.cars_filter_label.setMinimumSize(QSize(300, 0))
        self.cars_filter_label.setMaximumSize(QSize(16777215, 50))
        self.cars_filter_label.setLayoutDirection(Qt.LeftToRight)
        self.cars_filter_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.cars_filter_label)

        self.cars_filter = QLineEdit(self.cars_filter_frame)
        self.cars_filter.setObjectName(u"cars_filter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cars_filter.sizePolicy().hasHeightForWidth())
        self.cars_filter.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.cars_filter)


        self.verticalLayout_5.addWidget(self.cars_filter_frame)

        self.table_cars = QTableWidget(self.frame_cars)
        if (self.table_cars.columnCount() < 7):
            self.table_cars.setColumnCount(7)
        if (self.table_cars.rowCount() < 1):
            self.table_cars.setRowCount(1)
        self.table_cars.setObjectName(u"table_cars")
        self.table_cars.setStyleSheet(u"QTableWidget {\n"
"	color: rgb(220, 220, 220);\n"
"	gridline-color: rgb(90, 90, 90);\n"
"	\n"
"}\n"
"QHeaderView::section {\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QTableCornerButton::section {\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"}")
        self.table_cars.setFrameShape(QFrame.NoFrame)
        self.table_cars.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_cars.setShowGrid(True)
        self.table_cars.setGridStyle(Qt.DotLine)
        self.table_cars.setSortingEnabled(True)
        self.table_cars.setCornerButtonEnabled(True)
        self.table_cars.setRowCount(1)
        self.table_cars.setColumnCount(7)
        self.table_cars.horizontalHeader().setStretchLastSection(True)
        self.table_cars.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.table_cars)

        self.cars_buttons_frame = QFrame(self.frame_cars)
        self.cars_buttons_frame.setObjectName(u"cars_buttons_frame")
        self.cars_buttons_frame.setMinimumSize(QSize(0, 70))
        self.cars_buttons_frame.setMaximumSize(QSize(16777215, 70))
        self.cars_buttons_frame.setFrameShape(QFrame.NoFrame)
        self.cars_buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.cars_buttons_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_cars_add = QPushButton(self.cars_buttons_frame)
        self.btn_cars_add.setObjectName(u"btn_cars_add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_cars_add.sizePolicy().hasHeightForWidth())
        self.btn_cars_add.setSizePolicy(sizePolicy2)
        self.btn_cars_add.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_cars_add.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_cars_add)

        self.btn_cars_edit = QPushButton(self.cars_buttons_frame)
        self.btn_cars_edit.setObjectName(u"btn_cars_edit")
        sizePolicy2.setHeightForWidth(self.btn_cars_edit.sizePolicy().hasHeightForWidth())
        self.btn_cars_edit.setSizePolicy(sizePolicy2)
        self.btn_cars_edit.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_cars_edit.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_cars_edit)

        self.btn_cars_delete = QPushButton(self.cars_buttons_frame)
        self.btn_cars_delete.setObjectName(u"btn_cars_delete")
        sizePolicy2.setHeightForWidth(self.btn_cars_delete.sizePolicy().hasHeightForWidth())
        self.btn_cars_delete.setSizePolicy(sizePolicy2)
        self.btn_cars_delete.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_cars_delete.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_cars_delete)


        self.verticalLayout_5.addWidget(self.cars_buttons_frame)


        self.verticalLayout_4.addWidget(self.frame_cars)

        self.pages.addWidget(self.page_cars)
        self.page_money = QWidget()
        self.page_money.setObjectName(u"page_money")
        self.pages.addWidget(self.page_money)
        self.page_orders = QWidget()
        self.page_orders.setObjectName(u"page_orders")
        self.pages.addWidget(self.page_orders)
        self.page_parts = QWidget()
        self.page_parts.setObjectName(u"page_parts")
        self.pages.addWidget(self.page_parts)
        self.page_clients = QWidget()
        self.page_clients.setObjectName(u"page_clients")
        self.verticalLayout_10 = QVBoxLayout(self.page_clients)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_clients = QFrame(self.page_clients)
        self.frame_clients.setObjectName(u"frame_clients")
        self.frame_clients.setFrameShape(QFrame.StyledPanel)
        self.frame_clients.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_clients)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.clients_filter_frame = QFrame(self.frame_clients)
        self.clients_filter_frame.setObjectName(u"clients_filter_frame")
        self.clients_filter_frame.setMinimumSize(QSize(0, 40))
        self.clients_filter_frame.setMaximumSize(QSize(16777215, 16777215))
        self.clients_filter_frame.setFrameShape(QFrame.NoFrame)
        self.clients_filter_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.clients_filter_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.clients_filter_label = QLabel(self.clients_filter_frame)
        self.clients_filter_label.setObjectName(u"clients_filter_label")
        self.clients_filter_label.setMinimumSize(QSize(300, 0))
        self.clients_filter_label.setMaximumSize(QSize(16777215, 50))
        self.clients_filter_label.setLayoutDirection(Qt.LeftToRight)
        self.clients_filter_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.clients_filter_label)

        self.clients_filter = QLineEdit(self.clients_filter_frame)
        self.clients_filter.setObjectName(u"clients_filter")
        sizePolicy1.setHeightForWidth(self.clients_filter.sizePolicy().hasHeightForWidth())
        self.clients_filter.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.clients_filter)


        self.verticalLayout_9.addWidget(self.clients_filter_frame)

        self.table_clients = QTableWidget(self.frame_clients)
        if (self.table_clients.columnCount() < 7):
            self.table_clients.setColumnCount(7)
        if (self.table_clients.rowCount() < 1):
            self.table_clients.setRowCount(1)
        self.table_clients.setObjectName(u"table_clients")
        self.table_clients.setStyleSheet(u"QTableWidget {\n"
"	color: rgb(220, 220, 220);\n"
"	gridline-color: rgb(90, 90, 90);\n"
"	\n"
"}\n"
"QHeaderView::section {\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QTableCornerButton::section {\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"}")
        self.table_clients.setFrameShape(QFrame.NoFrame)
        self.table_clients.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_clients.setShowGrid(True)
        self.table_clients.setGridStyle(Qt.DotLine)
        self.table_clients.setSortingEnabled(True)
        self.table_clients.setCornerButtonEnabled(True)
        self.table_clients.setRowCount(1)
        self.table_clients.setColumnCount(7)
        self.table_clients.horizontalHeader().setStretchLastSection(True)
        self.table_clients.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_9.addWidget(self.table_clients)

        self.clients_btn_frame = QFrame(self.frame_clients)
        self.clients_btn_frame.setObjectName(u"clients_btn_frame")
        self.clients_btn_frame.setMinimumSize(QSize(0, 70))
        self.clients_btn_frame.setMaximumSize(QSize(16777215, 70))
        self.clients_btn_frame.setFrameShape(QFrame.NoFrame)
        self.clients_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.clients_btn_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_clients_add = QPushButton(self.clients_btn_frame)
        self.btn_clients_add.setObjectName(u"btn_clients_add")
        sizePolicy2.setHeightForWidth(self.btn_clients_add.sizePolicy().hasHeightForWidth())
        self.btn_clients_add.setSizePolicy(sizePolicy2)
        self.btn_clients_add.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_clients_add.setFlat(True)

        self.horizontalLayout_12.addWidget(self.btn_clients_add)

        self.btn_clients_edit = QPushButton(self.clients_btn_frame)
        self.btn_clients_edit.setObjectName(u"btn_clients_edit")
        sizePolicy2.setHeightForWidth(self.btn_clients_edit.sizePolicy().hasHeightForWidth())
        self.btn_clients_edit.setSizePolicy(sizePolicy2)
        self.btn_clients_edit.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_clients_edit.setFlat(True)

        self.horizontalLayout_12.addWidget(self.btn_clients_edit)

        self.btn_clients_delete = QPushButton(self.clients_btn_frame)
        self.btn_clients_delete.setObjectName(u"btn_clients_delete")
        sizePolicy2.setHeightForWidth(self.btn_clients_delete.sizePolicy().hasHeightForWidth())
        self.btn_clients_delete.setSizePolicy(sizePolicy2)
        self.btn_clients_delete.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_clients_delete.setFlat(True)

        self.horizontalLayout_12.addWidget(self.btn_clients_delete)


        self.verticalLayout_9.addWidget(self.clients_btn_frame)


        self.verticalLayout_10.addWidget(self.frame_clients)

        self.pages.addWidget(self.page_clients)
        self.page_houses = QWidget()
        self.page_houses.setObjectName(u"page_houses")
        self.pages.addWidget(self.page_houses)
        self.page_employees = QWidget()
        self.page_employees.setObjectName(u"page_employees")
        self.verticalLayout_8 = QVBoxLayout(self.page_employees)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_employees = QFrame(self.page_employees)
        self.frame_employees.setObjectName(u"frame_employees")
        self.frame_employees.setFrameShape(QFrame.StyledPanel)
        self.frame_employees.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_employees)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.empl_filter_frame = QFrame(self.frame_employees)
        self.empl_filter_frame.setObjectName(u"empl_filter_frame")
        self.empl_filter_frame.setMinimumSize(QSize(0, 40))
        self.empl_filter_frame.setMaximumSize(QSize(16777215, 16777215))
        self.empl_filter_frame.setFrameShape(QFrame.NoFrame)
        self.empl_filter_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.empl_filter_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.empl_filter_label = QLabel(self.empl_filter_frame)
        self.empl_filter_label.setObjectName(u"empl_filter_label")
        self.empl_filter_label.setMinimumSize(QSize(300, 0))
        self.empl_filter_label.setMaximumSize(QSize(16777215, 50))
        self.empl_filter_label.setLayoutDirection(Qt.LeftToRight)
        self.empl_filter_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.empl_filter_label)

        self.empl_filter = QLineEdit(self.empl_filter_frame)
        self.empl_filter.setObjectName(u"empl_filter")
        sizePolicy1.setHeightForWidth(self.empl_filter.sizePolicy().hasHeightForWidth())
        self.empl_filter.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.empl_filter)


        self.verticalLayout_7.addWidget(self.empl_filter_frame)

        self.table_employees = QTableWidget(self.frame_employees)
        if (self.table_employees.columnCount() < 7):
            self.table_employees.setColumnCount(7)
        if (self.table_employees.rowCount() < 1):
            self.table_employees.setRowCount(1)
        self.table_employees.setObjectName(u"table_employees")
        self.table_employees.setStyleSheet(u"QTableWidget {\n"
"	color: rgb(220, 220, 220);\n"
"	gridline-color: rgb(90, 90, 90);\n"
"	\n"
"}\n"
"QHeaderView::section {\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QTableCornerButton::section {\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"}")
        self.table_employees.setFrameShape(QFrame.NoFrame)
        self.table_employees.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_employees.setShowGrid(True)
        self.table_employees.setGridStyle(Qt.DotLine)
        self.table_employees.setSortingEnabled(True)
        self.table_employees.setCornerButtonEnabled(True)
        self.table_employees.setRowCount(1)
        self.table_employees.setColumnCount(7)
        self.table_employees.horizontalHeader().setStretchLastSection(True)
        self.table_employees.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_7.addWidget(self.table_employees)

        self.empl_buttons_frame = QFrame(self.frame_employees)
        self.empl_buttons_frame.setObjectName(u"empl_buttons_frame")
        self.empl_buttons_frame.setMinimumSize(QSize(0, 70))
        self.empl_buttons_frame.setMaximumSize(QSize(16777215, 70))
        self.empl_buttons_frame.setFrameShape(QFrame.NoFrame)
        self.empl_buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.empl_buttons_frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_empl_add = QPushButton(self.empl_buttons_frame)
        self.btn_empl_add.setObjectName(u"btn_empl_add")
        sizePolicy2.setHeightForWidth(self.btn_empl_add.sizePolicy().hasHeightForWidth())
        self.btn_empl_add.setSizePolicy(sizePolicy2)
        self.btn_empl_add.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_empl_add.setFlat(True)

        self.horizontalLayout_10.addWidget(self.btn_empl_add)

        self.btn_empl_edit = QPushButton(self.empl_buttons_frame)
        self.btn_empl_edit.setObjectName(u"btn_empl_edit")
        sizePolicy2.setHeightForWidth(self.btn_empl_edit.sizePolicy().hasHeightForWidth())
        self.btn_empl_edit.setSizePolicy(sizePolicy2)
        self.btn_empl_edit.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_empl_edit.setFlat(True)

        self.horizontalLayout_10.addWidget(self.btn_empl_edit)

        self.btn_empl_delete = QPushButton(self.empl_buttons_frame)
        self.btn_empl_delete.setObjectName(u"btn_empl_delete")
        sizePolicy2.setHeightForWidth(self.btn_empl_delete.sizePolicy().hasHeightForWidth())
        self.btn_empl_delete.setSizePolicy(sizePolicy2)
        self.btn_empl_delete.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_empl_delete.setFlat(True)

        self.horizontalLayout_10.addWidget(self.btn_empl_delete)


        self.verticalLayout_7.addWidget(self.empl_buttons_frame)


        self.verticalLayout_8.addWidget(self.frame_employees)

        self.pages.addWidget(self.page_employees)

        self.horizontalLayout_6.addWidget(self.pages)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Montserrat'; color:#232323;\">autopol</span></p></body></html>", None))
        self.logged_person.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Montserrat'; font-size:14pt; color:#dcdcdc;\"></span></p></body></html>", None))
        self.menu_money.setText(QCoreApplication.translate("MainWindow", u"Finanse", None))
        self.menu_parts.setText(QCoreApplication.translate("MainWindow", u"Cz\u0119\u015bci", None))
        self.menu_orders.setText(QCoreApplication.translate("MainWindow", u"Zam\u00f3wienia", None))
        self.menu_cars.setText(QCoreApplication.translate("MainWindow", u"Samochody", None))
        self.menu_clients.setText(QCoreApplication.translate("MainWindow", u"Klienci", None))
        self.menu_employees.setText(QCoreApplication.translate("MainWindow", u"Pracownicy", None))
        self.menu_houses.setText(QCoreApplication.translate("MainWindow", u"Fabryki", None))
        self.logout.setText("")
        self.user_icon.setText("")
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-family:'Montserrat'; color:#dcdcdc;\">Login</span></p></body></html>", None))
        self.login.setText("")
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Montserrat'; font-size:16pt; color:#dcdcdc;\">Has\u0142o</span></p></body></html>", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Zaloguj", None))
        self.cars_filter_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Montserrat'; font-size:14pt; color:#dcdcdc;\">Filtrowanie</span></p></body></html>", None))
        self.btn_cars_add.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.btn_cars_edit.setText(QCoreApplication.translate("MainWindow", u"Modyfikuj", None))
        self.btn_cars_delete.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
        self.clients_filter_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Montserrat'; font-size:14pt; color:#dcdcdc;\">Filtrowanie</span></p></body></html>", None))
        self.btn_clients_add.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.btn_clients_edit.setText(QCoreApplication.translate("MainWindow", u"Modyfikuj", None))
        self.btn_clients_delete.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
        self.empl_filter_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Montserrat'; font-size:14pt; color:#dcdcdc;\">Filtrowanie</span></p></body></html>", None))
        self.btn_empl_add.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.btn_empl_edit.setText(QCoreApplication.translate("MainWindow", u"Modyfikuj", None))
        self.btn_empl_delete.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
    # retranslateUi

