# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usuario_admiotDywg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_Admi(object):
    def setupUi(self, Admi):
        if not Admi.objectName():
            Admi.setObjectName(u"Admi")
        Admi.resize(476, 536)
        Admi.setMinimumSize(QSize(476, 536))
        Admi.setMaximumSize(QSize(476, 536))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Admi.setWindowIcon(icon)
        Admi.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Admi)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Admi)
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
        self.frame_2.setGeometry(QRect(10, 60, 461, 401))
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
"/* DATE */\n"
"QDateEdit\n"
"{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: #F3F4F6;\n"
"color:#9CA3AF;\n"
"padding:8px;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QDateEdit::drop-down\n"
"{\n"
"	image: url(:/prefijoNuevo/025-calendar-13.png);\n"
"    width:15px;\n"
"    height:15px;\n"
"padding:13px 20px 10px 10px;\n"
""
                        "}\n"
"\n"
"QDateEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
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
"QCombo"
                        "Box::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QCheckBox{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"color:#9CA3AF}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lbl5 = QLabel(self.frame_2)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(10, 90, 151, 21))
        self.lbl5.setStyleSheet(u"")
        self.lbl5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_dni = QLineEdit(self.frame_2)
        self.line_dni.setObjectName(u"line_dni")
        self.line_dni.setEnabled(True)
        self.line_dni.setGeometry(QRect(10, 36, 205, 40))
        self.line_dni.setStyleSheet(u"")
        self.line_dni.setMaxLength(8)
        self.line_dni.setFrame(True)
        self.line_dni.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.frame_2)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(10, 10, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl9 = QLabel(self.frame_2)
        self.lbl9.setObjectName(u"lbl9")
        self.lbl9.setGeometry(QRect(240, 10, 81, 21))
        self.lbl9.setStyleSheet(u"")
        self.lbl9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_nombre = QLineEdit(self.frame_2)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setGeometry(QRect(240, 36, 205, 40))
        self.line_nombre.setStyleSheet(u"")
        self.line_nombre.setMaxLength(100)
        self.line_nombre.setFrame(True)
        self.line_nombre.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_nombre.setClearButtonEnabled(False)
        self.line_apeP = QLineEdit(self.frame_2)
        self.line_apeP.setObjectName(u"line_apeP")
        self.line_apeP.setGeometry(QRect(10, 114, 205, 40))
        self.line_apeP.setStyleSheet(u"")
        self.line_apeP.setMaxLength(100)
        self.line_apeP.setFrame(True)
        self.line_apeP.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl2 = QLabel(self.frame_2)
        self.lbl2.setObjectName(u"lbl2")
        self.lbl2.setGeometry(QRect(240, 90, 91, 21))
        self.lbl2.setStyleSheet(u"")
        self.lbl2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl8 = QLabel(self.frame_2)
        self.lbl8.setObjectName(u"lbl8")
        self.lbl8.setGeometry(QRect(10, 166, 181, 21))
        self.lbl8.setStyleSheet(u"")
        self.lbl8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.date_naci = QDateEdit(self.frame_2)
        self.date_naci.setObjectName(u"date_naci")
        self.date_naci.setGeometry(QRect(10, 190, 205, 40))
        self.date_naci.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_naci.setStyleSheet(u"/*SPINBOX*/\n"
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
        self.date_naci.setCalendarPopup(False)
        self.cbox_genero = QComboBox(self.frame_2)
        self.cbox_genero.addItem("")
        self.cbox_genero.addItem("")
        self.cbox_genero.addItem("")
        self.cbox_genero.setObjectName(u"cbox_genero")
        self.cbox_genero.setGeometry(QRect(240, 114, 205, 40))
        self.cbox_genero.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_genero.setStyleSheet(u"")
        self.lbl10 = QLabel(self.frame_2)
        self.lbl10.setObjectName(u"lbl10")
        self.lbl10.setGeometry(QRect(320, 241, 81, 21))
        self.lbl10.setStyleSheet(u"")
        self.lbl10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl3 = QLabel(self.frame_2)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setGeometry(QRect(10, 244, 151, 21))
        self.lbl3.setStyleSheet(u"")
        self.lbl3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_correo = QLineEdit(self.frame_2)
        self.line_correo.setObjectName(u"line_correo")
        self.line_correo.setEnabled(True)
        self.line_correo.setGeometry(QRect(10, 270, 291, 40))
        self.line_correo.setStyleSheet(u"")
        self.line_correo.setMaxLength(100)
        self.line_correo.setFrame(True)
        self.line_correo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_20 = QFrame(self.frame_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(10, 346, 291, 40))
        self.frame_20.setStyleSheet(u"#frame_20{background: #F3F4F6;\n"
"border: 1px solid  #F3F4F6; ;\n"
"border-radius: 11px;}\n"
"")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line_contrasena = QLineEdit(self.frame_20)
        self.line_contrasena.setObjectName(u"line_contrasena")
        self.line_contrasena.setMinimumSize(QSize(0, 0))
        self.line_contrasena.setMaximumSize(QSize(16777215, 16777215))
        self.line_contrasena.setStyleSheet(u"")
        self.line_contrasena.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.line_contrasena)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(43, 0))
        self.frame_21.setStyleSheet(u"background-color: rgb(243, 244, 246);")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.bnt_ojoVis = QPushButton(self.frame_21)
        self.bnt_ojoVis.setObjectName(u"bnt_ojoVis")
        self.bnt_ojoVis.setGeometry(QRect(11, 5, 29, 25))
        self.bnt_ojoVis.setMinimumSize(QSize(29, 25))
        self.bnt_ojoVis.setFocusPolicy(Qt.NoFocus)
        self.bnt_ojoVis.setStyleSheet(u"background-color: Transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/ojo2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_ojoVis.setIcon(icon1)
        self.bnt_ojoVis.setIconSize(QSize(25, 25))
        self.bnt_ojoInv = QPushButton(self.frame_21)
        self.bnt_ojoInv.setObjectName(u"bnt_ojoInv")
        self.bnt_ojoInv.setGeometry(QRect(10, 5, 29, 25))
        self.bnt_ojoInv.setMinimumSize(QSize(29, 25))
        self.bnt_ojoInv.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_ojoInv.setFocusPolicy(Qt.NoFocus)
        self.bnt_ojoInv.setStyleSheet(u"background-color: Transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/invi2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_ojoInv.setIcon(icon2)
        self.bnt_ojoInv.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.frame_21)

        self.lbl6_2 = QLabel(self.frame_2)
        self.lbl6_2.setObjectName(u"lbl6_2")
        self.lbl6_2.setGeometry(QRect(10, 322, 151, 21))
        self.lbl6_2.setStyleSheet(u"")
        self.lbl6_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl6_3 = QLabel(self.frame_2)
        self.lbl6_3.setObjectName(u"lbl6_3")
        self.lbl6_3.setGeometry(QRect(320, 322, 81, 21))
        self.lbl6_3.setStyleSheet(u"")
        self.lbl6_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbox_estado = QComboBox(self.frame_2)
        self.cbox_estado.addItem("")
        self.cbox_estado.addItem("")
        self.cbox_estado.setObjectName(u"cbox_estado")
        self.cbox_estado.setGeometry(QRect(312, 346, 141, 40))
        self.cbox_estado.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estado.setStyleSheet(u"")
        self.admi = QCheckBox(self.frame_2)
        self.admi.setObjectName(u"admi")
        self.admi.setEnabled(True)
        self.admi.setGeometry(QRect(320, 266, 131, 17))
        self.user = QCheckBox(self.frame_2)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(320, 290, 111, 17))
        self.cbox_sedes = QComboBox(self.frame_2)
        self.cbox_sedes.addItem("")
        self.cbox_sedes.addItem("")
        self.cbox_sedes.addItem("")
        self.cbox_sedes.setObjectName(u"cbox_sedes")
        self.cbox_sedes.setGeometry(QRect(240, 190, 205, 40))
        self.cbox_sedes.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_sedes.setStyleSheet(u"")
        self.lbl2_2 = QLabel(self.frame_2)
        self.lbl2_2.setObjectName(u"lbl2_2")
        self.lbl2_2.setGeometry(QRect(240, 166, 91, 21))
        self.lbl2_2.setStyleSheet(u"")
        self.lbl2_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btn_guardar = QPushButton(self.frame)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(130, 470, 195, 47))
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
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/close (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeadmi.setIcon(icon3)
        self.btn_closeadmi.setIconSize(QSize(13, 13))
        self.btn_closeadmi.setAutoRaise(True)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 231, 27))
        self.label_3.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 22px;\n"
