# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_maingfxZVM.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTextEdit, QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(970, 642)
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.pg_overview = QWidget()
        self.pg_overview.setObjectName(u"pg_overview")
        self.pg_overview.setEnabled(False)
        self.tabWidget.addTab(self.pg_overview, "")
        self.pg_settings = QWidget()
        self.pg_settings.setObjectName(u"pg_settings")
        self.pg_settings.setEnabled(False)
        self.tabWidget.addTab(self.pg_settings, "")
        self.pg_initialization = QWidget()
        self.pg_initialization.setObjectName(u"pg_initialization")
        self.gridLayout_2 = QGridLayout(self.pg_initialization)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.pg_initialization)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(500, 0))
        self.groupBox.setMaximumSize(QSize(500, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_user = QLabel(self.groupBox)
        self.lb_user.setObjectName(u"lb_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_user.sizePolicy().hasHeightForWidth())
        self.lb_user.setSizePolicy(sizePolicy1)
        self.lb_user.setMinimumSize(QSize(0, 20))
        self.lb_user.setMaximumSize(QSize(16777215, 20))
        self.lb_user.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_3.addWidget(self.lb_user, 2, 0, 1, 1)

        self.txt_host = QTextEdit(self.groupBox)
        self.txt_host.setObjectName(u"txt_host")
        sizePolicy1.setHeightForWidth(self.txt_host.sizePolicy().hasHeightForWidth())
        self.txt_host.setSizePolicy(sizePolicy1)
        self.txt_host.setMinimumSize(QSize(0, 35))
        self.txt_host.setMaximumSize(QSize(16777215, 35))
        self.txt_host.setAcceptRichText(False)

        self.gridLayout_3.addWidget(self.txt_host, 1, 0, 1, 1)

        self.txt_user = QTextEdit(self.groupBox)
        self.txt_user.setObjectName(u"txt_user")
        sizePolicy1.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy1)
        self.txt_user.setMinimumSize(QSize(0, 35))
        self.txt_user.setMaximumSize(QSize(16777215, 35))
        self.txt_user.setAcceptRichText(False)

        self.gridLayout_3.addWidget(self.txt_user, 3, 0, 1, 1)

        self.lb_host = QLabel(self.groupBox)
        self.lb_host.setObjectName(u"lb_host")
        sizePolicy1.setHeightForWidth(self.lb_host.sizePolicy().hasHeightForWidth())
        self.lb_host.setSizePolicy(sizePolicy1)
        self.lb_host.setMinimumSize(QSize(0, 20))
        self.lb_host.setMaximumSize(QSize(16777215, 20))
        self.lb_host.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_3.addWidget(self.lb_host, 0, 0, 1, 1)

        self.lb_password = QLabel(self.groupBox)
        self.lb_password.setObjectName(u"lb_password")
        sizePolicy1.setHeightForWidth(self.lb_password.sizePolicy().hasHeightForWidth())
        self.lb_password.setSizePolicy(sizePolicy1)
        self.lb_password.setMinimumSize(QSize(0, 20))
        self.lb_password.setMaximumSize(QSize(16777215, 20))
        self.lb_password.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_3.addWidget(self.lb_password, 4, 0, 1, 1)

        self.txt_password = QTextEdit(self.groupBox)
        self.txt_password.setObjectName(u"txt_password")
        sizePolicy1.setHeightForWidth(self.txt_password.sizePolicy().hasHeightForWidth())
        self.txt_password.setSizePolicy(sizePolicy1)
        self.txt_password.setMinimumSize(QSize(0, 35))
        self.txt_password.setMaximumSize(QSize(16777215, 35))
        self.txt_password.setAcceptRichText(False)

        self.gridLayout_3.addWidget(self.txt_password, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.lb_empty = QLabel(self.pg_initialization)
        self.lb_empty.setObjectName(u"lb_empty")

        self.gridLayout_2.addWidget(self.lb_empty, 0, 1, 1, 1)

        self.lb_empty_2 = QLabel(self.pg_initialization)
        self.lb_empty_2.setObjectName(u"lb_empty_2")

        self.gridLayout_2.addWidget(self.lb_empty_2, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.pg_initialization)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setMinimumSize(QSize(500, 0))
        self.groupBox_2.setMaximumSize(QSize(500, 16777215))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.textEdit = QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(0, 35))
        self.textEdit.setMaximumSize(QSize(16777215, 35))
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(False)

        self.gridLayout_4.addWidget(self.textEdit, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.groupBox_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.textEdit_2.setMinimumSize(QSize(0, 35))
        self.textEdit_2.setMaximumSize(QSize(16777215, 35))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setAcceptRichText(False)

        self.gridLayout_4.addWidget(self.textEdit_2, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.btn_initBooking = QPushButton(self.groupBox_2)
        self.btn_initBooking.setObjectName(u"btn_initBooking")
        sizePolicy2.setHeightForWidth(self.btn_initBooking.sizePolicy().hasHeightForWidth())
        self.btn_initBooking.setSizePolicy(sizePolicy2)
        self.btn_initBooking.setMinimumSize(QSize(150, 35))
        self.btn_initBooking.setMaximumSize(QSize(150, 35))

        self.gridLayout_4.addWidget(self.btn_initBooking, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.pg_initialization, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        frm_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(frm_main)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"Budget Book", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_overview), QCoreApplication.translate("frm_main", u"Overview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_settings), QCoreApplication.translate("frm_main", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("frm_main", u"MySQL Connection", None))
        self.lb_user.setText(QCoreApplication.translate("frm_main", u"user ( e.g. root )", None))
        self.lb_host.setText(QCoreApplication.translate("frm_main", u"host ( e.g. localhost )", None))
        self.lb_password.setText(QCoreApplication.translate("frm_main", u"password", None))
        self.lb_empty.setText("")
        self.lb_empty_2.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("frm_main", u"Initialization", None))
        self.textEdit.setHtml(QCoreApplication.translate("frm_main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">db_budgetbook</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("frm_main", u"Table: Bookings", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("frm_main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tbl_bookings</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("frm_main", u"Database name", None))
        self.btn_initBooking.setText(QCoreApplication.translate("frm_main", u"initialize", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_initialization), QCoreApplication.translate("frm_main", u"Initialization", None))
    # retranslateUi

