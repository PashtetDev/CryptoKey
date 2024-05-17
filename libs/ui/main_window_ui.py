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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import libs.ui.icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 530)
        MainWindow.setMinimumSize(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
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
"background-color: transparent;\n"
"color: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"#from1, #from2{\n"
"padding-left: 5px;\n"
"color: #95d5b2;\n"
"}\n"
"#check, #alg{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:2, stop:0 #173B49, stop:0.55 #088572, stop:1 #088572);\n"
"border-radius: 10px;\n"
"}\n"
"#moreBtn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:2, stop:0 #08D472, stop:0.45 #088572, stop:1 #088572);\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"#moreBtn:hover{\n"
"border: 2px solid white;\n"
"}\n"
"#label_4, #newsTitle, #newsTitle2{\n"
"padding: 5px;\n"
"}\n"
"#custBtn{\n"
"margin-left: 7px;\n"
"background-color: #57b8ff;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"#custBtn:hover{\n"
"margin-left: 7px;\n"
"background-color: #1789fc;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"#custBtn:pressed{\n"
"margin-left: 7px;\n"
"background-color: #296eb4;\n"
"padding: 5px;\n"
"bord"
                        "er-radius: 10px;\n"
"}\n"
"#checkBtn, #readBtn, #checkBtn, #readBtn2, #readBtn3{\n"
"margin-left: 7px;\n"
"background-color: #088572;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"#checkBtn:hover, #readBtn2:hover, #readBtn3:hover, #readBtn:hover{\n"
"background-color:#173B49;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"#checkBtn:pressed, #readBtn2:pressed, #readBtn3:pressed, #readBtn:pressed{\n"
"background-color:  #0D0D15;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#custom{\n"
"background-color: qlineargradient(spread:pad, x-1:1, y1:0, x2:1, y2:2, stop:0 #a8dcd1, stop:0.3 #65def1, stop:1 #65def1);\n"
"border-radius: 10px;\n"
"}\n"
"#header{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:2, stop:0 #088572, stop:0.15 #088572, stop:0.5 #173B49, stop:1 #173B49);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"selection-background-color: #088572;\n"
"background-color: #173B49;\n"
"}\n"
"\n"
"#centralWidget{\n"
"background-color: #"
                        "0D0D15;\n"
"}\n"
"\n"
"#closeEditor{\n"
"background-color:#088572;\n"
"padding-left: -2px;\n"
"padding-right: -2px;\n"
"border-radius: 10px;\n"
"}\n"
"#closeEditor:hover{\n"
"background-color:  #173B49;\n"
"}\n"
"#closeEditor:pressed{\n"
"background-color: #0D0D15;\n"
"}\n"
"\n"
"#menuPanel{\n"
"background-color: #088572\n"
"}\n"
"\n"
"#loginWindow, #regWindow, #keyEditor{\n"
"background-color: #088572;\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"#mainBody > QLineEdit, #mainBody_2 > QLineEdit, #email{\n"
"background-color: #0D0D15;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#mainBody > QPushButton, #mainBody_2 > QPushButton, #signupBtn, #saveBtn, #generateBtn{\n"
"text-align: center;\n"
"width: 180px;\n"
"padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"#mainBody > QPushButton:hover, #signupBtn:hover, #mainBody_2 > QPushButton:hover, #saveBtn:hover, #generateBtn:hover{\n"
"background-color: #173B49;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#mainBody > QPushButton:pressed, #signupBtn:pressed, #mainBody_2 > "
                        "QPushButton:pressed, #saveBtn:pressed, #generateBtn:pressed{\n"
"border: 3px solid #0D0D15;\n"
"font-weight: bold;\n"
"background-color:#0D0D15;\n"
"}\n"
"\n"
"#menuPanel > QLabel{\n"
"text-align: left;\n"
"padding: 5px 7px;\n"
"}\n"
"#postTitle{\n"
"margin-left:2px;\n"
"}\n"
"#plainTextEdit{\n"
"margin-left:4px;\n"
"}\n"
"#title, #slogan{\n"
"text-align: left;\n"
"}\n"
"\n"
"#userIcon{\n"
"background-color: transparent;\n"
"border: 5px solid white;\n"
"border-radius: 40px\n"
"}\n"
"\n"
"QTableWidget {\n"
"margin-left: 10px;\n"
"}\n"
"\n"
"QTableWidget  QHeaderView{\n"
"color: #0D0D15;\n"
"}\n"
"\n"
"QTableWidget::section {\n"
"background-color: #173B49;\n"
"height: 50px;\n"
"color: #0D0D15;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"color: white;\n"
"background-color: #173B49;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"color: white;\n"
"background-color: #088572;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"color: white;\n"
"border: 2px solid  #088572;\n"
"}\n"
"\n"
"#menuPanel > QWid"
                        "get > QPushButton{\n"
"text-align :left;\n"
"background-color: #088572;\n"
"padding:5;\n"
"margin-left: 15px;\n"
"width: 180px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px\n"
"}\n"
"\n"
"#menuPanel > QWidget > QPushButton:hover{\n"
"background-color: #173B49;\n"
"border-left: 3px solid #173B49;\n"
"margin-left: 15px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px\n"
"}\n"
"\n"
"#menuPanel > QWidget > QPushButton:focus{\n"
"border-left: 3px solid #25CD85;\n"
"font-weight: bold;\n"
"padding-left:7px;\n"
"background-color: #0D0D15;\n"
"}\n"
"\n"
"#tgbotBtn{\n"
"text-align: center;\n"
"width: 150px;\n"
"padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"#tgbotBtn:hover{\n"
"background-color: #173B49;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#tgbotBtn:pressed{\n"
"border: 3px solid #0D0D15;\n"
"font-weight: bold;\n"
"background-color:#0D0D15;\n"
"}\n"
"\n"
"#buttons > QPushButton, #buttons_2 > QPushButton{\n"
"text-align: left;\n"
"padding:5;\n"
"}\n"
"\n"
" #buttons > QPushB"
                        "utton:hover, #buttons_2 > QPushButton:hover{\n"
"text-align: left;\n"
"border: 2px solid #173B49;\n"
"padding:5;\n"
"}\n"
"\n"
"#buttons > QPushButton:pressed, #buttons_2 > QPushButton:pressed{\n"
"text-align: left;\n"
"padding:5;\n"
"}\n"
"\n"
"#selectedPss{\n"
"padding-bottom:10px;\n"
"}")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QSize(700, 530))
        self.horizontalLayout_3 = QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.general = QWidget(self.centralWidget)
        self.general.setObjectName(u"general")
        sizePolicy.setHeightForWidth(self.general.sizePolicy().hasHeightForWidth())
        self.general.setSizePolicy(sizePolicy)
        self.general.setMinimumSize(QSize(0, 0))
        self.general.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.general)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.menuPanel = QWidget(self.general)
        self.menuPanel.setObjectName(u"menuPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuPanel.sizePolicy().hasHeightForWidth())
        self.menuPanel.setSizePolicy(sizePolicy1)
        self.menuPanel.setMinimumSize(QSize(200, 0))
        self.menuPanel.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.menuPanel)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 15, 0, 15)
        self.widget_3 = QWidget(self.menuPanel)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 5, 5, 0)
        self.title = QLabel(self.widget_3)
        self.title.setObjectName(u"title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.title, 0, Qt.AlignLeft)

        self.slogan = QLabel(self.widget_3)
        self.slogan.setObjectName(u"slogan")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semilight"])
        font2.setPointSize(10)
        self.slogan.setFont(font2)

        self.verticalLayout_11.addWidget(self.slogan)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.widget = QWidget(self.menuPanel)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainBtn = QPushButton(self.widget)
        self.mainBtn.setObjectName(u"mainBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainBtn.sizePolicy().hasHeightForWidth())
        self.mainBtn.setSizePolicy(sizePolicy4)
        self.mainBtn.setMinimumSize(QSize(0, 30))
        self.mainBtn.setMaximumSize(QSize(16777215, 30))
        self.mainBtn.setBaseSize(QSize(0, 0))
        self.mainBtn.setFont(font2)
        self.mainBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/pics/res/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.mainBtn.setIcon(icon)
        self.mainBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.mainBtn)

        self.managerBtn = QPushButton(self.widget)
        self.managerBtn.setObjectName(u"managerBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.managerBtn.sizePolicy().hasHeightForWidth())
        self.managerBtn.setSizePolicy(sizePolicy5)
        self.managerBtn.setFont(font2)
        self.managerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.managerBtn.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon1 = QIcon()
        icon1.addFile(u":/pics/res/shield.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.managerBtn.setIcon(icon1)
        self.managerBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.managerBtn)

        self.settingBtn = QPushButton(self.widget)
        self.settingBtn.setObjectName(u"settingBtn")
        sizePolicy5.setHeightForWidth(self.settingBtn.sizePolicy().hasHeightForWidth())
        self.settingBtn.setSizePolicy(sizePolicy5)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semilight"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.settingBtn.setFont(font3)
        self.settingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingBtn.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u":/pics/res/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon2)
        self.settingBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.settingBtn)


        self.verticalLayout_4.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tgbotBtn = QPushButton(self.menuPanel)
        self.tgbotBtn.setObjectName(u"tgbotBtn")
        sizePolicy5.setHeightForWidth(self.tgbotBtn.sizePolicy().hasHeightForWidth())
        self.tgbotBtn.setSizePolicy(sizePolicy5)
        self.tgbotBtn.setFont(font2)
        self.tgbotBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.tgbotBtn, 0, Qt.AlignHCenter)

        self.versionLabel = QLabel(self.menuPanel)
        self.versionLabel.setObjectName(u"versionLabel")
        sizePolicy2.setHeightForWidth(self.versionLabel.sizePolicy().hasHeightForWidth())
        self.versionLabel.setSizePolicy(sizePolicy2)
        self.versionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.versionLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.menuPanel)

        self.mainMenu = QWidget(self.general)
        self.mainMenu.setObjectName(u"mainMenu")
        sizePolicy.setHeightForWidth(self.mainMenu.sizePolicy().hasHeightForWidth())
        self.mainMenu.setSizePolicy(sizePolicy)
        self.mainMenu.setMinimumSize(QSize(0, 0))
        self.mainMenu.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.mainMenu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.passwordManager = QWidget(self.mainMenu)
        self.passwordManager.setObjectName(u"passwordManager")
        sizePolicy.setHeightForWidth(self.passwordManager.sizePolicy().hasHeightForWidth())
        self.passwordManager.setSizePolicy(sizePolicy)
        self.passwordManager.setMinimumSize(QSize(0, 0))
        self.passwordManager.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.passwordManager)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.passwordManager)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 0, 20)
        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Semilight"])
        font4.setPointSize(14)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_2 = QWidget(self.passwordManager)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(168, 168, 168));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
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

        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.buttons_2 = QWidget(self.widget_2)
        self.buttons_2.setObjectName(u"buttons_2")
        sizePolicy2.setHeightForWidth(self.buttons_2.sizePolicy().hasHeightForWidth())
        self.buttons_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_6 = QVBoxLayout(self.buttons_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 9, 0)
        self.newKeyBtn = QPushButton(self.buttons_2)
        self.newKeyBtn.setObjectName(u"newKeyBtn")
        sizePolicy2.setHeightForWidth(self.newKeyBtn.sizePolicy().hasHeightForWidth())
        self.newKeyBtn.setSizePolicy(sizePolicy2)
        self.newKeyBtn.setMinimumSize(QSize(200, 30))
        self.newKeyBtn.setMaximumSize(QSize(300, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Semibold"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.newKeyBtn.setFont(font5)
        self.newKeyBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newKeyBtn.setIconSize(QSize(25, 25))
        self.newKeyBtn.setAutoDefault(False)

        self.verticalLayout_6.addWidget(self.newKeyBtn)

        self.deleteBtn = QPushButton(self.buttons_2)
        self.deleteBtn.setObjectName(u"deleteBtn")
        sizePolicy2.setHeightForWidth(self.deleteBtn.sizePolicy().hasHeightForWidth())
        self.deleteBtn.setSizePolicy(sizePolicy2)
        self.deleteBtn.setMinimumSize(QSize(200, 30))
        self.deleteBtn.setMaximumSize(QSize(300, 30))
        self.deleteBtn.setFont(font5)
        self.deleteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteBtn.setIconSize(QSize(25, 25))
        self.deleteBtn.setAutoDefault(False)

        self.verticalLayout_6.addWidget(self.deleteBtn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.keyEditor = QWidget(self.buttons_2)
        self.keyEditor.setObjectName(u"keyEditor")
        sizePolicy.setHeightForWidth(self.keyEditor.sizePolicy().hasHeightForWidth())
        self.keyEditor.setSizePolicy(sizePolicy)
        self.keyEditor.setMinimumSize(QSize(0, 0))
        self.keyEditor.setMaximumSize(QSize(300, 450))
        self.verticalLayout_18 = QVBoxLayout(self.keyEditor)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(20, 20, 20, 20)
        self.mainBody_3 = QWidget(self.keyEditor)
        self.mainBody_3.setObjectName(u"mainBody_3")
        sizePolicy.setHeightForWidth(self.mainBody_3.sizePolicy().hasHeightForWidth())
        self.mainBody_3.setSizePolicy(sizePolicy)
        self.mainBody_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_20 = QVBoxLayout(self.mainBody_3)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.editorHeader = QWidget(self.mainBody_3)
        self.editorHeader.setObjectName(u"editorHeader")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.editorHeader.sizePolicy().hasHeightForWidth())
        self.editorHeader.setSizePolicy(sizePolicy6)
        self.horizontalLayout_7 = QHBoxLayout(self.editorHeader)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.titleEdit = QLineEdit(self.editorHeader)
        self.titleEdit.setObjectName(u"titleEdit")
        sizePolicy.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy)
        self.titleEdit.setFont(font5)
        self.titleEdit.setMaxLength(30)
        self.titleEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.titleEdit, 0, Qt.AlignLeft)

        self.closeEditor = QPushButton(self.editorHeader)
        self.closeEditor.setObjectName(u"closeEditor")
        sizePolicy5.setHeightForWidth(self.closeEditor.sizePolicy().hasHeightForWidth())
        self.closeEditor.setSizePolicy(sizePolicy5)
        self.closeEditor.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeEditor.setLayoutDirection(Qt.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u":/pics/res/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeEditor.setIcon(icon3)
        self.closeEditor.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.closeEditor, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.editorHeader, 0, Qt.AlignRight)

        self.stringEdit = QLineEdit(self.mainBody_3)
        self.stringEdit.setObjectName(u"stringEdit")
        font6 = QFont()
        font6.setPointSize(10)
        self.stringEdit.setFont(font6)

        self.verticalLayout_20.addWidget(self.stringEdit, 0, Qt.AlignTop)

        self.modelEdit = QComboBox(self.mainBody_3)
        self.modelEdit.addItem("")
        self.modelEdit.addItem("")
        self.modelEdit.addItem("")
        self.modelEdit.setObjectName(u"modelEdit")
        self.modelEdit.setFont(font2)
        self.modelEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelEdit.setEditable(False)
        self.modelEdit.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_20.addWidget(self.modelEdit)

        self.password = QLineEdit(self.mainBody_3)
        self.password.setObjectName(u"password")
        font7 = QFont()
        font7.setPointSize(12)
        self.password.setFont(font7)
        self.password.setReadOnly(True)

        self.verticalLayout_20.addWidget(self.password)

        self.saveBtn = QPushButton(self.mainBody_3)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy5.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy5)
        self.saveBtn.setFont(font5)
        self.saveBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.saveBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.mainBody_3)


        self.verticalLayout_6.addWidget(self.keyEditor)


        self.horizontalLayout_4.addWidget(self.buttons_2, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_2, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.passwordManager)

        self.settings = QWidget(self.mainMenu)
        self.settings.setObjectName(u"settings")
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setMinimumSize(QSize(0, 0))
        self.settings.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.settings)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.title_2 = QWidget(self.settings)
        self.title_2.setObjectName(u"title_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy7)
        self.verticalLayout_8 = QVBoxLayout(self.title_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 0, 20)
        self.label_2 = QLabel(self.title_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.title_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.user = QWidget(self.settings)
        self.user.setObjectName(u"user")
        sizePolicy2.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.user)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.userIcon = QLabel(self.user)
        self.userIcon.setObjectName(u"userIcon")
        sizePolicy5.setHeightForWidth(self.userIcon.sizePolicy().hasHeightForWidth())
        self.userIcon.setSizePolicy(sizePolicy5)
        self.userIcon.setMaximumSize(QSize(80, 80))
        self.userIcon.setPixmap(QPixmap(u":/pics/res/user.svg"))
        self.userIcon.setScaledContents(True)
        self.userIcon.setAlignment(Qt.AlignCenter)
        self.userIcon.setWordWrap(False)

        self.verticalLayout.addWidget(self.userIcon, 0, Qt.AlignHCenter)

        self.username = QLabel(self.user)
        self.username.setObjectName(u"username")
        sizePolicy2.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy2)
        self.username.setFont(font5)
        self.username.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.username)


        self.verticalLayout_5.addWidget(self.user, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.buttons = QWidget(self.settings)
        self.buttons.setObjectName(u"buttons")
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.buttons)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 15, -1, 20)
        self.pssChangeBtn = QPushButton(self.buttons)
        self.pssChangeBtn.setObjectName(u"pssChangeBtn")
        sizePolicy5.setHeightForWidth(self.pssChangeBtn.sizePolicy().hasHeightForWidth())
        self.pssChangeBtn.setSizePolicy(sizePolicy5)
        self.pssChangeBtn.setMinimumSize(QSize(270, 30))
        self.pssChangeBtn.setFont(font5)
        self.pssChangeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.pssChangeBtn)

        self.uploadBtn = QPushButton(self.buttons)
        self.uploadBtn.setObjectName(u"uploadBtn")
        sizePolicy5.setHeightForWidth(self.uploadBtn.sizePolicy().hasHeightForWidth())
        self.uploadBtn.setSizePolicy(sizePolicy5)
        self.uploadBtn.setMinimumSize(QSize(270, 30))
        self.uploadBtn.setFont(font5)
        self.uploadBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.uploadBtn)

        self.customBtn = QPushButton(self.buttons)
        self.customBtn.setObjectName(u"customBtn")
        sizePolicy5.setHeightForWidth(self.customBtn.sizePolicy().hasHeightForWidth())
        self.customBtn.setSizePolicy(sizePolicy5)
        self.customBtn.setMinimumSize(QSize(270, 30))
        self.customBtn.setFont(font5)
        self.customBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.customBtn)

        self.supportBtn = QPushButton(self.buttons)
        self.supportBtn.setObjectName(u"supportBtn")
        sizePolicy5.setHeightForWidth(self.supportBtn.sizePolicy().hasHeightForWidth())
        self.supportBtn.setSizePolicy(sizePolicy5)
        self.supportBtn.setMinimumSize(QSize(270, 30))
        self.supportBtn.setFont(font5)
        self.supportBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.supportBtn)

        self.delAccButton = QPushButton(self.buttons)
        self.delAccButton.setObjectName(u"delAccButton")
        sizePolicy5.setHeightForWidth(self.delAccButton.sizePolicy().hasHeightForWidth())
        self.delAccButton.setSizePolicy(sizePolicy5)
        self.delAccButton.setMinimumSize(QSize(270, 30))
        self.delAccButton.setFont(font5)
        self.delAccButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.delAccButton)

        self.quitBtn = QPushButton(self.buttons)
        self.quitBtn.setObjectName(u"quitBtn")
        sizePolicy2.setHeightForWidth(self.quitBtn.sizePolicy().hasHeightForWidth())
        self.quitBtn.setSizePolicy(sizePolicy2)
        self.quitBtn.setMinimumSize(QSize(270, 30))
        self.quitBtn.setFont(font5)
        self.quitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.quitBtn, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.buttons)


        self.horizontalLayout.addWidget(self.settings)

        self.mainPage = QWidget(self.mainMenu)
        self.mainPage.setObjectName(u"mainPage")
        sizePolicy.setHeightForWidth(self.mainPage.sizePolicy().hasHeightForWidth())
        self.mainPage.setSizePolicy(sizePolicy)
        self.mainPage.setMinimumSize(QSize(0, 0))
        self.mainPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.mainPage)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 20, 20, 20)
        self.header = QWidget(self.mainPage)
        self.header.setObjectName(u"header")
        sizePolicy3.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy3)
        self.header.setMinimumSize(QSize(0, 170))
        self.header.setMaximumSize(QSize(16777215, 170))
        self.horizontalLayout_9 = QHBoxLayout(self.header)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.image = QLabel(self.header)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(140, 140))
        self.image.setPixmap(QPixmap(u":/pics/res/image.png"))
        self.image.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.image)

        self.widget_8 = QWidget(self.header)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QSize(0, 140))
        self.widget_8.setMaximumSize(QSize(16777215, 140))
        self.verticalLayout_25 = QVBoxLayout(self.widget_8)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, -1, 0, 0)
        self.postTitle = QLabel(self.widget_8)
        self.postTitle.setObjectName(u"postTitle")
        sizePolicy5.setHeightForWidth(self.postTitle.sizePolicy().hasHeightForWidth())
        self.postTitle.setSizePolicy(sizePolicy5)
        self.postTitle.setFont(font1)

        self.verticalLayout_25.addWidget(self.postTitle, 0, Qt.AlignTop)

        self.plainTextEdit = QPlainTextEdit(self.widget_8)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy2.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy2)
        self.plainTextEdit.setMaximumSize(QSize(16777215, 50))
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_25.addWidget(self.plainTextEdit)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_7)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 10, 0)
        self.checkBtn = QPushButton(self.widget_9)
        self.checkBtn.setObjectName(u"checkBtn")
        self.checkBtn.setMinimumSize(QSize(150, 0))
        self.checkBtn.setMaximumSize(QSize(16777215, 16777215))
        self.checkBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.checkBtn)

        self.readBtn3 = QPushButton(self.widget_9)
        self.readBtn3.setObjectName(u"readBtn3")
        self.readBtn3.setMinimumSize(QSize(120, 0))
        self.readBtn3.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_10.addWidget(self.readBtn3)


        self.verticalLayout_25.addWidget(self.widget_9)


        self.horizontalLayout_9.addWidget(self.widget_8, 0, Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.header)

        self.widget_4 = QWidget(self.mainPage)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.check = QWidget(self.widget_4)
        self.check.setObjectName(u"check")
        self.check.setMinimumSize(QSize(0, 0))
        self.check.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_22 = QVBoxLayout(self.check)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.newsTitle = QPlainTextEdit(self.check)
        self.newsTitle.setObjectName(u"newsTitle")
        sizePolicy.setHeightForWidth(self.newsTitle.sizePolicy().hasHeightForWidth())
        self.newsTitle.setSizePolicy(sizePolicy)
        self.newsTitle.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI Semibold"])
        font8.setPointSize(9)
        font8.setBold(True)
        self.newsTitle.setFont(font8)
        self.newsTitle.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.newsTitle.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_22.addWidget(self.newsTitle)

        self.from1 = QLabel(self.check)
        self.from1.setObjectName(u"from1")

        self.verticalLayout_22.addWidget(self.from1, 0, Qt.AlignBottom)

        self.readBtn = QPushButton(self.check)
        self.readBtn.setObjectName(u"readBtn")
        sizePolicy5.setHeightForWidth(self.readBtn.sizePolicy().hasHeightForWidth())
        self.readBtn.setSizePolicy(sizePolicy5)
        self.readBtn.setMinimumSize(QSize(100, 0))
        self.readBtn.setFont(font3)
        self.readBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_22.addWidget(self.readBtn)


        self.horizontalLayout_5.addWidget(self.check)

        self.alg = QWidget(self.widget_4)
        self.alg.setObjectName(u"alg")
        self.alg.setMinimumSize(QSize(0, 0))
        self.alg.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_24 = QVBoxLayout(self.alg)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.newsTitle2 = QPlainTextEdit(self.alg)
        self.newsTitle2.setObjectName(u"newsTitle2")
        sizePolicy.setHeightForWidth(self.newsTitle2.sizePolicy().hasHeightForWidth())
        self.newsTitle2.setSizePolicy(sizePolicy)
        self.newsTitle2.setMaximumSize(QSize(16777215, 16777215))
        self.newsTitle2.setFont(font8)
        self.newsTitle2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.newsTitle2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_24.addWidget(self.newsTitle2)

        self.from2 = QLabel(self.alg)
        self.from2.setObjectName(u"from2")

        self.verticalLayout_24.addWidget(self.from2, 0, Qt.AlignBottom)

        self.readBtn2 = QPushButton(self.alg)
        self.readBtn2.setObjectName(u"readBtn2")
        sizePolicy5.setHeightForWidth(self.readBtn2.sizePolicy().hasHeightForWidth())
        self.readBtn2.setSizePolicy(sizePolicy5)
        self.readBtn2.setMinimumSize(QSize(100, 0))
        self.readBtn2.setFont(font3)
        self.readBtn2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_24.addWidget(self.readBtn2)


        self.horizontalLayout_5.addWidget(self.alg)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.widget_7 = QWidget(self.mainPage)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 150))
        self.widget_7.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.custom = QWidget(self.widget_7)
        self.custom.setObjectName(u"custom")
        sizePolicy.setHeightForWidth(self.custom.sizePolicy().hasHeightForWidth())
        self.custom.setSizePolicy(sizePolicy)
        self.custom.setMinimumSize(QSize(0, 100))
        self.custom.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_21 = QVBoxLayout(self.custom)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_4 = QPlainTextEdit(self.custom)
        self.label_4.setObjectName(u"label_4")
        font9 = QFont()
        font9.setFamilies([u"Segoe UI Semibold"])
        font9.setPointSize(10)
        font9.setBold(True)
        self.label_4.setFont(font9)
        self.label_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_21.addWidget(self.label_4)

        self.custBtn = QPushButton(self.custom)
        self.custBtn.setObjectName(u"custBtn")
        sizePolicy5.setHeightForWidth(self.custBtn.sizePolicy().hasHeightForWidth())
        self.custBtn.setSizePolicy(sizePolicy5)
        self.custBtn.setMinimumSize(QSize(100, 0))
        self.custBtn.setFont(font3)
        self.custBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_21.addWidget(self.custBtn)


        self.horizontalLayout_2.addWidget(self.custom)

        self.moreBtn = QPushButton(self.widget_7)
        self.moreBtn.setObjectName(u"moreBtn")
        sizePolicy6.setHeightForWidth(self.moreBtn.sizePolicy().hasHeightForWidth())
        self.moreBtn.setSizePolicy(sizePolicy6)
        self.moreBtn.setMinimumSize(QSize(130, 0))
        self.moreBtn.setMaximumSize(QSize(130, 100))
        self.moreBtn.setFont(font5)
        self.moreBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.moreBtn)


        self.verticalLayout_10.addWidget(self.widget_7, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.mainPage)


        self.horizontalLayout_6.addWidget(self.mainMenu)


        self.horizontalLayout_3.addWidget(self.general)

        self.regMenu = QWidget(self.centralWidget)
        self.regMenu.setObjectName(u"regMenu")
        sizePolicy.setHeightForWidth(self.regMenu.sizePolicy().hasHeightForWidth())
        self.regMenu.setSizePolicy(sizePolicy)
        self.regMenu.setMinimumSize(QSize(0, 0))
        self.regMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.regMenu)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.regWindow = QWidget(self.regMenu)
        self.regWindow.setObjectName(u"regWindow")
        sizePolicy1.setHeightForWidth(self.regWindow.sizePolicy().hasHeightForWidth())
        self.regWindow.setSizePolicy(sizePolicy1)
        self.regWindow.setMinimumSize(QSize(300, 450))
        self.regWindow.setMaximumSize(QSize(300, 450))
        self.verticalLayout_16 = QVBoxLayout(self.regWindow)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(20, 20, 20, 20)
        self.pics_2 = QLabel(self.regWindow)
        self.pics_2.setObjectName(u"pics_2")
        self.pics_2.setMinimumSize(QSize(100, 100))
        self.pics_2.setMaximumSize(QSize(100, 100))
        self.pics_2.setPixmap(QPixmap(u":/pics/res/shield.svg"))
        self.pics_2.setScaledContents(True)

        self.verticalLayout_16.addWidget(self.pics_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)

        self.mainBody_2 = QWidget(self.regWindow)
        self.mainBody_2.setObjectName(u"mainBody_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.mainBody_2.sizePolicy().hasHeightForWidth())
        self.mainBody_2.setSizePolicy(sizePolicy8)
        self.mainBody_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_17 = QVBoxLayout(self.mainBody_2)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.mainBody_2)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy2.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy2)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.email = QLineEdit(self.widget_5)
        self.email.setObjectName(u"email")
        self.email.setFont(font6)

        self.horizontalLayout_8.addWidget(self.email)

        self.emailCheck = QCheckBox(self.widget_5)
        self.emailCheck.setObjectName(u"emailCheck")
        self.emailCheck.setCheckable(False)
        self.emailCheck.setChecked(False)
        self.emailCheck.setAutoRepeat(False)
        self.emailCheck.setAutoExclusive(False)
        self.emailCheck.setTristate(False)

        self.horizontalLayout_8.addWidget(self.emailCheck)


        self.verticalLayout_17.addWidget(self.widget_5)

        self.codeInput = QLineEdit(self.mainBody_2)
        self.codeInput.setObjectName(u"codeInput")
        self.codeInput.setFont(font6)

        self.verticalLayout_17.addWidget(self.codeInput)

        self.sendCodeBtn = QPushButton(self.mainBody_2)
        self.sendCodeBtn.setObjectName(u"sendCodeBtn")
        sizePolicy4.setHeightForWidth(self.sendCodeBtn.sizePolicy().hasHeightForWidth())
        self.sendCodeBtn.setSizePolicy(sizePolicy4)
        self.sendCodeBtn.setFont(font5)
        self.sendCodeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.sendCodeBtn, 0, Qt.AlignHCenter)

        self.createPss = QLineEdit(self.mainBody_2)
        self.createPss.setObjectName(u"createPss")
        self.createPss.setFont(font6)

        self.verticalLayout_17.addWidget(self.createPss)

        self.confPss = QLineEdit(self.mainBody_2)
        self.confPss.setObjectName(u"confPss")
        self.confPss.setFont(font6)

        self.verticalLayout_17.addWidget(self.confPss)

        self.regBtn = QPushButton(self.mainBody_2)
        self.regBtn.setObjectName(u"regBtn")
        sizePolicy5.setHeightForWidth(self.regBtn.sizePolicy().hasHeightForWidth())
        self.regBtn.setSizePolicy(sizePolicy5)
        self.regBtn.setFont(font5)
        self.regBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.regBtn, 0, Qt.AlignHCenter)

        self.toExitBtn = QPushButton(self.mainBody_2)
        self.toExitBtn.setObjectName(u"toExitBtn")
        sizePolicy5.setHeightForWidth(self.toExitBtn.sizePolicy().hasHeightForWidth())
        self.toExitBtn.setSizePolicy(sizePolicy5)
        self.toExitBtn.setFont(font5)
        self.toExitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.toExitBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.mainBody_2)


        self.verticalLayout_19.addWidget(self.regWindow, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.regMenu)

        self.loginMenu = QWidget(self.centralWidget)
        self.loginMenu.setObjectName(u"loginMenu")
        sizePolicy.setHeightForWidth(self.loginMenu.sizePolicy().hasHeightForWidth())
        self.loginMenu.setSizePolicy(sizePolicy)
        self.loginMenu.setMinimumSize(QSize(0, 0))
        self.loginMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.loginMenu)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.loginWindow = QWidget(self.loginMenu)
        self.loginWindow.setObjectName(u"loginWindow")
        sizePolicy1.setHeightForWidth(self.loginWindow.sizePolicy().hasHeightForWidth())
        self.loginWindow.setSizePolicy(sizePolicy1)
        self.loginWindow.setMinimumSize(QSize(300, 450))
        self.loginWindow.setMaximumSize(QSize(300, 450))
        self.verticalLayout_15 = QVBoxLayout(self.loginWindow)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(20, 20, 20, 20)
        self.pics = QLabel(self.loginWindow)
        self.pics.setObjectName(u"pics")
        self.pics.setMinimumSize(QSize(100, 100))
        self.pics.setMaximumSize(QSize(100, 100))
        self.pics.setPixmap(QPixmap(u":/pics/res/shield.svg"))
        self.pics.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.pics, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.mainBody = QWidget(self.loginWindow)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy8.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy8)
        self.mainBody.setMinimumSize(QSize(0, 0))
        self.verticalLayout_13 = QVBoxLayout(self.mainBody)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.login = QLineEdit(self.mainBody)
        self.login.setObjectName(u"login")
        self.login.setFont(font6)
        self.login.setMaxLength(30)

        self.verticalLayout_13.addWidget(self.login, 0, Qt.AlignTop)

        self.pss = QLineEdit(self.mainBody)
        self.pss.setObjectName(u"pss")
        self.pss.setFont(font6)

        self.verticalLayout_13.addWidget(self.pss, 0, Qt.AlignTop)

        self.loginBtn = QPushButton(self.mainBody)
        self.loginBtn.setObjectName(u"loginBtn")
        sizePolicy5.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy5)
        self.loginBtn.setFont(font5)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.loginBtn, 0, Qt.AlignHCenter)

        self.resetPassBtn = QPushButton(self.mainBody)
        self.resetPassBtn.setObjectName(u"resetPassBtn")
        sizePolicy5.setHeightForWidth(self.resetPassBtn.sizePolicy().hasHeightForWidth())
        self.resetPassBtn.setSizePolicy(sizePolicy5)
        self.resetPassBtn.setFont(font5)
        self.resetPassBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.resetPassBtn, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_15.addWidget(self.mainBody)

        self.registration = QWidget(self.loginWindow)
        self.registration.setObjectName(u"registration")
        sizePolicy2.setHeightForWidth(self.registration.sizePolicy().hasHeightForWidth())
        self.registration.setSizePolicy(sizePolicy2)
        self.verticalLayout_14 = QVBoxLayout(self.registration)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.firstlyQ = QLabel(self.registration)
        self.firstlyQ.setObjectName(u"firstlyQ")
        self.firstlyQ.setFont(font6)

        self.verticalLayout_14.addWidget(self.firstlyQ)

        self.signupBtn = QPushButton(self.registration)
        self.signupBtn.setObjectName(u"signupBtn")
        sizePolicy5.setHeightForWidth(self.signupBtn.sizePolicy().hasHeightForWidth())
        self.signupBtn.setSizePolicy(sizePolicy5)
        self.signupBtn.setFont(font5)
        self.signupBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.signupBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.registration)


        self.verticalLayout_12.addWidget(self.loginWindow, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.loginMenu)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        self.modelEdit.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CryptoKeyPro", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"CryptoKey", None))
        self.slogan.setText(QCoreApplication.translate("MainWindow", u"Password Manager", None))
        self.mainBtn.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.managerBtn.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.tgbotBtn.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0433\u0440\u0430\u043c \u0431\u043e\u0442", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"v1.012.123.123", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None));
        self.newKeyBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.titleEdit.setText("")
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.closeEditor.setText("")
        self.stringEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.modelEdit.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.modelEdit.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0442\u043e\u0439", None))
        self.modelEdit.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u044c\u043d\u044b\u0439", None))

