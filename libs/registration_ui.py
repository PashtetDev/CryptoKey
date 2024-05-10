# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(200, 307)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setMinimumSize(QSize(200, 0))
        dialog.setMaximumSize(QSize(200, 307))
        dialog.setStyleSheet(u"* {\n"
"border: none;\n"
"background-color: transparent;\n"
"background: transparent;\n"
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
        self.verticalLayout = QVBoxLayout(dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.header = QWidget(dialog)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.header.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI Semilight"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.mainBody = QWidget(dialog)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy2)
        self.mainBody.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.mainBody)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.mainBody)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 132))
        self.widget.setMaximumSize(QSize(209, 132))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.email = QLineEdit(self.widget_2)
        self.email.setObjectName(u"email")

        self.horizontalLayout_2.addWidget(self.email)

        self.emailCheck = QCheckBox(self.widget_2)
        self.emailCheck.setObjectName(u"emailCheck")
        self.emailCheck.setCheckable(False)
        self.emailCheck.setChecked(False)
        self.emailCheck.setAutoRepeat(False)
        self.emailCheck.setAutoExclusive(False)
        self.emailCheck.setTristate(False)

        self.horizontalLayout_2.addWidget(self.emailCheck, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.codeInput = QLineEdit(self.widget)
        self.codeInput.setObjectName(u"codeInput")

        self.verticalLayout_3.addWidget(self.codeInput)

        self.sendCodeBtn = QPushButton(self.widget)
        self.sendCodeBtn.setObjectName(u"sendCodeBtn")
        sizePolicy.setHeightForWidth(self.sendCodeBtn.sizePolicy().hasHeightForWidth())
        self.sendCodeBtn.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.sendCodeBtn.setFont(font1)
        self.sendCodeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.sendCodeBtn)

        self.checkCodeBtn = QPushButton(self.widget)
        self.checkCodeBtn.setObjectName(u"checkCodeBtn")
        sizePolicy.setHeightForWidth(self.checkCodeBtn.sizePolicy().hasHeightForWidth())
        self.checkCodeBtn.setSizePolicy(sizePolicy)
        self.checkCodeBtn.setFont(font1)
        self.checkCodeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.checkCodeBtn)


        self.verticalLayout_2.addWidget(self.widget)

        self.pss = QLineEdit(self.mainBody)
        self.pss.setObjectName(u"pss")

        self.verticalLayout_2.addWidget(self.pss)

        self.confPss = QLineEdit(self.mainBody)
        self.confPss.setObjectName(u"confPss")

        self.verticalLayout_2.addWidget(self.confPss)

        self.regBtn = QPushButton(self.mainBody)
        self.regBtn.setObjectName(u"regBtn")
        sizePolicy3.setHeightForWidth(self.regBtn.sizePolicy().hasHeightForWidth())
        self.regBtn.setSizePolicy(sizePolicy3)
        self.regBtn.setFont(font1)
        self.regBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.regBtn)


        self.verticalLayout.addWidget(self.mainBody)


        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Setup", None))
        self.label.setText(QCoreApplication.translate("dialog", u"Sign up", None))
        self.email.setText("")
        self.email.setPlaceholderText(QCoreApplication.translate("dialog", u"E-mail", None))
        self.emailCheck.setText("")
        self.codeInput.setText("")
        self.codeInput.setPlaceholderText(QCoreApplication.translate("dialog", u"CODE", None))
        self.sendCodeBtn.setText(QCoreApplication.translate("dialog", u"Send the CODE", None))
        self.checkCodeBtn.setText(QCoreApplication.translate("dialog", u"Check the code", None))
        self.pss.setPlaceholderText(QCoreApplication.translate("dialog", u"Password", None))
        self.confPss.setPlaceholderText(QCoreApplication.translate("dialog", u"Confirm password", None))
        self.regBtn.setText(QCoreApplication.translate("dialog", u"Registration", None))
    # retranslateUi

