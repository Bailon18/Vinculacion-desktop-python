# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entregaWYaOxs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_EntregaUi(object):
    def setupUi(self, EntregaUi):
        if not EntregaUi.objectName():
            EntregaUi.setObjectName(u"EntregaUi")
        EntregaUi.resize(331, 335)
        EntregaUi.setMinimumSize(QSize(331, 335))
        EntregaUi.setMaximumSize(QSize(331, 335))
        EntregaUi.setStyleSheet(u"#Dialog{\n"
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
"	image:"
                        " url(:/menu/contraerabajo.png);\n"
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
"	image: url(:/menu/contraerarriba.png);\n"
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow{\n"
"	image: url(:/menu/contraerabajo.png);\n"
"     width: 11px;\n"
"     height: 11px;}\n"
"\n"
"QDateEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-"
                        "radius: 8px;\n"
"}\n"
"\n"
"\n"
"/*  BOTON */\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #3A4F50;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #344647;\n"
"border-radius: 4px; }\n"
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
"")
        self.frame_3 = QFrame(EntregaUi)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 331, 55))
        self.frame_3.setMinimumSize(QSize(0, 55))
        self.frame_3.setMaximumSize(QSize(16777215, 4455))
        self.frame_3.setStyleSheet(u"#frame_3{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}\n"
"\n"
"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 16px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.titulo_accion = QLabel(self.frame_3)
        self.titulo_accion.setObjectName(u"titulo_accion")
        self.titulo_accion.setGeometry(QRect(20, 5, 241, 31))
        self.titulo_accion.setStyleSheet(u"\n"
"font: 87 14pt \"Roboto Black\";")
        self.titulo_accion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.nombre_tutor = QLabel(self.frame_3)
        self.nombre_tutor.setObjectName(u"nombre_tutor")
        self.nombre_tutor.setGeometry(QRect(20, 32, 271, 22))
        self.nombre_tutor.setStyleSheet(u"")
        self.nombre_tutor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_closeadmi_3 = QToolButton(self.frame_3)
        self.btn_closeadmi_3.setObjectName(u"btn_closeadmi_3")
        self.btn_closeadmi_3.setGeometry(QRect(300, 7, 25, 25))
        self.btn_closeadmi_3.setFocusPolicy(Qt.NoFocus)
        self.btn_closeadmi_3.setStyleSheet(u"#btn_closeadmi_3{\n"
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
"#btn_closeadmi_3:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeadmi_3.setIcon(icon)
        self.btn_closeadmi_3.setIconSize(QSize(13, 13))
        self.btn_closeadmi_3.setAutoRaise(True)
        self.frame = QFrame(EntregaUi)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 54, 331, 281))
        self.frame.setStyleSheet(u"#frame{background-color:white;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 90, 331, 291))
        self.stackedWidget.setStyleSheet(u"/* Estilo Base del Bot\u00f3n de la Paginaci\u00f3n */\n"
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
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Hacer Clic (Pressed) */\n"
"QPushButton:pressed {\n"
"    background: #2e4546; /* Color de fondo m\u00e1s oscuro */\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#stackedWidget{background-color:white;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-r"
                        "adius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"#page{\n"
"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"\n"
"}")
        self.fecha_informe = QDateEdit(self.page)
        self.fecha_informe.setObjectName(u"fecha_informe")
        self.fecha_informe.setGeometry(QRect(10, 70, 171, 40))
        self.fecha_informe.setCalendarPopup(False)
        self.lbl9_4 = QLabel(self.page)
        self.lbl9_4.setObjectName(u"lbl9_4")
        self.lbl9_4.setGeometry(QRect(10, 40, 131, 21))
        self.lbl9_4.setStyleSheet(u"")
        self.lbl9_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btn_registrar_informe = QPushButton(self.page)
        self.btn_registrar_informe.setObjectName(u"btn_registrar_informe")
        self.btn_registrar_informe.setGeometry(QRect(140, 140, 181, 35))
        self.btn_registrar_informe.setMinimumSize(QSize(100, 35))
        self.btn_registrar_informe.setMaximumSize(QSize(200, 567))
        self.btn_registrar_informe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registrar_informe.setFocusPolicy(Qt.NoFocus)
        self.btn_registrar_informe.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_registrar_informe.setIcon(icon1)
        self.btn_registrar_informe.setIconSize(QSize(15, 21))
        self.lbl9_5 = QLabel(self.page)
        self.lbl9_5.setObjectName(u"lbl9_5")
        self.lbl9_5.setGeometry(QRect(200, 40, 91, 21))
        self.lbl9_5.setStyleSheet(u"")
        self.lbl9_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_mes = QLineEdit(self.page)
        self.line_mes.setObjectName(u"line_mes")
        self.line_mes.setEnabled(False)
        self.line_mes.setGeometry(QRect(200, 70, 121, 40))
        self.line_mes.setStyleSheet(u"")
        self.line_mes.setFrame(True)
        self.line_mes.setCursorPosition(0)
        self.line_mes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_mes.setDragEnabled(False)
        self.line_mes.setReadOnly(False)
        self.line_mes.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.line_mes.setClearButtonEnabled(False)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"#page_2{\n"
"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"\n"
"}")
        self.rbt_si_ficha = QRadioButton(self.page_2)
        self.rbt_si_ficha.setObjectName(u"rbt_si_ficha")
        self.rbt_si_ficha.setGeometry(QRect(20, 70, 61, 17))
        self.rbt_si_ficha.setChecked(True)
        self.rbt_no_ficha = QRadioButton(self.page_2)
        self.rbt_no_ficha.setObjectName(u"rbt_no_ficha")
        self.rbt_no_ficha.setGeometry(QRect(80, 70, 82, 17))
        self.pregunta_ficha = QLabel(self.page_2)
        self.pregunta_ficha.setObjectName(u"pregunta_ficha")
        self.pregunta_ficha.setGeometry(QRect(10, 40, 311, 21))
        self.pregunta_ficha.setStyleSheet(u"")
        self.pregunta_ficha.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btn_registrar_ficha = QPushButton(self.page_2)
        self.btn_registrar_ficha.setObjectName(u"btn_registrar_ficha")
        self.btn_registrar_ficha.setGeometry(QRect(140, 140, 181, 35))
        self.btn_registrar_ficha.setMinimumSize(QSize(100, 35))
        self.btn_registrar_ficha.setMaximumSize(QSize(200, 567))
        self.btn_registrar_ficha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registrar_ficha.setFocusPolicy(Qt.NoFocus)
        self.btn_registrar_ficha.setStyleSheet(u"")
        self.btn_registrar_ficha.setIcon(icon1)
        self.btn_registrar_ficha.setIconSize(QSize(15, 21))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"#page_3{\n"
