# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(489, 396)
        MainWindow.setMinimumSize(QSize(0, 343))
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
"#centralwidget{\n"
"background-color: #212529;\n"
"}\n"
"\n"
"#header, #mainBody, #person, #buttons {\n"
"background-color: #495057;\n"
"}\n"
"\n"
"#username, #title, #selectedPss{\n"
"background-color: #495057;\n"
"color: #E9ECEF;\n"
"}\n"
"\n"
"QTableWidget {\n"
"background: transparent;\n"
"background-color: #495057;\n"
"color: black;\n"
"}\n"
"\n"
"QHeaderView {\n"
"background: "
                        "transparent;\n"
"background-color: #495057;\n"
"color: black;\n"
"}\n"
"\n"
"QTableWidget::section {\n"
"background-color: #CED4DA;\n"
"height: 50px;\n"
"color: white;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"background-color: #CED4DA;\n"
"boarder-style: none;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"color: #FFF;\n"
"background-color: #ADB5BD;\n"
"boarder: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, -1)
        self.person = QWidget(self.centralwidget)
        self.person.setObjectName(u"person")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.person.sizePolicy().hasHeightForWidth())
        self.person.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.person)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.username = QLabel(self.person)
        self.username.setObjectName(u"username")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.username.setFont(font1)
        self.username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.username)

        self.buttons = QWidget(self.person)
        self.buttons.setObjectName(u"buttons")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy3)
        self.buttons.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.buttons)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.newKeyBtn = QPushButton(self.buttons)
        self.newKeyBtn.setObjectName(u"newKeyBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.newKeyBtn.sizePolicy().hasHeightForWidth())
        self.newKeyBtn.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.newKeyBtn.setFont(font2)
        self.newKeyBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newKeyBtn.setIconSize(QSize(25, 25))
        self.newKeyBtn.setAutoDefault(False)

        self.verticalLayout.addWidget(self.newKeyBtn)

        self.editBtn = QPushButton(self.buttons)
        self.editBtn.setObjectName(u"editBtn")
        sizePolicy4.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy4)
        self.editBtn.setFont(font2)
        self.editBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editBtn.setIconSize(QSize(25, 25))
        self.editBtn.setAutoDefault(False)

        self.verticalLayout.addWidget(self.editBtn)

        self.deleteBtn = QPushButton(self.buttons)
        self.deleteBtn.setObjectName(u"deleteBtn")
        sizePolicy4.setHeightForWidth(self.deleteBtn.sizePolicy().hasHeightForWidth())
        self.deleteBtn.setSizePolicy(sizePolicy4)
        self.deleteBtn.setFont(font2)
        self.deleteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteBtn.setIconSize(QSize(25, 25))
        self.deleteBtn.setAutoDefault(False)

        self.verticalLayout.addWidget(self.deleteBtn)


        self.verticalLayout_4.addWidget(self.buttons, 0, Qt.AlignTop)

        self.uploadBtn = QPushButton(self.person)
        self.uploadBtn.setObjectName(u"uploadBtn")
        sizePolicy4.setHeightForWidth(self.uploadBtn.sizePolicy().hasHeightForWidth())
        self.uploadBtn.setSizePolicy(sizePolicy4)
        self.uploadBtn.setFont(font2)
        self.uploadBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.uploadBtn, 0, Qt.AlignBottom)

        self.delAccButton = QPushButton(self.person)
        self.delAccButton.setObjectName(u"delAccButton")
        sizePolicy4.setHeightForWidth(self.delAccButton.sizePolicy().hasHeightForWidth())
        self.delAccButton.setSizePolicy(sizePolicy4)
        self.delAccButton.setFont(font2)

        self.verticalLayout_4.addWidget(self.delAccButton)

        self.quitBtn = QPushButton(self.person)
        self.quitBtn.setObjectName(u"quitBtn")
        sizePolicy4.setHeightForWidth(self.quitBtn.sizePolicy().hasHeightForWidth())
        self.quitBtn.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.quitBtn.setFont(font3)

        self.verticalLayout_4.addWidget(self.quitBtn)


        self.horizontalLayout_3.addWidget(self.person)

        self.general = QWidget(self.centralwidget)
        self.general.setObjectName(u"general")
        self.general.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.general)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.general)
        self.header.setObjectName(u"header")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy5)
        self.header.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(25, 9, 20, 9)
        self.title = QLabel(self.header)
        self.title.setObjectName(u"title")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy6)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Semibold"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.title.setFont(font4)
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title)


        self.verticalLayout_3.addWidget(self.header)

        self.mainBody = QWidget(self.general)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy7)
        self.verticalLayout_2 = QVBoxLayout(self.mainBody)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.mainBody)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(168, 168, 168));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy8)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setTextElideMode(Qt.ElideNone)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.selectedPss = QLineEdit(self.mainBody)
        self.selectedPss.setObjectName(u"selectedPss")
        self.selectedPss.setFont(font1)
        self.selectedPss.setAlignment(Qt.AlignCenter)
        self.selectedPss.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.selectedPss)


        self.verticalLayout_3.addWidget(self.mainBody)


        self.horizontalLayout_3.addWidget(self.general)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CryptoKeyPro", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"your@mail.com", None))
        self.newKeyBtn.setText(QCoreApplication.translate("MainWindow", u"New Key", None))
        self.editBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.uploadBtn.setText(QCoreApplication.translate("MainWindow", u"Download data", None))
        self.delAccButton.setText(QCoreApplication.translate("MainWindow", u"Delete account", None))
        self.quitBtn.setText(QCoreApplication.translate("MainWindow", u"QUIT", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"CryptoKey", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None));
        self.selectedPss.setText(QCoreApplication.translate("MainWindow", u"selectedPassword", None))
    # retranslateUi