#if QT_CONFIG(tooltip)
        self.modelEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.modelEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.modelEdit.setCurrentText("")
        self.modelEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u043c\u043e\u0434\u0435\u043b\u044c \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.userIcon.setText("")
        self.username.setText(QCoreApplication.translate("MainWindow", u"\u0442\u0432\u043e\u044f@\u043f\u043e\u0447\u0442\u0430.\u0440\u0443", None))
        self.pssChangeBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.uploadBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u0438", None))
        self.customBtn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043a\u0430\u0441\u0442\u043e\u043c\u043d\u044b\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.supportBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435 \u0432 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0443", None))
        self.delAccButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.quitBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u042b\u0419\u0422\u0418", None))
        self.image.setText("")
        self.postTitle.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0434\u0435\u0436\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u0442\u0430\u0439\u043d\u0430, \u0437\u0430\u0449\u0438\u0449\u0430\u044e\u0449\u0430\u044f \u0441\u043e\u043a\u0440\u043e\u0432\u0438\u0449\u0430 \u0442\u0432\u043e\u0435\u0433\u043e \u0446\u0438\u0444\u0440\u043e\u0432\u043e\u0433\u043e \u043c\u0438\u0440\u0430", None))
        self.checkBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043d\u0430\u0434\u0435\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.readBtn3.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043d\u0430\u0434\u0435\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.newsTitle.setPlainText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c \u043f\u043e \u043d\u0430\u0443\u043a\u0435: \u0442\u0440\u0443\u0434\u043d\u043e \u0432\u0437\u043b\u043e\u043c\u0430\u0442\u044c, \u043d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0437\u0430\u0431\u044b\u0442\u044c", None))
        self.from1.setText(QCoreApplication.translate("MainWindow", u"DataLine", None))
        self.readBtn.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u0442\u044c", None))
        self.newsTitle2.setPlainText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u043f\u0442\u043e\u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u044b. \u041a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0441 \u0442\u043e\u0447\u043a\u0438 \u0437\u0440\u0435\u043d\u0438\u044f \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u043a\u043b\u044e\u0447\u0435\u0439", None))
        self.from2.setText(QCoreApplication.translate("MainWindow", u"den_golub", None))
        self.readBtn2.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u0442\u044c", None))
        self.label_4.setPlainText(QCoreApplication.translate("MainWindow", u"\u0425\u043e\u0442\u0438\u0442\u0435 \u043d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u043d\u0430 Python \u0441\u0432\u043e\u0439 \u043a\u0430\u0441\u0442\u043e\u043c\u043d\u044b\u0439 \u0433\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439?", None))
        self.custBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.moreBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435", None))
        self.pics_2.setText("")
        self.email.setText("")
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.emailCheck.setText("")
        self.codeInput.setText("")
        self.codeInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u0414", None))
        self.sendCodeBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u041a\u041e\u0414", None))
        self.createPss.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.confPss.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.regBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.toExitBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043a\u043e \u0432\u0445\u043e\u0434\u0443", None))
        self.pics.setText("")
        self.login.setText("")
        self.login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.pss.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.resetPassBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.firstlyQ.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0435\u0440\u0432\u044b\u0439 \u0440\u0430\u0437?", None))
        self.signupBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

