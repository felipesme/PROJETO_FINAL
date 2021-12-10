# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastroAluno.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QWidget)
import file_login_rc
import file_menu_rc

class Ui_menu(object):
    def setupUi(self, menu):
        if not menu.objectName():
            menu.setObjectName(u"menu")
        menu.resize(800, 600)
        menu.setMinimumSize(QSize(800, 600))
        menu.setMaximumSize(QSize(800, 600))
        font = QFont()
        font.setBold(True)
        menu.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../.designer/REPERT\u00d3RIO/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        menu.setWindowIcon(icon)
        menu.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        self.centralwidget = QWidget(menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setMouseTracking(False)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setEnabled(True)
        self.content.setMinimumSize(QSize(210, 23))
        self.content.setMaximumSize(QSize(65, 16777215))
        self.content.setBaseSize(QSize(3, 0))
        self.content.setStyleSheet(u"background-color: rgb(0, 0, 112);")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.content)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 30, 140, 70))
        self.frame.setMinimumSize(QSize(140, 70))
        self.frame.setMaximumSize(QSize(140, 70))
        self.frame.setSizeIncrement(QSize(140, 70))
        self.frame.setStyleSheet(u"QFrame {\n"
"	;\n"
"	background-image: url(:/menu_img/logo_menu.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.content)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 130, 171, 411))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_home = QPushButton(self.frame_2)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setGeometry(QRect(0, 0, 161, 24))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        self.pushButton_home.setFont(font1)
        self.pushButton_home.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(237, 224, 7);\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas = QPushButton(self.frame_2)
        self.pushButton_listas.setObjectName(u"pushButton_listas")
        self.pushButton_listas.setGeometry(QRect(0, 50, 161, 24))
        self.pushButton_listas.setFont(font1)
        self.pushButton_listas.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_listas.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas_alunos = QPushButton(self.frame_2)
        self.pushButton_listas_alunos.setObjectName(u"pushButton_listas_alunos")
        self.pushButton_listas_alunos.setGeometry(QRect(20, 80, 141, 24))
        self.pushButton_listas_alunos.setFont(font1)
        self.pushButton_listas_alunos.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas_professores = QPushButton(self.frame_2)
        self.pushButton_listas_professores.setObjectName(u"pushButton_listas_professores")
        self.pushButton_listas_professores.setGeometry(QRect(20, 110, 141, 24))
        self.pushButton_listas_professores.setFont(font1)
        self.pushButton_listas_professores.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas_cursos = QPushButton(self.frame_2)
        self.pushButton_listas_cursos.setObjectName(u"pushButton_listas_cursos")
        self.pushButton_listas_cursos.setGeometry(QRect(20, 140, 141, 24))
        self.pushButton_listas_cursos.setFont(font1)
        self.pushButton_listas_cursos.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas_usuarios = QPushButton(self.frame_2)
        self.pushButton_listas_usuarios.setObjectName(u"pushButton_listas_usuarios")
        self.pushButton_listas_usuarios.setGeometry(QRect(20, 170, 141, 24))
        self.pushButton_listas_usuarios.setFont(font1)
        self.pushButton_listas_usuarios.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_cadastro = QPushButton(self.frame_2)
        self.pushButton_cadastro.setObjectName(u"pushButton_cadastro")
        self.pushButton_cadastro.setGeometry(QRect(0, 210, 161, 24))
        self.pushButton_cadastro.setFont(font1)
        self.pushButton_cadastro.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_cadastro_alunos = QPushButton(self.frame_2)
        self.pushButton_cadastro_alunos.setObjectName(u"pushButton_cadastro_alunos")
        self.pushButton_cadastro_alunos.setGeometry(QRect(20, 240, 141, 24))
        self.pushButton_cadastro_alunos.setFont(font1)
        self.pushButton_cadastro_alunos.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_cadastro_professores = QPushButton(self.frame_2)
        self.pushButton_cadastro_professores.setObjectName(u"pushButton_cadastro_professores")
        self.pushButton_cadastro_professores.setGeometry(QRect(20, 270, 141, 24))
        self.pushButton_cadastro_professores.setFont(font1)
        self.pushButton_cadastro_professores.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_cadastro_cursos = QPushButton(self.frame_2)
        self.pushButton_cadastro_cursos.setObjectName(u"pushButton_cadastro_cursos")
        self.pushButton_cadastro_cursos.setGeometry(QRect(20, 300, 141, 24))
        self.pushButton_cadastro_cursos.setFont(font1)
        self.pushButton_cadastro_cursos.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_cadastro_usuarios = QPushButton(self.frame_2)
        self.pushButton_cadastro_usuarios.setObjectName(u"pushButton_cadastro_usuarios")
        self.pushButton_cadastro_usuarios.setGeometry(QRect(20, 330, 141, 24))
        self.pushButton_cadastro_usuarios.setFont(font1)
        self.pushButton_cadastro_usuarios.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_cadastro_2 = QPushButton(self.frame_2)
        self.pushButton_cadastro_2.setObjectName(u"pushButton_cadastro_2")
        self.pushButton_cadastro_2.setGeometry(QRect(0, 370, 161, 24))
        self.pushButton_cadastro_2.setFont(font1)
        self.pushButton_cadastro_2.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.btn_deslogar = QFrame(self.content)
        self.btn_deslogar.setObjectName(u"btn_deslogar")
        self.btn_deslogar.setGeometry(QRect(10, 550, 31, 41))
        self.btn_deslogar.setStyleSheet(u"QFrame {	\n"
"	background-image: url(:/menu_img/menu_deslogar.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}")
        self.btn_deslogar.setFrameShape(QFrame.StyledPanel)
        self.btn_deslogar.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.content)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 560, 71, 24))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: normal;\n"
