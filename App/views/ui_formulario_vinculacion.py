# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario_vinculacionYklVMu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_FormularioVinculacion(object):
    def setupUi(self, FormularioVinculacion):
        if not FormularioVinculacion.objectName():
            FormularioVinculacion.setObjectName(u"FormularioVinculacion")
        FormularioVinculacion.resize(820, 557)
        FormularioVinculacion.setMinimumSize(QSize(486, 557))
        FormularioVinculacion.setMaximumSize(QSize(840, 557))
        self.gridLayout = QGridLayout(FormularioVinculacion)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormularioVinculacion)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{background-color: #f1f1f1;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px; \n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 821, 50))
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_close = QToolButton(self.frame_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(790, 10, 25, 25))
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
"#btn_close:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(13, 13))
        self.btn_close.setAutoRaise(True)
        self.lbl_titulo_ventana = QLabel(self.frame_2)
        self.lbl_titulo_ventana.setObjectName(u"lbl_titulo_ventana")
        self.lbl_titulo_ventana.setGeometry(QRect(19, 15, 401, 21))
        self.lbl_titulo_ventana.setStyleSheet(u"QLabel{font-family: \"Roboto\";\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 50, 821, 451))
        self.scrollArea.setStyleSheet(u"\n"
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
"    min-height: 12px;\n"
"    background-color: #F3F4F6; \n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    min-width: 25px"
                        ";\n"
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
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #E2E3E4;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    backgro"
                        "und-color: #F3F4F6;\n"
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
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #F3F4F6;\n"
"    border-bottom: 1px solid #E"
                        "2E3E4;\n"
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
"\n"
"QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"/* QLabe"
                        "l para Mostrar Error */\n"
"QLabel#errorCodigoies, #errorCampoEspecifico, #errorEstudianteNoEncontrado,#errorBuscar, #errorInstitucion, #errorProyecto, #errorTutor{\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    color: #D32F2F; \n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_registro_estudiante = QWidget()
        self.scroll_registro_estudiante.setObjectName(u"scroll_registro_estudiante")
        self.scroll_registro_estudiante.setGeometry(QRect(0, 0, 802, 950))
        self.scroll_registro_estudiante.setMinimumSize(QSize(0, 950))
        self.scroll_registro_estudiante.setStyleSheet(u"#scroll_registro_estudiante{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.datospersonales = QLabel(self.scroll_registro_estudiante)
        self.datospersonales.setObjectName(u"datospersonales")
        self.datospersonales.setGeometry(QRect(14, 10, 311, 21))
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
        self.line_codigo_ies = QLineEdit(self.scroll_registro_estudiante)
        self.line_codigo_ies.setObjectName(u"line_codigo_ies")
        self.line_codigo_ies.setEnabled(True)
        self.line_codigo_ies.setGeometry(QRect(260, 70, 221, 40))
        self.line_codigo_ies.setStyleSheet(u"")
        self.line_codigo_ies.setMaxLength(30)
        self.line_codigo_ies.setFrame(True)
        self.line_codigo_ies.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.scroll_registro_estudiante)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(260, 45, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl11_2 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_2.setObjectName(u"lbl11_2")
        self.lbl11_2.setGeometry(QRect(500, 45, 171, 21))
        self.lbl11_2.setStyleSheet(u"")
        self.lbl11_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_campo_especifico = QLineEdit(self.scroll_registro_estudiante)
        self.line_campo_especifico.setObjectName(u"line_campo_especifico")
        self.line_campo_especifico.setEnabled(True)
        self.line_campo_especifico.setGeometry(QRect(500, 70, 281, 40))
        self.line_campo_especifico.setStyleSheet(u"")
        self.line_campo_especifico.setMaxLength(30)
        self.line_campo_especifico.setFrame(True)
        self.line_campo_especifico.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbo_institucion = QComboBox(self.scroll_registro_estudiante)
        self.cbo_institucion.setObjectName(u"cbo_institucion")
        self.cbo_institucion.setGeometry(QRect(450, 154, 341, 40))
        self.lbl9_2 = QLabel(self.scroll_registro_estudiante)
        self.lbl9_2.setObjectName(u"lbl9_2")
        self.lbl9_2.setGeometry(QRect(450, 130, 221, 21))
        self.lbl9_2.setStyleSheet(u"")
        self.lbl9_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_97 = QLabel(self.scroll_registro_estudiante)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(18, 41, 161, 31))
        self.date_fecha_inicio = QDateEdit(self.scroll_registro_estudiante)
        self.date_fecha_inicio.setObjectName(u"date_fecha_inicio")
        self.date_fecha_inicio.setGeometry(QRect(18, 70, 221, 40))
        self.date_fecha_inicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_fecha_inicio.setStyleSheet(u"")
        self.date_fecha_inicio.setCalendarPopup(True)
        self.datoscontacto = QLabel(self.scroll_registro_estudiante)
        self.datoscontacto.setObjectName(u"datoscontacto")
        self.datoscontacto.setGeometry(QRect(14, 320, 241, 21))
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
        self.datosacademicos = QLabel(self.scroll_registro_estudiante)
        self.datosacademicos.setObjectName(u"datosacademicos")
        self.datosacademicos.setGeometry(QRect(18, 430, 231, 21))
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
        self.lbl9_5.setGeometry(QRect(22, 560, 201, 21))
        self.lbl9_5.setStyleSheet(u"")
        self.lbl9_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_periodo_academico = QLineEdit(self.scroll_registro_estudiante)
        self.line_periodo_academico.setObjectName(u"line_periodo_academico")
        self.line_periodo_academico.setEnabled(True)
        self.line_periodo_academico.setGeometry(QRect(20, 150, 411, 40))
        self.line_periodo_academico.setStyleSheet(u"")
        self.line_periodo_academico.setMaxLength(30)
        self.line_periodo_academico.setFrame(True)
        self.line_periodo_academico.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11_8 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_8.setObjectName(u"lbl11_8")
        self.lbl11_8.setGeometry(QRect(20, 124, 171, 21))
        self.lbl11_8.setStyleSheet(u"")
        self.lbl11_8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbo_proyecto = QComboBox(self.scroll_registro_estudiante)
        self.cbo_proyecto.setObjectName(u"cbo_proyecto")
        self.cbo_proyecto.setGeometry(QRect(18, 350, 771, 40))
        self.line_buscar_estudiante = QLineEdit(self.scroll_registro_estudiante)
        self.line_buscar_estudiante.setObjectName(u"line_buscar_estudiante")
        self.line_buscar_estudiante.setEnabled(True)
        self.line_buscar_estudiante.setGeometry(QRect(22, 490, 241, 40))
        self.line_buscar_estudiante.setStyleSheet(u"")
        self.line_buscar_estudiante.setMaxLength(30)
        self.line_buscar_estudiante.setFrame(True)
        self.line_buscar_estudiante.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11_3 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_3.setObjectName(u"lbl11_3")
        self.lbl11_3.setGeometry(QRect(22, 465, 171, 21))
        self.lbl11_3.setStyleSheet(u"")
        self.lbl11_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_nombre_seleccionado = QLineEdit(self.scroll_registro_estudiante)
        self.line_nombre_seleccionado.setObjectName(u"line_nombre_seleccionado")
        self.line_nombre_seleccionado.setEnabled(False)
        self.line_nombre_seleccionado.setGeometry(QRect(280, 490, 321, 40))
        self.line_nombre_seleccionado.setStyleSheet(u"")
        self.line_nombre_seleccionado.setMaxLength(30)
        self.line_nombre_seleccionado.setFrame(True)
        self.line_nombre_seleccionado.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11_4 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_4.setObjectName(u"lbl11_4")
        self.lbl11_4.setGeometry(QRect(280, 465, 201, 21))
        self.lbl11_4.setStyleSheet(u"")
        self.lbl11_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_cedula_seleccionado = QLineEdit(self.scroll_registro_estudiante)
        self.line_cedula_seleccionado.setObjectName(u"line_cedula_seleccionado")
        self.line_cedula_seleccionado.setEnabled(False)
        self.line_cedula_seleccionado.setGeometry(QRect(620, 490, 171, 40))
        self.line_cedula_seleccionado.setStyleSheet(u"")
        self.line_cedula_seleccionado.setMaxLength(30)
        self.line_cedula_seleccionado.setFrame(True)
        self.line_cedula_seleccionado.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11_9 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_9.setObjectName(u"lbl11_9")
        self.lbl11_9.setGeometry(QRect(620, 465, 171, 21))
        self.lbl11_9.setStyleSheet(u"")
        self.lbl11_9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.date_fecha_final = QDateEdit(self.scroll_registro_estudiante)
        self.date_fecha_final.setObjectName(u"date_fecha_final")
        self.date_fecha_final.setGeometry(QRect(22, 590, 241, 40))
        self.date_fecha_final.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_fecha_final.setStyleSheet(u"")
        self.date_fecha_final.setCalendarPopup(True)
        self.cbo_estado_vinculacion = QComboBox(self.scroll_registro_estudiante)
        self.cbo_estado_vinculacion.addItem("")
        self.cbo_estado_vinculacion.addItem("")
        self.cbo_estado_vinculacion.addItem("")
        self.cbo_estado_vinculacion.setObjectName(u"cbo_estado_vinculacion")
        self.cbo_estado_vinculacion.setGeometry(QRect(280, 590, 161, 40))
        self.lbl9_3 = QLabel(self.scroll_registro_estudiante)
        self.lbl9_3.setObjectName(u"lbl9_3")
        self.lbl9_3.setGeometry(QRect(280, 564, 221, 21))
        self.lbl9_3.setStyleSheet(u"")
        self.lbl9_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_horas = QLineEdit(self.scroll_registro_estudiante)
        self.line_horas.setObjectName(u"line_horas")
        self.line_horas.setEnabled(True)
        self.line_horas.setGeometry(QRect(460, 590, 141, 40))
        self.line_horas.setStyleSheet(u"")
        self.line_horas.setMaxLength(30)
        self.line_horas.setFrame(True)
        self.line_horas.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11_10 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_10.setObjectName(u"lbl11_10")
        self.lbl11_10.setGeometry(QRect(460, 564, 171, 21))
        self.lbl11_10.setStyleSheet(u"")
        self.lbl11_10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btn_agregar_estu_seleccionado = QPushButton(self.scroll_registro_estudiante)
        self.btn_agregar_estu_seleccionado.setObjectName(u"btn_agregar_estu_seleccionado")
        self.btn_agregar_estu_seleccionado.setGeometry(QRect(620, 590, 120, 40))
        self.btn_agregar_estu_seleccionado.setMinimumSize(QSize(120, 40))
        self.btn_agregar_estu_seleccionado.setMaximumSize(QSize(120, 40))
        self.btn_agregar_estu_seleccionado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_estu_seleccionado.setFocusPolicy(Qt.NoFocus)
        self.btn_agregar_estu_seleccionado.setStyleSheet(u"/* Bot\u00f3n Cancelar */\n"
"QPushButton#btn_agregar_estu_seleccionado {\n"
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
"    transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease; \n"
"}\n"
"\n"
"QPushButton#btn_agregar_estu_seleccionado:hover {\n"
"    background: rgba(63, 87, 88, 0.1); /* Fondo ligeramente oscuro en hover */\n"
"    color: #2e4546; \n"
"    border: 2px solid #2e4546;\n"
"}\n"
"\n"
"QPushButton#btn_agregar_estu_seleccionado:pressed {\n"
"    background: rgba(63, 87, 88, 0.2); /* Fondo m\u00e1s oscuro en estado presionado */\n"
"    color: #1c2d2e; \n"
"    border: 2px solid #1c2d2e;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar_estu_seleccionado.setIcon(icon1)
        self.btn_agregar_estu_seleccionado.setIconSize(QSize(15, 21))
        self.tabla_estudiante_seleccionado = QTableWidget(self.scroll_registro_estudiante)
        if (self.tabla_estudiante_seleccionado.columnCount() < 5):
            self.tabla_estudiante_seleccionado.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_estudiante_seleccionado.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_estudiante_seleccionado.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_estudiante_seleccionado.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_estudiante_seleccionado.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_estudiante_seleccionado.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla_estudiante_seleccionado.setObjectName(u"tabla_estudiante_seleccionado")
        self.tabla_estudiante_seleccionado.setGeometry(QRect(19, 680, 761, 251))
        self.tabla_estudiante_seleccionado.setStyleSheet(u"QTableWidget {\n"
"outline: 0px;\n"
"border:5px solid #f3f4f6;\n"
"border-radius:15px;\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 19px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;\n"
"}\n"
"\n"
"\n"
"/* cabezera*/\n"
"QHeaderView::section {\n"
"background-color:#f1f2f3;\n"
"border-style: none;\n"
"height:40px;\n"
"font-family: \"Roboto\";\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"text-transform: uppercase;\n"
"color: #212529;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget::disabled{\n"
"    background-color:#acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;}\n"
"\n"
"/*bordes internos*/\n"
"QTab"
                        "leWidget::item {\n"
"	border-bottom: 3px solid #f3f4f6;\n"
"\n"
"}\n"
"\n"
"QTableWidget:item:selected{\n"
"	background:white;/*color-seleccion*/\n"
"color: #2c3d3e;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tabla_estudiante_seleccionado.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_estudiante_seleccionado.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_estudiante_seleccionado.setShowGrid(False)
        self.tabla_estudiante_seleccionado.setSortingEnabled(False)
        self.tabla_estudiante_seleccionado.setWordWrap(True)
        self.tabla_estudiante_seleccionado.setCornerButtonEnabled(True)
        self.tabla_estudiante_seleccionado.horizontalHeader().setVisible(True)
        self.tabla_estudiante_seleccionado.horizontalHeader().setDefaultSectionSize(133)
        self.tabla_estudiante_seleccionado.horizontalHeader().setHighlightSections(True)
        self.tabla_estudiante_seleccionado.verticalHeader().setVisible(False)
        self.tabla_estudiante_seleccionado.verticalHeader().setDefaultSectionSize(40)
        self.tabla_estudiante_seleccionado.verticalHeader().setHighlightSections(True)
        self.lbl9_6 = QLabel(self.scroll_registro_estudiante)
        self.lbl9_6.setObjectName(u"lbl9_6")
        self.lbl9_6.setGeometry(QRect(20, 650, 241, 21))
        self.lbl9_6.setStyleSheet(u"font: 11pt \"Roboto\";")
        self.lbl9_6.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.datosTutor = QLabel(self.scroll_registro_estudiante)
        self.datosTutor.setObjectName(u"datosTutor")
        self.datosTutor.setGeometry(QRect(14, 220, 241, 21))
        self.datosTutor.setStyleSheet(u"#datosTutor\n"
" {\n"
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
        self.cbo_tutor = QComboBox(self.scroll_registro_estudiante)
        self.cbo_tutor.setObjectName(u"cbo_tutor")
        self.cbo_tutor.setGeometry(QRect(20, 250, 401, 40))
        self.errorCodigoies = QLabel(self.scroll_registro_estudiante)
        self.errorCodigoies.setObjectName(u"errorCodigoies")
        self.errorCodigoies.setGeometry(QRect(264, 113, 211, 16))
        self.errorCampoEspecifico = QLabel(self.scroll_registro_estudiante)
        self.errorCampoEspecifico.setObjectName(u"errorCampoEspecifico")
        self.errorCampoEspecifico.setGeometry(QRect(500, 110, 281, 16))
        self.errorCampoPeriodo = QLabel(self.scroll_registro_estudiante)
        self.errorCampoPeriodo.setObjectName(u"errorCampoPeriodo")
        self.errorCampoPeriodo.setGeometry(QRect(20, 190, 411, 16))
        self.errorEstudianteNoEncontrado = QLabel(self.scroll_registro_estudiante)
        self.errorEstudianteNoEncontrado.setObjectName(u"errorEstudianteNoEncontrado")
        self.errorEstudianteNoEncontrado.setGeometry(QRect(280, 530, 321, 16))
        self.errorBuscar = QLabel(self.scroll_registro_estudiante)
        self.errorBuscar.setObjectName(u"errorBuscar")
        self.errorBuscar.setGeometry(QRect(24, 530, 251, 16))
        self.id_estudiante_seleccionado = QLabel(self.scroll_registro_estudiante)
        self.id_estudiante_seleccionado.setObjectName(u"id_estudiante_seleccionado")
        self.id_estudiante_seleccionado.setGeometry(QRect(280, 450, 121, 16))
        self.errorInstitucion = QLabel(self.scroll_registro_estudiante)
        self.errorInstitucion.setObjectName(u"errorInstitucion")
        self.errorInstitucion.setGeometry(QRect(450, 195, 331, 16))
        self.errorTutor = QLabel(self.scroll_registro_estudiante)
        self.errorTutor.setObjectName(u"errorTutor")
        self.errorTutor.setGeometry(QRect(20, 290, 391, 16))
        self.errorProyecto = QLabel(self.scroll_registro_estudiante)
        self.errorProyecto.setObjectName(u"errorProyecto")
        self.errorProyecto.setGeometry(QRect(20, 390, 551, 16))
        self.scrollArea.setWidget(self.scroll_registro_estudiante)
        self.frame_pie_pagina = QFrame(self.frame)
        self.frame_pie_pagina.setObjectName(u"frame_pie_pagina")
        self.frame_pie_pagina.setGeometry(QRect(0, 501, 821, 51))
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
        self.frame_pie_pagina.setFrameShape(QFrame.StyledPanel)
        self.frame_pie_pagina.setFrameShadow(QFrame.Raised)
        self.btn_agregar_vinculacion = QPushButton(self.frame_pie_pagina)
        self.btn_agregar_vinculacion.setObjectName(u"btn_agregar_vinculacion")
        self.btn_agregar_vinculacion.setGeometry(QRect(610, 10, 180, 40))
        self.btn_agregar_vinculacion.setMinimumSize(QSize(180, 40))
        self.btn_agregar_vinculacion.setMaximumSize(QSize(110, 40))
        self.btn_agregar_vinculacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_vinculacion.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar_vinculacion.setIcon(icon2)
        self.btn_agregar_vinculacion.setIconSize(QSize(15, 21))
        self.cancelButton = QPushButton(self.frame_pie_pagina)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(480, 10, 120, 40))
        self.cancelButton.setMinimumSize(QSize(120, 40))
        self.cancelButton.setMaximumSize(QSize(120, 40))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setFocusPolicy(Qt.NoFocus)
        self.cancelButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/menu/no.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon3)
        self.cancelButton.setIconSize(QSize(15, 21))
        self.label_98 = QLabel(self.frame_pie_pagina)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(30, -50, 161, 31))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(FormularioVinculacion)

        QMetaObject.connectSlotsByName(FormularioVinculacion)
    # setupUi

    def retranslateUi(self, FormularioVinculacion):
        FormularioVinculacion.setWindowTitle(QCoreApplication.translate("FormularioVinculacion", u"Formulario Vinculacion", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("FormularioVinculacion", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.lbl_titulo_ventana.setText(QCoreApplication.translate("FormularioVinculacion", u"Registrar Nueva Vinculaci\u00f3n", None))
        self.datospersonales.setText(QCoreApplication.translate("FormularioVinculacion", u"Detalles de vinculaci\u00f3n", None))
        self.line_codigo_ies.setPlaceholderText(QCoreApplication.translate("FormularioVinculacion", u"Ingrese  codigo ies", None))
        self.lbl11.setText(QCoreApplication.translate("FormularioVinculacion", u"Codigo ies*", None))
        self.lbl11_2.setText(QCoreApplication.translate("FormularioVinculacion", u"Campo especifico", None))
        self.line_campo_especifico.setPlaceholderText(QCoreApplication.translate("FormularioVinculacion", u"Ingrese campo especi.. Ejem: 1-2A", None))
        self.lbl9_2.setText(QCoreApplication.translate("FormularioVinculacion", u"Instituci\u00f3n practica", None))
        self.label_97.setText(QCoreApplication.translate("FormularioVinculacion", u"Fecha Inicio", None))
        self.date_fecha_inicio.setDisplayFormat(QCoreApplication.translate("FormularioVinculacion", u"yyyy-MM-d", None))
        self.datoscontacto.setText(QCoreApplication.translate("FormularioVinculacion", u"Proyecto Asignado", None))
        self.datosacademicos.setText(QCoreApplication.translate("FormularioVinculacion", u"Estudiantes Asignados", None))
        self.lbl9_5.setText(QCoreApplication.translate("FormularioVinculacion", u"Fecha final vinculaci\u00f3n", None))
        self.line_periodo_academico.setText("")
        self.line_periodo_academico.setPlaceholderText(QCoreApplication.translate("FormularioVinculacion", u"Ingrese periodo academico Ejem: P1-2023, P2-2023", None))
        self.lbl11_8.setText(QCoreApplication.translate("FormularioVinculacion", u"Periodo academico", None))
        self.line_buscar_estudiante.setPlaceholderText(QCoreApplication.translate("FormularioVinculacion", u"filtrar cedula - nombre - apellidos", None))
        self.lbl11_3.setText(QCoreApplication.translate("FormularioVinculacion", u"Buscar estudiante", None))
        self.line_nombre_seleccionado.setPlaceholderText("")
        self.lbl11_4.setText(QCoreApplication.translate("FormularioVinculacion", u"Estudiante seleccionado", None))
        self.line_cedula_seleccionado.setPlaceholderText("")
        self.lbl11_9.setText(QCoreApplication.translate("FormularioVinculacion", u"Cedula estudiante", None))
        self.date_fecha_final.setDisplayFormat(QCoreApplication.translate("FormularioVinculacion", u"yyyy-MM-d", None))
        self.cbo_estado_vinculacion.setItemText(0, QCoreApplication.translate("FormularioVinculacion", u"Pendiente", None))
        self.cbo_estado_vinculacion.setItemText(1, QCoreApplication.translate("FormularioVinculacion", u"En Proceso", None))
        self.cbo_estado_vinculacion.setItemText(2, QCoreApplication.translate("FormularioVinculacion", u"Culminado", None))

        self.lbl9_3.setText(QCoreApplication.translate("FormularioVinculacion", u"Estado de vinculaci\u00f3n", None))
        self.line_horas.setText(QCoreApplication.translate("FormularioVinculacion", u"0", None))
        self.line_horas.setPlaceholderText("")
        self.lbl11_10.setText(QCoreApplication.translate("FormularioVinculacion", u"N\u00b0 Horas", None))
        self.btn_agregar_estu_seleccionado.setText(QCoreApplication.translate("FormularioVinculacion", u"Agregar", None))
        ___qtablewidgetitem = self.tabla_estudiante_seleccionado.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormularioVinculacion", u"Id", None));
        ___qtablewidgetitem1 = self.tabla_estudiante_seleccionado.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormularioVinculacion", u"Cedula", None));
        ___qtablewidgetitem2 = self.tabla_estudiante_seleccionado.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormularioVinculacion", u"Estudiante", None));
        ___qtablewidgetitem3 = self.tabla_estudiante_seleccionado.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormularioVinculacion", u"Estado Vin.", None));
        ___qtablewidgetitem4 = self.tabla_estudiante_seleccionado.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormularioVinculacion", u"Accion", None));
        self.lbl9_6.setText(QCoreApplication.translate("FormularioVinculacion", u"Lista de estudiantes asignados", None))
        self.datosTutor.setText(QCoreApplication.translate("FormularioVinculacion", u"Tutor Asignado", None))
        self.errorCodigoies.setText("")
        self.errorCampoEspecifico.setText("")
        self.errorCampoPeriodo.setText("")
        self.errorEstudianteNoEncontrado.setText("")
        self.errorBuscar.setText("")
        self.id_estudiante_seleccionado.setText(QCoreApplication.translate("FormularioVinculacion", u"TextLabel", None))
        self.errorInstitucion.setText("")
        self.errorTutor.setText("")
        self.errorProyecto.setText("")
        self.btn_agregar_vinculacion.setText(QCoreApplication.translate("FormularioVinculacion", u"Guardar vinculaci\u00f3n", None))
        self.cancelButton.setText(QCoreApplication.translate("FormularioVinculacion", u"Cancelar", None))
        self.label_98.setText(QCoreApplication.translate("FormularioVinculacion", u"Fecha Nacimiento", None))
    # retranslateUi

