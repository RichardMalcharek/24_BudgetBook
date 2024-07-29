# region LIBRARIES ##########################################################
#############################################################################

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui_main import Ui_frm_main
import json
import mysql.connector

# endregion #################################################################


# region UNUSED LIBRARIES ###################################################
from PySide6.QtWidgets import QPushButton, QFileDialog, QLabel, QCalendarWidget, QTableView, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon
from datetime import datetime, timedelta
from PySide6.QtCore import QLocale, QDate, Qt, QAbstractTableModel
import pandas as pd
import os
import sys
import time
import csv
# endregion #################################################################


# region INFORMATION ABOUT VARIABLES ########################################
#############################################################################

#### SERVER
#   Server host name        self.host
#   Server user name        self.user
#   Server password         self.password
#   Server connection       self.my_db

#### DATABASE
#   Database Cursor         self.myCursor
#   Database name           self.dbName
#   Table name              self.tbl_bookings

# endregion


class Frm_main(QMainWindow, Ui_frm_main):


# region __init__ & BUTTON CONFIGURATION ####################################
#############################################################################
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        #### TRYING TO CONNECT TO SERVER AND FIND DATABASE WHEN LUNCHING
        self.getConfig()            # gets the values from config.json
        self.tryConnectors()        # tries Server Connection and looking for Database


        #### BUTTONS - CONNECTION
        self.btn_saveConnect.clicked.connect(self.saveConfig)   # saves changed Server information and re-runs tryConnectors()

# endregion #################################################################


# region CONNECTION TEST ####################################################
############################################################################

#### GENERAL TRY FUNCTION
    def tryConnectors(self):
        if self.tryValues() and self.tryConnection(): # == TRUE -> connection works
            self.tabWidget.insertTab(0,self.pg_overview, "Overview")
            self.tabWidget.insertTab(1,self.pg_settings, "Settings")
            self.tabWidget.insertTab(2,self.pg_initialization, "Initialization")
            self.tabWidget.setCurrentWidget(self.pg_initialization)
            self.tryDatabase()

        else:
            self.tabWidget.insertTab(0,self.pg_initialization, "Initialization")
            
            self.tabWidget.removeTab(self.tabWidget.indexOf(self.pg_overview))
            self.tabWidget.removeTab(self.tabWidget.indexOf(self.pg_settings))

            self.tabWidget.setCurrentWidget(self.pg_initialization)


#### TRY FOR VALUES
    def tryValues(self):
        return self.user != "" and self.host != "" and self.password != ""


#### TRY TO CONNECT SERVER
    def tryConnection(self):
        msgTitle = "Try Server-Connection"
        msg = "Server connection error. \nhost, user or password are incorrect."
        try:
            self.my_db = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password
            )
            if self.my_db.is_connected():
                return True
            else:
                self.systemnachricht(msg, msgTitle)
                return False
        except:
            self.systemnachricht(msg, msgTitle)
            return False


#### TRY DATABASE
    def tryDatabase(self):
        self.initCursor()

        self.myCursor.execute(f"SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = '{self.dbName}'")
        result = self.myCursor.fetchone()
        if result:
            pass
        else:
            self.myCursor.execute(f"CREATE DATABASE {self.dbName}")


#### Initiate CURSOR
    def initCursor(self):
        self.myCursor = self.my_db.cursor()

# endregion #################################################################


# region CONNECTION CONFIGURATION ###########################################
#############################################################################

#### SET CONNECTION
    def getConfig(self):

        self.configFile = "config.json"

        self.openConfig()
        self.host = self.constants.get('host')
        self.user = self.constants.get('user')
        self.password = self.constants.get('password')

        self.dbName = self.constants.get('database')
        self.tbl_bookings = self.constants.get('tbl_bookings')

        self.txt_host.setText(self.host)
        self.txt_user.setText(self.user)
        self.txt_password.setText(self.password)


#### OPEN CONNECTION
    def openConfig(self):
        with open(self.configFile, 'r') as f:
            self.constants = json.load(f)


#### SAVE CONNECTION
    def saveConfig(self):
        self.constants['host'] = self.txt_host.text()
        self.constants['user'] = self.txt_user.text()
        self.constants['password'] = self.txt_password.text()

        self.host = self.txt_host.text()
        self.user = self.txt_user.text()
        self.password = self.txt_password.text()
        
        with open(self.configFile, 'w') as f:
            json.dump(self.constants, f)
        
        self.tryConnectors()

# endregion #################################################################


# region GENERAL FUNCTIONS ##################################################
#############################################################################

#### CREATE SYSTEM MSG
    def systemnachricht(self,msg, msgTitle):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(msgTitle)
        msg_box.setText(msg)
        msg_box.exec()

# endregion


# region EXECUTION ##########################################################
#############################################################################

app = QApplication()
frm_main = Frm_main()
frm_main.show()
app.exec()

# endregion ################################################################