"	background-color: rgb(0, 0, 112);\n"
"	color: rgb(237, 224, 7);\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout.addWidget(self.content)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 341, 81))
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 30px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.stackedWidget.addWidget(self.pg_home)
        self.pg_listas_alunos = QWidget()
        self.pg_listas_alunos.setObjectName(u"pg_listas_alunos")
        self.label_2 = QLabel(self.pg_listas_alunos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 40, 241, 41))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 20px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.tableWidget = QTableWidget(self.pg_listas_alunos)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 110, 581, 471))
        self.stackedWidget.addWidget(self.pg_listas_alunos)
        self.pg_listas_professores = QWidget()
        self.pg_listas_professores.setObjectName(u"pg_listas_professores")
        self.tableWidget_2 = QTableWidget(self.pg_listas_professores)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(30, 100, 561, 451))
        self.label_3 = QLabel(self.pg_listas_professores)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 30, 291, 41))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 20px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.stackedWidget.addWidget(self.pg_listas_professores)
        self.pg_listas_impressao = QWidget()
        self.pg_listas_impressao.setObjectName(u"pg_listas_impressao")
        self.label_4 = QLabel(self.pg_listas_impressao)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 20, 291, 41))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 20px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.stackedWidget.addWidget(self.pg_listas_impressao)
        self.pg_listas_nteressados = QWidget()
        self.pg_listas_nteressados.setObjectName(u"pg_listas_nteressados")
        self.stackedWidget.addWidget(self.pg_listas_nteressados)
        self.pg_listas_funcionarios = QWidget()
        self.pg_listas_funcionarios.setObjectName(u"pg_listas_funcionarios")
        self.stackedWidget.addWidget(self.pg_listas_funcionarios)
        self.pg_cadastro_alunos = QWidget()
        self.pg_cadastro_alunos.setObjectName(u"pg_cadastro_alunos")
        self.label_5 = QLabel(self.pg_cadastro_alunos)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 291, 41))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font: 35px Montserrat, sans-serif;\n"
