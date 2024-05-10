# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_new.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(204, 289)
        MainWindow.setMinimumSize(QSize(204, 289))
        MainWindow.setMaximumSize(QSize(204, 302))
        MainWindow.setStyleSheet(u"* {\n"
"border: none;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"}\n"
"\n"
"#centralwidget {\n"
"background-color: #212529;\n"
"}\n"
"\n"
"QPushButton {\n"
"border-radius: 15px;\n"
"padding: 5px 15px;\n"
"background-color:  #ADB5BD;\n"
"color: #E9ECEF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #6C757D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:  #343A40;\n"
"}\n"
"\n"
"#quitBtn {\n"
"border-radius: 15px;\n"
"padding: 5px 15px;\n"
"background-color:  #da1e37;\n"
"color: #E9ECEF;\n"
"}\n"
"\n"
"#quitBtn:hover {\n"
"background-color:  #b21e35;\n"
"}\n"
"\n"
"#quitBtn:pressed {\n"
"background-color:  #85182a;\n"
"}\n"
"\n"
"#header, #mainBody, #registration {\n"
"background-color: #495057;\n"
"}\n"
"\n"
"#title, QLabel, QLineEdit {\n"
"background: transparent;\n"
"color: #E9ECEF;\n"
"}\n"
"\n"
"QTableView {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: #CED4DA;\n"
"height: 50px;\n"
""
                        "color: white;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"background-color: #CED4DA;\n"
"boarder-style: none;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"color: #FFF;\n"
"background-color: #ADB5BD;\n"
"boarder: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.header)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Segoe UI Semilight"])
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.mainBody.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.mainBody)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login = QLineEdit(self.mainBody)
        self.login.setObjectName(u"login")
        font1 = QFont()
        font1.setPointSize(12)
        self.login.setFont(font1)
        self.login.setMaxLength(30)

        self.verticalLayout_2.addWidget(self.login)

        self.pss = QLineEdit(self.mainBody)
        self.pss.setObjectName(u"pss")
        self.pss.setFont(font1)

        self.verticalLayout_2.addWidget(self.pss)

        self.loginBtn = QPushButton(self.mainBody)
        self.loginBtn.setObjectName(u"loginBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.loginBtn.setFont(font2)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.loginBtn)

        self.resetPassBtn = QPushButton(self.mainBody)
        self.resetPassBtn.setObjectName(u"resetPassBtn")
        sizePolicy2.setHeightForWidth(self.resetPassBtn.sizePolicy().hasHeightForWidth())
        self.resetPassBtn.setSizePolicy(sizePolicy2)
        self.resetPassBtn.setFont(font2)
        self.resetPassBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.resetPassBtn)


        self.verticalLayout.addWidget(self.mainBody)

        self.registration = QWidget(self.centralwidget)
        self.registration.setObjectName(u"registration")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.registration.sizePolicy().hasHeightForWidth())
        self.registration.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.registration)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.registration)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_5)

        self.signupBtn = QPushButton(self.registration)
        self.signupBtn.setObjectName(u"signupBtn")
        sizePolicy2.setHeightForWidth(self.signupBtn.sizePolicy().hasHeightForWidth())
        self.signupBtn.setSizePolicy(sizePolicy2)
        self.signupBtn.setFont(font2)
        self.signupBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.signupBtn)


        self.verticalLayout.addWidget(self.registration)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.login.setText("")
        self.login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pss.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.resetPassBtn.setText(QCoreApplication.translate("MainWindow", u"Reset password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Firstly?", None))
        self.signupBtn.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
    # retranslateUi

