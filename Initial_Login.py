# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Initial_Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Heading = QLabel(self.centralwidget)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setGeometry(QRect(240, 60, 331, 101))
        font = QFont()
        font.setPointSize(44)
        self.Heading.setFont(font)
        self.Heading.setAlignment(Qt.AlignCenter)
        self.Login = QPushButton(self.centralwidget)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(190, 190, 221, 81))
        font1 = QFont()
        font1.setPointSize(25)
        self.Login.setFont(font1)
        self.SignUp = QPushButton(self.centralwidget)
        self.SignUp.setObjectName(u"SignUp")
        self.SignUp.setGeometry(QRect(430, 190, 221, 81))
        self.SignUp.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Heading.setText(QCoreApplication.translate("MainWindow", u"Health Monitor", None))
        self.Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.SignUp.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
    # retranslateUi