"line-height: 40px;\n"
"letter-spacing: 0.02em;\n"
"color:#ffffff;")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.line_dni, self.line_nombre)
        QWidget.setTabOrder(self.line_nombre, self.line_apeP)
        QWidget.setTabOrder(self.line_apeP, self.cbox_genero)
        QWidget.setTabOrder(self.cbox_genero, self.date_naci)
        QWidget.setTabOrder(self.date_naci, self.cbox_sedes)
        QWidget.setTabOrder(self.cbox_sedes, self.line_correo)
        QWidget.setTabOrder(self.line_correo, self.admi)
        QWidget.setTabOrder(self.admi, self.user)
        QWidget.setTabOrder(self.user, self.line_contrasena)
        QWidget.setTabOrder(self.line_contrasena, self.cbox_estado)

        self.retranslateUi(Admi)

        self.cbox_estado.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Admi)
    # setupUi

    def retranslateUi(self, Admi):
        Admi.setWindowTitle(QCoreApplication.translate("Admi", u"Dialog", None))
        self.lbl5.setText(QCoreApplication.translate("Admi", u"Apellidos", None))
        self.line_dni.setPlaceholderText(QCoreApplication.translate("Admi", u"Ingrese n\u00famero de DNI", None))
        self.lbl11.setText(QCoreApplication.translate("Admi", u"Documento Identidad*", None))
        self.lbl9.setText(QCoreApplication.translate("Admi", u"Nombre*", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("Admi", u"Ingrese nombre", None))
        self.line_apeP.setPlaceholderText(QCoreApplication.translate("Admi", u"Ingrese apellido paterno", None))
        self.lbl2.setText(QCoreApplication.translate("Admi", u"Genero", None))
        self.lbl8.setText(QCoreApplication.translate("Admi", u"Fecha de nacimiento*", None))
        self.date_naci.setDisplayFormat(QCoreApplication.translate("Admi", u"yyyy-MM-d", None))
        self.cbox_genero.setItemText(0, QCoreApplication.translate("Admi", u"Seleccionar", None))
        self.cbox_genero.setItemText(1, QCoreApplication.translate("Admi", u"Masculino", None))
        self.cbox_genero.setItemText(2, QCoreApplication.translate("Admi", u"Femenino", None))

        self.lbl10.setText(QCoreApplication.translate("Admi", u"Roles*", None))
        self.lbl3.setText(QCoreApplication.translate("Admi", u"Correo electronico*", None))
        self.line_correo.setPlaceholderText(QCoreApplication.translate("Admi", u"Ingrese correo", None))
        self.line_contrasena.setPlaceholderText(QCoreApplication.translate("Admi", u"Ingrese contrase\u00f1a", None))
        self.bnt_ojoVis.setText("")
        self.bnt_ojoInv.setText("")
        self.lbl6_2.setText(QCoreApplication.translate("Admi", u"Contrase\u00f1a*", None))
        self.lbl6_3.setText(QCoreApplication.translate("Admi", u"Estado*", None))
        self.cbox_estado.setItemText(0, QCoreApplication.translate("Admi", u"Inactivo", None))
        self.cbox_estado.setItemText(1, QCoreApplication.translate("Admi", u"Activo", None))

        self.admi.setText(QCoreApplication.translate("Admi", u"Administrador", None))
        self.user.setText(QCoreApplication.translate("Admi", u"Usuario", None))
        self.cbox_sedes.setItemText(0, QCoreApplication.translate("Admi", u"Seleccionar", None))
        self.cbox_sedes.setItemText(1, QCoreApplication.translate("Admi", u"Santillana", None))
        self.cbox_sedes.setItemText(2, QCoreApplication.translate("Admi", u"Mayorca", None))

        self.lbl2_2.setText(QCoreApplication.translate("Admi", u"Sede", None))
        self.btn_guardar.setText(QCoreApplication.translate("Admi", u"Guardar", None))
#if QT_CONFIG(tooltip)
        self.btn_closeadmi.setToolTip(QCoreApplication.translate("Admi", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeadmi.setText("")
        self.label_3.setText(QCoreApplication.translate("Admi", u"Nuevo usuario", None))
    # retranslateUi

