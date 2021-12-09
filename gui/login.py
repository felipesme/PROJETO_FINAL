# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import file_login_rc

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(1024, 600)
        login.setMinimumSize(QSize(1024, 600))
        login.setMaximumSize(QSize(1024, 600))
        icon = QIcon()
        icon.addFile(u"../REPERT\u00d3RIO/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        login.setWindowIcon(icon)
        login.setStyleSheet(u"background-color: rgb(0, 0, 112);")
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 35))
        self.top_bar.setStyleSheet(u"")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.frame_error = QFrame(self.top_bar)
        self.frame_error.setObjectName(u"frame_error")
        self.frame_error.setMinimumSize(QSize(300, 0))
        self.frame_error.setMaximumSize(QSize(300, 16777215))
        self.frame_error.setStyleSheet(u"background-color: #ede007;\n"
"border-radius: 15px;\n"
"\n"
"")
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 5)
        self.error = QLabel(self.frame_error)
        self.error.setObjectName(u"error")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.error.setFont(font)
        self.error.setStyleSheet(u"color: rgb(0, 0, 112);")
        self.error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.error)

        self.buttom_error = QPushButton(self.frame_error)
        self.buttom_error.setObjectName(u"buttom_error")
        self.buttom_error.setMaximumSize(QSize(20, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.buttom_error.setFont(font1)
        self.buttom_error.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 0, 112);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 83, 213);\n"
"}")

        self.horizontalLayout_3.addWidget(self.buttom_error)


        self.horizontalLayout_2.addWidget(self.frame_error)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(280, 140))
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_area = QFrame(self.content)
        self.login_area.setObjectName(u"login_area")
        self.login_area.setEnabled(True)
        self.login_area.setMaximumSize(QSize(450, 16777215))
        self.login_area.setStyleSheet(u"background-color: rgb(0, 0, 112);")
        self.login_area.setFrameShape(QFrame.NoFrame)
        self.login_area.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.login_area)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(85, 260, 280, 41))
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_3 = QLineEdit(self.login_area)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(85, 310, 280, 41))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.checkBox = QCheckBox(self.login_area)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(85, 360, 131, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.checkBox.setFont(font2)
        self.checkBox.setFocusPolicy(Qt.WheelFocus)
        self.checkBox.setStyleSheet(u"QCheckBox  {\n"
"	color: rgb(237, 224, 7)\n"
"}\n"
"\n"
"QCheckBox:indicator  {\n"
"	border: 1px solid rgb(237, 224, 7);\n"
"	border-radius: 3px;\n"
"	width: 12px;	\n"
"	height: 12px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked  {\n"
"	border: 1px solid rgb(237, 224, 7);\n"
"	background-color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.pushButton = QPushButton(self.login_area)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(85, 400, 280, 41))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(187, 237, 6);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.frame = QFrame(self.login_area)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(85, 50, 280, 140))
        self.frame.setMinimumSize(QSize(280, 140))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-image: url(:/login_img/logo_login.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.login_area)


        self.verticalLayout.addWidget(self.content)

        self.button = QFrame(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setMaximumSize(QSize(16777215, 20))
        self.button.setStyleSheet(u"")
        self.button.setFrameShape(QFrame.NoFrame)
        self.button.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.button)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(870, -2, 141, 20))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setItalic(False)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(223, 223, 223);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.button)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, -2, 61, 20))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(223, 223, 223);")

        self.verticalLayout.addWidget(self.button)

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"speak now - login", None))
        self.error.setText(QCoreApplication.translate("login", u"Usu\u00e1rio ou senha inv\u00e1lida. ", None))
        self.buttom_error.setText(QCoreApplication.translate("login", u"X", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("login", u"usu\u00e1rio", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("login", u"senha", None))
        self.checkBox.setText(QCoreApplication.translate("login", u"lembrar usu\u00e1rio", None))
        self.pushButton.setText(QCoreApplication.translate("login", u"acessar", None))
        self.label.setText(QCoreApplication.translate("login", u"developed by Felipe S.", None))
        self.label_2.setText(QCoreApplication.translate("login", u"Vers\u00e3o 1.0", None))
    # retranslateUi

