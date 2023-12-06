# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usuario_perfilWEIkjq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_Perfil(object):
    def setupUi(self, Perfil):
        if not Perfil.objectName():
            Perfil.setObjectName(u"Perfil")
        Perfil.setEnabled(True)
        Perfil.resize(445, 620)
        Perfil.setMinimumSize(QSize(445, 620))
        Perfil.setMaximumSize(QSize(445, 620))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Perfil.setWindowIcon(icon)
        Perfil.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Perfil)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Perfil)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"\n"
"#frame{background-color:white;border-radius:10px}\n"
"\n"
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
"QLineEdit::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
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
"	padding:"
                        " 10px 10px 10px 20px;\n"
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
"/*  BOTON */\n"
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
"QPushButton:hover{background: #2e3e3f;\n"
"border-radius: 8px; }\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.line_apeP = QLineEdit(self.frame)
        self.line_apeP.setObjectName(u"line_apeP")
        self.line_apeP.setEnabled(True)
        self.line_apeP.setGeometry(QRect(217, 260, 205, 40))
        self.line_apeP.setStyleSheet(u"")
        self.line_apeP.setMaxLength(100)
        self.line_apeP.setFrame(True)
        self.line_apeP.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_nombre = QLineEdit(self.frame)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setEnabled(True)
        self.line_nombre.setGeometry(QRect(217, 173, 205, 40))
        self.line_nombre.setStyleSheet(u"")
        self.line_nombre.setMaxLength(100)
        self.line_nombre.setFrame(True)
        self.line_nombre.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_nombre.setClearButtonEnabled(False)
        self.lbl9 = QLabel(self.frame)
        self.lbl9.setObjectName(u"lbl9")
        self.lbl9.setGeometry(QRect(217, 150, 81, 21))
        self.lbl9.setStyleSheet(u"")
        self.lbl9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_dni = QLineEdit(self.frame)
        self.line_dni.setObjectName(u"line_dni")
        self.line_dni.setEnabled(False)
        self.line_dni.setGeometry(QRect(217, 94, 205, 40))
        self.line_dni.setStyleSheet(u"")
        self.line_dni.setMaxLength(100)
        self.line_dni.setFrame(True)
        self.line_dni.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.frame)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(217, 70, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl5 = QLabel(self.frame)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(217, 233, 151, 21))
        self.lbl5.setStyleSheet(u"")
        self.lbl5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbox_genero = QComboBox(self.frame)
        self.cbox_genero.addItem("")
        self.cbox_genero.addItem("")
        self.cbox_genero.addItem("")
        self.cbox_genero.setObjectName(u"cbox_genero")
        self.cbox_genero.setGeometry(QRect(24, 260, 168, 40))
        self.cbox_genero.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_genero.setStyleSheet(u"")
        self.lbl8 = QLabel(self.frame)
        self.lbl8.setObjectName(u"lbl8")
        self.lbl8.setGeometry(QRect(24, 315, 171, 21))
        self.lbl8.setStyleSheet(u"")
        self.lbl8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.date_naci = QDateEdit(self.frame)
        self.date_naci.setObjectName(u"date_naci")
        self.date_naci.setGeometry(QRect(24, 340, 171, 40))
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
        self.lbl2 = QLabel(self.frame)
        self.lbl2.setObjectName(u"lbl2")
        self.lbl2.setGeometry(QRect(24, 235, 91, 21))
        self.lbl2.setStyleSheet(u"")
        self.lbl2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_cargo = QLineEdit(self.frame)
        self.line_cargo.setObjectName(u"line_cargo")
        self.line_cargo.setEnabled(False)
        self.line_cargo.setGeometry(QRect(220, 340, 205, 40))
        self.line_cargo.setStyleSheet(u"")
        self.line_cargo.setMaxLength(20)
        self.line_cargo.setFrame(True)
        self.line_cargo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl10 = QLabel(self.frame)
        self.lbl10.setObjectName(u"lbl10")
        self.lbl10.setGeometry(QRect(221, 314, 81, 21))
        self.lbl10.setStyleSheet(u"")
        self.lbl10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl3 = QLabel(self.frame)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setGeometry(QRect(24, 396, 121, 21))
        self.lbl3.setStyleSheet(u"")
        self.lbl3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_correo = QLineEdit(self.frame)
        self.line_correo.setObjectName(u"line_correo")
        self.line_correo.setEnabled(False)
        self.line_correo.setGeometry(QRect(24, 420, 401, 40))
        self.line_correo.setStyleSheet(u"")
        self.line_correo.setMaxLength(100)
        self.line_correo.setFrame(True)
        self.line_correo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl1 = QLabel(self.frame)
        self.lbl1.setObjectName(u"lbl1")
        self.lbl1.setGeometry(QRect(24, 472, 101, 21))
        self.lbl1.setStyleSheet(u"")
        self.lbl1.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btn_guardar = QPushButton(self.frame)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(130, 560, 195, 47))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_guardar.sizePolicy().hasHeightForWidth())
        self.btn_guardar.setSizePolicy(sizePolicy)
        self.btn_guardar.setSizeIncrement(QSize(0, 0))
        self.btn_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_guardar.setFocusPolicy(Qt.NoFocus)
        self.btn_guardar.setAutoFillBackground(False)
        self.btn_guardar.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/image (10).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guardar.setIcon(icon1)
        self.btn_guardar.setIconSize(QSize(21, 21))
        self.btn_guardar.setCheckable(False)
        self.btn_guardar.setAutoRepeat(False)
        self.btn_guardar.setAutoExclusive(False)
        self.btn_guardar.setAutoDefault(False)
        self.btn_guardar.setFlat(False)
        self.frame_20 = QFrame(self.frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(24, 499, 400, 40))
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
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/ojo2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_ojoVis.setIcon(icon2)
        self.bnt_ojoVis.setIconSize(QSize(25, 25))
        self.bnt_ojoInv = QPushButton(self.frame_21)
        self.bnt_ojoInv.setObjectName(u"bnt_ojoInv")
        self.bnt_ojoInv.setGeometry(QRect(10, 5, 29, 25))
        self.bnt_ojoInv.setMinimumSize(QSize(29, 25))
        self.bnt_ojoInv.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_ojoInv.setFocusPolicy(Qt.NoFocus)
        self.bnt_ojoInv.setStyleSheet(u"background-color: Transparent;")
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/invi2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_ojoInv.setIcon(icon3)
        self.bnt_ojoInv.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.frame_21)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 140, 140))
        self.label.setStyleSheet(u"")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setPixmap(QPixmap(u":/prefijoNuevo/tapaRad11.png"))
        self.label.setScaledContents(True)
        self.lbl_perfil = QLabel(self.frame)
        self.lbl_perfil.setObjectName(u"lbl_perfil")
        self.lbl_perfil.setGeometry(QRect(30, 70, 140, 140))
        self.lbl_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbl_perfil.setStyleSheet(u"")
        self.lbl_perfil.setFrameShape(QFrame.NoFrame)
        self.lbl_perfil.setScaledContents(True)
        self.lbl_perfil.setMargin(0)
        self.btn_foto = QToolButton(self.frame)
        self.btn_foto.setObjectName(u"btn_foto")
        self.btn_foto.setGeometry(QRect(131, 156, 35, 35))
        self.btn_foto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_foto.setFocusPolicy(Qt.NoFocus)
        self.btn_foto.setStyleSheet(u"QToolButton{\n"
"\n"
"	\n"
"	background-color: rgba(0, 0, 0,0.5);\n"
"\n"
"	border:0px;\n"
"	border-radius:17px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/prefijoNuevo/btnCam.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/prefijoNuevo/btnCam1.png", QSize(), QIcon.Active, QIcon.Off)
        self.btn_foto.setIcon(icon4)
        self.btn_foto.setIconSize(QSize(22, 22))
        self.btn_foto.setAutoRaise(True)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 447, 50))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 91, 27))
        self.label_3.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 22px;\n"
