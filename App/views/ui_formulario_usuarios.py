# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario_usuariosCEPfOL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_FormularioUsuario(object):
    def setupUi(self, FormularioUsuario):
        if not FormularioUsuario.objectName():
            FormularioUsuario.setObjectName(u"FormularioUsuario")
        FormularioUsuario.resize(476, 520)
        FormularioUsuario.setMinimumSize(QSize(476, 520))
        FormularioUsuario.setMaximumSize(QSize(476, 520))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        FormularioUsuario.setWindowIcon(icon)
        FormularioUsuario.setStyleSheet(u"")
        self.gridLayout = QGridLayout(FormularioUsuario)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormularioUsuario)
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
        self.btn_guardar.setGeometry(QRect(320, 426, 136, 40))
        self.btn_guardar.setMinimumSize(QSize(136, 40))
        self.btn_guardar.setMaximumSize(QSize(120, 40))
        self.btn_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_guardar.setFocusPolicy(Qt.NoFocus)
        self.btn_guardar.setStyleSheet(u"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    background: #3f5758;\n"
"    border: none; \n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #4a6b6c; \n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background: #2e4546;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        self.btn_guardar.setIconSize(QSize(15, 21))
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 461, 411))
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"/* QLabel para Mostrar Error */\n"
"QLabel#errorNombres, #errorApellidos, #errorIdentificacion, #errorFechaNacimiento, #errorCorreo, #errorTelefono, #errorDireccion, #errorContrasena{\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    color: #D32F2F; \n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.lbl5 = QLabel(self.frame_4)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(10, 113, 151, 21))
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
        self.line_apeP.setGeometry(QRect(10, 138, 205, 40))
        self.line_apeP.setStyleSheet(u"")
        self.line_apeP.setMaxLength(100)
        self.line_apeP.setFrame(True)
        self.line_apeP.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl10 = QLabel(self.frame_4)
        self.lbl10.setObjectName(u"lbl10")
        self.lbl10.setGeometry(QRect(320, 212, 82, 21))
        self.lbl10.setStyleSheet(u"")
        self.lbl10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl3 = QLabel(self.frame_4)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setGeometry(QRect(10, 212, 151, 21))
        self.lbl3.setStyleSheet(u"")
        self.lbl3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_correo = QLineEdit(self.frame_4)
        self.line_correo.setObjectName(u"line_correo")
        self.line_correo.setEnabled(True)
        self.line_correo.setGeometry(QRect(10, 236, 291, 40))
        self.line_correo.setStyleSheet(u"")
        self.line_correo.setMaxLength(100)
        self.line_correo.setFrame(True)
        self.line_correo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl6_2 = QLabel(self.frame_4)
        self.lbl6_2.setObjectName(u"lbl6_2")
        self.lbl6_2.setGeometry(QRect(10, 310, 151, 21))
        self.lbl6_2.setStyleSheet(u"")
        self.lbl6_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl6_3 = QLabel(self.frame_4)
        self.lbl6_3.setObjectName(u"lbl6_3")
        self.lbl6_3.setGeometry(QRect(242, 110, 81, 21))
        self.lbl6_3.setStyleSheet(u"")
        self.lbl6_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbox_estado = QComboBox(self.frame_4)
        self.cbox_estado.addItem("")
        self.cbox_estado.addItem("")
        self.cbox_estado.setObjectName(u"cbox_estado")
        self.cbox_estado.setGeometry(QRect(240, 140, 205, 40))
        self.cbox_estado.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estado.setStyleSheet(u"")
        self.admi = QRadioButton(self.frame_4)
        self.admi.setObjectName(u"admi")
        self.admi.setEnabled(True)
        self.admi.setGeometry(QRect(320, 238, 131, 17))
        self.admi.setChecked(True)
        self.tutor = QRadioButton(self.frame_4)
        self.tutor.setObjectName(u"tutor")
        self.tutor.setGeometry(QRect(320, 260, 111, 17))
        self.line_contrasena = QLineEdit(self.frame_4)
        self.line_contrasena.setObjectName(u"line_contrasena")
        self.line_contrasena.setEnabled(True)
        self.line_contrasena.setGeometry(QRect(10, 340, 291, 38))
        self.line_contrasena.setMinimumSize(QSize(0, 0))
        self.line_contrasena.setMaximumSize(QSize(16777215, 16777215))
        self.line_contrasena.setStyleSheet(u"")
        self.line_contrasena.setEchoMode(QLineEdit.Password)
        self.errorNombres = QLabel(self.frame_4)
        self.errorNombres.setObjectName(u"errorNombres")
        self.errorNombres.setGeometry(QRect(242, 77, 201, 16))
        self.errorApellidos = QLabel(self.frame_4)
        self.errorApellidos.setObjectName(u"errorApellidos")
        self.errorApellidos.setGeometry(QRect(10, 179, 201, 16))
        self.errorIdentificacion = QLabel(self.frame_4)
        self.errorIdentificacion.setObjectName(u"errorIdentificacion")
        self.errorIdentificacion.setGeometry(QRect(12, 76, 201, 16))
        self.errorCorreo = QLabel(self.frame_4)
        self.errorCorreo.setObjectName(u"errorCorreo")
        self.errorCorreo.setGeometry(QRect(10, 277, 291, 16))
        self.errorContrasena = QLabel(self.frame_4)
        self.errorContrasena.setObjectName(u"errorContrasena")
        self.errorContrasena.setGeometry(QRect(10, 380, 291, 16))

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

        self.retranslateUi(FormularioUsuario)

        self.cbox_estado.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(FormularioUsuario)
    # setupUi

    def retranslateUi(self, FormularioUsuario):
        FormularioUsuario.setWindowTitle(QCoreApplication.translate("FormularioUsuario", u"Dialog", None))
        self.btn_guardar.setText(QCoreApplication.translate("FormularioUsuario", u"Guardar", None))
        self.lbl5.setText(QCoreApplication.translate("FormularioUsuario", u"Apellidos*", None))
        self.line_dni.setPlaceholderText(QCoreApplication.translate("FormularioUsuario", u"Ejm:  9929289833", None))
        self.lbl11.setText(QCoreApplication.translate("FormularioUsuario", u"C\u00e9dula*", None))
        self.lbl9.setText(QCoreApplication.translate("FormularioUsuario", u"Nombre*", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("FormularioUsuario", u"Ingrese nombre", None))
        self.line_apeP.setPlaceholderText(QCoreApplication.translate("FormularioUsuario", u"Ingrese apellidos", None))
        self.lbl10.setText(QCoreApplication.translate("FormularioUsuario", u"Cargo*", None))
        self.lbl3.setText(QCoreApplication.translate("FormularioUsuario", u"Correo electronico*", None))
        self.line_correo.setPlaceholderText(QCoreApplication.translate("FormularioUsuario", u"Ingrese correo", None))
        self.lbl6_2.setText(QCoreApplication.translate("FormularioUsuario", u"Contrase\u00f1a*", None))
        self.lbl6_3.setText(QCoreApplication.translate("FormularioUsuario", u"Estado*", None))
        self.cbox_estado.setItemText(0, QCoreApplication.translate("FormularioUsuario", u"Inactivo", None))
        self.cbox_estado.setItemText(1, QCoreApplication.translate("FormularioUsuario", u"Activo", None))

        self.admi.setText(QCoreApplication.translate("FormularioUsuario", u"Administrador", None))
        self.tutor.setText(QCoreApplication.translate("FormularioUsuario", u"Otros", None))
        self.line_contrasena.setPlaceholderText(QCoreApplication.translate("FormularioUsuario", u"Ingrese contrase\u00f1a", None))
        self.errorNombres.setText("")
        self.errorApellidos.setText("")
        self.errorIdentificacion.setText("")
        self.errorCorreo.setText("")
        self.errorContrasena.setText("")
#if QT_CONFIG(tooltip)
        self.btn_closeedit.setToolTip(QCoreApplication.translate("FormularioUsuario", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeedit.setText("")
        self.lbl_titulo_ventana.setText(QCoreApplication.translate("FormularioUsuario", u"Nuevo Usuario", None))
        self.lbl_usuariologeado.setText("")
    # retranslateUi

