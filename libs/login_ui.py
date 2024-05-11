# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        MainWindow.resize(212, 299)
        MainWindow.setMinimumSize(QSize(212, 299))
        MainWindow.setMaximumSize(QSize(212, 299))
        palette = QPalette()
        brush = QBrush(QColor(233, 236, 239, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(33, 37, 41, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(233, 236, 239, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe UI Light"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"* {\n"
"border: none;\n"
"background-color: #212529;\n"
"color: #E9ECEF;\n"
"padding: 0;\n"
"margin: 0;\n"
"}\n"
"\n"
"#dialog {\n"
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
"QPushButton:hover{\n"
"background-color:  #6C757D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:  #343A40;\n"
"}\n"
"\n"
"#header, #mainBody, #registration {\n"
"background-color: #495057;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background: transparent;\n"
"color: #E9ECEF;\n"
"}\n"
"\n"
"QComboBox, QLabel {\n"
"background: transparent;\n"
"background-color: #495057;\n"
"color: #E9ECEF;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 0, -1)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.title = QLabel(self.header)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semilight"])
        font1.setPointSize(12)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title)


        self.verticalLayout.addWidget(self.header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.mainBody.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.mainBody)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.login = QLineEdit(self.mainBody)
        self.login.setObjectName(u"login")
        font2 = QFont()
        font2.setPointSize(12)
        self.login.setFont(font2)
        self.login.setMaxLength(30)

        self.verticalLayout_3.addWidget(self.login)

        self.pss = QLineEdit(self.mainBody)
        self.pss.setObjectName(u"pss")
        self.pss.setFont(font2)

        self.verticalLayout_3.addWidget(self.pss)

        self.loginBtn = QPushButton(self.mainBody)
        self.loginBtn.setObjectName(u"loginBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.loginBtn.setFont(font3)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.loginBtn)

        self.resetPassBtn = QPushButton(self.mainBody)
        self.resetPassBtn.setObjectName(u"resetPassBtn")
        sizePolicy2.setHeightForWidth(self.resetPassBtn.sizePolicy().hasHeightForWidth())
        self.resetPassBtn.setSizePolicy(sizePolicy2)
        self.resetPassBtn.setFont(font3)
        self.resetPassBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.resetPassBtn)


        self.verticalLayout.addWidget(self.mainBody)

        self.registration = QWidget(self.centralwidget)
        self.registration.setObjectName(u"registration")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.registration.sizePolicy().hasHeightForWidth())
        self.registration.setSizePolicy(sizePolicy3)
        self.verticalLayout_4 = QVBoxLayout(self.registration)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.firstlyQ = QLabel(self.registration)
        self.firstlyQ.setObjectName(u"firstlyQ")
        self.firstlyQ.setFont(font2)

        self.verticalLayout_4.addWidget(self.firstlyQ)

        self.signupBtn = QPushButton(self.registration)
        self.signupBtn.setObjectName(u"signupBtn")
        sizePolicy2.setHeightForWidth(self.signupBtn.sizePolicy().hasHeightForWidth())
        self.signupBtn.setSizePolicy(sizePolicy2)
        self.signupBtn.setFont(font3)
        self.signupBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.signupBtn)


        self.verticalLayout.addWidget(self.registration)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.login.setText("")
        self.login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.pss.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.resetPassBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.firstlyQ.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0435\u0440\u0432\u044b\u0439 \u0440\u0430\u0437?", None))
        self.signupBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