"	font-weight: normal;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"")
        self.lineEdit_5 = QLineEdit(self.pg_cadastro_alunos)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 180, 241, 31))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.lineEdit_6 = QLineEdit(self.pg_cadastro_alunos)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(30, 120, 501, 31))
        self.lineEdit_6.setStyleSheet(u"QLineEdit {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.lineEdit_3 = QLineEdit(self.pg_cadastro_alunos)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 240, 501, 31))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.label_8 = QLabel(self.pg_cadastro_alunos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 100, 141, 19))
        self.label_8.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.comboBox = QComboBox(self.pg_cadastro_alunos)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 310, 241, 31))
        self.comboBox.setStyleSheet(u"QComboBox {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 2px solid grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"     background: white;\n"
" }")
        self.label_9 = QLabel(self.pg_cadastro_alunos)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 290, 61, 19))
        self.label_9.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.label_10 = QLabel(self.pg_cadastro_alunos)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(300, 160, 81, 19))
        self.label_10.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.label_11 = QLabel(self.pg_cadastro_alunos)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 220, 51, 19))
        self.label_11.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.label_12 = QLabel(self.pg_cadastro_alunos)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 160, 47, 19))
        self.label_12.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.lineEdit_7 = QLineEdit(self.pg_cadastro_alunos)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(310, 310, 221, 31))
        self.lineEdit_7.setStyleSheet(u"QLineEdit {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.lineEdit_8 = QLineEdit(self.pg_cadastro_alunos)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(290, 180, 241, 31))
        self.lineEdit_8.setStyleSheet(u"QLineEdit {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.label_13 = QLabel(self.pg_cadastro_alunos)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(320, 290, 91, 19))
        self.label_13.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(self.pg_cadastro_alunos)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(294, 420, 111, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color:  rgb(255, 82, 85);\n"
"	font: 9pt \"Segoe UI\";\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"    color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(187, 237, 6);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_3 = QPushButton(self.pg_cadastro_alunos)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(430, 420, 111, 41))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color:  rgb(131, 255, 156);\n"
"\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"	font: 8pt \"Segoe UI Historic\";\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(187, 237, 6);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.stackedWidget.addWidget(self.pg_cadastro_alunos)

        self.horizontalLayout.addWidget(self.stackedWidget)

        menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(menu)
    # setupUi

    def retranslateUi(self, menu):
        menu.setWindowTitle(QCoreApplication.translate("menu", u"speak now - menu", None))
        self.pushButton_home.setText(QCoreApplication.translate("menu", u"Home", None))
        self.pushButton_listas.setText(QCoreApplication.translate("menu", u"Listas", None))
        self.pushButton_listas_alunos.setText(QCoreApplication.translate("menu", u"Alunos", None))
        self.pushButton_listas_professores.setText(QCoreApplication.translate("menu", u"Professores", None))
        self.pushButton_listas_cursos.setText(QCoreApplication.translate("menu", u"Impress\u00e3o", None))
        self.pushButton_listas_usuarios.setText(QCoreApplication.translate("menu", u"Usu\u00e1rios", None))
        self.pushButton_cadastro.setText(QCoreApplication.translate("menu", u"Cadastro", None))
        self.pushButton_cadastro_alunos.setText(QCoreApplication.translate("menu", u"Alunos", None))
        self.pushButton_cadastro_professores.setText(QCoreApplication.translate("menu", u"Professores", None))
        self.pushButton_cadastro_cursos.setText(QCoreApplication.translate("menu", u"Cursos", None))
        self.pushButton_cadastro_usuarios.setText(QCoreApplication.translate("menu", u"Usu\u00e1rios", None))
        self.pushButton_cadastro_2.setText(QCoreApplication.translate("menu", u"Relat\u00f3rios", None))
        self.pushButton.setText(QCoreApplication.translate("menu", u"Deslogar", None))
        self.label.setText(QCoreApplication.translate("menu", u"Bem-vindo(a)!", None))
        self.label_2.setText(QCoreApplication.translate("menu", u"Informa\u00e7\u00f5es alunos", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("menu", u"NOME", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("menu", u"CPF", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("menu", u"TELEFONE", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("menu", u"CURSO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("menu", u"SEMESTRE", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("menu", u"A\u00c7\u00c3O", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("menu", u"NOME", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("menu", u"CPF", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("menu", u"TELEFONE", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("menu", u"CURSO", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("menu", u"QUANT.", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("menu", u"A\u00c7\u00c3O", None));
        self.label_3.setText(QCoreApplication.translate("menu", u"Informa\u00e7\u00f5es professores", None))
        self.label_4.setText(QCoreApplication.translate("menu", u"Informa\u00e7\u00f5es impress\u00e3o", None))
        self.label_5.setText(QCoreApplication.translate("menu", u"Cadastro > alunos", None))
        self.label_8.setText(QCoreApplication.translate("menu", u"NOME COMPLETO", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("menu", u"Ingl\u00eas", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("menu", u"Espanhol", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("menu", u"Franc\u00eas", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("menu", u"Alem\u00e3o", None))

        self.label_9.setText(QCoreApplication.translate("menu", u"CURSO", None))
        self.label_10.setText(QCoreApplication.translate("menu", u"TELEFONE", None))
        self.label_11.setText(QCoreApplication.translate("menu", u"EMAIL", None))
        self.label_12.setText(QCoreApplication.translate("menu", u"CPF", None))
        self.label_13.setText(QCoreApplication.translate("menu", u"SEMESTRE", None))
        self.pushButton_2.setText(QCoreApplication.translate("menu", u"CONFIRMAR", None))
        self.pushButton_3.setText(QCoreApplication.translate("menu", u"CANCELAR", None))
    # retranslateUi