"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"\n"
"}")
        self.rbt_no_memorandum = QRadioButton(self.page_3)
        self.rbt_no_memorandum.setObjectName(u"rbt_no_memorandum")
        self.rbt_no_memorandum.setGeometry(QRect(70, 70, 51, 17))
        self.pregunta_memorandum = QLabel(self.page_3)
        self.pregunta_memorandum.setObjectName(u"pregunta_memorandum")
        self.pregunta_memorandum.setGeometry(QRect(10, 40, 311, 21))
        self.pregunta_memorandum.setStyleSheet(u"")
        self.pregunta_memorandum.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.rbt_si_memorandum = QRadioButton(self.page_3)
        self.rbt_si_memorandum.setObjectName(u"rbt_si_memorandum")
        self.rbt_si_memorandum.setGeometry(QRect(20, 70, 41, 17))
        self.rbt_si_memorandum.setChecked(True)
        self.btn_registrar_memorandum = QPushButton(self.page_3)
        self.btn_registrar_memorandum.setObjectName(u"btn_registrar_memorandum")
        self.btn_registrar_memorandum.setGeometry(QRect(129, 130, 191, 35))
        self.btn_registrar_memorandum.setMinimumSize(QSize(100, 35))
        self.btn_registrar_memorandum.setMaximumSize(QSize(200, 567))
        self.btn_registrar_memorandum.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registrar_memorandum.setFocusPolicy(Qt.NoFocus)
        self.btn_registrar_memorandum.setStyleSheet(u"")
        self.btn_registrar_memorandum.setIcon(icon1)
        self.btn_registrar_memorandum.setIconSize(QSize(15, 21))
        self.stackedWidget.addWidget(self.page_3)
        self.lbl9_3 = QLabel(self.frame)
        self.lbl9_3.setObjectName(u"lbl9_3")
        self.lbl9_3.setGeometry(QRect(10, 10, 101, 21))
        self.lbl9_3.setStyleSheet(u"")
        self.lbl9_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbo_tipo_entrega = QComboBox(self.frame)
        self.cbo_tipo_entrega.addItem("")
        self.cbo_tipo_entrega.addItem("")
        self.cbo_tipo_entrega.addItem("")
        self.cbo_tipo_entrega.setObjectName(u"cbo_tipo_entrega")
        self.cbo_tipo_entrega.setGeometry(QRect(10, 40, 311, 40))
        self.cbo_tipo_entrega.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbo_tipo_entrega.setStyleSheet(u"")
        self.cbo_tipo_entrega.setMaxVisibleItems(67)

        self.retranslateUi(EntregaUi)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EntregaUi)
    # setupUi

    def retranslateUi(self, EntregaUi):
        EntregaUi.setWindowTitle(QCoreApplication.translate("EntregaUi", u"Entrega", None))
        self.titulo_accion.setText(QCoreApplication.translate("EntregaUi", u"Nueva Entrega", None))
        self.nombre_tutor.setText(QCoreApplication.translate("EntregaUi", u"Nueva Afiliaci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btn_closeadmi_3.setToolTip(QCoreApplication.translate("EntregaUi", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeadmi_3.setText("")
        self.fecha_informe.setDisplayFormat(QCoreApplication.translate("EntregaUi", u"yyyy-MM-dd", None))
        self.lbl9_4.setText(QCoreApplication.translate("EntregaUi", u"Fecha  entrega", None))
        self.btn_registrar_informe.setText(QCoreApplication.translate("EntregaUi", u"Registrar entrega", None))
        self.lbl9_5.setText(QCoreApplication.translate("EntregaUi", u"Mes", None))
        self.line_mes.setPlaceholderText("")
        self.rbt_si_ficha.setText(QCoreApplication.translate("EntregaUi", u"SI", None))
        self.rbt_no_ficha.setText(QCoreApplication.translate("EntregaUi", u"NO", None))
        self.pregunta_ficha.setText(QCoreApplication.translate("EntregaUi", u"\u00bfEntrego ficha?", None))
        self.btn_registrar_ficha.setText(QCoreApplication.translate("EntregaUi", u"Registrar entrega", None))
        self.rbt_no_memorandum.setText(QCoreApplication.translate("EntregaUi", u"NO", None))
        self.pregunta_memorandum.setText(QCoreApplication.translate("EntregaUi", u"\u00bfEntreg\u00f3 Memorandum?", None))
        self.rbt_si_memorandum.setText(QCoreApplication.translate("EntregaUi", u"SI", None))
        self.btn_registrar_memorandum.setText(QCoreApplication.translate("EntregaUi", u"Registrar entrega", None))
        self.lbl9_3.setText(QCoreApplication.translate("EntregaUi", u"Tipo entrega", None))
        self.cbo_tipo_entrega.setItemText(0, QCoreApplication.translate("EntregaUi", u"Informe", None))
        self.cbo_tipo_entrega.setItemText(1, QCoreApplication.translate("EntregaUi", u"Ficha", None))
        self.cbo_tipo_entrega.setItemText(2, QCoreApplication.translate("EntregaUi", u"Memorandum", None))

    # retranslateUi

