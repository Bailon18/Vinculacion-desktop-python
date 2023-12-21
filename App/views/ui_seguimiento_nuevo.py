# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seguimiento_nuevoshzxUh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_rc
import source_rc

class Ui_SeguimientoNuevo(object):
    def setupUi(self, SeguimientoNuevo):
        if not SeguimientoNuevo.objectName():
            SeguimientoNuevo.setObjectName(u"SeguimientoNuevo")
        SeguimientoNuevo.setEnabled(True)
        SeguimientoNuevo.resize(430, 550)
        SeguimientoNuevo.setMinimumSize(QSize(430, 550))
        SeguimientoNuevo.setMaximumSize(QSize(580, 550))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        SeguimientoNuevo.setWindowIcon(icon)
        SeguimientoNuevo.setStyleSheet(u"QTableWidget {\n"
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
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"text-transform: uppercase;\n"
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
""
                        "\n"
"/*bordes internos*/\n"
"QTableWidget::item {\n"
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
"\n"
"/*SCROLL VERTICAL*/\n"
"\n"
"QScrollBar:vertical{\n"
"	background: #f3f4f6;\n"
"	width: 11px; \n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"	background: #cdcecf;\n"
"    border-radius:3px;\n"
"	margin: 0px 0px 3px 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0 px;\n"
"}\n"
"\n"
"\n"
"/*SCROLL HORIZONTAL*/\n"
"\n"
"QScrollBar:horizontal{\n"
"	background: #f3f4f6;\n"
"	height: 11px; \n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"	background: #cdcecf;\n"
"    border-radius:3px;\n"
"	margin: 3px 2px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"	height: 0 "
                        "px;\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(SeguimientoNuevo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(SeguimientoNuevo)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"\n"
"#frame{background-color:white;border-radius:10px}\n"
"\n"
"\n"
"QLabel{\n"
"font-family: Roboto;\n"
"font-style: bold;\n"
"font-weight: 450;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;}\n"
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
"QCheckBox{font-family: Roboto;\n"
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
""
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
"min-width: 25px; min-height: 12px; "
                        "background-color: #F3F4F6; \n"
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
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.lbl8 = QLabel(self.frame)
        self.lbl8.setObjectName(u"lbl8")
        self.lbl8.setGeometry(QRect(19, 70, 371, 21))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setBold(True)
        font.setWeight(60)
        self.lbl8.setFont(font)
        self.lbl8.setStyleSheet(u"#lbl8{\n"
"\n"
"font-family: Roboto ;\n"
"font-style: bold;\n"
"font-weight: 480;\n"
"font-size: 17px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"color: #374151}")
        self.lbl8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 431, 50))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lbl_nombre_estudiante = QLabel(self.frame_2)
        self.lbl_nombre_estudiante.setObjectName(u"lbl_nombre_estudiante")
        self.lbl_nombre_estudiante.setGeometry(QRect(20, 10, 361, 27))
        self.lbl_nombre_estudiante.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 17px;\n"
