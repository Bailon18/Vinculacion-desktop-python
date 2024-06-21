# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario_proyectosUyMVCb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_FormularioProyectos(object):
    def setupUi(self, FormularioProyectos):
        if not FormularioProyectos.objectName():
            FormularioProyectos.setObjectName(u"FormularioProyectos")
        FormularioProyectos.resize(486, 480)
        FormularioProyectos.setMinimumSize(QSize(486, 480))
        FormularioProyectos.setMaximumSize(QSize(486, 480))
        self.gridLayout = QGridLayout(FormularioProyectos)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormularioProyectos)
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
        self.frame_2.setGeometry(QRect(0, 0, 488, 50))
        self.frame_2.setMinimumSize(QSize(488, 50))
        self.frame_2.setMaximumSize(QSize(488, 50))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_close = QToolButton(self.frame_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(454, 6, 25, 25))
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
        icon = QIcon()
        icon.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(13, 13))
        self.btn_close.setAutoRaise(True)
        self.lbl_titulo_ventana = QLabel(self.frame_2)
        self.lbl_titulo_ventana.setObjectName(u"lbl_titulo_ventana")
        self.lbl_titulo_ventana.setGeometry(QRect(19, 15, 401, 21))
        self.lbl_titulo_ventana.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 50, 491, 371))
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
"/* PLANTEXT*/\n"
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
"\n"
"/* QLabel para Mostrar Error */\n"
"QLabel#errorNombre{\n"
"    font-fami"
                        "ly: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    color: #D32F2F; \n"
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
"QComboBox::"
                        "focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_registro_estudiante = QWidget()
        self.scroll_registro_estudiante.setObjectName(u"scroll_registro_estudiante")
        self.scroll_registro_estudiante.setGeometry(QRect(0, 0, 489, 369))
        self.scroll_registro_estudiante.setMinimumSize(QSize(0, 250))
        self.scroll_registro_estudiante.setStyleSheet(u"#scroll_registro_estudiante{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.lbl11 = QLabel(self.scroll_registro_estudiante)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(20, 20, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.plain_descripcion = QPlainTextEdit(self.scroll_registro_estudiante)
        self.plain_descripcion.setObjectName(u"plain_descripcion")
        self.plain_descripcion.setGeometry(QRect(20, 180, 441, 91))
        self.plain_descripcion.setMinimumSize(QSize(0, 0))
        self.plain_descripcion.setMaximumSize(QSize(16777215, 16777215))
        self.plain_descripcion.setStyleSheet(u"")
        self.lbl11_2 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_2.setObjectName(u"lbl11_2")
        self.lbl11_2.setGeometry(QRect(20, 150, 171, 21))
        self.lbl11_2.setStyleSheet(u"")
        self.lbl11_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.errorNombre = QLabel(self.scroll_registro_estudiante)
        self.errorNombre.setObjectName(u"errorNombre")
        self.errorNombre.setGeometry(QRect(20, 117, 441, 16))
        self.lbl11_3 = QLabel(self.scroll_registro_estudiante)
        self.lbl11_3.setObjectName(u"lbl11_3")
        self.lbl11_3.setGeometry(QRect(20, 290, 171, 21))
        self.lbl11_3.setStyleSheet(u"")
        self.lbl11_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbo_estado = QComboBox(self.scroll_registro_estudiante)
        self.cbo_estado.addItem("")
        self.cbo_estado.addItem("")
        self.cbo_estado.setObjectName(u"cbo_estado")
        self.cbo_estado.setGeometry(QRect(20, 312, 221, 40))
        self.line_nombre = QPlainTextEdit(self.scroll_registro_estudiante)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setGeometry(QRect(20, 44, 441, 71))
        self.line_nombre.setMinimumSize(QSize(0, 0))
        self.line_nombre.setMaximumSize(QSize(16777215, 16777215))
        self.line_nombre.setStyleSheet(u"")
        self.scrollArea.setWidget(self.scroll_registro_estudiante)
        self.frame_pie_pagina = QFrame(self.frame)
        self.frame_pie_pagina.setObjectName(u"frame_pie_pagina")
        self.frame_pie_pagina.setGeometry(QRect(0, 418, 491, 61))
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
        self.frame_pie_pagina.setFrameShape(QFrame.StyledPanel)
        self.frame_pie_pagina.setFrameShadow(QFrame.Raised)
        self.btn_agregar_proyecto = QPushButton(self.frame_pie_pagina)
        self.btn_agregar_proyecto.setObjectName(u"btn_agregar_proyecto")
        self.btn_agregar_proyecto.setGeometry(QRect(290, 13, 180, 40))
        self.btn_agregar_proyecto.setMinimumSize(QSize(180, 40))
        self.btn_agregar_proyecto.setMaximumSize(QSize(110, 40))
        self.btn_agregar_proyecto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_proyecto.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar_proyecto.setIcon(icon1)
        self.btn_agregar_proyecto.setIconSize(QSize(15, 21))
        self.cancelButton = QPushButton(self.frame_pie_pagina)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(160, 13, 120, 40))
        self.cancelButton.setMinimumSize(QSize(120, 40))
        self.cancelButton.setMaximumSize(QSize(120, 40))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setFocusPolicy(Qt.NoFocus)
        self.cancelButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/menu/no.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon2)
        self.cancelButton.setIconSize(QSize(15, 21))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(FormularioProyectos)

        QMetaObject.connectSlotsByName(FormularioProyectos)
    # setupUi

    def retranslateUi(self, FormularioProyectos):
        FormularioProyectos.setWindowTitle(QCoreApplication.translate("FormularioProyectos", u"Formulario Proyecto", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("FormularioProyectos", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.lbl_titulo_ventana.setText(QCoreApplication.translate("FormularioProyectos", u"Registra nuevo proyecto", None))
        self.lbl11.setText(QCoreApplication.translate("FormularioProyectos", u"Nombre*", None))
        self.lbl11_2.setText(QCoreApplication.translate("FormularioProyectos", u"Descripci\u00f3n ( Opcional )", None))
        self.errorNombre.setText("")
        self.lbl11_3.setText(QCoreApplication.translate("FormularioProyectos", u"Estado", None))
        self.cbo_estado.setItemText(0, QCoreApplication.translate("FormularioProyectos", u"Activo", None))
        self.cbo_estado.setItemText(1, QCoreApplication.translate("FormularioProyectos", u"Inactivo", None))

        self.btn_agregar_proyecto.setText(QCoreApplication.translate("FormularioProyectos", u"Guardar proyecto", None))
        self.cancelButton.setText(QCoreApplication.translate("FormularioProyectos", u"Cancelar", None))
    # retranslateUi

