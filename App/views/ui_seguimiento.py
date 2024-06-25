# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seguimientoWfdIkV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_FormularioSeguimiento(object):
    def setupUi(self, FormularioSeguimiento):
        if not FormularioSeguimiento.objectName():
            FormularioSeguimiento.setObjectName(u"FormularioSeguimiento")
        FormularioSeguimiento.resize(620, 620)
        FormularioSeguimiento.setMinimumSize(QSize(620, 620))
        FormularioSeguimiento.setMaximumSize(QSize(620, 620))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        FormularioSeguimiento.setWindowIcon(icon)
        FormularioSeguimiento.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(FormularioSeguimiento)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormularioSeguimiento)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"frame{\n"
"background-color:#f1f1f1;\n"
"border-bottom-right-radius: 10;\n"
"border-bottom-left-radius: 10;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stack_principal = QStackedWidget(self.frame)
        self.stack_principal.setObjectName(u"stack_principal")
        self.stack_principal.setStyleSheet(u"\n"
"stack_principal{\n"
"	background-color:#f1f1f1;\n"
"}\n"
"\n"
"QLabel{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 450;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;}\n"
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
""
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
"QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::dow"
                        "n-button {\n"
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
"    border-bottom: 1px solid #E2E3E4;\n"
"}\n"
"\n"
"")
        self.stack_principal.setFrameShape(QFrame.NoFrame)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"#page_2{background-color: #ffffff;\n"
"border-bottom-right-radius: 10;\n"
"border-bottom-left-radius: 10;}\n"
"\n"
"")
        self.label_39 = QLabel(self.page_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(20, 160, 311, 31))
        self.label_39.setStyleSheet(u"QLabel {\n"
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
        self.frame_17 = QFrame(self.page_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(10, 200, 601, 301))
        self.frame_17.setStyleSheet(u"#frame_17{\n"
" border:8px solid white;\n"
"border-radius:18px\n"
"}")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_17)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.tabla_listado_actividades = QTableWidget(self.frame_17)
        if (self.tabla_listado_actividades.columnCount() < 4):
            self.tabla_listado_actividades.setColumnCount(4)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setForeground(brush);
        self.tabla_listado_actividades.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_listado_actividades.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_listado_actividades.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_listado_actividades.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tabla_listado_actividades.rowCount() < 3):
            self.tabla_listado_actividades.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_listado_actividades.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_listado_actividades.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_listado_actividades.setVerticalHeaderItem(2, __qtablewidgetitem6)
        self.tabla_listado_actividades.setObjectName(u"tabla_listado_actividades")
        self.tabla_listado_actividades.setStyleSheet(u"/* Estilo Base del QTableWidget */\n"
"QTableWidget {\n"
"    outline: 0px;\n"
"    border: 5px solid #f3f4f6;\n"
"    border-radius: 15px;\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    line-height: 19px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #6B7280;\n"
"    gridline-color: #e0e0e0; /* Color de las l\u00edneas de la cuadr\u00edcula */\n"
"}\n"
"\n"
"/* Estilo de las Celdas */\n"
"QTableWidget::item {\n"
"    border-bottom: 3px solid #f3f4f6;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Estilo de las Celdas Seleccionadas */\n"
"QTableWidget::item:selected {\n"
"    background: #465e5f; /* Fondo m\u00e1s claro para la celda seleccionada */\n"
"    color: #ffffff; /* Color de texto claro para las celdas seleccionadas */\n"
"}\n"
"\n"
"/* Estilo de las Celdas Deshabilitadas */\n"
"QTableWidget::disabled {\n"
"    background-color: #acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"}\n"
""
                        "\n"
