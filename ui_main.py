# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainXyvmYs.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(950, 668)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        frm_main.setFont(font)
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        self.tabWidget.setFont(font1)
        self.pg_overview = QWidget()
        self.pg_overview.setObjectName(u"pg_overview")
        self.pg_overview.setEnabled(False)
        self.tabWidget.addTab(self.pg_overview, "")
        self.pg_accruals = QWidget()
        self.pg_accruals.setObjectName(u"pg_accruals")
        self.gridLayout_4 = QGridLayout(self.pg_accruals)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.txt_accr_amount = QLineEdit(self.pg_accruals)
        self.txt_accr_amount.setObjectName(u"txt_accr_amount")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_accr_amount.sizePolicy().hasHeightForWidth())
        self.txt_accr_amount.setSizePolicy(sizePolicy)
        self.txt_accr_amount.setMinimumSize(QSize(150, 30))
        self.txt_accr_amount.setMaximumSize(QSize(150, 30))
        self.txt_accr_amount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.txt_accr_amount, 3, 1, 1, 1)

        self.txt_accr_period = QLineEdit(self.pg_accruals)
        self.txt_accr_period.setObjectName(u"txt_accr_period")
        sizePolicy.setHeightForWidth(self.txt_accr_period.sizePolicy().hasHeightForWidth())
        self.txt_accr_period.setSizePolicy(sizePolicy)
        self.txt_accr_period.setMinimumSize(QSize(150, 30))
        self.txt_accr_period.setMaximumSize(QSize(150, 30))
        self.txt_accr_period.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.txt_accr_period, 3, 2, 1, 1)

        self.lb_accr_period = QLabel(self.pg_accruals)
        self.lb_accr_period.setObjectName(u"lb_accr_period")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_accr_period.sizePolicy().hasHeightForWidth())
        self.lb_accr_period.setSizePolicy(sizePolicy1)
        self.lb_accr_period.setMinimumSize(QSize(150, 30))
        self.lb_accr_period.setMaximumSize(QSize(150, 30))

        self.gridLayout_4.addWidget(self.lb_accr_period, 2, 2, 1, 1)

        self.lb_accr_amount = QLabel(self.pg_accruals)
        self.lb_accr_amount.setObjectName(u"lb_accr_amount")
        sizePolicy1.setHeightForWidth(self.lb_accr_amount.sizePolicy().hasHeightForWidth())
        self.lb_accr_amount.setSizePolicy(sizePolicy1)
        self.lb_accr_amount.setMinimumSize(QSize(150, 30))
        self.lb_accr_amount.setMaximumSize(QSize(150, 30))

        self.gridLayout_4.addWidget(self.lb_accr_amount, 2, 1, 1, 1)

        self.txt_accr_annual = QLineEdit(self.pg_accruals)
        self.txt_accr_annual.setObjectName(u"txt_accr_annual")
        sizePolicy.setHeightForWidth(self.txt_accr_annual.sizePolicy().hasHeightForWidth())
        self.txt_accr_annual.setSizePolicy(sizePolicy)
        self.txt_accr_annual.setMinimumSize(QSize(150, 30))
        self.txt_accr_annual.setMaximumSize(QSize(150, 30))
        self.txt_accr_annual.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.txt_accr_annual.setReadOnly(False)

        self.gridLayout_4.addWidget(self.txt_accr_annual, 3, 3, 1, 1)

        self.lb_accr_annual = QLabel(self.pg_accruals)
        self.lb_accr_annual.setObjectName(u"lb_accr_annual")
        sizePolicy1.setHeightForWidth(self.lb_accr_annual.sizePolicy().hasHeightForWidth())
        self.lb_accr_annual.setSizePolicy(sizePolicy1)
        self.lb_accr_annual.setMinimumSize(QSize(150, 30))
        self.lb_accr_annual.setMaximumSize(QSize(150, 30))

        self.gridLayout_4.addWidget(self.lb_accr_annual, 1, 3, 2, 1)

        self.btn_accr_save = QPushButton(self.pg_accruals)
        self.btn_accr_save.setObjectName(u"btn_accr_save")
        sizePolicy.setHeightForWidth(self.btn_accr_save.sizePolicy().hasHeightForWidth())
        self.btn_accr_save.setSizePolicy(sizePolicy)
        self.btn_accr_save.setMinimumSize(QSize(150, 30))
        self.btn_accr_save.setMaximumSize(QSize(150, 30))

        self.gridLayout_4.addWidget(self.btn_accr_save, 5, 5, 1, 1)

        self.txt_accr_concern = QLineEdit(self.pg_accruals)
        self.txt_accr_concern.setObjectName(u"txt_accr_concern")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_accr_concern.sizePolicy().hasHeightForWidth())
        self.txt_accr_concern.setSizePolicy(sizePolicy2)
        self.txt_accr_concern.setMinimumSize(QSize(250, 30))
        self.txt_accr_concern.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.txt_accr_concern, 3, 4, 1, 2)

        self.lb_acct_concern = QLabel(self.pg_accruals)
        self.lb_acct_concern.setObjectName(u"lb_acct_concern")
        sizePolicy2.setHeightForWidth(self.lb_acct_concern.sizePolicy().hasHeightForWidth())
        self.lb_acct_concern.setSizePolicy(sizePolicy2)
        self.lb_acct_concern.setMinimumSize(QSize(250, 30))
        self.lb_acct_concern.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.lb_acct_concern, 2, 4, 1, 2)

        self.tbl_accruals = QTableWidget(self.pg_accruals)
        self.tbl_accruals.setObjectName(u"tbl_accruals")

        self.gridLayout_4.addWidget(self.tbl_accruals, 8, 1, 1, 5)

        self.tabWidget.addTab(self.pg_accruals, "")
        self.pg_initialization = QWidget()
        self.pg_initialization.setObjectName(u"pg_initialization")
        self.gridLayout_2 = QGridLayout(self.pg_initialization)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.box_Connect = QGroupBox(self.pg_initialization)
        self.box_Connect.setObjectName(u"box_Connect")
        sizePolicy.setHeightForWidth(self.box_Connect.sizePolicy().hasHeightForWidth())
        self.box_Connect.setSizePolicy(sizePolicy)
        self.box_Connect.setMinimumSize(QSize(500, 272))
        self.box_Connect.setMaximumSize(QSize(500, 272))
        self.box_Connect.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.gridLayout_3 = QGridLayout(self.box_Connect)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.txt_host = QLineEdit(self.box_Connect)
        self.txt_host.setObjectName(u"txt_host")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txt_host.sizePolicy().hasHeightForWidth())
        self.txt_host.setSizePolicy(sizePolicy3)
        self.txt_host.setMinimumSize(QSize(0, 30))
        self.txt_host.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.txt_host, 1, 0, 1, 2)

        self.btn_saveConnect = QPushButton(self.box_Connect)
        self.btn_saveConnect.setObjectName(u"btn_saveConnect")
        sizePolicy.setHeightForWidth(self.btn_saveConnect.sizePolicy().hasHeightForWidth())
        self.btn_saveConnect.setSizePolicy(sizePolicy)
        self.btn_saveConnect.setMinimumSize(QSize(150, 30))
        self.btn_saveConnect.setMaximumSize(QSize(150, 30))

        self.gridLayout_3.addWidget(self.btn_saveConnect, 6, 1, 1, 1)

        self.lb_password = QLabel(self.box_Connect)
        self.lb_password.setObjectName(u"lb_password")
        sizePolicy3.setHeightForWidth(self.lb_password.sizePolicy().hasHeightForWidth())
        self.lb_password.setSizePolicy(sizePolicy3)
        self.lb_password.setMinimumSize(QSize(0, 30))
        self.lb_password.setMaximumSize(QSize(16777215, 30))
        self.lb_password.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_3.addWidget(self.lb_password, 4, 0, 1, 2)

        self.lb_user = QLabel(self.box_Connect)
        self.lb_user.setObjectName(u"lb_user")
        sizePolicy3.setHeightForWidth(self.lb_user.sizePolicy().hasHeightForWidth())
        self.lb_user.setSizePolicy(sizePolicy3)
        self.lb_user.setMinimumSize(QSize(0, 30))
        self.lb_user.setMaximumSize(QSize(16777215, 30))
        self.lb_user.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_3.addWidget(self.lb_user, 2, 0, 1, 2)

        self.lb_empty_3 = QLabel(self.box_Connect)
        self.lb_empty_3.setObjectName(u"lb_empty_3")

        self.gridLayout_3.addWidget(self.lb_empty_3, 6, 0, 1, 1)

        self.txt_user = QLineEdit(self.box_Connect)
        self.txt_user.setObjectName(u"txt_user")
        sizePolicy3.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy3)
        self.txt_user.setMinimumSize(QSize(0, 30))
        self.txt_user.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.txt_user, 3, 0, 1, 2)

        self.txt_password = QLineEdit(self.box_Connect)
        self.txt_password.setObjectName(u"txt_password")
        sizePolicy3.setHeightForWidth(self.txt_password.sizePolicy().hasHeightForWidth())
        self.txt_password.setSizePolicy(sizePolicy3)
        self.txt_password.setMinimumSize(QSize(0, 30))
        self.txt_password.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.txt_password, 5, 0, 1, 2)

        self.lb_host = QLabel(self.box_Connect)
        self.lb_host.setObjectName(u"lb_host")
        sizePolicy3.setHeightForWidth(self.lb_host.sizePolicy().hasHeightForWidth())
        self.lb_host.setSizePolicy(sizePolicy3)
        self.lb_host.setMinimumSize(QSize(0, 30))
        self.lb_host.setMaximumSize(QSize(16777215, 30))
        self.lb_host.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_3.addWidget(self.lb_host, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.box_Connect, 0, 0, 1, 1)

        self.lb_empty = QLabel(self.pg_initialization)
        self.lb_empty.setObjectName(u"lb_empty")

        self.gridLayout_2.addWidget(self.lb_empty, 1, 0, 1, 1)

        self.lb_empty_2 = QLabel(self.pg_initialization)
        self.lb_empty_2.setObjectName(u"lb_empty_2")

        self.gridLayout_2.addWidget(self.lb_empty_2, 0, 1, 2, 1)

        self.tabWidget.addTab(self.pg_initialization, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        frm_main.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.txt_host, self.txt_user)
        QWidget.setTabOrder(self.txt_user, self.txt_password)
        QWidget.setTabOrder(self.txt_password, self.btn_saveConnect)

        self.retranslateUi(frm_main)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"Budget Book", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_overview), QCoreApplication.translate("frm_main", u"Overview", None))
        self.txt_accr_amount.setText("")
        self.txt_accr_period.setText("")
        self.lb_accr_period.setText(QCoreApplication.translate("frm_main", u"Period (in months)", None))
        self.lb_accr_amount.setText(QCoreApplication.translate("frm_main", u"periodic amount", None))
        self.txt_accr_annual.setText("")
        self.txt_accr_annual.setPlaceholderText(QCoreApplication.translate("frm_main", u"00000,00", None))
        self.lb_accr_annual.setText(QCoreApplication.translate("frm_main", u"annual amount", None))
        self.btn_accr_save.setText(QCoreApplication.translate("frm_main", u"Save", None))
        self.txt_accr_concern.setText("")
        self.lb_acct_concern.setText(QCoreApplication.translate("frm_main", u"Concerns", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_accruals), QCoreApplication.translate("frm_main", u"Accruals", None))
        self.box_Connect.setTitle(QCoreApplication.translate("frm_main", u"MySQL Connection", None))
        self.btn_saveConnect.setText(QCoreApplication.translate("frm_main", u"Save", None))
        self.lb_password.setText(QCoreApplication.translate("frm_main", u"password", None))
        self.lb_user.setText(QCoreApplication.translate("frm_main", u"user ( e.g. root )", None))
        self.lb_empty_3.setText("")
        self.txt_password.setText("")
        self.lb_host.setText(QCoreApplication.translate("frm_main", u"host ( e.g. localhost )", None))
        self.lb_empty.setText("")
        self.lb_empty_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_initialization), QCoreApplication.translate("frm_main", u"Initialization", None))
    # retranslateUi

