# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'support_window.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(274, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(274, 320))
        Dialog.setMaximumSize(QSize(274, 320))
        Dialog.setStyleSheet(u"* {\n"
"border: none;\n"
"background-color: transparent;\n"
"color: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"	selection-background-color: #088572;\n"
"	background-color: #173B49;\n"
"}\n"
"\n"
"#centralWidget{\n"
"background-color: #088572;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QDialog{\n"
"background-color: #0D0D15;\n"
"}\n"
"\n"
"#mainBody > QLineEdit, #mainBody_2 > QLineEdit, #email{\n"
"background-color: #0D0D15;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#sendBtn{\n"
"text-align: center;\n"
"width: 180px;\n"
"padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"#sendBtn:hover{\n"
"background-color: #173B49;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#sendBtn:pressed{\n"
"border: 3px solid #0D0D15;\n"
"font-weight: bold;\n"
"background-color:#0D0D15;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.centralWidget = QWidget(Dialog)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy1)
        self.centralWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_20 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.themeEdit = QComboBox(self.centralWidget)
        self.themeEdit.addItem("")
        self.themeEdit.addItem("")
        self.themeEdit.addItem("")
        self.themeEdit.addItem("")
        self.themeEdit.setObjectName(u"themeEdit")
        font = QFont()
        font.setFamilies([u"Segoe UI Semilight"])
        font.setPointSize(10)
        self.themeEdit.setFont(font)
        self.themeEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.themeEdit.setEditable(False)
        self.themeEdit.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_20.addWidget(self.themeEdit)

        self.textEdit = QPlainTextEdit(self.centralWidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(0, 0))

        self.verticalLayout_20.addWidget(self.textEdit)

        self.sendBtn = QPushButton(self.centralWidget)
        self.sendBtn.setObjectName(u"sendBtn")
        sizePolicy2.setHeightForWidth(self.sendBtn.sizePolicy().hasHeightForWidth())
        self.sendBtn.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.sendBtn.setFont(font1)
        self.sendBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.sendBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.centralWidget)


        self.retranslateUi(Dialog)

        self.themeEdit.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Support", None))
        self.themeEdit.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044e", None))
        self.themeEdit.setItemText(1, QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 \u0432 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0443", None))
        self.themeEdit.setItemText(2, QCoreApplication.translate("Dialog", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0432 \u0440\u0430\u0431\u043e\u0442\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.themeEdit.setItemText(3, QCoreApplication.translate("Dialog", u"-\u0431\u0435\u0437 \u0442\u0435\u043c\u044b-", None))

#if QT_CONFIG(tooltip)
        self.themeEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.themeEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.themeEdit.setCurrentText("")
        self.themeEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u0430 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f", None))
        self.textEdit.setPlainText("")
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435", None))
        self.sendBtn.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

