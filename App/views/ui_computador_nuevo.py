# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'computador_nuevoQhaGos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_Computador(object):
    def setupUi(self, Computador):
        if not Computador.objectName():
            Computador.setObjectName(u"Computador")
        Computador.resize(476, 500)
        Computador.setMinimumSize(QSize(476, 500))
        Computador.setMaximumSize(QSize(476, 500))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Computador.setWindowIcon(icon)
        Computador.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Computador)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Computador)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{background-color:white;border-radius:10px}\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #54BFC9;\n"
"border-radius: 8px;}\n"
"\n"
"QPushButton:hover{background: #439CA8;\n"
"border-radius: 8px; }\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 65, 461, 351))
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 450;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;}\n"
"\n"
"\n"
"QLineEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: #F3F4F6;\n"
"border: 2px solid #F3F4F6;\n"
"border-radius: 8px;\n"
"color:#9CA3AF;\n"
"padding:10px}\n"
"\n"
"QLineEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"/* COMBOBOX */\n"
"\n"
"QComboBox{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: #F3F4F6;\n"
"color:#9CA3AF;\n"
"border-radius:8px;\n"
"padding:10px;\n"
"combobox-popup: 0;\n"
"border: 2px solid #F3F4F6;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
""
                        "	padding: 10px 10px 10px 20px;\n"
" }\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color:#9CA3AF;\n"
"	font-size:14px;\n"
"	background-color: #F3F4F6;\n"
"	selection-background-color:#344647;\n"
"	selection-color:#ffffff;\n"
"	outline: 0px;\n"
"   border: 1px solid #344647;\n"
" border-radius:8px;\n"
"padding:10px\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/prefijoNuevo/flecha_oscuro.png);\n"
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* PLANTEXT*/\n"
"QPlainTextEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: #F3F4F6;\n"
"border: 2px solid #F3F4F6;\n"
"border-radius: 8px;\n"
"color:#9CA3AF;\n"
"padding:10px}\n"
"\n"
"QPlainTextEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QC"
                        "heckBox{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"color:#9CA3AF}\n"