"/* Estilo de las Secciones de la Cabecera */\n"
"QHeaderView::section {\n"
"    background-color: #f1f2f3;\n"
"    border-style: none;\n"
"    height: 40px;\n"
"    font-family: \"Roboto\";\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"}\n"
"\n"
"/* Estilo de las Secciones Horizontales de la Cabecera */\n"
"QHeaderView::section:horizontal {\n"
"    font-size: 14px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"   text-transform: uppercase; /* Convertir texto a may\u00fasculas */;\n"
"    color: #212529;\n"
"    border-bottom: 2px solid #e0e0e0; /* Separador inferior */\n"
"}\n"
"\n"
"")
        self.tabla_listado_actividades.setFrameShape(QFrame.NoFrame)
        self.tabla_listado_actividades.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_listado_actividades.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_listado_actividades.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_listado_actividades.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_listado_actividades.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_listado_actividades.setShowGrid(False)
        self.tabla_listado_actividades.setSortingEnabled(False)
        self.tabla_listado_actividades.horizontalHeader().setMinimumSectionSize(39)
        self.tabla_listado_actividades.horizontalHeader().setHighlightSections(False)
        self.tabla_listado_actividades.verticalHeader().setVisible(False)
        self.tabla_listado_actividades.verticalHeader().setMinimumSectionSize(23)
        self.tabla_listado_actividades.verticalHeader().setDefaultSectionSize(50)

        self.gridLayout_30.addWidget(self.tabla_listado_actividades, 0, 0, 1, 1)

        self.btn_nuevo_seguimiento = QPushButton(self.page_2)
        self.btn_nuevo_seguimiento.setObjectName(u"btn_nuevo_seguimiento")
        self.btn_nuevo_seguimiento.setGeometry(QRect(420, 90, 181, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_nuevo_seguimiento.sizePolicy().hasHeightForWidth())
        self.btn_nuevo_seguimiento.setSizePolicy(sizePolicy)
        self.btn_nuevo_seguimiento.setSizeIncrement(QSize(0, 0))
        self.btn_nuevo_seguimiento.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nuevo_seguimiento.setFocusPolicy(Qt.NoFocus)
        self.btn_nuevo_seguimiento.setAutoFillBackground(False)
        self.btn_nuevo_seguimiento.setStyleSheet(u"\n"
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
"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nuevo_seguimiento.setIcon(icon1)
        self.btn_nuevo_seguimiento.setIconSize(QSize(12, 38))
        self.btn_nuevo_seguimiento.setCheckable(False)
        self.btn_nuevo_seguimiento.setAutoRepeat(False)
        self.btn_nuevo_seguimiento.setAutoExclusive(False)
        self.btn_nuevo_seguimiento.setAutoDefault(False)
        self.btn_nuevo_seguimiento.setFlat(False)
        self.fecha_inicio_seguimiento = QDateEdit(self.page_2)
        self.fecha_inicio_seguimiento.setObjectName(u"fecha_inicio_seguimiento")
        self.fecha_inicio_seguimiento.setGeometry(QRect(20, 90, 165, 40))
        self.fecha_inicio_seguimiento.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.fecha_inicio_seguimiento.setCalendarPopup(True)
        self.fecha_final_seguimiento = QDateEdit(self.page_2)
        self.fecha_final_seguimiento.setObjectName(u"fecha_final_seguimiento")
        self.fecha_final_seguimiento.setGeometry(QRect(210, 90, 165, 40))
        self.fecha_final_seguimiento.setCalendarPopup(True)
        self.fecha_final_seguimiento.setCurrentSectionIndex(0)
        self.label_99 = QLabel(self.page_2)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(20, 60, 161, 31))
        self.label_100 = QLabel(self.page_2)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(210, 60, 161, 31))
        self.label_41 = QLabel(self.page_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(20, 20, 241, 31))
        self.label_41.setStyleSheet(u"QLabel{\n"
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
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 510, 591, 61))
        self.frame_2.setStyleSheet(u"/* Estilo de la Etiqueta */\n"
"QLabel {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"    margin-top: 20px; /* Incrementamos el margen superior para m\u00e1s espacio */\n"
"}\n"
"\n"
"/* Estilo Base del Bot\u00f3n de la Paginaci\u00f3n */\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 10px 20px; /* Incrementamos el padding para un mejor tama\u00f1o de bot\u00f3n */\n"
"    background: #3f5758;\n"
"    border: none; /* Eliminamos el borde por defecto */\n"
"    border-radius: 8px; /* Ajustamos el border-radius */\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Pasar el Rat\u00f3n (Hover) */\n"
"QPushButton:hover {\n"
"    background: #4a6b6c; /* Color de fondo m\u00e1s claro */\n"
"    border-r"
                        "adius: 8px;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Hacer Clic (Pressed) */\n"
"QPushButton:pressed {\n"
"    background: #2e4546; /* Color de fondo m\u00e1s oscuro */\n"
"    border-radius: 8px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_pag_desp_seguimiento = QPushButton(self.frame_2)
        self.btn_pag_desp_seguimiento.setObjectName(u"btn_pag_desp_seguimiento")
        self.btn_pag_desp_seguimiento.setGeometry(QRect(521, 11, 59, 29))
        self.btn_pag_desp_seguimiento.setMinimumSize(QSize(59, 29))
        self.btn_pag_desp_seguimiento.setMaximumSize(QSize(110, 20))
        self.btn_pag_desp_seguimiento.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_desp_seguimiento.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/menu/hacia-adelante.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pag_desp_seguimiento.setIcon(icon2)
        self.btn_pag_desp_seguimiento.setIconSize(QSize(15, 21))
        self.btn_pag_antes_seguimiento = QPushButton(self.frame_2)
        self.btn_pag_antes_seguimiento.setObjectName(u"btn_pag_antes_seguimiento")
        self.btn_pag_antes_seguimiento.setGeometry(QRect(405, 11, 59, 29))
        self.btn_pag_antes_seguimiento.setMinimumSize(QSize(59, 29))
        self.btn_pag_antes_seguimiento.setMaximumSize(QSize(110, 20))
        self.btn_pag_antes_seguimiento.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_antes_seguimiento.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/menu/hacia-atras.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pag_antes_seguimiento.setIcon(icon3)
        self.btn_pag_antes_seguimiento.setIconSize(QSize(15, 21))
        self.lbl_pagina_seguimiento = QLabel(self.frame_2)
        self.lbl_pagina_seguimiento.setObjectName(u"lbl_pagina_seguimiento")
        self.lbl_pagina_seguimiento.setGeometry(QRect(470, 0, 45, 42))
        self.lbl_pagina_seguimiento.setMinimumSize(QSize(45, 0))
        self.lbl_pagina_seguimiento.setStyleSheet(u"")
        self.lbl_pagina_seguimiento.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stack_principal.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stack_principal, 1, 0, 1, 1)

        self.frame_19 = QFrame(self.frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 54))
        self.frame_19.setStyleSheet(u"#frame_19{background: #0B3A4C ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}\n"
"\n"
"#frame_19{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Plain)
        self.lbl_nombrepaciente = QLabel(self.frame_19)
        self.lbl_nombrepaciente.setObjectName(u"lbl_nombrepaciente")
        self.lbl_nombrepaciente.setGeometry(QRect(20, 4, 361, 23))
        self.lbl_nombrepaciente.setMinimumSize(QSize(0, 8))
        self.lbl_nombrepaciente.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")
        self.btn_close = QToolButton(self.frame_19)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(590, 10, 25, 25))
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
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)
        self.btn_close.setIconSize(QSize(13, 13))
        self.btn_close.setAutoRaise(True)
        self.lbl_nombreestudiante = QLabel(self.frame_19)
        self.lbl_nombreestudiante.setObjectName(u"lbl_nombreestudiante")
        self.lbl_nombreestudiante.setGeometry(QRect(20, 29, 491, 20))
        self.lbl_nombreestudiante.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")

        self.gridLayout.addWidget(self.frame_19, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(FormularioSeguimiento)

        self.stack_principal.setCurrentIndex(0)
        self.btn_nuevo_seguimiento.setDefault(False)


        QMetaObject.connectSlotsByName(FormularioSeguimiento)
    # setupUi

    def retranslateUi(self, FormularioSeguimiento):
        FormularioSeguimiento.setWindowTitle(QCoreApplication.translate("FormularioSeguimiento", u"Sesiones", None))
        self.label_39.setText(QCoreApplication.translate("FormularioSeguimiento", u"Lista de actividades realizadas", None))
        ___qtablewidgetitem = self.tabla_listado_actividades.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormularioSeguimiento", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_listado_actividades.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormularioSeguimiento", u"FECHA ACTIVIDAD", None));
        ___qtablewidgetitem2 = self.tabla_listado_actividades.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormularioSeguimiento", u"HORA ACTIVIDAD", None));
        ___qtablewidgetitem3 = self.tabla_listado_actividades.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormularioSeguimiento", u"ACCIONES", None));
        ___qtablewidgetitem4 = self.tabla_listado_actividades.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormularioSeguimiento", u"Nueva fila", None));
        ___qtablewidgetitem5 = self.tabla_listado_actividades.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormularioSeguimiento", u"Nueva fila", None));
        ___qtablewidgetitem6 = self.tabla_listado_actividades.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FormularioSeguimiento", u"Nueva fila", None));
        self.btn_nuevo_seguimiento.setText(QCoreApplication.translate("FormularioSeguimiento", u"Nuevo seguimiento", None))
        self.fecha_inicio_seguimiento.setDisplayFormat(QCoreApplication.translate("FormularioSeguimiento", u"yyyy-MM-d", None))
        self.fecha_final_seguimiento.setDisplayFormat(QCoreApplication.translate("FormularioSeguimiento", u"yyyy-MM-d", None))
        self.label_99.setText(QCoreApplication.translate("FormularioSeguimiento", u"Selecciona fecha inicio", None))
        self.label_100.setText(QCoreApplication.translate("FormularioSeguimiento", u"Selecciona fecha final", None))
        self.label_41.setText(QCoreApplication.translate("FormularioSeguimiento", u"Filtrar Actividades", None))
        self.btn_pag_desp_seguimiento.setText("")
        self.btn_pag_antes_seguimiento.setText("")
        self.lbl_pagina_seguimiento.setText(QCoreApplication.translate("FormularioSeguimiento", u"2000", None))
        self.lbl_nombrepaciente.setText(QCoreApplication.translate("FormularioSeguimiento", u"Seguimiento", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("FormularioSeguimiento", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.lbl_nombreestudiante.setText(QCoreApplication.translate("FormularioSeguimiento", u"Jose Mariano Martinez Jimenez", None))
    # retranslateUi