"line-height: 40px;\n"
"letter-spacing: 0.02em;\n"
"color:#ffffff;")
        self.btn_closeseguimiento = QToolButton(self.frame_2)
        self.btn_closeseguimiento.setObjectName(u"btn_closeseguimiento")
        self.btn_closeseguimiento.setGeometry(QRect(400, 10, 25, 25))
        self.btn_closeseguimiento.setFocusPolicy(Qt.NoFocus)
        self.btn_closeseguimiento.setStyleSheet(u"#btn_closeseguimiento{\n"
"font-family: Roboto;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"background-color: #d5d5d8;\n"
"color: #6B7280;\n"
"border-radius:11px\n"
"}\n"
"\n"
"#btn_closeseguimiento:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeseguimiento.setIcon(icon1)
        self.btn_closeseguimiento.setIconSize(QSize(13, 13))
        self.btn_closeseguimiento.setAutoRaise(True)
        self.lbl_nombreestudiante = QLabel(self.frame)
        self.lbl_nombreestudiante.setObjectName(u"lbl_nombreestudiante")
        self.lbl_nombreestudiante.setGeometry(QRect(20, 100, 341, 16))
        self.lbl8_2 = QLabel(self.frame)
        self.lbl8_2.setObjectName(u"lbl8_2")
        self.lbl8_2.setGeometry(QRect(20, 140, 201, 21))
        self.lbl8_2.setFont(font)
        self.lbl8_2.setStyleSheet(u"#lbl8_2{\n"
"\n"
"font-family: Roboto ;\n"
"font-style: bold;\n"
"font-weight: 480;\n"
"font-size: 17px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"color: #374151}")
        self.lbl8_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.fecha_seguimiento = QDateEdit(self.frame)
        self.fecha_seguimiento.setObjectName(u"fecha_seguimiento")
        self.fecha_seguimiento.setGeometry(QRect(20, 200, 230, 40))
        self.fecha_seguimiento.setCursor(QCursor(Qt.PointingHandCursor))
        self.fecha_seguimiento.setStyleSheet(u"")
        self.fecha_seguimiento.setCalendarPopup(False)
        self.label_96 = QLabel(self.frame)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(20, 170, 161, 31))
        self.spb_numerohoras = QSpinBox(self.frame)
        self.spb_numerohoras.setObjectName(u"spb_numerohoras")
        self.spb_numerohoras.setEnabled(False)
        self.spb_numerohoras.setGeometry(QRect(290, 200, 71, 41))
        self.lbl5 = QLabel(self.frame)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(290, 175, 101, 21))
        self.lbl5.setStyleSheet(u"")
        self.lbl5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.plain_observacion = QPlainTextEdit(self.frame)
        self.plain_observacion.setObjectName(u"plain_observacion")
        self.plain_observacion.setGeometry(QRect(20, 290, 391, 191))
        self.label_97 = QLabel(self.frame)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(20, 260, 161, 31))
        self.btn_guardar = QPushButton(self.frame)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(300, 490, 110, 40))
        self.btn_guardar.setMinimumSize(QSize(100, 40))
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
        icon2 = QIcon()
        icon2.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guardar.setIcon(icon2)
        self.btn_guardar.setIconSize(QSize(15, 21))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(SeguimientoNuevo)

        QMetaObject.connectSlotsByName(SeguimientoNuevo)
    # setupUi

    def retranslateUi(self, SeguimientoNuevo):
        SeguimientoNuevo.setWindowTitle(QCoreApplication.translate("SeguimientoNuevo", u"Seguimiento", None))
        self.lbl8.setText(QCoreApplication.translate("SeguimientoNuevo", u"Estudiante asignado", None))
        self.lbl_nombre_estudiante.setText(QCoreApplication.translate("SeguimientoNuevo", u"Seguimiento", None))
#if QT_CONFIG(tooltip)
        self.btn_closeseguimiento.setToolTip(QCoreApplication.translate("SeguimientoNuevo", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeseguimiento.setText("")
        self.lbl_nombreestudiante.setText(QCoreApplication.translate("SeguimientoNuevo", u"tutor asignado", None))
        self.lbl8_2.setText(QCoreApplication.translate("SeguimientoNuevo", u"Detalles", None))
        self.fecha_seguimiento.setDisplayFormat(QCoreApplication.translate("SeguimientoNuevo", u"d-MM-yyyy", None))
        self.label_96.setText(QCoreApplication.translate("SeguimientoNuevo", u"Fecha seguimiento*", None))
        self.lbl5.setText(QCoreApplication.translate("SeguimientoNuevo", u"N\u00b0 horas", None))
        self.label_97.setText(QCoreApplication.translate("SeguimientoNuevo", u"Observaciones*", None))
        self.btn_guardar.setText(QCoreApplication.translate("SeguimientoNuevo", u"Guardar", None))
    # retranslateUi

