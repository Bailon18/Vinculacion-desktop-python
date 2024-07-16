# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario_seguimiento_estudiantemcekuS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_FormularioSeguimientoEstudiante(object):
    def setupUi(self, FormularioSeguimientoEstudiante):
        if not FormularioSeguimientoEstudiante.objectName():
            FormularioSeguimientoEstudiante.setObjectName(u"FormularioSeguimientoEstudiante")
        FormularioSeguimientoEstudiante.resize(510, 557)
        FormularioSeguimientoEstudiante.setMinimumSize(QSize(510, 557))
        FormularioSeguimientoEstudiante.setMaximumSize(QSize(510, 557))
        self.gridLayout = QGridLayout(FormularioSeguimientoEstudiante)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormularioSeguimientoEstudiante)
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
        self.scrollArea.setGeometry(QRect(0, 50, 511, 461))
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
"\n"
"\n"
"/* QLabel para Mostrar Error */\n"
"QLabel#errorHora, #errorListActividades, #errorEvidencias{\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    color: #D32F2F; \n"
"}\n"
"\n"
"/*SPINBOX*/\n"
"QSpinBox{\n"
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
"QSpinBox::up-button {\n"
"min-width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QSpinBox::down-button {\n"
"min-width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QSpinBox::up-arrow{\n"
"	image: url(:/menu/contraerarriba.png);\n"
"     width: 9px;\n"
"     height: 9px;\n"
"}\n"
"\n"
"QSpinBox"
                        "::down-arrow{\n"
