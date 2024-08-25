# region LIBRARIES #############################################################
################################################################################

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui_main import Ui_frm_main
import json
import mysql.connector

# endregion ####################################################################

# region RELEVANT VARIABLES ####################################################
################################################################################

#### SERVER
#   Server host name        self.host
#   Server user name        self.user
#   Server password         self.password
#   Server connection       self.my_db

#### DATABASE
#   Database Cursor         self.myCursor
#   Database name           self.dbName
#   Table name              self.db_tbl_accruals

# endregion ####################################################################

class Frm_main(QMainWindow, Ui_frm_main):                                       ######## class to start the UI
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class DBConnection(Frm_main):                                                   ######## class to create/connect to Server/Database/Table
    def __init__(self):
        super().__init__()
        self.configFile = "config.json"                                         # sets name of configuration file

        self.dbName = "db_budgetbook"                                           # sets name of the Database
        # Tables
        self.db_tbl_accruals = "tbl_accruals"

    def tryConnectors(self):                                                    #### Key Function to try Connections
        if self.tryValues() and self.tryConnection():                           # == TRUE -> connection works
            self.tabWidget.insertTab(0,self.pg_overview, "Overview")
            self.tabWidget.insertTab(2,self.pg_initialization, "Initialization")
            self.tabWidget.setCurrentWidget(self.pg_overview)
            self.tryDatabase()                                                  # Tests if Database is created
            self.tryTables()                                                    # Tests if Tables are created
        else:                                                                   # If no Connection other Tabs are hidden
            self.tabWidget.insertTab(0,self.pg_initialization, "Initialization")
            self.tabWidget.removeTab(self.tabWidget.indexOf(self.pg_overview))
            self.tabWidget.setCurrentWidget(self.pg_initialization)

# region Sub functions for tryConnectors() #####################################
################################################################################
    def tryValues(self):                                                        #### Tries if user/host/server are empty
        return self.user != "" and self.host != "" and self.password != ""

    def tryConnection(self):                                                    #### Tries to connect to Server
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

    def tryDatabase(self):                                                      #### Tries if Database exists, else creates it
        self.initCursor()

        self.myCursor.execute(f"SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = '{self.dbName}'")
        result = self.myCursor.fetchone()
        if result:
            pass
        else:
            self.myCursor.execute(f"CREATE DATABASE {self.dbName}")

        self.myCursor.execute(f'USE {self.dbName}')
        
    def tryTables(self):                                                        #### Tries if Tables exist, else creates them
        Tables = [self.db_tbl_accruals]

        tableDict = {                                                           # Dicts contains Table creation scripts
            self.db_tbl_accruals: f'''
                                CREATE TABLE {self.db_tbl_accruals} (
                                    Concern VARCHAR(255),
                                    p_amount DECIMAL(9, 2),
                                    period INT,
                                    a_ammount DECIMAL(9, 2)
                                );
                                '''
        }

        for table in Tables:
            self.myCursor.execute(f"SHOW TABLES LIKE '{table}';")
            result = self.myCursor.fetchone()

            if result:
                pass
            else:
                self.myCursor.execute(tableDict[table])
    
    def initCursor(self):                                                       #### initialize cursor
        self.myCursor = self.my_db.cursor()

# endregion ####################################################################

# region Configuration Management ##############################################
################################################################################
    def getConfig(self):                                                        #### opens configuration file and sets default configurations for server aso.

        with open(self.configFile, 'r') as f:
            self.constants = json.load(f)

        self.host = self.constants.get('host')
        self.user = self.constants.get('user')
        self.password = self.constants.get('password')

        self.txt_host.setText(self.host)
        self.txt_user.setText(self.user)
        self.txt_password.setText(self.password)

    def saveConfig(self):                                                       #### saves changed configurations in file and retries Server Connection
        self.constants['host'] = self.txt_host.text()
        self.constants['user'] = self.txt_user.text()
        self.constants['password'] = self.txt_password.text()

        self.host = self.txt_host.text()
        self.user = self.txt_user.text()
        self.password = self.txt_password.text()
        
        with open(self.configFile, 'w') as f:
            json.dump(self.constants, f)
        
        self.tryConnectors()

# endregion ####################################################################

    def systemnachricht(self,msg, msgTitle):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(msgTitle)
        msg_box.setText(msg)
        msg_box.exec()

class Procedure(DBConnection):                                                  ######## main class for organization
    def __init__(self):                                                         #### manages Buttons and inital procedures
        super().__init__()

        # when starting the script it initialy gets the configuration and tries the server Connection
        self.getConfig()                                                        # gets the values from config.json
        self.tryConnectors()                                                    # tries Server Connection and looking for Database

        # BUTTONS - Configuration
        self.btn_saveConnect.clicked.connect(self.saveConfig)                   # saves changed Server information and re-runs tryConnectors()



# region EXECUTION #############################################################
################################################################################

app = QApplication()
init = Procedure()
init.show()
app.exec()

# endregion ####################################################################