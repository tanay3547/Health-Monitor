# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Heading = QLabel(self.centralwidget)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setGeometry(QRect(230, 80, 331, 101))
        font = QFont()
        font.setPointSize(44)
        self.Heading.setFont(font)
        self.Heading.setAlignment(Qt.AlignCenter)
        self.Login = QPushButton(self.centralwidget)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(260, 290, 131, 41))
        self.SignUp = QPushButton(self.centralwidget)
        self.SignUp.setObjectName(u"SignUp")
        self.SignUp.setGeometry(QRect(400, 290, 131, 41))
        self.Username = QLineEdit(self.centralwidget)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(300, 170, 191, 51))
        self.Username.setMaxLength(50)
        self.Username.setAlignment(Qt.AlignCenter)
        self.Password = QLineEdit(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(300, 230, 191, 51))
        self.Password.setMaxLength(50)
        self.Password.setAlignment(Qt.AlignCenter)
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
        self.Username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
    # retranslateUi

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
     

if (__name__ == '__main__'):

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())