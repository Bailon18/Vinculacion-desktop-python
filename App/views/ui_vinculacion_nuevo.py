# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vinculacion_nuevoxBmQkq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_NuevaVinculacion(object):
    def setupUi(self, NuevaVinculacion):
        if not NuevaVinculacion.objectName():
            NuevaVinculacion.setObjectName(u"NuevaVinculacion")
        NuevaVinculacion.resize(710, 606)
        NuevaVinculacion.setMinimumSize(QSize(600, 600))
        NuevaVinculacion.setMaximumSize(QSize(710, 606))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        NuevaVinculacion.setWindowIcon(icon)
        NuevaVinculacion.setStyleSheet(u"")
        self.gridLayout = QGridLayout(NuevaVinculacion)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(NuevaVinculacion)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{background-color:white;border-radius:10px}\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #54BFC9;\n"
"border-radius: 8px;}\n"
"\n"
"QPushButton:hover{background: #439CA8;\n"
"border-radius: 8px; }\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 70, 691, 471))
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	\n"
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
""
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
"\n"
"\n"
"\n"
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
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QCheckBox{"
                        "font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"color:#9CA3AF}\n"
"\n"
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
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow{\n"
"	image: url(:/menu/contraerabajo.png);\n"
"     width:11px;\n"
"     height: 11px;}\n"
"\n"
"QSpinBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QDateEdit{\n"
"font-family: Roboto;\n"
"font-styl"
                        "e: normal;\n"
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
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lbl5 = QLabel(self.frame_2)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(10, 280, 101, 21))
        self.lbl5.setStyleSheet(u"")
        self.lbl5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_nombreapellidos = QLineEdit(self.frame_2)
        self.line_nombreapellidos.setObjectName(u"line_nombreapellidos")
        self.line_nombreapellidos.setEnabled(True)
        self.line_nombreapellidos.setGeometry(QRect(10, 36, 431, 40))
        self.line_nombreapellidos.setStyleSheet(u"")
        self.line_nombreapellidos.setMaxLength(30)
        self.line_nombreapellidos.setFrame(True)
        self.line_nombreapellidos.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.frame_2)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(10, 10, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl9 = QLabel(self.frame_2)
        self.lbl9.setObjectName(u"lbl9")
        self.lbl9.setGeometry(QRect(240, 97, 81, 21))
        self.lbl9.setStyleSheet(u"")
        self.lbl9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbox_carrera = QComboBox(self.frame_2)
        self.cbox_carrera.setObjectName(u"cbox_carrera")
        self.cbox_carrera.setGeometry(QRect(240, 120, 205, 40))
        self.cbox_carrera.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_carrera.setStyleSheet(u"")
        self.label_95 = QLabel(self.frame_2)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(10, 190, 161, 31))
        self.fecha_inicio = QDateEdit(self.frame_2)
        self.fecha_inicio.setObjectName(u"fecha_inicio")
        self.fecha_inicio.setGeometry(QRect(240, 220, 205, 40))
        self.fecha_inicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.fecha_inicio.setStyleSheet(u"")
        self.fecha_inicio.setCalendarPopup(False)
        self.lbl9_2 = QLabel(self.frame_2)
        self.lbl9_2.setObjectName(u"lbl9_2")
        self.lbl9_2.setGeometry(QRect(470, 10, 131, 21))
        self.lbl9_2.setStyleSheet(u"")
        self.lbl9_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_identificacion = QLineEdit(self.frame_2)
        self.line_identificacion.setObjectName(u"line_identificacion")
        self.line_identificacion.setEnabled(True)
        self.line_identificacion.setGeometry(QRect(10, 120, 205, 40))
        self.line_identificacion.setStyleSheet(u"")
        self.line_identificacion.setFrame(True)
        self.line_identificacion.setCursorPosition(0)
        self.line_identificacion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_identificacion.setDragEnabled(False)
        self.line_identificacion.setReadOnly(False)
        self.line_identificacion.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.line_identificacion.setClearButtonEnabled(False)
        self.line_periodoacademico = QLineEdit(self.frame_2)
        self.line_periodoacademico.setObjectName(u"line_periodoacademico")
        self.line_periodoacademico.setEnabled(True)
        self.line_periodoacademico.setGeometry(QRect(10, 220, 205, 40))
        self.line_periodoacademico.setStyleSheet(u"")
        self.line_periodoacademico.setMaxLength(30)
        self.line_periodoacademico.setFrame(True)
        self.line_periodoacademico.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbo_tipo_identificacion = QComboBox(self.frame_2)
        self.cbo_tipo_identificacion.addItem("")
        self.cbo_tipo_identificacion.addItem("")
        self.cbo_tipo_identificacion.addItem("")
        self.cbo_tipo_identificacion.setObjectName(u"cbo_tipo_identificacion")
        self.cbo_tipo_identificacion.setGeometry(QRect(470, 36, 205, 40))
        self.lbl9_4 = QLabel(self.frame_2)
        self.lbl9_4.setObjectName(u"lbl9_4")
        self.lbl9_4.setGeometry(QRect(10, 94, 131, 21))
        self.lbl9_4.setStyleSheet(u"")
        self.lbl9_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_96 = QLabel(self.frame_2)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(240, 190, 161, 31))
        self.fecha_final = QDateEdit(self.frame_2)
        self.fecha_final.setObjectName(u"fecha_final")
        self.fecha_final.setGeometry(QRect(470, 220, 205, 40))
        self.fecha_final.setCursor(QCursor(Qt.PointingHandCursor))
        self.fecha_final.setStyleSheet(u"")
        self.fecha_final.setCalendarPopup(False)
        self.label_97 = QLabel(self.frame_2)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(470, 190, 161, 31))
        self.spb_numerohoras = QSpinBox(self.frame_2)
        self.spb_numerohoras.setObjectName(u"spb_numerohoras")
        self.spb_numerohoras.setEnabled(False)
        self.spb_numerohoras.setGeometry(QRect(10, 310, 71, 41))
        self.line_campoespecifico = QLineEdit(self.frame_2)
        self.line_campoespecifico.setObjectName(u"line_campoespecifico")
        self.line_campoespecifico.setEnabled(True)
        self.line_campoespecifico.setGeometry(QRect(240, 310, 205, 40))
        self.line_campoespecifico.setStyleSheet(u"")
        self.line_campoespecifico.setMaxLength(30)
        self.line_campoespecifico.setFrame(True)
        self.line_campoespecifico.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl9_5 = QLabel(self.frame_2)
        self.lbl9_5.setObjectName(u"lbl9_5")
        self.lbl9_5.setGeometry(QRect(240, 280, 131, 21))
        self.lbl9_5.setStyleSheet(u"")
        self.lbl9_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl5_2 = QLabel(self.frame_2)
        self.lbl5_2.setObjectName(u"lbl5_2")
        self.lbl5_2.setGeometry(QRect(470, 280, 151, 21))
        self.lbl5_2.setStyleSheet(u"")
        self.lbl5_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbo_tutor = QComboBox(self.frame_2)
        self.cbo_tutor.setObjectName(u"cbo_tutor")
        self.cbo_tutor.setGeometry(QRect(470, 310, 205, 40))
        self.lbl9_3 = QLabel(self.frame_2)
        self.lbl9_3.setObjectName(u"lbl9_3")
        self.lbl9_3.setGeometry(QRect(470, 97, 101, 21))
        self.lbl9_3.setStyleSheet(u"")
        self.lbl9_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbo_institucion = QComboBox(self.frame_2)
        self.cbo_institucion.setObjectName(u"cbo_institucion")
        self.cbo_institucion.setGeometry(QRect(470, 120, 205, 40))
        self.cbo_institucion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbo_institucion.setStyleSheet(u"")
        self.cbo_proyectos = QComboBox(self.frame_2)
        self.cbo_proyectos.setObjectName(u"cbo_proyectos")
        self.cbo_proyectos.setGeometry(QRect(10, 400, 661, 40))
        self.cbo_proyectos.setMinimumSize(QSize(661, 40))
        self.cbo_proyectos.setMaximumSize(QSize(661, 40))
        self.cbo_proyectos.setMaxVisibleItems(10)
        self.cbo_proyectos.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cbo_proyectos.setDuplicatesEnabled(False)
        self.lbl5_3 = QLabel(self.frame_2)
        self.lbl5_3.setObjectName(u"lbl5_3")
        self.lbl5_3.setGeometry(QRect(10, 370, 151, 21))
        self.lbl5_3.setStyleSheet(u"")
        self.lbl5_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_codigoies = QLineEdit(self.frame_2)
        self.line_codigoies.setObjectName(u"line_codigoies")
        self.line_codigoies.setEnabled(True)
        self.line_codigoies.setGeometry(QRect(104, 310, 111, 40))
        self.line_codigoies.setStyleSheet(u"")
        self.line_codigoies.setMaxLength(30)
        self.line_codigoies.setFrame(True)
        self.line_codigoies.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl5_4 = QLabel(self.frame_2)
        self.lbl5_4.setObjectName(u"lbl5_4")
        self.lbl5_4.setGeometry(QRect(110, 280, 101, 21))
        self.lbl5_4.setStyleSheet(u"")
        self.lbl5_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btn_guardar = QPushButton(self.frame)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(480, 550, 195, 40))
        self.btn_guardar.setMinimumSize(QSize(195, 40))
        self.btn_guardar.setMaximumSize(QSize(110, 40))
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
"QPushButton:hover{background: #344647;\n"
"border-radius: 8px; }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guardar.setIcon(icon1)
        self.btn_guardar.setIconSize(QSize(15, 21))
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 711, 70))
        self.frame_3.setMinimumSize(QSize(0, 70))
        self.frame_3.setMaximumSize(QSize(16777215, 4455))
        self.frame_3.setStyleSheet(u"#frame_3{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}\n"
"\n"
"QLabel{\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 17px;\n"
"line-height: 40px;\n"
"letter-spacing: 0.02em;\n"
"color:#ffffff;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_closeadmi = QToolButton(self.frame_3)
        self.btn_closeadmi.setObjectName(u"btn_closeadmi")
        self.btn_closeadmi.setGeometry(QRect(680, 10, 25, 25))
        self.btn_closeadmi.setFocusPolicy(Qt.NoFocus)
        self.btn_closeadmi.setStyleSheet(u"#btn_closeadmi{\n"
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
"#btn_closeadmi:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeadmi.setIcon(icon2)
        self.btn_closeadmi.setIconSize(QSize(13, 13))
        self.btn_closeadmi.setAutoRaise(True)
        self.axax = QLabel(self.frame_3)
        self.axax.setObjectName(u"axax")
        self.axax.setGeometry(QRect(20, 10, 201, 31))
        self.axax.setStyleSheet(u"")
        self.axax.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.vinculacion_titulo_2 = QLabel(self.frame_3)
        self.vinculacion_titulo_2.setObjectName(u"vinculacion_titulo_2")
        self.vinculacion_titulo_2.setGeometry(QRect(20, 40, 81, 31))
        self.vinculacion_titulo_2.setStyleSheet(u"")
        self.vinculacion_titulo_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.vinculacion_titulo = QLabel(self.frame_3)
        self.vinculacion_titulo.setObjectName(u"vinculacion_titulo")
        self.vinculacion_titulo.setGeometry(QRect(220, 10, 391, 31))
        self.vinculacion_titulo.setStyleSheet(u"")
        self.vinculacion_titulo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.vinculacion_estado = QLabel(self.frame_3)
        self.vinculacion_estado.setObjectName(u"vinculacion_estado")
        self.vinculacion_estado.setGeometry(QRect(100, 40, 171, 31))
        self.vinculacion_estado.setStyleSheet(u"")
        self.vinculacion_estado.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.line_nombreapellidos, self.cbo_tipo_identificacion)
        QWidget.setTabOrder(self.cbo_tipo_identificacion, self.line_identificacion)
        QWidget.setTabOrder(self.line_identificacion, self.cbox_carrera)
        QWidget.setTabOrder(self.cbox_carrera, self.cbo_institucion)
        QWidget.setTabOrder(self.cbo_institucion, self.line_periodoacademico)
        QWidget.setTabOrder(self.line_periodoacademico, self.fecha_inicio)
        QWidget.setTabOrder(self.fecha_inicio, self.fecha_final)
        QWidget.setTabOrder(self.fecha_final, self.spb_numerohoras)
        QWidget.setTabOrder(self.spb_numerohoras, self.line_codigoies)
        QWidget.setTabOrder(self.line_codigoies, self.line_campoespecifico)
        QWidget.setTabOrder(self.line_campoespecifico, self.cbo_tutor)
        QWidget.setTabOrder(self.cbo_tutor, self.cbo_proyectos)

        self.retranslateUi(NuevaVinculacion)

        QMetaObject.connectSlotsByName(NuevaVinculacion)
    # setupUi

    def retranslateUi(self, NuevaVinculacion):
        NuevaVinculacion.setWindowTitle(QCoreApplication.translate("NuevaVinculacion", u"Vinculaci\u00f3n", None))
        self.lbl5.setText(QCoreApplication.translate("NuevaVinculacion", u"N\u00b0 horas", None))
        self.line_nombreapellidos.setPlaceholderText(QCoreApplication.translate("NuevaVinculacion", u"Ingrese nombre y apellidos", None))
        self.lbl11.setText(QCoreApplication.translate("NuevaVinculacion", u"Nombre y apellidos*", None))
        self.lbl9.setText(QCoreApplication.translate("NuevaVinculacion", u"Carrera*", None))
        self.label_95.setText(QCoreApplication.translate("NuevaVinculacion", u"Periodo Academico*", None))
        self.fecha_inicio.setDisplayFormat(QCoreApplication.translate("NuevaVinculacion", u"d-MM-yyyy", None))
        self.lbl9_2.setText(QCoreApplication.translate("NuevaVinculacion", u"Tipo identificaci\u00f3n*", None))
        self.line_identificacion.setText("")
        self.line_identificacion.setPlaceholderText(QCoreApplication.translate("NuevaVinculacion", u"ingrese identificacion", None))
        self.line_periodoacademico.setPlaceholderText(QCoreApplication.translate("NuevaVinculacion", u"Ingrese periodo acad...", None))
        self.cbo_tipo_identificacion.setItemText(0, QCoreApplication.translate("NuevaVinculacion", u"Cedula", None))
        self.cbo_tipo_identificacion.setItemText(1, QCoreApplication.translate("NuevaVinculacion", u"Carnet extranjeria", None))
        self.cbo_tipo_identificacion.setItemText(2, QCoreApplication.translate("NuevaVinculacion", u"Pasaporte", None))

        self.lbl9_4.setText(QCoreApplication.translate("NuevaVinculacion", u"Identificacion*", None))
        self.label_96.setText(QCoreApplication.translate("NuevaVinculacion", u"Fecha inicio*", None))
        self.fecha_final.setDisplayFormat(QCoreApplication.translate("NuevaVinculacion", u"d-MM-yyyy", None))
        self.label_97.setText(QCoreApplication.translate("NuevaVinculacion", u"Fecha final", None))
        self.line_campoespecifico.setPlaceholderText(QCoreApplication.translate("NuevaVinculacion", u"ingrese identificacion", None))
        self.lbl9_5.setText(QCoreApplication.translate("NuevaVinculacion", u"Campo especifico*", None))
        self.lbl5_2.setText(QCoreApplication.translate("NuevaVinculacion", u"Tutor Asignado*", None))
        self.lbl9_3.setText(QCoreApplication.translate("NuevaVinculacion", u"Instituci\u00f3n", None))
        self.cbo_proyectos.setPlaceholderText("")
        self.lbl5_3.setText(QCoreApplication.translate("NuevaVinculacion", u"Proyecto Asignado*", None))
        self.line_codigoies.setPlaceholderText(QCoreApplication.translate("NuevaVinculacion", u"Cod. ies", None))
        self.lbl5_4.setText(QCoreApplication.translate("NuevaVinculacion", u"N\u00b0 Ies*", None))
        self.btn_guardar.setText(QCoreApplication.translate("NuevaVinculacion", u"Guardar", None))
#if QT_CONFIG(tooltip)
        self.btn_closeadmi.setToolTip(QCoreApplication.translate("NuevaVinculacion", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeadmi.setText("")
        self.axax.setText(QCoreApplication.translate("NuevaVinculacion", u"Nueva Vinculaci\u00f3n", None))
        self.vinculacion_titulo_2.setText(QCoreApplication.translate("NuevaVinculacion", u"Estado:", None))
        self.vinculacion_titulo.setText(QCoreApplication.translate("NuevaVinculacion", u"Nueva Afiliaci\u00f3n", None))
        self.vinculacion_estado.setText(QCoreApplication.translate("NuevaVinculacion", u"Pendiente", None))
    # retranslateUi

