# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reliability.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import libs.ui.icons

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(403, 530)
        Dialog.setMinimumSize(QSize(350, 530))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        Dialog.setStyleSheet(u"* {\n"
"border: none;\n"
"background-color: transparent;\n"
"color: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"\n"
"QDialog{\n"
"background-color: #0D0D15;\n"
"}\n"
"\n"
"QLabel{\n"
"color: white;\n"
"}\n"
"\n"
"#window{\n"
"background-color: #088572;\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: #0D0D15;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"text-align: center;\n"
"width: 180px;\n"
"padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #173B49;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 3px solid #0D0D15;\n"
"font-weight: bold;\n"
"background-color:#0D0D15;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.window = QWidget(Dialog)
        self.window.setObjectName(u"window")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window.sizePolicy().hasHeightForWidth())
        self.window.setSizePolicy(sizePolicy)
        self.window.setMinimumSize(QSize(300, 259))
        self.window.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.window)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(20, 20, 20, 20)
        self.pics = QLabel(self.window)
        self.pics.setObjectName(u"pics")
        self.pics.setMinimumSize(QSize(50, 50))
        self.pics.setMaximumSize(QSize(50, 50))
        self.pics.setPixmap(QPixmap(u":/pics/res/key.svg"))
        self.pics.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.pics, 0, Qt.AlignHCenter)

        self.plainTextEdit = QPlainTextEdit(self.window)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_15.addWidget(self.plainTextEdit)

        self.mainBody = QWidget(self.window)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.mainBody.setMinimumSize(QSize(0, 0))
        self.verticalLayout_13 = QVBoxLayout(self.mainBody)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.mainBody)

        self.registration = QWidget(self.window)
        self.registration.setObjectName(u"registration")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.registration.sizePolicy().hasHeightForWidth())
        self.registration.setSizePolicy(sizePolicy2)
        self.verticalLayout_14 = QVBoxLayout(self.registration)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.mngBtn = QPushButton(self.registration)
        self.mngBtn.setObjectName(u"mngBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mngBtn.sizePolicy().hasHeightForWidth())
        self.mngBtn.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(12)
        font.setBold(True)
        self.mngBtn.setFont(font)
        self.mngBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.mngBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.registration)


        self.verticalLayout.addWidget(self.window, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Reliability", None))
        self.pics.setText("")
        self.mngBtn.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
    # retranslateUi

