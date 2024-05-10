# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'key_editor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(200, 231)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setMinimumSize(QSize(200, 0))
        dialog.setMaximumSize(QSize(200, 231))
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
"QPushButton:hover {\n"
"background-color:  #6C757D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:  #343A40;\n"
"}\n"
"\n"
"#header, #mainBody {\n"
"background-color: #495057;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background: transparent;\n"
"color: #E9ECEF;\n"
"}\n"
"\n"
"QComboBox {\n"
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
        self.header.setMinimumSize(QSize(100, 0))
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.titleEdit = QLineEdit(self.header)
        self.titleEdit.setObjectName(u"titleEdit")
        font = QFont()
        font.setFamilies([u"Segoe UI Semilight"])
        font.setPointSize(12)
        self.titleEdit.setFont(font)
        self.titleEdit.setMaxLength(20)
        self.titleEdit.setAlignment(Qt.AlignCenter)
        self.titleEdit.setDragEnabled(False)
        self.titleEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.titleEdit)


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
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stringEdit = QLineEdit(self.mainBody)
        self.stringEdit.setObjectName(u"stringEdit")
        font1 = QFont()
        font1.setPointSize(10)
        self.stringEdit.setFont(font1)
        self.stringEdit.setMaxLength(30)

        self.verticalLayout_2.addWidget(self.stringEdit)

        self.modelEdit = QComboBox(self.mainBody)
        self.modelEdit.addItem("")
        self.modelEdit.addItem("")
        self.modelEdit.addItem("")
        self.modelEdit.setObjectName(u"modelEdit")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semilight"])
        font2.setPointSize(10)
        self.modelEdit.setFont(font2)
        self.modelEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelEdit.setEditable(False)
        self.modelEdit.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_2.addWidget(self.modelEdit)

        self.password = QLineEdit(self.mainBody)
        self.password.setObjectName(u"password")
        font3 = QFont()
        font3.setPointSize(12)
        self.password.setFont(font3)
        self.password.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.password)

        self.generateBtn = QPushButton(self.mainBody)
        self.generateBtn.setObjectName(u"generateBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.generateBtn.sizePolicy().hasHeightForWidth())
        self.generateBtn.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Semibold"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.generateBtn.setFont(font4)
        self.generateBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.generateBtn)

        self.saveBtn = QPushButton(self.mainBody)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy3.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy3)
        self.saveBtn.setFont(font4)
        self.saveBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.saveBtn)


        self.verticalLayout.addWidget(self.mainBody)


        self.retranslateUi(dialog)

        self.modelEdit.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"KeyEditor", None))
        self.titleEdit.setText("")
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("dialog", u"Title", None))
        self.stringEdit.setPlaceholderText(QCoreApplication.translate("dialog", u"Your string", None))
        self.modelEdit.setItemText(0, QCoreApplication.translate("dialog", u"Simple", None))
        self.modelEdit.setItemText(1, QCoreApplication.translate("dialog", u"Text", None))
        self.modelEdit.setItemText(2, QCoreApplication.translate("dialog", u"Strong", None))

#if QT_CONFIG(tooltip)
        self.modelEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.modelEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.modelEdit.setCurrentText("")
        self.modelEdit.setPlaceholderText(QCoreApplication.translate("dialog", u"Choose generative model", None))
        self.password.setText(QCoreApplication.translate("dialog", u"Password", None))
        self.generateBtn.setText(QCoreApplication.translate("dialog", u"Generate", None))
        self.saveBtn.setText(QCoreApplication.translate("dialog", u"Save", None))
    # retranslateUi

