# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario_vinculacion_detalleBzGvoY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_FormularioVinculacionDetalle(object):
    def setupUi(self, FormularioVinculacionDetalle):
        if not FormularioVinculacionDetalle.objectName():
            FormularioVinculacionDetalle.setObjectName(u"FormularioVinculacionDetalle")
        FormularioVinculacionDetalle.resize(820, 557)
        FormularioVinculacionDetalle.setMinimumSize(QSize(486, 557))
        FormularioVinculacionDetalle.setMaximumSize(QSize(840, 557))
        self.gridLayout = QGridLayout(FormularioVinculacionDetalle)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormularioVinculacionDetalle)
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
        self.scrollArea.setStyleSheet(u"/* Estilo para el t\u00edtulo de secci\u00f3n (Detalle vinculacion) */\n"
"QLabel#datospersonales {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: #344647;\n"
"}\n"
"\n"
"/* Estilo para el subt\u00edtulo del detalle (Nombre) */\n"
"QLabel#titulo_fecha,#titulo_codigo_ies, #titulo_campo_especifico,\n"
" #titulo_periodo_academico, #titulo_institucion,\n"
" #titulo_nombres_tutor, #titulo_cedula_tutor, #titulo_telefono_tutor, #titulo_correo_tutor, #titulo_nombre_proyecto {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: 500;\n"
"    font-size: 15px;\n"
"    color: #6B7280;\n"
"}\n"
"\n"
"/* Estilo para el detalle (Bailon paucar montes) */\n"
"QLabel#date_fecha_inicio, #line_codigo_ies, #line_campo_especifico, #line_periodo_academico, #cbo_institucion,\n"
"#line_nombres_tutor, #line_cedula_tutor, #line_telefono_tutor, #line_correo_tutor, #line_nombre_proyecto {\n"
"    font-family: Roboto;\n"
"    font-style: n"
                        "ormal;\n"
"    font-weight: normal;\n"
"    font-size: 13px;\n"
"    color: #9CA3AF;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_registro_estudiante = QWidget()
        self.scroll_registro_estudiante.setObjectName(u"scroll_registro_estudiante")
        self.scroll_registro_estudiante.setGeometry(QRect(0, -173, 802, 900))
        self.scroll_registro_estudiante.setMinimumSize(QSize(0, 900))
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
        self.titulo_codigo_ies = QLabel(self.scroll_registro_estudiante)
        self.titulo_codigo_ies.setObjectName(u"titulo_codigo_ies")
        self.titulo_codigo_ies.setGeometry(QRect(190, 48, 171, 21))
        self.titulo_codigo_ies.setStyleSheet(u"")
        self.titulo_codigo_ies.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.titulo_campo_especifico = QLabel(self.scroll_registro_estudiante)
        self.titulo_campo_especifico.setObjectName(u"titulo_campo_especifico")
        self.titulo_campo_especifico.setGeometry(QRect(350, 48, 171, 21))
        self.titulo_campo_especifico.setStyleSheet(u"")
        self.titulo_campo_especifico.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.titulo_institucion = QLabel(self.scroll_registro_estudiante)
        self.titulo_institucion.setObjectName(u"titulo_institucion")
        self.titulo_institucion.setGeometry(QRect(20, 120, 221, 21))
        self.titulo_institucion.setStyleSheet(u"")
        self.titulo_institucion.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.titulo_fecha = QLabel(self.scroll_registro_estudiante)
        self.titulo_fecha.setObjectName(u"titulo_fecha")
        self.titulo_fecha.setGeometry(QRect(18, 48, 161, 21))
        self.datoscontacto = QLabel(self.scroll_registro_estudiante)
        self.datoscontacto.setObjectName(u"datoscontacto")
        self.datoscontacto.setGeometry(QRect(14, 390, 241, 21))
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
        self.datosacademicos.setGeometry(QRect(16, 500, 281, 21))
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
        self.titulo_periodo_academico = QLabel(self.scroll_registro_estudiante)
        self.titulo_periodo_academico.setObjectName(u"titulo_periodo_academico")
        self.titulo_periodo_academico.setGeometry(QRect(590, 48, 171, 21))
        self.titulo_periodo_academico.setStyleSheet(u"")
        self.titulo_periodo_academico.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
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
        self.tabla_estudiante_seleccionado.setGeometry(QRect(20, 550, 761, 301))
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
        self.datosTutor = QLabel(self.scroll_registro_estudiante)
        self.datosTutor.setObjectName(u"datosTutor")
        self.datosTutor.setGeometry(QRect(14, 190, 241, 21))
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
        self.date_fecha_inicio = QLabel(self.scroll_registro_estudiante)
        self.date_fecha_inicio.setObjectName(u"date_fecha_inicio")
        self.date_fecha_inicio.setGeometry(QRect(20, 76, 161, 16))
        self.line_codigo_ies = QLabel(self.scroll_registro_estudiante)
        self.line_codigo_ies.setObjectName(u"line_codigo_ies")
        self.line_codigo_ies.setGeometry(QRect(190, 76, 151, 16))
        self.line_campo_especifico = QLabel(self.scroll_registro_estudiante)
        self.line_campo_especifico.setObjectName(u"line_campo_especifico")
        self.line_campo_especifico.setGeometry(QRect(350, 76, 211, 16))
        self.line_periodo_academico = QLabel(self.scroll_registro_estudiante)
        self.line_periodo_academico.setObjectName(u"line_periodo_academico")
        self.line_periodo_academico.setGeometry(QRect(590, 76, 191, 16))
        self.cbo_institucion = QLabel(self.scroll_registro_estudiante)
        self.cbo_institucion.setObjectName(u"cbo_institucion")
        self.cbo_institucion.setGeometry(QRect(20, 149, 701, 16))
        self.line_telefono_tutor = QLabel(self.scroll_registro_estudiante)
        self.line_telefono_tutor.setObjectName(u"line_telefono_tutor")
        self.line_telefono_tutor.setGeometry(QRect(590, 258, 201, 20))
        self.titulo_nombres_tutor = QLabel(self.scroll_registro_estudiante)
        self.titulo_nombres_tutor.setObjectName(u"titulo_nombres_tutor")
        self.titulo_nombres_tutor.setGeometry(QRect(18, 230, 161, 21))
        self.line_cedula_tutor = QLabel(self.scroll_registro_estudiante)
        self.line_cedula_tutor.setObjectName(u"line_cedula_tutor")
        self.line_cedula_tutor.setGeometry(QRect(350, 258, 201, 16))
        self.line_nombres_tutor = QLabel(self.scroll_registro_estudiante)
        self.line_nombres_tutor.setObjectName(u"line_nombres_tutor")
        self.line_nombres_tutor.setGeometry(QRect(20, 258, 161, 16))
        self.titulo_cedula_tutor = QLabel(self.scroll_registro_estudiante)
        self.titulo_cedula_tutor.setObjectName(u"titulo_cedula_tutor")
        self.titulo_cedula_tutor.setGeometry(QRect(350, 230, 171, 21))
        self.titulo_cedula_tutor.setStyleSheet(u"")
        self.titulo_cedula_tutor.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.titulo_telefono_tutor = QLabel(self.scroll_registro_estudiante)
        self.titulo_telefono_tutor.setObjectName(u"titulo_telefono_tutor")
        self.titulo_telefono_tutor.setGeometry(QRect(590, 230, 171, 21))
        self.titulo_telefono_tutor.setStyleSheet(u"")
        self.titulo_telefono_tutor.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_correo_tutor = QLabel(self.scroll_registro_estudiante)
        self.line_correo_tutor.setObjectName(u"line_correo_tutor")
        self.line_correo_tutor.setGeometry(QRect(20, 330, 281, 16))
        self.titulo_correo_tutor = QLabel(self.scroll_registro_estudiante)
        self.titulo_correo_tutor.setObjectName(u"titulo_correo_tutor")
        self.titulo_correo_tutor.setGeometry(QRect(20, 300, 171, 21))
        self.titulo_correo_tutor.setStyleSheet(u"")
        self.titulo_correo_tutor.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btn_descargar = QPushButton(self.scroll_registro_estudiante)
        self.btn_descargar.setObjectName(u"btn_descargar")
        self.btn_descargar.setGeometry(QRect(350, 310, 151, 40))
        self.btn_descargar.setMinimumSize(QSize(74, 40))
        self.btn_descargar.setMaximumSize(QSize(242, 40))
        self.btn_descargar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_descargar.setStyleSheet(u"/* Bot\u00f3n Exportar a PDF */\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    background: #e06666; /* Rojo oscuro para exportar */\n"
"    border: none; \n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #b95454; /* Rojo m\u00e1s oscuro en hover */\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #803232; /* Rojo a\u00fan m\u00e1s oscuro en estado presionado */\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/exportar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_descargar.setIcon(icon1)
        self.btn_descargar.setIconSize(QSize(15, 21))
        self.titulo_nombre_proyecto = QLabel(self.scroll_registro_estudiante)
        self.titulo_nombre_proyecto.setObjectName(u"titulo_nombre_proyecto")
        self.titulo_nombre_proyecto.setGeometry(QRect(18, 432, 161, 21))
        self.line_nombre_proyecto = QLabel(self.scroll_registro_estudiante)
        self.line_nombre_proyecto.setObjectName(u"line_nombre_proyecto")
        self.line_nombre_proyecto.setGeometry(QRect(20, 460, 761, 16))
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
"\n"
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
""
                        "    border-radius: 8px; \n"
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
        self.label_98 = QLabel(self.frame_pie_pagina)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(30, -50, 161, 31))
        self.btn_exportar_detalle = QPushButton(self.frame_pie_pagina)
        self.btn_exportar_detalle.setObjectName(u"btn_exportar_detalle")
        self.btn_exportar_detalle.setGeometry(QRect(540, 10, 241, 40))
        self.btn_exportar_detalle.setMinimumSize(QSize(74, 40))
        self.btn_exportar_detalle.setMaximumSize(QSize(242, 40))
        self.btn_exportar_detalle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportar_detalle.setStyleSheet(u"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    background: #e06666;\n"
"    border: none; \n"
"    border-radius: 8px; \n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #b95454; \n"
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
"    border-radius: 8px; \n"
"\n"
"}\n"
"\n"
"QPushButton#cancelButton:hover {\n"
"    background: rgba(63, 87, 88, 0.1); /* Fondo ligeramente oscuro en h"
                        "over */\n"
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
        self.btn_exportar_detalle.setIcon(icon1)
        self.btn_exportar_detalle.setIconSize(QSize(15, 21))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(FormularioVinculacionDetalle)

        QMetaObject.connectSlotsByName(FormularioVinculacionDetalle)
    # setupUi

    def retranslateUi(self, FormularioVinculacionDetalle):
        FormularioVinculacionDetalle.setWindowTitle(QCoreApplication.translate("FormularioVinculacionDetalle", u"Formulario Vinculacion", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("FormularioVinculacionDetalle", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.lbl_titulo_ventana.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Detalle vinculacion", None))
        self.datospersonales.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Detalles de vinculaci\u00f3n", None))
        self.titulo_codigo_ies.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Codigo Ies", None))
        self.titulo_campo_especifico.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Campo especifico", None))
        self.titulo_institucion.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Instituci\u00f3n practica", None))
        self.titulo_fecha.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Fecha Inicio", None))
        self.datoscontacto.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Detalle Proyecto Asignado", None))
        self.datosacademicos.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Lista de estudiantes asignados", None))
        self.titulo_periodo_academico.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Periodo academico", None))
        ___qtablewidgetitem = self.tabla_estudiante_seleccionado.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Id", None));
        ___qtablewidgetitem1 = self.tabla_estudiante_seleccionado.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Cedula", None));
        ___qtablewidgetitem2 = self.tabla_estudiante_seleccionado.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Estudiante", None));
        ___qtablewidgetitem3 = self.tabla_estudiante_seleccionado.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Estado Vin.", None));
        ___qtablewidgetitem4 = self.tabla_estudiante_seleccionado.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Nro horas", None));
        self.datosTutor.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Detalle tutor asignado", None))
        self.date_fecha_inicio.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.line_codigo_ies.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.line_campo_especifico.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.line_periodo_academico.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.cbo_institucion.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.line_telefono_tutor.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.titulo_nombres_tutor.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Nombre y apellidos", None))
        self.line_cedula_tutor.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.line_nombres_tutor.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.titulo_cedula_tutor.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Cedula", None))
        self.titulo_telefono_tutor.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Tel\u00e9fono", None))
        self.line_correo_tutor.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.titulo_correo_tutor.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Correo", None))
        self.btn_descargar.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Descargar cv", None))
        self.titulo_nombre_proyecto.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Nombre proyecto", None))
        self.line_nombre_proyecto.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"TextLabel", None))
        self.label_98.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Fecha Nacimiento", None))
        self.btn_exportar_detalle.setText(QCoreApplication.translate("FormularioVinculacionDetalle", u"Exportar detalle vinculaci\u00f3n", None))
    # retranslateUi

