# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainKBAMll.ui'
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
        MainWindow.resize(823, 497)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")

        #main tab widget
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QSize(801, 450))
        self.tabWidget.setMaximumSize(QSize(801, 450))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet(u"QTabBar::tab::disabled {width: 0; height: 0; margin: 30; padding: 0; border: none;}\n"
"")
        self.tabWidget.setInputMethodHints(Qt.ImhNone)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setIconSize(QSize(20, 20))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)

        #dashboard tab
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.tabWidget.addTab(self.dashboard, "")

        #activity log tab
        self.activitylog = QWidget()
        self.activitylog.setObjectName(u"activitylog")

        self.gridLayout = QGridLayout(self.activitylog)
        self.gridLayout.setObjectName(u"gridLayout")

        self.tableActivityLog = QTableView(self.activitylog)
        self.tableActivityLog.setObjectName(u"tableActivityLog")
        self.tableActivityLog.setSortingEnabled(False)

        self.btnAddActivityLog = QPushButton(self.activitylog)
        self.btnAddActivityLog.setObjectName(u"btnAddActivityLog")

        self.btnDeleteActivityLog = QPushButton(self.activitylog)
        self.btnDeleteActivityLog.setObjectName(u"btnDeleteActivityLog")

        self.gridLayout.addWidget(self.tableActivityLog, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.btnAddActivityLog, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.btnDeleteActivityLog, 1, 1, 1, 1)

        self.tabWidget.addTab(self.activitylog, "")


        #data tab
        self.data = QWidget()
        self.data.setObjectName(u"data")
        self.data.setEnabled(True)
        self.tabWidget.addTab(self.data, "")

        #settings tab
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.gridLayout_2 = QGridLayout(self.settings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.settings_tabwidget = QTabWidget(self.settings)
        self.settings_tabwidget.setObjectName(u"settings_tabwidget")
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.settings_tabwidget.setFont(font)
        self.settings_tabwidget.setLayoutDirection(Qt.LeftToRight)
        self.settings_tabwidget.setTabPosition(QTabWidget.West)
        self.settings_tabwidget.setTabShape(QTabWidget.Rounded)
        self.settings_tabwidget.setElideMode(Qt.ElideNone)
        self.settings_tabwidget.setUsesScrollButtons(False)
        self.settings_tabwidget.setDocumentMode(False)
        self.account_settings_tab = QWidget()
        self.account_settings_tab.setObjectName(u"account_settings_tab")
        self.label = QLabel(self.account_settings_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 91, 16))
        self.label_2 = QLabel(self.account_settings_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 91, 16))
        self.label_3 = QLabel(self.account_settings_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 150, 91, 16))
        self.label_4 = QLabel(self.account_settings_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 240, 91, 16))
        self.label_5 = QLabel(self.account_settings_tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 240, 91, 16))
        self.label_6 = QLabel(self.account_settings_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 240, 91, 16))
        self.settings_tabwidget.addTab(self.account_settings_tab, "")
        self.privacy_settings_tab = QWidget()
        self.privacy_settings_tab.setObjectName(u"privacy_settings_tab")
        self.gridLayout_5 = QGridLayout(self.privacy_settings_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_9 = QLabel(self.privacy_settings_tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAutoFillBackground(False)
        self.label_9.setFrameShape(QFrame.NoFrame)
        self.label_9.setFrameShadow(QFrame.Plain)

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.settings_tabwidget.addTab(self.privacy_settings_tab, "")
        self.faq_settings_tab = QWidget()
        self.faq_settings_tab.setObjectName(u"faq_settings_tab")
        self.gridLayout_4 = QGridLayout(self.faq_settings_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.faq_settings_tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.settings_tabwidget.addTab(self.faq_settings_tab, "")
        self.about_settings_tab = QWidget()
        self.about_settings_tab.setObjectName(u"about_settings_tab")
        self.gridLayout_3 = QGridLayout(self.about_settings_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.about_settings_tab)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setKerning(True)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.settings_tabwidget.addTab(self.about_settings_tab, "")

        self.gridLayout_2.addWidget(self.settings_tabwidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.settings, "")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.settings_tabwidget, self.btnAddActivityLog)
        QWidget.setTabOrder(self.btnAddActivityLog, self.btnDeleteActivityLog)
        QWidget.setTabOrder(self.btnDeleteActivityLog, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tableActivityLog)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.settings_tabwidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Health Monitor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dashboard), QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btnAddActivityLog.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btnDeleteActivityLog.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.activitylog), QCoreApplication.translate("MainWindow", u"Activity Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data), QCoreApplication.translate("MainWindow", u"Data", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.settings_tabwidget.setTabText(self.settings_tabwidget.indexOf(self.account_settings_tab), QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.settings_tabwidget.setTabText(self.settings_tabwidget.indexOf(self.privacy_settings_tab), QCoreApplication.translate("MainWindow", u"Privacy", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.settings_tabwidget.setTabText(self.settings_tabwidget.indexOf(self.faq_settings_tab), QCoreApplication.translate("MainWindow", u"FAQ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">This is About page</span></p><p><br/></p><p>We will put information about who created this project</p><p>Devs Names</p><p>Class Name</p></body></html>", None))
        self.settings_tabwidget.setTabText(self.settings_tabwidget.indexOf(self.about_settings_tab), QCoreApplication.translate("MainWindow", u"About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connectMe()
        self.populateActivityLog()

    def populateActivityLog(self):
    	print("")
    
    def connectMe(self):
        self.btnAddActivityLog.clicked.connect(self.btnAddActivityLogListener)
        self.btnDeleteActivityLog.clicked.connect(self.btnDeleteActivityLogListener)

    def btnAddActivityLogListener(self):
    	print("add")

    def btnDeleteActivityLogListener(self):
    	print("delete")

if (__name__ == '__main__'):

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