"\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lbl5 = QLabel(self.frame_2)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(10, 180, 151, 21))
        self.lbl5.setStyleSheet(u"")
        self.lbl5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_serial = QLineEdit(self.frame_2)
        self.line_serial.setObjectName(u"line_serial")
        self.line_serial.setEnabled(True)
        self.line_serial.setGeometry(QRect(10, 36, 205, 40))
        self.line_serial.setStyleSheet(u"")
        self.line_serial.setMaxLength(30)
        self.line_serial.setFrame(True)
        self.line_serial.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.frame_2)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(10, 10, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl9 = QLabel(self.frame_2)
        self.lbl9.setObjectName(u"lbl9")
        self.lbl9.setGeometry(QRect(10, 97, 81, 21))
        self.lbl9.setStyleSheet(u"")
        self.lbl9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbox_compania = QComboBox(self.frame_2)
        self.cbox_compania.addItem("")
        self.cbox_compania.addItem("")
        self.cbox_compania.addItem("")
        self.cbox_compania.setObjectName(u"cbox_compania")
        self.cbox_compania.setGeometry(QRect(10, 204, 205, 40))
        self.cbox_compania.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_compania.setStyleSheet(u"")
        self.cbox_modelo = QComboBox(self.frame_2)
        self.cbox_modelo.addItem("")
        self.cbox_modelo.addItem("")
        self.cbox_modelo.addItem("")
        self.cbox_modelo.setObjectName(u"cbox_modelo")
        self.cbox_modelo.setGeometry(QRect(10, 120, 205, 40))
        self.cbox_modelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_modelo.setStyleSheet(u"")
        self.label_95 = QLabel(self.frame_2)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(10, 260, 161, 31))
        self.fecha_registro = QDateEdit(self.frame_2)
        self.fecha_registro.setObjectName(u"fecha_registro")
        self.fecha_registro.setGeometry(QRect(240, 204, 151, 40))
        self.fecha_registro.setCursor(QCursor(Qt.PointingHandCursor))
        self.fecha_registro.setStyleSheet(u"/*SPINBOX*/\n"
"QDateEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: #F3F4F6;\n"
"color:#9CA3AF;\n"
"padding:8px;\n"
"border-radius:8px; }\n"
"\n"
"QDateEdit::up-button {\n"
"min-width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QDateEdit::down-button {\n"
"min-width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QDateEdit::up-arrow{\n"
"	image: url(:/prefijoNuevo/comDownP.png);\n"
"     width: 9px;\n"
"     height: 9px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow{\n"
"	image:url(:/prefijoNuevo/comUpP.png);\n"
"     width: 9px;\n"
"     height: 9px;}\n"
"\n"
"QDateEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #526974;\n"
"border-radius: 8px;\n"
"}")
        self.fecha_registro.setCalendarPopup(False)
        self.lbl8 = QLabel(self.frame_2)
        self.lbl8.setObjectName(u"lbl8")
        self.lbl8.setGeometry(QRect(240, 180, 181, 21))
        self.lbl8.setStyleSheet(u"")
        self.lbl8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.check_fecha = QCheckBox(self.frame_2)
        self.check_fecha.setObjectName(u"check_fecha")
        self.check_fecha.setEnabled(True)
        self.check_fecha.setGeometry(QRect(400, 210, 61, 17))
        self.lbl9_2 = QLabel(self.frame_2)
        self.lbl9_2.setObjectName(u"lbl9_2")
        self.lbl9_2.setGeometry(QRect(240, 10, 81, 21))
        self.lbl9_2.setStyleSheet(u"")
        self.lbl9_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_placa = QLineEdit(self.frame_2)
        self.line_placa.setObjectName(u"line_placa")
        self.line_placa.setEnabled(True)
        self.line_placa.setGeometry(QRect(240, 36, 205, 40))
        self.line_placa.setStyleSheet(u"")
        self.line_placa.setMaxLength(30)
        self.line_placa.setFrame(True)
        self.line_placa.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl9_3 = QLabel(self.frame_2)
        self.lbl9_3.setObjectName(u"lbl9_3")
        self.lbl9_3.setGeometry(QRect(240, 97, 81, 21))
        self.lbl9_3.setStyleSheet(u"")
        self.lbl9_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_marca = QLineEdit(self.frame_2)
        self.line_marca.setObjectName(u"line_marca")
        self.line_marca.setEnabled(True)
        self.line_marca.setGeometry(QRect(240, 120, 205, 40))
        self.line_marca.setStyleSheet(u"")
        self.line_marca.setMaxLength(30)
        self.line_marca.setFrame(True)
        self.line_marca.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_ticket = QLineEdit(self.frame_2)
        self.line_ticket.setObjectName(u"line_ticket")
        self.line_ticket.setEnabled(True)
        self.line_ticket.setGeometry(QRect(10, 290, 205, 40))
        self.line_ticket.setStyleSheet(u"")
        self.line_ticket.setMaxLength(30)
        self.line_ticket.setFrame(True)
        self.line_ticket.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_serial = QLabel(self.frame_2)
        self.lbl_serial.setObjectName(u"lbl_serial")
        self.lbl_serial.setGeometry(QRect(12, 76, 191, 16))
        self.lbl_serial.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.lbl_placa = QLabel(self.frame_2)
        self.lbl_placa.setObjectName(u"lbl_placa")
        self.lbl_placa.setGeometry(QRect(241, 77, 191, 16))
        self.lbl_placa.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.lbl_ticket = QLabel(self.frame_2)
        self.lbl_ticket.setObjectName(u"lbl_ticket")
        self.lbl_ticket.setGeometry(QRect(10, 330, 191, 16))
        self.lbl_ticket.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.lbl_marca = QLabel(self.frame_2)
        self.lbl_marca.setObjectName(u"lbl_marca")
        self.lbl_marca.setGeometry(QRect(240, 160, 191, 16))
        self.lbl_marca.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.line_id = QLineEdit(self.frame_2)
        self.line_id.setObjectName(u"line_id")
        self.line_id.setEnabled(True)
        self.line_id.setGeometry(QRect(240, 290, 205, 40))
        self.line_id.setStyleSheet(u"")
        self.line_id.setMaxLength(30)
        self.line_id.setFrame(True)
        self.line_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_guardar = QPushButton(self.frame)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(130, 430, 195, 47))
        self.btn_guardar.setMinimumSize(QSize(195, 47))
        self.btn_guardar.setMaximumSize(QSize(110, 47))
        self.btn_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_guardar.setFocusPolicy(Qt.NoFocus)
        self.btn_guardar.setStyleSheet(u"/*  BOTON */\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #3A4F50;\n"
"border-radius: 8px;}\n"
"\n"
"QPushButton:hover{background: #344647;\n"
"border-radius: 8px; }\n"
"")
        self.btn_guardar.setIconSize(QSize(15, 21))
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 477, 50))
        self.frame_3.setStyleSheet(u"#frame_3{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_closeadmi = QToolButton(self.frame_3)
        self.btn_closeadmi.setObjectName(u"btn_closeadmi")
        self.btn_closeadmi.setGeometry(QRect(440, 10, 25, 25))
        self.btn_closeadmi.setFocusPolicy(Qt.NoFocus)
        self.btn_closeadmi.setStyleSheet(u"#btn_closeadmi{\n"
"font-family: Roboto;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"background-color: #d5d5d8;\n"
"color: #6B7280;\n"
"border-radius:11px\n"
"}\n"
"\n"
"\n"
"\n"
"#btn_closeadmi:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/close (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeadmi.setIcon(icon1)
        self.btn_closeadmi.setIconSize(QSize(13, 13))
        self.btn_closeadmi.setAutoRaise(True)
        self.title_computador = QLabel(self.frame_3)
        self.title_computador.setObjectName(u"title_computador")
        self.title_computador.setGeometry(QRect(20, 10, 301, 27))
        self.title_computador.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 22px;\n"
"line-height: 40px;\n"
"letter-spacing: 0.02em;\n"
"color:#ffffff;")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.line_serial, self.line_placa)
        QWidget.setTabOrder(self.line_placa, self.cbox_modelo)
        QWidget.setTabOrder(self.cbox_modelo, self.line_marca)
        QWidget.setTabOrder(self.line_marca, self.cbox_compania)
        QWidget.setTabOrder(self.cbox_compania, self.fecha_registro)
        QWidget.setTabOrder(self.fecha_registro, self.check_fecha)
        QWidget.setTabOrder(self.check_fecha, self.line_ticket)

        self.retranslateUi(Computador)

        QMetaObject.connectSlotsByName(Computador)
    # setupUi

    def retranslateUi(self, Computador):
        Computador.setWindowTitle(QCoreApplication.translate("Computador", u"Dialog", None))
        self.lbl5.setText(QCoreApplication.translate("Computador", u"Compa\u00f1ia*", None))
        self.line_serial.setPlaceholderText(QCoreApplication.translate("Computador", u"Ingrese serial", None))
        self.lbl11.setText(QCoreApplication.translate("Computador", u"Serial*", None))
        self.lbl9.setText(QCoreApplication.translate("Computador", u"Modelo*", None))
        self.cbox_compania.setItemText(0, QCoreApplication.translate("Computador", u"Seleccionar", None))
        self.cbox_compania.setItemText(1, QCoreApplication.translate("Computador", u"Masculino", None))
        self.cbox_compania.setItemText(2, QCoreApplication.translate("Computador", u"Femenino", None))

        self.cbox_modelo.setItemText(0, QCoreApplication.translate("Computador", u"Seleccionar", None))
        self.cbox_modelo.setItemText(1, QCoreApplication.translate("Computador", u"Santillana", None))
        self.cbox_modelo.setItemText(2, QCoreApplication.translate("Computador", u"Mayorca", None))

        self.label_95.setText(QCoreApplication.translate("Computador", u"ticket", None))
        self.fecha_registro.setDisplayFormat(QCoreApplication.translate("Computador", u"d-MM-yyyy", None))
        self.lbl8.setText(QCoreApplication.translate("Computador", u"Fecha de registro*", None))
        self.check_fecha.setText(QCoreApplication.translate("Computador", u"Hoy", None))
        self.lbl9_2.setText(QCoreApplication.translate("Computador", u"Placa*", None))
        self.line_placa.setPlaceholderText(QCoreApplication.translate("Computador", u"ingrese placa", None))
        self.lbl9_3.setText(QCoreApplication.translate("Computador", u"Marca*", None))
        self.line_marca.setPlaceholderText(QCoreApplication.translate("Computador", u"ingrese marca", None))
        self.line_ticket.setPlaceholderText(QCoreApplication.translate("Computador", u"ingrese ticket", None))
        self.lbl_serial.setText("")
        self.lbl_placa.setText("")
        self.lbl_ticket.setText("")
        self.lbl_marca.setText("")
        self.line_id.setPlaceholderText(QCoreApplication.translate("Computador", u"ingrese placa", None))
        self.btn_guardar.setText(QCoreApplication.translate("Computador", u"Guardar", None))
#if QT_CONFIG(tooltip)
        self.btn_closeadmi.setToolTip(QCoreApplication.translate("Computador", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeadmi.setText("")
        self.title_computador.setText(QCoreApplication.translate("Computador", u"Nueva Computadora", None))
    # retranslateUi

