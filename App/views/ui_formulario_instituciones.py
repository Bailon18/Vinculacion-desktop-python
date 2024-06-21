# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario_institucionesxWMFvO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_FormularioInstitucion(object):
    def setupUi(self, FormularioInstitucion):
        if not FormularioInstitucion.objectName():
            FormularioInstitucion.setObjectName(u"FormularioInstitucion")
        FormularioInstitucion.resize(476, 520)
        FormularioInstitucion.setMinimumSize(QSize(476, 520))
        FormularioInstitucion.setMaximumSize(QSize(476, 520))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        FormularioInstitucion.setWindowIcon(icon)
        FormularioInstitucion.setStyleSheet(u"")
        self.gridLayout = QGridLayout(FormularioInstitucion)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormularioInstitucion)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{background-color: #f1f1f1;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px; \n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;}\n"
"")
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
"#frame_pie_pagina{background-color: #f1f1f1; \n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;}\n"
"\n"
"/*  BOTON */\n"
"\n"
"QPushButton {\n"
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
"}\n"
"\n"
"\n"
"/* Bot\u00f3n Cance"
                        "lar */\n"
"QPushButton#cancelButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #3f5758;\n"
"    padding: 8px 16px;\n"
"    background: transparent;\n"
"    border: 2px solid #3f5758; \n"
"    border-radius: 8px; \n"
"\n"
"}\n"
"\n"
"QPushButton#cancelButton:hover {\n"
"    background: rgba(63, 87, 88, 0.1); /* Fondo ligeramente oscuro en hover */\n"
"    color: #2e4546; \n"
"    border: 2px solid #2e4546;\n"
"}\n"
"\n"
"QPushButton#cancelButton:pressed {\n"
"    background: rgba(63, 87, 88, 0.2); /* Fondo m\u00e1s oscuro en estado presionado */\n"
"    color: #1c2d2e; \n"
"    border: 2px solid #1c2d2e;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 461, 391))
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"/* QLabel para Mostrar Error */\n"
"QLabel#errorNombre, #errorTelefono, #errorDireccion{\n"
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
        self.lbl5.setGeometry(QRect(10, 103, 151, 21))
        self.lbl5.setStyleSheet(u"")
        self.lbl5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_nombre_institucion = QLineEdit(self.frame_4)
        self.line_nombre_institucion.setObjectName(u"line_nombre_institucion")
        self.line_nombre_institucion.setEnabled(True)
        self.line_nombre_institucion.setGeometry(QRect(10, 36, 431, 40))
        self.line_nombre_institucion.setStyleSheet(u"")
        self.line_nombre_institucion.setMaxLength(102)
        self.line_nombre_institucion.setFrame(True)
        self.line_nombre_institucion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.frame_4)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(10, 10, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl3 = QLabel(self.frame_4)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setGeometry(QRect(10, 196, 151, 21))
        self.lbl3.setStyleSheet(u"")
        self.lbl3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_direccion_institucion = QLineEdit(self.frame_4)
        self.line_direccion_institucion.setObjectName(u"line_direccion_institucion")
        self.line_direccion_institucion.setEnabled(True)
        self.line_direccion_institucion.setGeometry(QRect(10, 220, 431, 40))
        self.line_direccion_institucion.setStyleSheet(u"")
        self.line_direccion_institucion.setMaxLength(100)
        self.line_direccion_institucion.setFrame(True)
        self.line_direccion_institucion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl6_3 = QLabel(self.frame_4)
        self.lbl6_3.setObjectName(u"lbl6_3")
        self.lbl6_3.setGeometry(QRect(242, 105, 81, 21))
        self.lbl6_3.setStyleSheet(u"")
        self.lbl6_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbox_estado_intitucion = QComboBox(self.frame_4)
        self.cbox_estado_intitucion.addItem("")
        self.cbox_estado_intitucion.addItem("")
        self.cbox_estado_intitucion.setObjectName(u"cbox_estado_intitucion")
        self.cbox_estado_intitucion.setGeometry(QRect(240, 130, 205, 40))
        self.cbox_estado_intitucion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estado_intitucion.setStyleSheet(u"")
        self.cbo_tipoIdentificacion = QComboBox(self.frame_4)
        self.cbo_tipoIdentificacion.addItem("")
        self.cbo_tipoIdentificacion.addItem("")
        self.cbo_tipoIdentificacion.addItem("")
        self.cbo_tipoIdentificacion.setObjectName(u"cbo_tipoIdentificacion")
        self.cbo_tipoIdentificacion.setGeometry(QRect(10, 130, 221, 40))
        self.errorNombre = QLabel(self.frame_4)
        self.errorNombre.setObjectName(u"errorNombre")
        self.errorNombre.setGeometry(QRect(10, 76, 431, 16))
        self.lbl11_4 = QLabel(self.frame_4)
        self.lbl11_4.setObjectName(u"lbl11_4")
        self.lbl11_4.setGeometry(QRect(10, 290, 221, 21))
        self.lbl11_4.setStyleSheet(u"")
        self.lbl11_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_telefono = QLineEdit(self.frame_4)
        self.line_telefono.setObjectName(u"line_telefono")
        self.line_telefono.setEnabled(True)
        self.line_telefono.setGeometry(QRect(10, 316, 221, 40))
        self.line_telefono.setStyleSheet(u"")
        self.line_telefono.setMaxLength(30)
        self.line_telefono.setFrame(True)
        self.line_telefono.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.errorDireccion = QLabel(self.frame_4)
        self.errorDireccion.setObjectName(u"errorDireccion")
        self.errorDireccion.setGeometry(QRect(10, 261, 431, 16))
        self.errorTelefono = QLabel(self.frame_4)
        self.errorTelefono.setObjectName(u"errorTelefono")
        self.errorTelefono.setGeometry(QRect(10, 360, 221, 16))
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 409, 481, 61))
        self.frame_5.setStyleSheet(u"#frame_5{background-color: #f1f1f1; \n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;}\n"
"\n"
"/*  BOTON */\n"
"\n"
"QPushButton {\n"
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
"}\n"
"\n"
"\n"
"/* Bot\u00f3n Cancelar */\n"
"QPushButton#cancelButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #3f5758;\n"
"    padding: 8px 16px;\n"
"    background: transparent;\n"
"    border: 2px solid #3f5758; \n"
"    border-rad"
                        "ius: 8px; \n"
"}\n"
"\n"
"QPushButton#cancelButton:hover {\n"
"    background: rgba(63, 87, 88, 0.1); /* Fondo ligeramente oscuro en hover */\n"
"    color: #2e4546; \n"
"    border: 2px solid #2e4546;\n"
"}\n"
"\n"
"QPushButton#cancelButton:pressed {\n"
"    background: rgba(63, 87, 88, 0.2); /* Fondo m\u00e1s oscuro en estado presionado */\n"
"    color: #1c2d2e; \n"
"    border: 2px solid #1c2d2e;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.btn_guardar_institiucion = QPushButton(self.frame_5)
        self.btn_guardar_institiucion.setObjectName(u"btn_guardar_institiucion")
        self.btn_guardar_institiucion.setGeometry(QRect(280, 10, 180, 40))
        self.btn_guardar_institiucion.setMinimumSize(QSize(180, 40))
        self.btn_guardar_institiucion.setMaximumSize(QSize(120, 40))
        self.btn_guardar_institiucion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_guardar_institiucion.setFocusPolicy(Qt.NoFocus)
        self.btn_guardar_institiucion.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guardar_institiucion.setIcon(icon1)
        self.btn_guardar_institiucion.setIconSize(QSize(15, 21))
        self.cancelButton = QPushButton(self.frame_5)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(150, 10, 120, 40))
        self.cancelButton.setMinimumSize(QSize(120, 40))
        self.cancelButton.setMaximumSize(QSize(120, 40))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setFocusPolicy(Qt.NoFocus)
        self.cancelButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/menu/no.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon2)
        self.cancelButton.setIconSize(QSize(15, 21))

        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_close = QToolButton(self.frame_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(445, 11, 25, 25))
        self.btn_close.setFocusPolicy(Qt.NoFocus)
        self.btn_close.setStyleSheet(u"#btn_close{\n"
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
"#btn_close:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)
        self.btn_close.setIconSize(QSize(13, 13))
        self.btn_close.setAutoRaise(True)
        self.lbl_titulo_ventana = QLabel(self.frame_2)
        self.lbl_titulo_ventana.setObjectName(u"lbl_titulo_ventana")
        self.lbl_titulo_ventana.setGeometry(QRect(19, 16, 341, 19))
        self.lbl_titulo_ventana.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")
        self.lbl_instituto_seleccionado = QLabel(self.frame_2)
        self.lbl_instituto_seleccionado.setObjectName(u"lbl_instituto_seleccionado")
        self.lbl_instituto_seleccionado.setGeometry(QRect(20, 27, 411, 21))
        self.lbl_instituto_seleccionado.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.line_nombre_institucion, self.cbox_estado_intitucion)
        QWidget.setTabOrder(self.cbox_estado_intitucion, self.line_direccion_institucion)

        self.retranslateUi(FormularioInstitucion)

        self.cbox_estado_intitucion.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(FormularioInstitucion)
    # setupUi

    def retranslateUi(self, FormularioInstitucion):
        FormularioInstitucion.setWindowTitle(QCoreApplication.translate("FormularioInstitucion", u"Formulario Institucion", None))
        self.lbl5.setText(QCoreApplication.translate("FormularioInstitucion", u"Tipo de instituci\u00f3n*", None))
        self.line_nombre_institucion.setPlaceholderText(QCoreApplication.translate("FormularioInstitucion", u"Ingrese nombre de la instituci\u00f3n", None))
        self.lbl11.setText(QCoreApplication.translate("FormularioInstitucion", u"Nombre instituci\u00f3n*", None))
        self.lbl3.setText(QCoreApplication.translate("FormularioInstitucion", u"Direcci\u00f3n ( Opcional )", None))
        self.line_direccion_institucion.setPlaceholderText(QCoreApplication.translate("FormularioInstitucion", u"Ingrese la direcci\u00f3n ", None))
        self.lbl6_3.setText(QCoreApplication.translate("FormularioInstitucion", u"Estado*", None))
        self.cbox_estado_intitucion.setItemText(0, QCoreApplication.translate("FormularioInstitucion", u"Inactivo", None))
        self.cbox_estado_intitucion.setItemText(1, QCoreApplication.translate("FormularioInstitucion", u"Activo", None))

        self.cbo_tipoIdentificacion.setItemText(0, QCoreApplication.translate("FormularioInstitucion", u"Publica", None))
        self.cbo_tipoIdentificacion.setItemText(1, QCoreApplication.translate("FormularioInstitucion", u"Privada", None))
        self.cbo_tipoIdentificacion.setItemText(2, QCoreApplication.translate("FormularioInstitucion", u"Otro", None))

        self.errorNombre.setText("")
        self.lbl11_4.setText(QCoreApplication.translate("FormularioInstitucion", u"Tel\u00e9fono", None))
        self.line_telefono.setPlaceholderText(QCoreApplication.translate("FormularioInstitucion", u"Ingrese telefono", None))
        self.errorDireccion.setText("")
        self.errorTelefono.setText("")
        self.btn_guardar_institiucion.setText(QCoreApplication.translate("FormularioInstitucion", u"Guardar institucion", None))
        self.cancelButton.setText(QCoreApplication.translate("FormularioInstitucion", u"Cancelar", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("FormularioInstitucion", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.lbl_titulo_ventana.setText(QCoreApplication.translate("FormularioInstitucion", u"Formulario de registro de instituciones", None))
        self.lbl_instituto_seleccionado.setText("")
    # retranslateUi

