# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogintQhEqS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from auth_connect import login, signup, checkUsername

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 771, 531))

        #homepage widget
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.Heading_2 = QLabel(self.homepage)
        self.Heading_2.setObjectName(u"Heading_2")
        self.Heading_2.setGeometry(QRect(130, 70, 511, 101))
        font = QFont()
        font.setPointSize(44)
        self.Heading_2.setFont(font)
        self.Heading_2.setAlignment(Qt.AlignCenter)
        self.homeLogin = QPushButton(self.homepage)
        self.homeLogin.setObjectName(u"homeLogin")
        self.homeLogin.setGeometry(QRect(170, 220, 191, 71))
        self.homeSignup = QPushButton(self.homepage)
        self.homeSignup.setObjectName(u"homeSignup")
        self.homeSignup.setGeometry(QRect(380, 220, 191, 71))
        self.stackedWidget.addWidget(self.homepage)


        #login page
        self.loginpage = QWidget()
        self.loginpage.setObjectName(u"loginpage")
        self.Heading = QLabel(self.loginpage)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setGeometry(QRect(150, 100, 511, 101))
        self.Heading.setFont(font)
        self.Heading.setAlignment(Qt.AlignCenter)
        self.Login = QPushButton(self.loginpage)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(320, 330, 131, 41))
        self.logInUsername = QLineEdit(self.loginpage)
        self.logInUsername.setObjectName(u"logInUsername")
        self.logInUsername.setGeometry(QRect(290, 210, 191, 51))
        self.logInUsername.setMaxLength(50)
        self.logInUsername.setAlignment(Qt.AlignCenter)
        self.logInPassword = QLineEdit(self.loginpage)
        self.logInPassword.setObjectName(u"logInPassword")
        self.logInPassword.setGeometry(QRect(290, 270, 191, 51))
        self.logInPassword.setMaxLength(50)
        self.logInPassword.setAlignment(Qt.AlignCenter)
        self.logInPassword.setEchoMode(QLineEdit.Password)
        self.loginBack = QPushButton(self.loginpage)
        self.loginBack.setObjectName(u"loginBack")
        self.loginBack.setGeometry(QRect(320, 380, 131, 41))
        self.stackedWidget.addWidget(self.loginpage)

        #signup page
        self.signuppage = QWidget()
        self.signuppage.setObjectName(u"signuppage")
        self.Signup = QPushButton(self.signuppage)
        self.Signup.setObjectName(u"Signup")
        self.Signup.setGeometry(QRect(330, 310, 131, 41))
        self.Heading_3 = QLabel(self.signuppage)
        self.Heading_3.setObjectName(u"Heading_3")
        self.Heading_3.setGeometry(QRect(160, 80, 511, 101))
        self.Heading_3.setFont(font)
        self.Heading_3.setAlignment(Qt.AlignCenter)
        self.signUpUsername = QLineEdit(self.signuppage)
        self.signUpUsername.setObjectName(u"signUpUsername")
        self.signUpUsername.setGeometry(QRect(300, 190, 191, 51))
        self.signUpUsername.setMaxLength(50)
        self.signUpUsername.setAlignment(Qt.AlignCenter)
        self.signUpPassword = QLineEdit(self.signuppage)
        self.signUpPassword.setObjectName(u"signUpPassword")
        self.signUpPassword.setGeometry(QRect(300, 250, 191, 51))
        self.signUpPassword.setMaxLength(50)
        self.signUpPassword.setAlignment(Qt.AlignCenter)
        self.signUpPassword.setEchoMode(QLineEdit.Password)
        self.signUpBack = QPushButton(self.signuppage)
        self.signUpBack.setObjectName(u"signUpBack")
        self.signUpBack.setGeometry(QRect(330, 360, 131, 41))
        self.checkUsernameLabel = QLabel(self.signuppage)
        self.checkUsernameLabel.setObjectName(u"checkUsername")
        self.checkUsernameLabel.setGeometry(QRect(500, 200, 271, 21))
        self.stackedWidget.addWidget(self.signuppage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Heading_2.setText(QCoreApplication.translate("MainWindow", u"Health Monitor", None))
        self.homeLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.homeSignup.setText(QCoreApplication.translate("MainWindow", u"Signup", None))
        self.logInPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Heading.setText(QCoreApplication.translate("MainWindow", u"Health Monitor", None))
        self.logInUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.loginBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Signup.setText(QCoreApplication.translate("MainWindow", u"Signup", None))
        self.Heading_3.setText(QCoreApplication.translate("MainWindow", u"Health Monitor", None))
        self.signUpUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.signUpPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signUpBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi


class MainWindow(QMainWindow, Ui_MainWindow):

    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connectMe()
    
    def connectMe(self):
        self.homeLogin.clicked.connect(self.btnhomeLoginListener)
        self.homeSignup.clicked.connect(self.btnhomeSignUpListener)
        self.loginBack.clicked.connect(self.btnhomeBackListener)
        self.signUpBack.clicked.connect(self.btnhomeBackListener)
        self.Login.clicked.connect(self.btnLoginListener)
        self.Signup.clicked.connect(self.btnSignupListener)
        self.signUpUsername.textChanged.connect(self.checkSignupUsername)



    def checkSignupUsername(self):
        username = self.signUpUsername.text()
        if checkUsername(username):
            self.checkUsernameLabel.setText("Username already exists. Not so cool")
            self.checkUsernameLabel.setStyleSheet("color: red")
        else:
            self.checkUsernameLabel.setText("Username Available")
            self.checkUsernameLabel.setStyleSheet("color: green")


    def btnhomeBackListener(self):
        self.stackedWidget.setCurrentIndex(0)


    def btnhomeLoginListener(self):
        self.stackedWidget.setCurrentIndex(1)

    def btnhomeSignUpListener(self):
        self.stackedWidget.setCurrentIndex(2)


    def btnLoginListener(self):
        username=self.logInUsername.text()
        password=self.logInPassword.text()

        if username=="" or password=="":
            return

        if login(username, password):
            print("redirect to dashboard")

    def btnSignupListener(self):
        username = self.signUpUsername.text()
        password = self.signUpPassword.text()

        if username=="" or password=="":
            return

        if signup(username, password):
            print("redirect to dashboard")

if (__name__ == '__main__'):

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())