" image: url(:/menu/contraerabajo.png);\n"
"     width: 9px;\n"
"     height: 9px;}\n"
"\n"
"QSpinBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #3a4f50;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
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
"border: 2px solid #3a4f50;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scroll_registro_estudiante = QWidget()
        self.scroll_registro_estudiante.setObjectName(u"scroll_registro_estudiante")
        self.scroll_registro_estudiante.setGeometry(QRect(0, 0, 494, 800))
        self.scroll_registro_estudiante.setMinimumSize(QSize(0, 800))
        self.scroll_registro_estudiante.setStyleSheet(u"#scroll_registro_estudiante{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"")
        self.datospersonales = QLabel(self.scroll_registro_estudiante)
        self.datospersonales.setObjectName(u"datospersonales")
        self.datospersonales.setGeometry(QRect(7, 20, 261, 21))
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
        self.label_97 = QLabel(self.scroll_registro_estudiante)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(10, 61, 161, 31))
        self.fecha_actividad = QDateEdit(self.scroll_registro_estudiante)
        self.fecha_actividad.setObjectName(u"fecha_actividad")
        self.fecha_actividad.setGeometry(QRect(10, 90, 221, 40))
        self.fecha_actividad.setCursor(QCursor(Qt.PointingHandCursor))
        self.fecha_actividad.setStyleSheet(u"")
        self.fecha_actividad.setCalendarPopup(True)
        self.datosacademicos = QLabel(self.scroll_registro_estudiante)
        self.datosacademicos.setObjectName(u"datosacademicos")
        self.datosacademicos.setGeometry(QRect(4, 500, 351, 21))
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
        self.horas_spinx = QSpinBox(self.scroll_registro_estudiante)
        self.horas_spinx.setObjectName(u"horas_spinx")
        self.horas_spinx.setGeometry(QRect(270, 90, 211, 41))
        self.horas_spinx.setMaximum(96)
        self.label_98 = QLabel(self.scroll_registro_estudiante)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(280, 60, 181, 31))
        self.actividades_plain = QPlainTextEdit(self.scroll_registro_estudiante)
        self.actividades_plain.setObjectName(u"actividades_plain")
        self.actividades_plain.setGeometry(QRect(10, 190, 471, 261))
        self.btn_subir_fotos = QPushButton(self.scroll_registro_estudiante)
        self.btn_subir_fotos.setObjectName(u"btn_subir_fotos")
        self.btn_subir_fotos.setGeometry(QRect(10, 540, 221, 35))
        self.btn_subir_fotos.setStyleSheet(u"\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"	background-color: #baba00;\n"
"    border: none; \n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #d3d300; \n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background: #ecec00;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/menu/subir-imagen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_subir_fotos.setIcon(icon)
        self.btn_subir_fotos.setIconSize(QSize(19, 19))
        self.btn_subir_archivo = QPushButton(self.scroll_registro_estudiante)
        self.btn_subir_archivo.setObjectName(u"btn_subir_archivo")
        self.btn_subir_archivo.setGeometry(QRect(270, 540, 211, 35))
        self.btn_subir_archivo.setStyleSheet(u"\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"	background-color: #cf7c00;\n"
"    border: none; \n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #de8200; \n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background: #ff9500;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/menu/archivo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_subir_archivo.setIcon(icon1)
        self.btn_subir_archivo.setIconSize(QSize(19, 19))
        self.observacion_plain = QPlainTextEdit(self.scroll_registro_estudiante)
        self.observacion_plain.setObjectName(u"observacion_plain")
        self.observacion_plain.setGeometry(QRect(10, 660, 471, 101))
        self.datosacademicos_2 = QLabel(self.scroll_registro_estudiante)
        self.datosacademicos_2.setObjectName(u"datosacademicos_2")
        self.datosacademicos_2.setGeometry(QRect(10, 630, 271, 21))
        self.datosacademicos_2.setStyleSheet(u"#datosacademicos {\n"
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
        self.lbl_nombre_archivo_seleccionado = QLabel(self.scroll_registro_estudiante)
        self.lbl_nombre_archivo_seleccionado.setObjectName(u"lbl_nombre_archivo_seleccionado")
        self.lbl_nombre_archivo_seleccionado.setGeometry(QRect(10, 583, 171, 16))
        self.lbl_nombre_archivo_seleccionado.setStyleSheet(u"color:rgb(48, 165, 255);\n"
"font: italic 10pt \"Roboto\";")
        self.lbl_nombre_archivo_seleccionado_2 = QLabel(self.scroll_registro_estudiante)
        self.lbl_nombre_archivo_seleccionado_2.setObjectName(u"lbl_nombre_archivo_seleccionado_2")
        self.lbl_nombre_archivo_seleccionado_2.setGeometry(QRect(270, 580, 171, 16))
        self.lbl_nombre_archivo_seleccionado_2.setStyleSheet(u"color:rgb(48, 165, 255);\n"
"font: italic 10pt \"Roboto\";")
        self.label_99 = QLabel(self.scroll_registro_estudiante)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(10, 157, 221, 31))
        self.errorHora = QLabel(self.scroll_registro_estudiante)
        self.errorHora.setObjectName(u"errorHora")
        self.errorHora.setGeometry(QRect(272, 131, 211, 16))
        self.errorListActividades = QLabel(self.scroll_registro_estudiante)
        self.errorListActividades.setObjectName(u"errorListActividades")
        self.errorListActividades.setGeometry(QRect(12, 454, 461, 16))
        self.errorEvidencias = QLabel(self.scroll_registro_estudiante)
        self.errorEvidencias.setObjectName(u"errorEvidencias")
        self.errorEvidencias.setGeometry(QRect(10, 603, 461, 16))
        self.btn_descargar_foto = QPushButton(self.scroll_registro_estudiante)
        self.btn_descargar_foto.setObjectName(u"btn_descargar_foto")
        self.btn_descargar_foto.setGeometry(QRect(198, 577, 31, 31))
        icon2 = QIcon()
        icon2.addFile(u":/menu/descargar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_descargar_foto.setIcon(icon2)
        self.btn_descargar_foto.setIconSize(QSize(20, 20))
        self.btn_descargar_foto.setCheckable(False)
        self.btn_descargar_foto.setAutoRepeat(False)
        self.btn_descargar_foto.setAutoDefault(True)
        self.btn_descargar_foto.setFlat(False)
        self.btn_descargar_archivo = QPushButton(self.scroll_registro_estudiante)
        self.btn_descargar_archivo.setObjectName(u"btn_descargar_archivo")
        self.btn_descargar_archivo.setGeometry(QRect(450, 577, 31, 31))
        self.btn_descargar_archivo.setIcon(icon2)
        self.btn_descargar_archivo.setIconSize(QSize(20, 20))
        self.btn_descargar_archivo.setCheckable(False)
        self.btn_descargar_archivo.setAutoRepeat(False)
        self.btn_descargar_archivo.setAutoDefault(True)
        self.btn_descargar_archivo.setFlat(False)
        self.scrollArea.setWidget(self.scroll_registro_estudiante)
        self.frame_pie_pagina = QFrame(self.frame)
        self.frame_pie_pagina.setObjectName(u"frame_pie_pagina")
        self.frame_pie_pagina.setGeometry(QRect(0, 507, 501, 51))
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
"    b"
                        "order-radius: 8px; \n"
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
        self.horizontalLayout = QHBoxLayout(self.frame_pie_pagina)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(self.frame_pie_pagina)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(120, 40))
        self.cancelButton.setMaximumSize(QSize(120, 40))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setFocusPolicy(Qt.NoFocus)
        self.cancelButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/menu/no.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon3)
        self.cancelButton.setIconSize(QSize(15, 21))

        self.horizontalLayout.addWidget(self.cancelButton)

        self.btn_agregar_actividad = QPushButton(self.frame_pie_pagina)
        self.btn_agregar_actividad.setObjectName(u"btn_agregar_actividad")
        self.btn_agregar_actividad.setMinimumSize(QSize(180, 40))
        self.btn_agregar_actividad.setMaximumSize(QSize(110, 40))
        self.btn_agregar_actividad.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_actividad.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar_actividad.setIcon(icon4)
        self.btn_agregar_actividad.setIconSize(QSize(15, 21))

        self.horizontalLayout.addWidget(self.btn_agregar_actividad)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 511, 51))
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_closeedit = QToolButton(self.frame_2)
        self.btn_closeedit.setObjectName(u"btn_closeedit")
        self.btn_closeedit.setGeometry(QRect(480, 9, 25, 25))
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
        icon5 = QIcon()
        icon5.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeedit.setIcon(icon5)
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


        self.retranslateUi(FormularioSeguimientoEstudiante)

        self.btn_descargar_foto.setDefault(False)
        self.btn_descargar_archivo.setDefault(False)


        QMetaObject.connectSlotsByName(FormularioSeguimientoEstudiante)
    # setupUi

    def retranslateUi(self, FormularioSeguimientoEstudiante):
        FormularioSeguimientoEstudiante.setWindowTitle(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Formulario Estudiante", None))
        self.datospersonales.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Datos de  Actividad", None))
        self.label_97.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Fecha actividad", None))
        self.fecha_actividad.setDisplayFormat(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"yyyy-MM-d", None))
        self.datosacademicos.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Evidencia de actividad realizada", None))
        self.label_98.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Horas  actividad realizadas", None))
        self.btn_subir_fotos.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Subir fotos", None))
        self.btn_subir_archivo.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Subir archivo", None))
        self.datosacademicos_2.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Observaci\u00f3n ( opcional )", None))
        self.lbl_nombre_archivo_seleccionado.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"ningun archivo seleccionado", None))
        self.lbl_nombre_archivo_seleccionado_2.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"ningun archivo seleccionado", None))
        self.label_99.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Lista de actividades realizados", None))
        self.errorHora.setText("")
        self.errorListActividades.setText("")
        self.errorEvidencias.setText("")
#if QT_CONFIG(tooltip)
        self.btn_descargar_foto.setToolTip(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Descargar archivo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_descargar_foto.setText("")
#if QT_CONFIG(tooltip)
        self.btn_descargar_archivo.setToolTip(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Descargar archivo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_descargar_archivo.setText("")
        self.cancelButton.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Cancelar", None))
        self.btn_agregar_actividad.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Guardar actividad", None))
#if QT_CONFIG(tooltip)
        self.btn_closeedit.setToolTip(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeedit.setText("")
        self.lbl_titulo_ventana.setText(QCoreApplication.translate("FormularioSeguimientoEstudiante", u"Registrar Nuevo Actividad", None))
    # retranslateUi