"line-height: 40px;\n"
"letter-spacing: 0.02em;\n"
"color:#ffffff;")
        self.btn_closeperfil = QToolButton(self.frame_2)
        self.btn_closeperfil.setObjectName(u"btn_closeperfil")
        self.btn_closeperfil.setGeometry(QRect(410, 6, 25, 25))
        self.btn_closeperfil.setFocusPolicy(Qt.NoFocus)
        self.btn_closeperfil.setStyleSheet(u"#btn_closeperfil{\n"
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
"#btn_closeperfil:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/prefijoNuevo/close (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeperfil.setIcon(icon5)
        self.btn_closeperfil.setIconSize(QSize(13, 13))
        self.btn_closeperfil.setAutoRaise(True)
        self.line_apeP.raise_()
        self.line_nombre.raise_()
        self.lbl9.raise_()
        self.line_dni.raise_()
        self.lbl11.raise_()
        self.lbl5.raise_()
        self.cbox_genero.raise_()
        self.lbl8.raise_()
        self.date_naci.raise_()
        self.lbl2.raise_()
        self.line_cargo.raise_()
        self.lbl10.raise_()
        self.lbl3.raise_()
        self.line_correo.raise_()
        self.lbl1.raise_()
        self.btn_guardar.raise_()
        self.frame_20.raise_()
        self.lbl_perfil.raise_()
        self.label.raise_()
        self.btn_foto.raise_()
        self.frame_2.raise_()

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.line_dni, self.line_nombre)
        QWidget.setTabOrder(self.line_nombre, self.cbox_genero)
        QWidget.setTabOrder(self.cbox_genero, self.line_apeP)
        QWidget.setTabOrder(self.line_apeP, self.date_naci)
        QWidget.setTabOrder(self.date_naci, self.line_cargo)
        QWidget.setTabOrder(self.line_cargo, self.line_correo)
        QWidget.setTabOrder(self.line_correo, self.line_contrasena)

        self.retranslateUi(Perfil)
        self.line_nombre.windowTitleChanged.connect(self.line_nombre.setFocus)

        self.btn_guardar.setDefault(False)


        QMetaObject.connectSlotsByName(Perfil)
    # setupUi

    def retranslateUi(self, Perfil):
        Perfil.setWindowTitle(QCoreApplication.translate("Perfil", u"Dialog", None))
        self.line_apeP.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ingrese apellido paterno", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ingrese nombre", None))
        self.lbl9.setText(QCoreApplication.translate("Perfil", u"Nombre*", None))
        self.line_dni.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ingrese numero de DNI", None))
        self.lbl11.setText(QCoreApplication.translate("Perfil", u"Documento Identidad*", None))
        self.lbl5.setText(QCoreApplication.translate("Perfil", u"Apellidos*", None))
        self.cbox_genero.setItemText(0, QCoreApplication.translate("Perfil", u"Seleccionar", None))
        self.cbox_genero.setItemText(1, QCoreApplication.translate("Perfil", u"Masculino", None))
        self.cbox_genero.setItemText(2, QCoreApplication.translate("Perfil", u"Femenino", None))

        self.lbl8.setText(QCoreApplication.translate("Perfil", u"Fecha de nacimiento*", None))
        self.date_naci.setDisplayFormat(QCoreApplication.translate("Perfil", u"yyyy-MM-d", None))
        self.lbl2.setText(QCoreApplication.translate("Perfil", u"Genero*", None))
        self.line_cargo.setText("")
        self.lbl10.setText(QCoreApplication.translate("Perfil", u"Cargo*", None))
        self.lbl3.setText(QCoreApplication.translate("Perfil", u"Correo:", None))
        self.line_correo.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ingrese correo", None))
        self.lbl1.setText(QCoreApplication.translate("Perfil", u"Contrase\u00f1a*", None))
        self.btn_guardar.setText(QCoreApplication.translate("Perfil", u" Guardar", None))
        self.line_contrasena.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ingrese contrase\u00f1a", None))
        self.bnt_ojoVis.setText("")
        self.bnt_ojoInv.setText("")
        self.label.setText("")
        self.lbl_perfil.setText("")
        self.btn_foto.setText("")
        self.label_3.setText(QCoreApplication.translate("Perfil", u"Mi perfil", None))
#if QT_CONFIG(tooltip)
        self.btn_closeperfil.setToolTip(QCoreApplication.translate("Perfil", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeperfil.setText("")
    # retranslateUi

