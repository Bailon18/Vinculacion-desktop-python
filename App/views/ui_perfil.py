# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perfilYqLhDQ.ui'
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
        Perfil.resize(476, 490)
        Perfil.setMinimumSize(QSize(476, 400))
        Perfil.setMaximumSize(QSize(476, 490))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Perfil.setWindowIcon(icon)
        Perfil.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Perfil)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Perfil)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"background-color: rgb(255, 255, 255);\n"
"border-Bottom-left-radius: 10px;\n"
"border-Bottom-right-radius: 10px;\n"
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
"border: 2px solid #3A4F50;\n"
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
"    w"
                        "idth:15px;\n"
"    height:15px;\n"
"padding:13px 20px 10px 10px;\n"
"}\n"
"\n"
"QDateEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #3A4F50;\n"
"border-radius: 8px;\n"
"}\n"
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
"	image: url(:/menu/contraerabajo.png);\n"
"     width: 11px;\n"
"     hei"
                        "ght: 11px;\n"
"}\n"
"\n"
"QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox {combobox-popup: 0}\n"
"\n"
"QRadioButton{font-family: Roboto;\n"
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
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_guardar = QPushButton(self.frame_3)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(330, 380, 120, 40))
        self.btn_guardar.setMinimumSize(QSize(120, 40))
        self.btn_guardar.setMaximumSize(QSize(120, 40))
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
"QPushButton:hover{background: #344748;\n"
"border-radius: 8px; }\n"
"")
        self.btn_guardar.setIconSize(QSize(15, 21))
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 461, 351))
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.lbl5 = QLabel(self.frame_4)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(10, 93, 151, 21))
        self.lbl5.setStyleSheet(u"")
        self.lbl5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_dni = QLineEdit(self.frame_4)
        self.line_dni.setObjectName(u"line_dni")
        self.line_dni.setEnabled(True)
        self.line_dni.setGeometry(QRect(10, 36, 205, 40))
        self.line_dni.setStyleSheet(u"")
        self.line_dni.setMaxLength(11)
        self.line_dni.setFrame(True)
        self.line_dni.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.frame_4)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(10, 10, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl9 = QLabel(self.frame_4)
        self.lbl9.setObjectName(u"lbl9")
        self.lbl9.setGeometry(QRect(240, 10, 81, 21))
        self.lbl9.setStyleSheet(u"")
        self.lbl9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_nombre = QLineEdit(self.frame_4)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setEnabled(True)
        self.line_nombre.setGeometry(QRect(240, 36, 205, 40))
        self.line_nombre.setStyleSheet(u"")
        self.line_nombre.setMaxLength(100)
        self.line_nombre.setFrame(True)
        self.line_nombre.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_nombre.setClearButtonEnabled(False)
        self.line_apeP = QLineEdit(self.frame_4)
        self.line_apeP.setObjectName(u"line_apeP")
        self.line_apeP.setEnabled(True)
        self.line_apeP.setGeometry(QRect(10, 118, 205, 40))
        self.line_apeP.setStyleSheet(u"")
        self.line_apeP.setMaxLength(100)
        self.line_apeP.setFrame(True)
        self.line_apeP.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl10 = QLabel(self.frame_4)
        self.lbl10.setObjectName(u"lbl10")
        self.lbl10.setGeometry(QRect(320, 180, 82, 21))
        self.lbl10.setStyleSheet(u"")
        self.lbl10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl3 = QLabel(self.frame_4)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setGeometry(QRect(10, 180, 151, 21))
        self.lbl3.setStyleSheet(u"")
        self.lbl3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_correo = QLineEdit(self.frame_4)
        self.line_correo.setObjectName(u"line_correo")
        self.line_correo.setEnabled(True)
        self.line_correo.setGeometry(QRect(10, 204, 291, 40))
        self.line_correo.setStyleSheet(u"")
        self.line_correo.setMaxLength(100)
        self.line_correo.setFrame(True)
        self.line_correo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl6_2 = QLabel(self.frame_4)
        self.lbl6_2.setObjectName(u"lbl6_2")
        self.lbl6_2.setGeometry(QRect(10, 262, 151, 21))
        self.lbl6_2.setStyleSheet(u"")
        self.lbl6_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl6_3 = QLabel(self.frame_4)
        self.lbl6_3.setObjectName(u"lbl6_3")
        self.lbl6_3.setGeometry(QRect(242, 95, 81, 21))
        self.lbl6_3.setStyleSheet(u"")
        self.lbl6_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbox_estado = QComboBox(self.frame_4)
        self.cbox_estado.addItem("")
        self.cbox_estado.addItem("")
        self.cbox_estado.setObjectName(u"cbox_estado")
        self.cbox_estado.setGeometry(QRect(240, 120, 205, 40))
        self.cbox_estado.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estado.setStyleSheet(u"")
        self.admi = QRadioButton(self.frame_4)
        self.admi.setObjectName(u"admi")
        self.admi.setEnabled(True)
        self.admi.setGeometry(QRect(320, 206, 131, 17))
        self.tutor = QRadioButton(self.frame_4)
        self.tutor.setObjectName(u"tutor")
        self.tutor.setGeometry(QRect(320, 228, 111, 17))
        self.line_contrasena = QLineEdit(self.frame_4)
        self.line_contrasena.setObjectName(u"line_contrasena")
        self.line_contrasena.setEnabled(True)
        self.line_contrasena.setGeometry(QRect(10, 290, 291, 38))
        self.line_contrasena.setMinimumSize(QSize(0, 0))
        self.line_contrasena.setMaximumSize(QSize(16777215, 16777215))
        self.line_contrasena.setStyleSheet(u"")
        self.line_contrasena.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_closeedit = QToolButton(self.frame_2)
        self.btn_closeedit.setObjectName(u"btn_closeedit")
        self.btn_closeedit.setGeometry(QRect(450, 6, 25, 25))
        self.btn_closeedit.setFocusPolicy(Qt.NoFocus)
        self.btn_closeedit.setStyleSheet(u"#btn_closeedit{\n"
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
"#btn_closeedit:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeedit.setIcon(icon1)
        self.btn_closeedit.setIconSize(QSize(13, 13))
        self.btn_closeedit.setAutoRaise(True)
        self.lbl_titulo_ventana = QLabel(self.frame_2)
        self.lbl_titulo_ventana.setObjectName(u"lbl_titulo_ventana")
        self.lbl_titulo_ventana.setGeometry(QRect(19, 4, 241, 19))
        self.lbl_titulo_ventana.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")
        self.lbl_usuariologeado = QLabel(self.frame_2)
        self.lbl_usuariologeado.setObjectName(u"lbl_usuariologeado")
        self.lbl_usuariologeado.setGeometry(QRect(20, 27, 341, 21))
        self.lbl_usuariologeado.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.line_dni, self.line_nombre)
        QWidget.setTabOrder(self.line_nombre, self.line_apeP)
        QWidget.setTabOrder(self.line_apeP, self.cbox_estado)
        QWidget.setTabOrder(self.cbox_estado, self.line_correo)
        QWidget.setTabOrder(self.line_correo, self.admi)
        QWidget.setTabOrder(self.admi, self.tutor)

        self.retranslateUi(Perfil)

        self.cbox_estado.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Perfil)
    # setupUi

    def retranslateUi(self, Perfil):
        Perfil.setWindowTitle(QCoreApplication.translate("Perfil", u"Dialog", None))
        self.btn_guardar.setText(QCoreApplication.translate("Perfil", u"Guardar", None))
        self.lbl5.setText(QCoreApplication.translate("Perfil", u"Apellidos*", None))
        self.line_dni.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ejm:  992928983-3", None))
        self.lbl11.setText(QCoreApplication.translate("Perfil", u"Documento Identidad*", None))
        self.lbl9.setText(QCoreApplication.translate("Perfil", u"Nombre*", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ingrese nombre", None))
        self.line_apeP.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ingrese apellido paterno", None))
        self.lbl10.setText(QCoreApplication.translate("Perfil", u"Cargo*", None))
        self.lbl3.setText(QCoreApplication.translate("Perfil", u"Correo electronico*", None))
        self.line_correo.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ingrese correo", None))
        self.lbl6_2.setText(QCoreApplication.translate("Perfil", u"Contrase\u00f1a*", None))
        self.lbl6_3.setText(QCoreApplication.translate("Perfil", u"Estado*", None))
        self.cbox_estado.setItemText(0, QCoreApplication.translate("Perfil", u"Inactivo", None))
        self.cbox_estado.setItemText(1, QCoreApplication.translate("Perfil", u"Activo", None))

        self.admi.setText(QCoreApplication.translate("Perfil", u"Administrador", None))
        self.tutor.setText(QCoreApplication.translate("Perfil", u"Tutor", None))
        self.line_contrasena.setPlaceholderText(QCoreApplication.translate("Perfil", u"Ingrese contrase\u00f1a", None))
#if QT_CONFIG(tooltip)
        self.btn_closeedit.setToolTip(QCoreApplication.translate("Perfil", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeedit.setText("")
        self.lbl_titulo_ventana.setText(QCoreApplication.translate("Perfil", u"Nuevo Usuario", None))
        self.lbl_usuariologeado.setText("")
    # retranslateUi

