# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario_estudiantesPROWAK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_FormularioEstudiante(object):
    def setupUi(self, FormularioEstudiante):
        if not FormularioEstudiante.objectName():
            FormularioEstudiante.setObjectName(u"FormularioEstudiante")
        FormularioEstudiante.resize(486, 557)
        FormularioEstudiante.setMinimumSize(QSize(486, 557))
        FormularioEstudiante.setMaximumSize(QSize(486, 557))
        self.gridLayout = QGridLayout(FormularioEstudiante)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormularioEstudiante)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{background-color: #f1f1f1;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px; \n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 50, 491, 461))
        self.scrollArea.setStyleSheet(u"#scrollArea{background-color: #f1f1f1; \n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;}\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 450;\n"
"font-size: 14px;\n"
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
"QDateEdit {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    letter-spacing: 0.02em;\n"
"    background: #F3F4F6;\n"
"    color: #9CA3AF;\n"
"    padding: 8px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QDateEdit::up-button {\n"
"    min-width: 25px;\n"
"    min-height: 12p"
                        "x;\n"
"    background-color: #F3F4F6; \n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    min-width: 25px;\n"
"    min-height: 12px;\n"
"    background-color: #F3F4F6; \n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QDateEdit::up-arrow {\n"
"    image: url(:/menu/contraerarriba.png);\n"
"    width: 11px;\n"
"    height: 11px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/menu/contraerabajo.png);\n"
"    width: 11px;\n"
"    height: 11px;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    background: #FFFFFF;\n"
"    border: 2px solid #344647;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* Estilo para el QCalendarWidget */\n"
"QCalendarWidget {\n"
"    font-family: Roboto;\n"
"    background: #F3F4F6;\n"
"    color: #344647;\n"
"    border: 2px solid #344647;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    background-color: #F3F4F6;\n"
"    color: #344647;\n"
"    font-size: 14px;\n"
"    border: none;\n"
"    margin: 5px;\n"
"    padding: 5px;\n"
"}\n"
""
                        "\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #E2E3E4;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    background-color: #F3F4F6;\n"
"    color: #344647;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    background: #F3F4F6;\n"
"    color: #344647;\n"
"    font-size: 14px;\n"
"    border: 1px solid #E2E3E4;\n"
"    border-radius: 4px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    background: #E2E3E4;\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-arrow, QCalendarWidget QSpinBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    font-size: 14px;\n"
"    color: #344647;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: #689091;\n"
"    selection-color: #FFFFFF;\n"
"    outline: none;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled {\n"
"    color: #9CA3AF;\n"
"}\n"
""
                        "\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #F3F4F6;\n"
"    border-bottom: 1px solid #E2E3E4;\n"
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
"     height: 11px;\n"
"}\n"
""
                        "\n"
"QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"/* QLabel para Mostrar Error */\n"
"QLabel#errorNombres, #errorApellidos, #errorIdentificacion, #errorFechaNacimiento, #errorCorreo, #errorTelefono, #errorDireccion{\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    color: #D32F2F; \n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scroll_registro_estudiante = QWidget()
        self.scroll_registro_estudiante.setObjectName(u"scroll_registro_estudiante")
        self.scroll_registro_estudiante.setGeometry(QRect(0, -229, 474, 690))
        self.scroll_registro_estudiante.setMinimumSize(QSize(0, 690))
        self.scroll_registro_estudiante.setStyleSheet(u"#scroll_registro_estudiante{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"")
        self.datospersonales = QLabel(self.scroll_registro_estudiante)
        self.datospersonales.setObjectName(u"datospersonales")
        self.datospersonales.setGeometry(QRect(10, 20, 161, 21))
        self.datospersonales.setStyleSheet(u"#datospersonales {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 17px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #000000; \n"
"    padding: 2px; \n"
"    text-decoration: underline; /* Agrega subrayado */\n"
"}\n"
"")
        self.line_nombres = QLineEdit(self.scroll_registro_estudiante)
        self.line_nombres.setObjectName(u"line_nombres")
        self.line_nombres.setEnabled(True)
        self.line_nombres.setGeometry(QRect(20, 76, 221, 40))
        self.line_nombres.setStyleSheet(u"")
        self.line_nombres.setMaxLength(30)
        self.line_nombres.setFrame(True)
        self.line_nombres.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.scroll_registro_estudiante)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(20, 50, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl11_2 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_2.setObjectName(u"lbl11_2")
        self.lbl11_2.setGeometry(QRect(250, 54, 171, 21))
        self.lbl11_2.setStyleSheet(u"")
        self.lbl11_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_apellidos = QLineEdit(self.scroll_registro_estudiante)
        self.line_apellidos.setObjectName(u"line_apellidos")
        self.line_apellidos.setEnabled(True)
        self.line_apellidos.setGeometry(QRect(250, 77, 221, 40))
        self.line_apellidos.setStyleSheet(u"")
        self.line_apellidos.setMaxLength(30)
        self.line_apellidos.setFrame(True)
        self.line_apellidos.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbo_tipoIdentificacion = QComboBox(self.scroll_registro_estudiante)
        self.cbo_tipoIdentificacion.addItem("")
        self.cbo_tipoIdentificacion.addItem("")
        self.cbo_tipoIdentificacion.addItem("")
        self.cbo_tipoIdentificacion.setObjectName(u"cbo_tipoIdentificacion")
        self.cbo_tipoIdentificacion.setGeometry(QRect(20, 170, 221, 40))
        self.lbl9_2 = QLabel(self.scroll_registro_estudiante)
        self.lbl9_2.setObjectName(u"lbl9_2")
        self.lbl9_2.setGeometry(QRect(20, 144, 131, 21))
        self.lbl9_2.setStyleSheet(u"")
        self.lbl9_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_identificacion = QLineEdit(self.scroll_registro_estudiante)
        self.line_identificacion.setObjectName(u"line_identificacion")
        self.line_identificacion.setEnabled(True)
        self.line_identificacion.setGeometry(QRect(250, 170, 221, 40))
        self.line_identificacion.setStyleSheet(u"")
        self.line_identificacion.setFrame(True)
        self.line_identificacion.setCursorPosition(0)
        self.line_identificacion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_identificacion.setDragEnabled(False)
        self.line_identificacion.setReadOnly(False)
        self.line_identificacion.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.line_identificacion.setClearButtonEnabled(False)
        self.lbl9_4 = QLabel(self.scroll_registro_estudiante)
        self.lbl9_4.setObjectName(u"lbl9_4")
        self.lbl9_4.setGeometry(QRect(250, 144, 131, 21))
        self.lbl9_4.setStyleSheet(u"")
        self.lbl9_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_97 = QLabel(self.scroll_registro_estudiante)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(20, 234, 161, 31))
        self.date_fechaNacimiento = QDateEdit(self.scroll_registro_estudiante)
        self.date_fechaNacimiento.setObjectName(u"date_fechaNacimiento")
        self.date_fechaNacimiento.setGeometry(QRect(20, 263, 221, 40))
        self.date_fechaNacimiento.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_fechaNacimiento.setStyleSheet(u"")
        self.date_fechaNacimiento.setCalendarPopup(True)
        self.lbl9_3 = QLabel(self.scroll_registro_estudiante)
        self.lbl9_3.setObjectName(u"lbl9_3")
        self.lbl9_3.setGeometry(QRect(250, 238, 131, 21))
        self.lbl9_3.setStyleSheet(u"")
        self.lbl9_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbo_genero = QComboBox(self.scroll_registro_estudiante)
        self.cbo_genero.addItem("")
        self.cbo_genero.addItem("")
        self.cbo_genero.addItem("")
        self.cbo_genero.setObjectName(u"cbo_genero")
        self.cbo_genero.setGeometry(QRect(250, 263, 221, 40))
        self.datoscontacto = QLabel(self.scroll_registro_estudiante)
        self.datoscontacto.setObjectName(u"datoscontacto")
        self.datoscontacto.setGeometry(QRect(10, 330, 171, 21))
        self.datoscontacto.setStyleSheet(u"#datoscontacto {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 17px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #000000; \n"
"    padding: 2px; \n"
"    text-decoration: underline; /* Agrega subrayado */\n"
"}\n"
"")
        self.lbl11_3 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_3.setObjectName(u"lbl11_3")
        self.lbl11_3.setGeometry(QRect(20, 364, 171, 21))
        self.lbl11_3.setStyleSheet(u"")
        self.lbl11_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_correo = QLineEdit(self.scroll_registro_estudiante)
        self.line_correo.setObjectName(u"line_correo")
        self.line_correo.setEnabled(True)
        self.line_correo.setGeometry(QRect(20, 390, 221, 40))
        self.line_correo.setStyleSheet(u"")
        self.line_correo.setMaxLength(30)
        self.line_correo.setFrame(True)
        self.line_correo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_telefono = QLineEdit(self.scroll_registro_estudiante)
        self.line_telefono.setObjectName(u"line_telefono")
        self.line_telefono.setEnabled(True)
        self.line_telefono.setGeometry(QRect(250, 390, 221, 40))
        self.line_telefono.setStyleSheet(u"")
        self.line_telefono.setMaxLength(30)
        self.line_telefono.setFrame(True)
        self.line_telefono.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11_4 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_4.setObjectName(u"lbl11_4")
        self.lbl11_4.setGeometry(QRect(250, 364, 171, 21))
        self.lbl11_4.setStyleSheet(u"")
        self.lbl11_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_direccion = QLineEdit(self.scroll_registro_estudiante)
        self.line_direccion.setObjectName(u"line_direccion")
        self.line_direccion.setEnabled(True)
        self.line_direccion.setGeometry(QRect(20, 480, 451, 40))
        self.line_direccion.setStyleSheet(u"")
        self.line_direccion.setMaxLength(30)
        self.line_direccion.setFrame(True)
        self.line_direccion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11_5 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_5.setObjectName(u"lbl11_5")
        self.lbl11_5.setGeometry(QRect(20, 454, 171, 21))
        self.lbl11_5.setStyleSheet(u"")
        self.lbl11_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.datosacademicos = QLabel(self.scroll_registro_estudiante)
        self.datosacademicos.setObjectName(u"datosacademicos")
        self.datosacademicos.setGeometry(QRect(10, 550, 181, 21))
        self.datosacademicos.setStyleSheet(u"#datosacademicos {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 17px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #000000; \n"
"    padding: 2px; \n"
"    text-decoration: underline; /* Agrega subrayado */\n"
"}\n"
"")
        self.lbl9_5 = QLabel(self.scroll_registro_estudiante)
        self.lbl9_5.setObjectName(u"lbl9_5")
        self.lbl9_5.setGeometry(QRect(20, 584, 131, 21))
        self.lbl9_5.setStyleSheet(u"")
        self.lbl9_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbo_carrera = QComboBox(self.scroll_registro_estudiante)
        self.cbo_carrera.setObjectName(u"cbo_carrera")
        self.cbo_carrera.setGeometry(QRect(20, 610, 451, 40))
        self.errorNombres = QLabel(self.scroll_registro_estudiante)
        self.errorNombres.setObjectName(u"errorNombres")
        self.errorNombres.setGeometry(QRect(20, 115, 221, 16))
        self.errorApellidos = QLabel(self.scroll_registro_estudiante)
        self.errorApellidos.setObjectName(u"errorApellidos")
        self.errorApellidos.setGeometry(QRect(250, 120, 221, 16))
        self.errorIdentificacion = QLabel(self.scroll_registro_estudiante)
        self.errorIdentificacion.setObjectName(u"errorIdentificacion")
        self.errorIdentificacion.setGeometry(QRect(250, 210, 221, 16))
        self.errorFechaNacimiento = QLabel(self.scroll_registro_estudiante)
        self.errorFechaNacimiento.setObjectName(u"errorFechaNacimiento")
        self.errorFechaNacimiento.setGeometry(QRect(20, 300, 221, 16))
        self.errorCorreo = QLabel(self.scroll_registro_estudiante)
        self.errorCorreo.setObjectName(u"errorCorreo")
        self.errorCorreo.setGeometry(QRect(20, 430, 221, 16))
        self.errorTelefono = QLabel(self.scroll_registro_estudiante)
        self.errorTelefono.setObjectName(u"errorTelefono")
        self.errorTelefono.setGeometry(QRect(250, 430, 221, 16))
        self.errorDireccion = QLabel(self.scroll_registro_estudiante)
        self.errorDireccion.setObjectName(u"errorDireccion")
        self.errorDireccion.setGeometry(QRect(20, 520, 441, 16))
        self.scrollArea.setWidget(self.scroll_registro_estudiante)
        self.frame_pie_pagina = QFrame(self.frame)
        self.frame_pie_pagina.setObjectName(u"frame_pie_pagina")
        self.frame_pie_pagina.setGeometry(QRect(0, 490, 491, 61))
        self.frame_pie_pagina.setStyleSheet(u"#frame_pie_pagina{background-color: #f1f1f1; \n"
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
"    transition: background-color 0.3s ease, color 0.3s ease; \n"
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
"    back"
                        "ground: transparent;\n"
"    border: 2px solid #3f5758; \n"
"    border-radius: 8px; \n"
"    transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease; \n"
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
"")
        self.frame_pie_pagina.setFrameShape(QFrame.NoFrame)
        self.frame_pie_pagina.setFrameShadow(QFrame.Raised)
        self.btn_agregar_estudiantes = QPushButton(self.frame_pie_pagina)
        self.btn_agregar_estudiantes.setObjectName(u"btn_agregar_estudiantes")
        self.btn_agregar_estudiantes.setGeometry(QRect(290, 15, 180, 40))
        self.btn_agregar_estudiantes.setMinimumSize(QSize(180, 40))
        self.btn_agregar_estudiantes.setMaximumSize(QSize(110, 40))
        self.btn_agregar_estudiantes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_estudiantes.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar_estudiantes.setIcon(icon)
        self.btn_agregar_estudiantes.setIconSize(QSize(15, 21))
        self.cancelButton = QPushButton(self.frame_pie_pagina)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(160, 14, 120, 40))
        self.cancelButton.setMinimumSize(QSize(120, 40))
        self.cancelButton.setMaximumSize(QSize(120, 40))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setFocusPolicy(Qt.NoFocus)
        self.cancelButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/no.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QSize(15, 21))
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 488, 51))
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_closeedit = QToolButton(self.frame_2)
        self.btn_closeedit.setObjectName(u"btn_closeedit")
        self.btn_closeedit.setGeometry(QRect(450, 9, 25, 25))
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
        icon2 = QIcon()
        icon2.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeedit.setIcon(icon2)
        self.btn_closeedit.setIconSize(QSize(13, 13))
        self.btn_closeedit.setAutoRaise(True)
        self.lbl_titulo_ventana = QLabel(self.frame_2)
        self.lbl_titulo_ventana.setObjectName(u"lbl_titulo_ventana")
        self.lbl_titulo_ventana.setGeometry(QRect(18, 14, 401, 21))
        self.lbl_titulo_ventana.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(FormularioEstudiante)

        QMetaObject.connectSlotsByName(FormularioEstudiante)
    # setupUi

    def retranslateUi(self, FormularioEstudiante):
        FormularioEstudiante.setWindowTitle(QCoreApplication.translate("FormularioEstudiante", u"Formulario Estudiante", None))
        self.datospersonales.setText(QCoreApplication.translate("FormularioEstudiante", u"Datos Personales", None))
        self.line_nombres.setPlaceholderText(QCoreApplication.translate("FormularioEstudiante", u"Ingrese  nombres", None))
        self.lbl11.setText(QCoreApplication.translate("FormularioEstudiante", u"Nombres*", None))
        self.lbl11_2.setText(QCoreApplication.translate("FormularioEstudiante", u"Apellidos*", None))
        self.line_apellidos.setPlaceholderText(QCoreApplication.translate("FormularioEstudiante", u"Ingrese apellidos", None))
        self.cbo_tipoIdentificacion.setItemText(0, QCoreApplication.translate("FormularioEstudiante", u"Cedula", None))
        self.cbo_tipoIdentificacion.setItemText(1, QCoreApplication.translate("FormularioEstudiante", u"Carnet extranjeria", None))
        self.cbo_tipoIdentificacion.setItemText(2, QCoreApplication.translate("FormularioEstudiante", u"Pasaporte", None))

        self.lbl9_2.setText(QCoreApplication.translate("FormularioEstudiante", u"Tipo identificaci\u00f3n*", None))
        self.line_identificacion.setPlaceholderText(QCoreApplication.translate("FormularioEstudiante", u"Ejm:  992928983-3", None))
        self.lbl9_4.setText(QCoreApplication.translate("FormularioEstudiante", u"Nro Identificacion*", None))
        self.label_97.setText(QCoreApplication.translate("FormularioEstudiante", u"Fecha Nacimiento", None))
        self.date_fechaNacimiento.setDisplayFormat(QCoreApplication.translate("FormularioEstudiante", u"yyyy-MM-d", None))
        self.lbl9_3.setText(QCoreApplication.translate("FormularioEstudiante", u"Genero*", None))
        self.cbo_genero.setItemText(0, QCoreApplication.translate("FormularioEstudiante", u"Masculino", None))
        self.cbo_genero.setItemText(1, QCoreApplication.translate("FormularioEstudiante", u"Femenino", None))
        self.cbo_genero.setItemText(2, QCoreApplication.translate("FormularioEstudiante", u"Otro", None))

        self.datoscontacto.setText(QCoreApplication.translate("FormularioEstudiante", u"Datos Contacto", None))
        self.lbl11_3.setText(QCoreApplication.translate("FormularioEstudiante", u"Correo*", None))
        self.line_correo.setPlaceholderText(QCoreApplication.translate("FormularioEstudiante", u"Ingrese correo", None))
        self.line_telefono.setPlaceholderText(QCoreApplication.translate("FormularioEstudiante", u"Ingrese telefono", None))
        self.lbl11_4.setText(QCoreApplication.translate("FormularioEstudiante", u"Tel\u00e9fono*", None))
        self.line_direccion.setPlaceholderText(QCoreApplication.translate("FormularioEstudiante", u"Ingrese calle , pais", None))
        self.lbl11_5.setText(QCoreApplication.translate("FormularioEstudiante", u"Direcci\u00f3n*", None))
        self.datosacademicos.setText(QCoreApplication.translate("FormularioEstudiante", u"Datos Acad\u00e9micos", None))
        self.lbl9_5.setText(QCoreApplication.translate("FormularioEstudiante", u"Carrera*", None))
        self.errorNombres.setText("")
        self.errorApellidos.setText("")
        self.errorIdentificacion.setText("")
        self.errorFechaNacimiento.setText("")
        self.errorCorreo.setText("")
        self.errorTelefono.setText("")
        self.errorDireccion.setText("")
        self.btn_agregar_estudiantes.setText(QCoreApplication.translate("FormularioEstudiante", u"Guardar estudiante", None))
        self.cancelButton.setText(QCoreApplication.translate("FormularioEstudiante", u"Cancelar", None))
#if QT_CONFIG(tooltip)
        self.btn_closeedit.setToolTip(QCoreApplication.translate("FormularioEstudiante", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeedit.setText("")
        self.lbl_titulo_ventana.setText(QCoreApplication.translate("FormularioEstudiante", u"Registrar Nuevo Estudiante", None))
    # retranslateUi

