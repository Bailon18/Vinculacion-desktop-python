# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seguimientoetrQBg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_rc

class Ui_Seguimiento(object):
    def setupUi(self, Seguimiento):
        if not Seguimiento.objectName():
            Seguimiento.setObjectName(u"Seguimiento")
        Seguimiento.resize(620, 560)
        Seguimiento.setMinimumSize(QSize(620, 560))
        Seguimiento.setMaximumSize(QSize(620, 600))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Seguimiento.setWindowIcon(icon)
        Seguimiento.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(Seguimiento)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Seguimiento)
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
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;}\n"
"\n"
"")
        self.stack_principal.setFrameShape(QFrame.NoFrame)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_9 = QGridLayout(self.page_4)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.page_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 603, 680))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 680))
        self.frame_10.setStyleSheet(u"#frame_10{background-color:#ffffff}\n"
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
"border: 2px solid #54BFC9;\n"
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
"    width:15px;\n"
"    height:15px;\n"
"padding:13px 20px 10px 10px;\n"
"}\n"
"\n"
"QDateEdit::focus{"
                        "\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
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
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"	padding: 10px 10px 10px 20px;\n"
" }\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color:#9CA3AF;\n"
"	font-size:14px;\n"
"	background-color: #F3F4F6;\n"
"	selection-background-color:#54BFC9;\n"
"	selection-color:#FFFFFF;\n"
"	outline: 0px;\n"
"   border: 1px solid #D1D5DB;\n"
" border-radius:8px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/prefijoNuevo/flecha_oscuro.png);\n"
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"/* LISTA */\n"
"\n"
"\n"
""
                        "QListWidget{\n"
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
"\n"
"QListView::item:selected\n"
"{\n"
"    background-color: #F3F4F6; color: #9CA3AF;\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QListView::item:focus\n"
"{\n"
"background: #54BFC9;\n"
"border-radius:8px;\n"
"color:white}\n"
"\n"
"\n"
"QListWidget::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"\n"
"}")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 1))
        self.label_33.setMaximumSize(QSize(16777215, 1))
        self.label_33.setStyleSheet(u"border: 1px solid #D1D5DB;\n"
"")

        self.verticalLayout.addWidget(self.label_33)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 421))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Sunken)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 10, 911, 659))
        self.frame_13.setMinimumSize(QSize(0, 421))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Sunken)
        self.stackedWidget_2 = QStackedWidget(self.frame_13)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 10, 911, 718))
        self.stackedWidget_2.setStyleSheet(u"")
        self.pag_agregarSesion = QWidget()
        self.pag_agregarSesion.setObjectName(u"pag_agregarSesion")
        self.pag_agregarSesion.setMinimumSize(QSize(0, 0))
        self.pag_agregarSesion.setMaximumSize(QSize(16777215, 16777215))
        self.pag_agregarSesion.setStyleSheet(u"#pag_agregarSesion{\n"
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
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"/* DATE */\n"
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
"min-"
                        "width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QDateEdit::up-arrow{\n"
"	image: url(:/prefijoNuevo/comDownP.png);\n"
"     width: 9px;\n"
"     height: 9px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow{\n"
"	image:url(:/prefijoNuevo/comUpP.png);\n"
"     width: 9px;\n"
"     height: 9px;}\n"
"\n"
"QDateEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
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
"padding:10px\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"	padding: 10px 10px 10px 20px;\n"
" }\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color:#9CA3AF;\n"
"	font-size:14px;\n"
"	background-color: #F3F4F6;\n"
"	selection-background-color:#54BFC9;\n"
"	selection-color:#FFFFFF;\n"
"	outline: 0px;\n"
""
                        "   border: 1px solid #D1D5DB;\n"
" border-radius:8px;\n"
"padding:10px\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/prefijoNuevo/flecha_oscuro.png);\n"
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QComboBox {combobox-popup: 0}\n"
"\n"
"/* LISTA */\n"
"\n"
"\n"
"QListWidget{\n"
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
"\n"
"QListView::item:selected\n"
"{\n"
"    background-color: #F3F4F6; color: #9CA3AF;\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QListView::item:focus\n"
"{\n"
"background: #54BFC9;\n"
"border-radius:8px;\n"
"color:white}\n"
"\n"
"\n"
"QListWidget::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*SPINBOX*/\n"
""
                        "/*SPINBOX*/\n"
"QSpinBox,QDoubleSpinBox{\n"
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
"QSpinBox::up-button,QDoubleSpinBox::up-button{\n"
"min-width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QSpinBox::down-button,QDoubleSpinBox::down-button{\n"
"min-width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QSpinBox::up-arrow,QDoubleSpinBox::up-arrow{\n"
"	image: url(:/prefijoNuevo/comDownP.png);\n"
"     width: 9px;\n"
"     height: 9px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow,QDoubleSpinBox::down-arrow{\n"
"	image:url(:/prefijoNuevo/comUpP.png);\n"
"     width: 9px;\n"
"     height: 9px;}\n"
"\n"
"QSpinBox::hover,QDoubleSpinBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QSpinBox::focus{\n"
"background: #FFFF"
                        "FF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
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
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"/* BOTON*/\n"
"/*  BOTON */\n"
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
"\n"
"")
        self.datefecha_atencion = QDateEdit(self.pag_agregarSesion)
        self.datefecha_atencion.setObjectName(u"datefecha_atencion")
        self.datefecha_atencion.setGeometry(QRect(620, 69, 280, 47))
        self.datefecha_atencion.setMinimumSize(QSize(0, 40))
        self.datefecha_atencion.setCursor(QCursor(Qt.PointingHandCursor))
        self.datefecha_atencion.setStyleSheet(u"")
        self.datefecha_atencion.setCalendarPopup(False)
        self.label_84 = QLabel(self.pag_agregarSesion)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(20, 428, 161, 31))
        self.label_79 = QLabel(self.pag_agregarSesion)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(620, 140, 133, 21))
        self.label_80 = QLabel(self.pag_agregarSesion)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(320, 140, 111, 21))
        self.label_81 = QLabel(self.pag_agregarSesion)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(20, 140, 151, 21))
        self.cbox_estadosesion = QComboBox(self.pag_agregarSesion)
        self.cbox_estadosesion.addItem("")
        self.cbox_estadosesion.addItem("")
        self.cbox_estadosesion.addItem("")
        self.cbox_estadosesion.addItem("")
        self.cbox_estadosesion.addItem("")
        self.cbox_estadosesion.addItem("")
        self.cbox_estadosesion.setObjectName(u"cbox_estadosesion")
        self.cbox_estadosesion.setGeometry(QRect(20, 459, 280, 47))
        self.cbox_estadosesion.setMinimumSize(QSize(0, 40))
        self.cbox_estadosesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estadosesion.setStyleSheet(u"")
        self.line_duracion = QLineEdit(self.pag_agregarSesion)
        self.line_duracion.setObjectName(u"line_duracion")
        self.line_duracion.setEnabled(False)
        self.line_duracion.setGeometry(QRect(620, 164, 280, 47))
        self.line_duracion.setMinimumSize(QSize(0, 40))
        self.label_88 = QLabel(self.pag_agregarSesion)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(320, 250, 181, 31))
        self.label_89 = QLabel(self.pag_agregarSesion)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(620, 39, 151, 31))
        self.spin_horafinal = QSpinBox(self.pag_agregarSesion)
        self.spin_horafinal.setObjectName(u"spin_horafinal")
        self.spin_horafinal.setGeometry(QRect(320, 164, 280, 47))
        self.spin_horafinal.setMinimumSize(QSize(0, 40))
        self.spin_horafinal.setMinimum(8)
        self.spin_horafinal.setMaximum(24)
        self.spin_horafinal.setValue(8)
        self.plain_observacion = QPlainTextEdit(self.pag_agregarSesion)
        self.plain_observacion.setObjectName(u"plain_observacion")
        self.plain_observacion.setGeometry(QRect(20, 549, 581, 91))
        self.plain_observacion.setMinimumSize(QSize(0, 0))
        self.plain_observacion.setMaximumSize(QSize(16777215, 16777215))
        self.plain_observacion.setStyleSheet(u"")
        self.label_90 = QLabel(self.pag_agregarSesion)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(320, 340, 280, 31))
        self.label_91 = QLabel(self.pag_agregarSesion)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(620, 250, 181, 31))
        self.label_92 = QLabel(self.pag_agregarSesion)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(20, 39, 191, 31))
        self.spin_monto = QDoubleSpinBox(self.pag_agregarSesion)
        self.spin_monto.setObjectName(u"spin_monto")
        self.spin_monto.setEnabled(False)
        self.spin_monto.setGeometry(QRect(620, 280, 280, 47))
        self.spin_monto.setMinimumSize(QSize(0, 40))
        self.spin_monto.setCursor(QCursor(Qt.PointingHandCursor))
        self.spin_monto.setStyleSheet(u"")
        self.cbox_tipocita = QComboBox(self.pag_agregarSesion)
        self.cbox_tipocita.addItem("")
        self.cbox_tipocita.addItem("")
        self.cbox_tipocita.addItem("")
        self.cbox_tipocita.addItem("")
        self.cbox_tipocita.addItem("")
        self.cbox_tipocita.addItem("")
        self.cbox_tipocita.setObjectName(u"cbox_tipocita")
        self.cbox_tipocita.setGeometry(QRect(20, 280, 280, 47))
        self.cbox_tipocita.setMinimumSize(QSize(0, 40))
        self.cbox_tipocita.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_tipocita.setStyleSheet(u"")
        self.cbox_estadopago = QComboBox(self.pag_agregarSesion)
        self.cbox_estadopago.addItem("")
        self.cbox_estadopago.addItem("")
        self.cbox_estadopago.addItem("")
        self.cbox_estadopago.addItem("")
        self.cbox_estadopago.addItem("")
        self.cbox_estadopago.setObjectName(u"cbox_estadopago")
        self.cbox_estadopago.setEnabled(False)
        self.cbox_estadopago.setGeometry(QRect(20, 370, 280, 47))
        self.cbox_estadopago.setMinimumSize(QSize(0, 40))
        self.cbox_estadopago.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estadopago.setStyleSheet(u"")
        self.cbox_centroatencion = QComboBox(self.pag_agregarSesion)
        self.cbox_centroatencion.addItem("")
        self.cbox_centroatencion.addItem("")
        self.cbox_centroatencion.addItem("")
        self.cbox_centroatencion.addItem("")
        self.cbox_centroatencion.setObjectName(u"cbox_centroatencion")
        self.cbox_centroatencion.setGeometry(QRect(20, 69, 280, 47))
        self.cbox_centroatencion.setMinimumSize(QSize(0, 40))
        self.cbox_centroatencion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_centroatencion.setStyleSheet(u"")
        self.label_93 = QLabel(self.pag_agregarSesion)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(320, 39, 181, 31))
        self.spin_horainicio = QSpinBox(self.pag_agregarSesion)
        self.spin_horainicio.setObjectName(u"spin_horainicio")
        self.spin_horainicio.setGeometry(QRect(20, 164, 280, 47))
        self.spin_horainicio.setMinimumSize(QSize(0, 40))
        self.spin_horainicio.setMinimum(8)
        self.spin_horainicio.setMaximum(24)
        self.spin_horainicio.setValue(8)
        self.label_43 = QLabel(self.pag_agregarSesion)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(20, 0, 221, 21))
        self.label_43.setStyleSheet(u"/*#label{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 21px;\n"
"letter-spacing: 0.02em;\n"
"color: #374151;}\n"
"*/\n"
"#label_43{\n"
"/* H5-medium */\n"
"\n"
"font-family: Roboto ;\n"
"font-style: bold;\n"
"font-weight: 480;\n"
"font-size: 21px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"color: #374151}")
        self.spin_cantidadsesiones = QSpinBox(self.pag_agregarSesion)
        self.spin_cantidadsesiones.setObjectName(u"spin_cantidadsesiones")
        self.spin_cantidadsesiones.setEnabled(False)
        self.spin_cantidadsesiones.setGeometry(QRect(320, 69, 280, 47))
        self.spin_cantidadsesiones.setMinimumSize(QSize(0, 40))
        self.spin_cantidadsesiones.setCursor(QCursor(Qt.PointingHandCursor))
        self.spin_cantidadsesiones.setStyleSheet(u"")
        self.spin_cantidadsesiones.setMinimum(1)
        self.label_94 = QLabel(self.pag_agregarSesion)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(20, 250, 280, 31))
        self.date_fechapago = QDateEdit(self.pag_agregarSesion)
        self.date_fechapago.setObjectName(u"date_fechapago")
        self.date_fechapago.setEnabled(False)
        self.date_fechapago.setGeometry(QRect(320, 370, 280, 47))
        self.date_fechapago.setMinimumSize(QSize(0, 40))
        self.date_fechapago.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_fechapago.setStyleSheet(u"")
        self.date_fechapago.setCalendarPopup(False)
        self.label_95 = QLabel(self.pag_agregarSesion)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(20, 520, 161, 31))
        self.label_96 = QLabel(self.pag_agregarSesion)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(20, 340, 280, 31))
        self.label_97 = QLabel(self.pag_agregarSesion)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(620, 340, 151, 31))
        self.line_2 = QFrame(self.pag_agregarSesion)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 225, 881, 16))
        self.line_2.setStyleSheet(u"\n"
"color: #D1D5DB\n"
"")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.cbox_mediopago = QComboBox(self.pag_agregarSesion)
        self.cbox_mediopago.addItem("")
        self.cbox_mediopago.addItem("")
        self.cbox_mediopago.addItem("")
        self.cbox_mediopago.addItem("")
        self.cbox_mediopago.addItem("")
        self.cbox_mediopago.addItem("")
        self.cbox_mediopago.addItem("")
        self.cbox_mediopago.addItem("")
        self.cbox_mediopago.setObjectName(u"cbox_mediopago")
        self.cbox_mediopago.setEnabled(False)
        self.cbox_mediopago.setGeometry(QRect(620, 370, 281, 47))
        self.cbox_mediopago.setMinimumSize(QSize(0, 40))
        self.cbox_mediopago.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_mediopago.setStyleSheet(u"")
        self.line_costoasignado = QDoubleSpinBox(self.pag_agregarSesion)
        self.line_costoasignado.setObjectName(u"line_costoasignado")
        self.line_costoasignado.setEnabled(False)
        self.line_costoasignado.setGeometry(QRect(320, 280, 280, 47))
        self.line_costoasignado.setMinimumSize(QSize(0, 40))
        self.line_costoasignado.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_costoasignado.setStyleSheet(u"")
        self.frame_invisible = QFrame(self.pag_agregarSesion)
        self.frame_invisible.setObjectName(u"frame_invisible")
        self.frame_invisible.setGeometry(QRect(310, 430, 601, 81))
        self.frame_invisible.setFrameShape(QFrame.NoFrame)
        self.frame_invisible.setFrameShadow(QFrame.Raised)
        self.label_109 = QLabel(self.frame_invisible)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(10, 0, 161, 31))
        self.date_fechantigua = QDateEdit(self.frame_invisible)
        self.date_fechantigua.setObjectName(u"date_fechantigua")
        self.date_fechantigua.setEnabled(False)
        self.date_fechantigua.setGeometry(QRect(10, 29, 280, 47))
        self.date_fechantigua.setMinimumSize(QSize(0, 40))
        self.date_fechantigua.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_fechantigua.setStyleSheet(u"")
        self.date_fechantigua.setCalendarPopup(False)
        self.date_reprogramacion = QDateEdit(self.frame_invisible)
        self.date_reprogramacion.setObjectName(u"date_reprogramacion")
        self.date_reprogramacion.setGeometry(QRect(310, 30, 280, 47))
        self.date_reprogramacion.setMinimumSize(QSize(0, 40))
        self.date_reprogramacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_reprogramacion.setStyleSheet(u"")
        self.date_reprogramacion.setCalendarPopup(False)
        self.label_86 = QLabel(self.frame_invisible)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(310, 1, 161, 31))
        self.stackedWidget_2.addWidget(self.pag_agregarSesion)
        self.pag_editarSesion = QWidget()
        self.pag_editarSesion.setObjectName(u"pag_editarSesion")
        self.pag_editarSesion.setStyleSheet(u"#pag_editarSesion{\n"
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
"QLineEdit::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"/* DATE */\n"
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
"min-w"
                        "idth: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QDateEdit::up-arrow{\n"
"	image: url(:/prefijoNuevo/comDownP.png);\n"
"     width: 9px;\n"
"     height: 9px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow{\n"
"	image:url(:/prefijoNuevo/comUpP.png);\n"
"     width: 9px;\n"
"     height: 9px;}\n"
"\n"
"QDateEdit::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
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
"padding:10px\n"
"}\n"
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
"	selection-background-color:#54BFC9;\n"
"	selection-color:#FFFFFF;\n"
"	outline: 0px;\n"
"   bo"
                        "rder: 1px solid #D1D5DB;\n"
" border-radius:8px;\n"
"padding:10px\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/prefijoNuevo/flecha_oscuro.png);\n"
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QComboBox {combobox-popup: 0}\n"
"\n"
"\n"
"\n"
"/* LISTA */\n"
"\n"
"\n"
"QListWidget{\n"
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
"\n"
"QListView::item:selected\n"
"{\n"
"    background-color: #F3F4F6; color: #9CA3AF;\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QListView::item:hover\n"
"{\n"
"background: #54BFC9;\n"
"border-radius:8px;\n"
"color:white}\n"
"\n"
"\n"
"QListWidget::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*SPINBOX"
                        "*/\n"
"QSpinBox,QDoubleSpinBox{\n"
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
"QSpinBox::up-button,QDoubleSpinBox::up-button{\n"
"min-width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QSpinBox::down-button,QDoubleSpinBox::down-button{\n"
"min-width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QSpinBox::up-arrow,QDoubleSpinBox::up-arrow{\n"
"	image: url(:/prefijoNuevo/comDownP.png);\n"
"     width: 9px;\n"
"     height: 9px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow,QDoubleSpinBox::down-arrow{\n"
"	image:url(:/prefijoNuevo/comUpP.png);\n"
"     width: 9px;\n"
"     height: 9px;}\n"
"\n"
"QSpinBox::hover,QDoubleSpinBox::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QSpinBox::focus{\n"
"background: #FFFFFF;\n"
"b"
                        "order: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
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
"QPlainTextEdit::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"/* BOTON*/\n"
"/*  BOTON */\n"
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
        self.spin_cantidadsesiones2 = QSpinBox(self.pag_editarSesion)
        self.spin_cantidadsesiones2.setObjectName(u"spin_cantidadsesiones2")
        self.spin_cantidadsesiones2.setEnabled(False)
        self.spin_cantidadsesiones2.setGeometry(QRect(320, 69, 280, 47))
        self.spin_cantidadsesiones2.setMinimumSize(QSize(0, 40))
        self.spin_cantidadsesiones2.setCursor(QCursor(Qt.PointingHandCursor))
        self.spin_cantidadsesiones2.setStyleSheet(u"")
        self.spin_cantidadsesiones2.setMinimum(1)
        self.cbox_estadopago2 = QComboBox(self.pag_editarSesion)
        self.cbox_estadopago2.addItem("")
        self.cbox_estadopago2.addItem("")
        self.cbox_estadopago2.addItem("")
        self.cbox_estadopago2.addItem("")
        self.cbox_estadopago2.addItem("")
        self.cbox_estadopago2.setObjectName(u"cbox_estadopago2")
        self.cbox_estadopago2.setGeometry(QRect(20, 370, 280, 47))
        self.cbox_estadopago2.setMinimumSize(QSize(0, 40))
        self.cbox_estadopago2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estadopago2.setStyleSheet(u"")
        self.spin_horainicio2 = QSpinBox(self.pag_editarSesion)
        self.spin_horainicio2.setObjectName(u"spin_horainicio2")
        self.spin_horainicio2.setGeometry(QRect(20, 164, 280, 47))
        self.spin_horainicio2.setMinimumSize(QSize(0, 40))
        self.spin_horainicio2.setMinimum(8)
        self.spin_horainicio2.setMaximum(21)
        self.spin_horainicio2.setValue(8)
        self.label_51 = QLabel(self.pag_editarSesion)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(20, 0, 151, 21))
        self.label_51.setStyleSheet(u"/*#label{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 21px;\n"
"letter-spacing: 0.02em;\n"
"color: #374151;}\n"
"*/\n"
"#label_51{\n"
"/* H5-medium */\n"
"\n"
"font-family: Roboto ;\n"
"font-style: bold;\n"
"font-weight: 480;\n"
"font-size: 21px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"color: #374151}")
        self.label_111 = QLabel(self.pag_editarSesion)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(20, 250, 280, 31))
        self.line_4 = QFrame(self.pag_editarSesion)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(20, 223, 881, 20))
        self.line_4.setStyleSheet(u"\n"
"color: #D1D5DB\n"
"")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.HLine)
        self.spin_horafinal2 = QSpinBox(self.pag_editarSesion)
        self.spin_horafinal2.setObjectName(u"spin_horafinal2")
        self.spin_horafinal2.setGeometry(QRect(320, 164, 280, 47))
        self.spin_horafinal2.setMinimumSize(QSize(0, 40))
        self.spin_horafinal2.setMinimum(8)
        self.spin_horafinal2.setMaximum(21)
        self.datefecha_atencion2 = QDateEdit(self.pag_editarSesion)
        self.datefecha_atencion2.setObjectName(u"datefecha_atencion2")
        self.datefecha_atencion2.setGeometry(QRect(620, 69, 280, 47))
        self.datefecha_atencion2.setMinimumSize(QSize(0, 40))
        self.datefecha_atencion2.setCursor(QCursor(Qt.PointingHandCursor))
        self.datefecha_atencion2.setStyleSheet(u"")
        self.datefecha_atencion2.setCalendarPopup(False)
        self.cbox_centroatencion2 = QComboBox(self.pag_editarSesion)
        self.cbox_centroatencion2.addItem("")
        self.cbox_centroatencion2.addItem("")
        self.cbox_centroatencion2.addItem("")
        self.cbox_centroatencion2.addItem("")
        self.cbox_centroatencion2.setObjectName(u"cbox_centroatencion2")
        self.cbox_centroatencion2.setGeometry(QRect(20, 69, 280, 47))
        self.cbox_centroatencion2.setMinimumSize(QSize(0, 40))
        self.cbox_centroatencion2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_centroatencion2.setStyleSheet(u"")
        self.label_112 = QLabel(self.pag_editarSesion)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(20, 140, 151, 21))
        self.label_113 = QLabel(self.pag_editarSesion)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(320, 250, 181, 31))
        self.label_114 = QLabel(self.pag_editarSesion)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(20, 340, 280, 31))
        self.label_115 = QLabel(self.pag_editarSesion)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(620, 340, 131, 31))
        self.date_fechapago2 = QDateEdit(self.pag_editarSesion)
        self.date_fechapago2.setObjectName(u"date_fechapago2")
        self.date_fechapago2.setGeometry(QRect(320, 370, 280, 47))
        self.date_fechapago2.setMinimumSize(QSize(0, 40))
        self.date_fechapago2.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_fechapago2.setStyleSheet(u"")
        self.date_fechapago2.setCalendarPopup(False)
        self.label_116 = QLabel(self.pag_editarSesion)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(20, 39, 191, 31))
        self.label_117 = QLabel(self.pag_editarSesion)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(620, 39, 141, 31))
        self.label_118 = QLabel(self.pag_editarSesion)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(620, 140, 133, 21))
        self.cbox_mediopago2 = QComboBox(self.pag_editarSesion)
        self.cbox_mediopago2.addItem("")
        self.cbox_mediopago2.addItem("")
        self.cbox_mediopago2.addItem("")
        self.cbox_mediopago2.addItem("")
        self.cbox_mediopago2.addItem("")
        self.cbox_mediopago2.addItem("")
        self.cbox_mediopago2.addItem("")
        self.cbox_mediopago2.addItem("")
        self.cbox_mediopago2.setObjectName(u"cbox_mediopago2")
        self.cbox_mediopago2.setGeometry(QRect(620, 370, 281, 47))
        self.cbox_mediopago2.setMinimumSize(QSize(0, 40))
        self.cbox_mediopago2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_mediopago2.setStyleSheet(u"")
        self.line_duracion2 = QLineEdit(self.pag_editarSesion)
        self.line_duracion2.setObjectName(u"line_duracion2")
        self.line_duracion2.setEnabled(False)
        self.line_duracion2.setGeometry(QRect(620, 164, 280, 47))
        self.line_duracion2.setMinimumSize(QSize(0, 40))
        self.label_119 = QLabel(self.pag_editarSesion)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(320, 140, 111, 21))
        self.label_120 = QLabel(self.pag_editarSesion)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(320, 39, 181, 31))
        self.spin_monto2 = QDoubleSpinBox(self.pag_editarSesion)
        self.spin_monto2.setObjectName(u"spin_monto2")
        self.spin_monto2.setEnabled(True)
        self.spin_monto2.setGeometry(QRect(620, 280, 280, 47))
        self.spin_monto2.setMinimumSize(QSize(0, 40))
        self.spin_monto2.setCursor(QCursor(Qt.PointingHandCursor))
        self.spin_monto2.setStyleSheet(u"")
        self.plain_observacion2 = QPlainTextEdit(self.pag_editarSesion)
        self.plain_observacion2.setObjectName(u"plain_observacion2")
        self.plain_observacion2.setGeometry(QRect(20, 549, 581, 91))
        self.plain_observacion2.setMinimumSize(QSize(0, 0))
        self.plain_observacion2.setMaximumSize(QSize(16777215, 16777215))
        self.plain_observacion2.setStyleSheet(u"")
        self.label_121 = QLabel(self.pag_editarSesion)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(20, 428, 161, 31))
        self.label_122 = QLabel(self.pag_editarSesion)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(320, 340, 280, 31))
        self.label_123 = QLabel(self.pag_editarSesion)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(20, 518, 161, 31))
        self.label_124 = QLabel(self.pag_editarSesion)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setGeometry(QRect(620, 250, 181, 31))
        self.cbox_estadosesion2 = QComboBox(self.pag_editarSesion)
        self.cbox_estadosesion2.addItem("")
        self.cbox_estadosesion2.addItem("")
        self.cbox_estadosesion2.addItem("")
        self.cbox_estadosesion2.addItem("")
        self.cbox_estadosesion2.addItem("")
        self.cbox_estadosesion2.addItem("")
        self.cbox_estadosesion2.setObjectName(u"cbox_estadosesion2")
        self.cbox_estadosesion2.setGeometry(QRect(20, 460, 280, 47))
        self.cbox_estadosesion2.setMinimumSize(QSize(0, 40))
        self.cbox_estadosesion2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estadosesion2.setStyleSheet(u"")
        self.frame_20 = QFrame(self.pag_editarSesion)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(310, 439, 601, 81))
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.date_fechantigua2 = QDateEdit(self.frame_20)
        self.date_fechantigua2.setObjectName(u"date_fechantigua2")
        self.date_fechantigua2.setEnabled(False)
        self.date_fechantigua2.setGeometry(QRect(10, 20, 280, 47))
        self.date_fechantigua2.setMinimumSize(QSize(0, 40))
        self.date_fechantigua2.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_fechantigua2.setStyleSheet(u"")
        self.date_fechantigua2.setCalendarPopup(False)
        self.label_125 = QLabel(self.frame_20)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(10, -9, 161, 31))
        self.date_reprogramacion2 = QDateEdit(self.frame_20)
        self.date_reprogramacion2.setObjectName(u"date_reprogramacion2")
        self.date_reprogramacion2.setGeometry(QRect(310, 20, 280, 47))
        self.date_reprogramacion2.setMinimumSize(QSize(0, 40))
        self.date_reprogramacion2.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_reprogramacion2.setStyleSheet(u"")
        self.date_reprogramacion2.setCalendarPopup(False)
        self.label_126 = QLabel(self.frame_20)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setGeometry(QRect(310, -9, 201, 31))
        self.line_costoasignado2 = QDoubleSpinBox(self.pag_editarSesion)
        self.line_costoasignado2.setObjectName(u"line_costoasignado2")
        self.line_costoasignado2.setEnabled(False)
        self.line_costoasignado2.setGeometry(QRect(320, 280, 280, 47))
        self.line_costoasignado2.setMinimumSize(QSize(0, 40))
        self.line_costoasignado2.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_costoasignado2.setStyleSheet(u"")
        self.cbox_tipocita2 = QComboBox(self.pag_editarSesion)
        self.cbox_tipocita2.addItem("")
        self.cbox_tipocita2.addItem("")
        self.cbox_tipocita2.addItem("")
        self.cbox_tipocita2.addItem("")
        self.cbox_tipocita2.addItem("")
        self.cbox_tipocita2.addItem("")
        self.cbox_tipocita2.setObjectName(u"cbox_tipocita2")
        self.cbox_tipocita2.setGeometry(QRect(20, 280, 280, 47))
        self.cbox_tipocita2.setMinimumSize(QSize(0, 40))
        self.cbox_tipocita2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_tipocita2.setStyleSheet(u"")
        self.stackedWidget_2.addWidget(self.pag_editarSesion)

        self.verticalLayout.addWidget(self.frame_11)


        self.gridLayout_10.addWidget(self.frame_10, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_9.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.page_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 66))
        self.frame_9.setStyleSheet(u"#frame_9{background-color: #f1f1f1; \n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;}\n"
"\n"
"\n"
"\n"
"/*  BOTON */\n"
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
"\n"
"")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.btn_actualizar_sesion = QPushButton(self.frame_9)
        self.btn_actualizar_sesion.setObjectName(u"btn_actualizar_sesion")
        self.btn_actualizar_sesion.setGeometry(QRect(760, 10, 151, 47))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_actualizar_sesion.sizePolicy().hasHeightForWidth())
        self.btn_actualizar_sesion.setSizePolicy(sizePolicy)
        self.btn_actualizar_sesion.setSizeIncrement(QSize(0, 0))
        self.btn_actualizar_sesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_actualizar_sesion.setFocusPolicy(Qt.NoFocus)
        self.btn_actualizar_sesion.setAutoFillBackground(False)
        self.btn_actualizar_sesion.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/anadir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_actualizar_sesion.setIcon(icon1)
        self.btn_actualizar_sesion.setIconSize(QSize(21, 35))
        self.btn_actualizar_sesion.setCheckable(False)
        self.btn_actualizar_sesion.setAutoRepeat(False)
        self.btn_actualizar_sesion.setAutoExclusive(False)
        self.btn_actualizar_sesion.setAutoDefault(False)
        self.btn_actualizar_sesion.setFlat(False)
        self.btn_cancelar = QPushButton(self.frame_9)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(600, 10, 151, 47))
        self.btn_cancelar.setFocusPolicy(Qt.NoFocus)
        self.btn_agregar_sesion = QPushButton(self.frame_9)
        self.btn_agregar_sesion.setObjectName(u"btn_agregar_sesion")
        self.btn_agregar_sesion.setGeometry(QRect(760, 10, 151, 47))
        sizePolicy.setHeightForWidth(self.btn_agregar_sesion.sizePolicy().hasHeightForWidth())
        self.btn_agregar_sesion.setSizePolicy(sizePolicy)
        self.btn_agregar_sesion.setSizeIncrement(QSize(0, 0))
        self.btn_agregar_sesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_sesion.setFocusPolicy(Qt.NoFocus)
        self.btn_agregar_sesion.setAutoFillBackground(False)
        self.btn_agregar_sesion.setStyleSheet(u"")
        self.btn_agregar_sesion.setIcon(icon1)
        self.btn_agregar_sesion.setIconSize(QSize(21, 35))
        self.btn_agregar_sesion.setCheckable(False)
        self.btn_agregar_sesion.setAutoRepeat(False)
        self.btn_agregar_sesion.setAutoExclusive(False)
        self.btn_agregar_sesion.setAutoDefault(False)
        self.btn_agregar_sesion.setFlat(False)

        self.gridLayout_9.addWidget(self.frame_9, 1, 0, 1, 1)

        self.stack_principal.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: #f1f1f1;\n"
"border-bottom-right-radius: 10;\n"
"border-bottom-left-radius: 10;")
        self.label_39 = QLabel(self.page_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(20, 30, 241, 31))
        self.label_39.setStyleSheet(u"QLabel{\n"
"font-family: Roboto ;\n"
"font-style: bold;\n"
"font-weight: 480;\n"
"font-size: 21px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"color: #374151}")
        self.frame_17 = QFrame(self.page_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(14, 80, 591, 341))
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
        self.tabla_sesion = QTableWidget(self.frame_17)
        if (self.tabla_sesion.columnCount() < 4):
            self.tabla_sesion.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_sesion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_sesion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_sesion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_sesion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tabla_sesion.rowCount() < 3):
            self.tabla_sesion.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_sesion.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_sesion.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_sesion.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_sesion.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_sesion.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_sesion.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_sesion.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_sesion.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_sesion.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_sesion.setItem(1, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_sesion.setItem(1, 3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_sesion.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_sesion.setItem(2, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_sesion.setItem(2, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_sesion.setItem(2, 3, __qtablewidgetitem18)
        self.tabla_sesion.setObjectName(u"tabla_sesion")
        self.tabla_sesion.setStyleSheet(u"QTableWidget {\n"
"outline: 0px;\n"
"border:2px solid #f3f4f6;\n"
"border-radius:18px;\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 19px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* cabezera*/\n"
"QHeaderView::section {\n"
"border-style: none;\n"
"height:50px;\n"
"font-family: \"Roboto\";\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal{\n"
"font-family: Roboto;\n"
"font-style:normal ;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"letter-spacing: 0.04em;\n"
"color:#212529;\n"
"background-color:#F1F1F1 ;\n"
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
"QTableWidget::item {\n"
"	border-"
                        "bottom: 4px solid #f3f4f6;\n"
"border-style:ridge\n"
"\n"
"}\n"
"\n"
"QTableWidget:item:selected{\n"
"	background:white;/*color-seleccion*/\n"
"color: #54bfc9;\n"
"}\n"
"\n"
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
"	height: 0 px;\n"
"}\n"
"\n"
"")
        self.tabla_sesion.setFrameShape(QFrame.NoFrame)
        self.tabla_sesion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_sesion.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_sesion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_sesion.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_sesion.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_sesion.setShowGrid(False)
        self.tabla_sesion.setSortingEnabled(False)
        self.tabla_sesion.horizontalHeader().setMinimumSectionSize(39)
        self.tabla_sesion.horizontalHeader().setHighlightSections(False)
        self.tabla_sesion.verticalHeader().setVisible(False)
        self.tabla_sesion.verticalHeader().setMinimumSectionSize(23)
        self.tabla_sesion.verticalHeader().setDefaultSectionSize(41)

        self.gridLayout_30.addWidget(self.tabla_sesion, 0, 0, 1, 1)

        self.cbox_rangosesiones = QComboBox(self.page_2)
        self.cbox_rangosesiones.addItem("")
        self.cbox_rangosesiones.addItem("")
        self.cbox_rangosesiones.addItem("")
        self.cbox_rangosesiones.addItem("")
        self.cbox_rangosesiones.setObjectName(u"cbox_rangosesiones")
        self.cbox_rangosesiones.setGeometry(QRect(92, 440, 71, 38))
        self.cbox_rangosesiones.setMinimumSize(QSize(0, 0))
        self.cbox_rangosesiones.setMaximumSize(QSize(92, 38))
        self.cbox_rangosesiones.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_rangosesiones.setStyleSheet(u"QComboBox{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: #FFFFFF;\n"
"color:#9CA3AF;\n"
"border-radius:8px;\n"
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
"\n"
"QComboBox QAbstractItemView {\n"
"	color:#9CA3AF;\n"
"	font-size:14px;\n"
"	background-color: #F3F4F6;\n"
"	selection-background-color:#54BFC9;\n"
"	selection-color:#FFFFFF;\n"
"	outline: 0px;\n"
"   border: 1px solid #D1D5DB;\n"
" border-radius:8px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"\n"
"	image: url(:/prefijoNuevo/flecha_oscuro.png);\n"
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox {combobox-popup: 0}")
        self.btn_agregarses = QPushButton(self.page_2)
        self.btn_agregarses.setObjectName(u"btn_agregarses")
        self.btn_agregarses.setGeometry(QRect(430, 20, 161, 40))
        sizePolicy.setHeightForWidth(self.btn_agregarses.sizePolicy().hasHeightForWidth())
        self.btn_agregarses.setSizePolicy(sizePolicy)
        self.btn_agregarses.setSizeIncrement(QSize(0, 0))
        self.btn_agregarses.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregarses.setFocusPolicy(Qt.NoFocus)
        self.btn_agregarses.setAutoFillBackground(False)
        self.btn_agregarses.setStyleSheet(u"\n"
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
        self.btn_agregarses.setIcon(icon2)
        self.btn_agregarses.setIconSize(QSize(12, 38))
        self.btn_agregarses.setCheckable(False)
        self.btn_agregarses.setAutoRepeat(False)
        self.btn_agregarses.setAutoExclusive(False)
        self.btn_agregarses.setAutoDefault(False)
        self.btn_agregarses.setFlat(False)
        self.label_44 = QLabel(self.page_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(20, 441, 71, 31))
        self.label_44.setMinimumSize(QSize(0, 0))
        self.label_44.setMaximumSize(QSize(16777215, 16777215))
        self.label_44.setStyleSheet(u"QLabel{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 450;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;}\n"
"")
        self.label_45 = QLabel(self.page_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(172, 440, 81, 31))
        self.label_45.setMinimumSize(QSize(0, 0))
        self.label_45.setMaximumSize(QSize(16777215, 16777215))
        self.label_45.setStyleSheet(u"QLabel{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 450;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;}\n"
"")
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
        self.btn_closeseguimiento = QToolButton(self.frame_19)
        self.btn_closeseguimiento.setObjectName(u"btn_closeseguimiento")
        self.btn_closeseguimiento.setGeometry(QRect(590, 10, 25, 25))
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
"\n"
"\n"
"#btn_closeseguimiento:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeseguimiento.setIcon(icon3)
        self.btn_closeseguimiento.setIconSize(QSize(13, 13))
        self.btn_closeseguimiento.setAutoRaise(True)
        self.lbl_nombreestudiante = QLabel(self.frame_19)
        self.lbl_nombreestudiante.setObjectName(u"lbl_nombreestudiante")
        self.lbl_nombreestudiante.setGeometry(QRect(20, 29, 411, 20))
        self.lbl_nombreestudiante.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")

        self.gridLayout.addWidget(self.frame_19, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.cbox_centroatencion, self.spin_cantidadsesiones)
        QWidget.setTabOrder(self.spin_cantidadsesiones, self.datefecha_atencion)
        QWidget.setTabOrder(self.datefecha_atencion, self.spin_horainicio)
        QWidget.setTabOrder(self.spin_horainicio, self.spin_horafinal)
        QWidget.setTabOrder(self.spin_horafinal, self.line_duracion)
        QWidget.setTabOrder(self.line_duracion, self.cbox_tipocita)
        QWidget.setTabOrder(self.cbox_tipocita, self.line_costoasignado)
        QWidget.setTabOrder(self.line_costoasignado, self.spin_monto)
        QWidget.setTabOrder(self.spin_monto, self.cbox_estadopago)
        QWidget.setTabOrder(self.cbox_estadopago, self.date_fechapago)
        QWidget.setTabOrder(self.date_fechapago, self.cbox_mediopago)
        QWidget.setTabOrder(self.cbox_mediopago, self.cbox_estadosesion)
        QWidget.setTabOrder(self.cbox_estadosesion, self.date_fechantigua)
        QWidget.setTabOrder(self.date_fechantigua, self.date_reprogramacion)
        QWidget.setTabOrder(self.date_reprogramacion, self.plain_observacion)
        QWidget.setTabOrder(self.plain_observacion, self.cbox_centroatencion2)
        QWidget.setTabOrder(self.cbox_centroatencion2, self.spin_cantidadsesiones2)
        QWidget.setTabOrder(self.spin_cantidadsesiones2, self.datefecha_atencion2)
        QWidget.setTabOrder(self.datefecha_atencion2, self.spin_horainicio2)
        QWidget.setTabOrder(self.spin_horainicio2, self.spin_horafinal2)
        QWidget.setTabOrder(self.spin_horafinal2, self.line_duracion2)
        QWidget.setTabOrder(self.line_duracion2, self.cbox_tipocita2)
        QWidget.setTabOrder(self.cbox_tipocita2, self.line_costoasignado2)
        QWidget.setTabOrder(self.line_costoasignado2, self.spin_monto2)
        QWidget.setTabOrder(self.spin_monto2, self.cbox_estadopago2)
        QWidget.setTabOrder(self.cbox_estadopago2, self.date_fechapago2)
        QWidget.setTabOrder(self.date_fechapago2, self.cbox_mediopago2)
        QWidget.setTabOrder(self.cbox_mediopago2, self.cbox_estadosesion2)
        QWidget.setTabOrder(self.cbox_estadosesion2, self.date_fechantigua2)
        QWidget.setTabOrder(self.date_fechantigua2, self.date_reprogramacion2)
        QWidget.setTabOrder(self.date_reprogramacion2, self.plain_observacion2)
        QWidget.setTabOrder(self.plain_observacion2, self.scrollArea_4)
        QWidget.setTabOrder(self.scrollArea_4, self.tabla_sesion)
        QWidget.setTabOrder(self.tabla_sesion, self.cbox_rangosesiones)

        self.retranslateUi(Seguimiento)

        self.stack_principal.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.btn_actualizar_sesion.setDefault(False)
        self.btn_agregar_sesion.setDefault(False)
        self.btn_agregarses.setDefault(False)


        QMetaObject.connectSlotsByName(Seguimiento)
    # setupUi

    def retranslateUi(self, Seguimiento):
        Seguimiento.setWindowTitle(QCoreApplication.translate("Seguimiento", u"Sesiones", None))
        self.label_33.setText("")
        self.datefecha_atencion.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.label_84.setText(QCoreApplication.translate("Seguimiento", u"Estado sesi\u00f3n*", None))
        self.label_79.setText(QCoreApplication.translate("Seguimiento", u"Duracion sesi\u00f3n*", None))
        self.label_80.setText(QCoreApplication.translate("Seguimiento", u"Hora final*", None))
        self.label_81.setText(QCoreApplication.translate("Seguimiento", u"Hora inicio*", None))
        self.cbox_estadosesion.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_estadosesion.setItemText(1, QCoreApplication.translate("Seguimiento", u"Pendiente", None))
        self.cbox_estadosesion.setItemText(2, QCoreApplication.translate("Seguimiento", u"Asisti\u00f3", None))
        self.cbox_estadosesion.setItemText(3, QCoreApplication.translate("Seguimiento", u"Tardanza", None))
        self.cbox_estadosesion.setItemText(4, QCoreApplication.translate("Seguimiento", u"Reprogramado", None))
        self.cbox_estadosesion.setItemText(5, QCoreApplication.translate("Seguimiento", u"Falta injustificada", None))

        self.line_duracion.setText(QCoreApplication.translate("Seguimiento", u"1", None))
        self.label_88.setText(QCoreApplication.translate("Seguimiento", u"Costo Asignado*", None))
        self.label_89.setText(QCoreApplication.translate("Seguimiento", u"Fecha de atenci\u00f3n*", None))
        self.spin_horafinal.setSuffix(QCoreApplication.translate("Seguimiento", u":59", None))
        self.spin_horafinal.setPrefix("")
        self.label_90.setText(QCoreApplication.translate("Seguimiento", u"Fecha de pago*", None))
        self.label_91.setText(QCoreApplication.translate("Seguimiento", u"Costo Pagar*", None))
        self.label_92.setText(QCoreApplication.translate("Seguimiento", u"Centro de atenci\u00f3n*", None))
        self.spin_monto.setPrefix(QCoreApplication.translate("Seguimiento", u"S/.", None))
        self.spin_monto.setSuffix("")
        self.cbox_tipocita.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_tipocita.setItemText(1, QCoreApplication.translate("Seguimiento", u"Individual", None))
        self.cbox_tipocita.setItemText(2, QCoreApplication.translate("Seguimiento", u"Pareja", None))
        self.cbox_tipocita.setItemText(3, QCoreApplication.translate("Seguimiento", u"Familiar", None))
        self.cbox_tipocita.setItemText(4, QCoreApplication.translate("Seguimiento", u"Evaluaci\u00f3n", None))
        self.cbox_tipocita.setItemText(5, QCoreApplication.translate("Seguimiento", u"Emdr", None))

        self.cbox_estadopago.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_estadopago.setItemText(1, QCoreApplication.translate("Seguimiento", u"Pago pendiente", None))
        self.cbox_estadopago.setItemText(2, QCoreApplication.translate("Seguimiento", u"Pag\u00f3 adelantado", None))
        self.cbox_estadopago.setItemText(3, QCoreApplication.translate("Seguimiento", u"Pag\u00f3 mismo d\u00eda", None))
        self.cbox_estadopago.setItemText(4, QCoreApplication.translate("Seguimiento", u"Ayuda total", None))

        self.cbox_centroatencion.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_centroatencion.setItemText(1, QCoreApplication.translate("Seguimiento", u"Centro padma", None))
        self.cbox_centroatencion.setItemText(2, QCoreApplication.translate("Seguimiento", u"Centro m\u00e9dico", None))
        self.cbox_centroatencion.setItemText(3, QCoreApplication.translate("Seguimiento", u"Virtual", None))

        self.label_93.setText(QCoreApplication.translate("Seguimiento", u"Cantidad de sesiones*", None))
        self.spin_horainicio.setSuffix(QCoreApplication.translate("Seguimiento", u":00", None))
        self.label_43.setText(QCoreApplication.translate("Seguimiento", u"Agregar sesi\u00f3n", None))
        self.label_94.setText(QCoreApplication.translate("Seguimiento", u"Tipo cita*", None))
        self.date_fechapago.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.label_95.setText(QCoreApplication.translate("Seguimiento", u"Obervaci\u00f3n", None))
        self.label_96.setText(QCoreApplication.translate("Seguimiento", u"Estado de pago*", None))
        self.label_97.setText(QCoreApplication.translate("Seguimiento", u"Medio de pago*", None))
        self.cbox_mediopago.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_mediopago.setItemText(1, QCoreApplication.translate("Seguimiento", u"BBVA Padma", None))
        self.cbox_mediopago.setItemText(2, QCoreApplication.translate("Seguimiento", u"BCP Carmen", None))
        self.cbox_mediopago.setItemText(3, QCoreApplication.translate("Seguimiento", u"YAPE Carmen", None))
        self.cbox_mediopago.setItemText(4, QCoreApplication.translate("Seguimiento", u"PLIN Carmen", None))
        self.cbox_mediopago.setItemText(5, QCoreApplication.translate("Seguimiento", u"Efectivo", None))
        self.cbox_mediopago.setItemText(6, QCoreApplication.translate("Seguimiento", u"Convenio H&I", None))
        self.cbox_mediopago.setItemText(7, QCoreApplication.translate("Seguimiento", u"Convenio Tejiendo sonrisas", None))

        self.line_costoasignado.setPrefix(QCoreApplication.translate("Seguimiento", u"S/.", None))
        self.line_costoasignado.setSuffix("")
        self.label_109.setText(QCoreApplication.translate("Seguimiento", u"Fecha Antigua", None))
        self.date_fechantigua.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.date_reprogramacion.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.label_86.setText(QCoreApplication.translate("Seguimiento", u"Fecha reprogramada", None))
        self.cbox_estadopago2.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_estadopago2.setItemText(1, QCoreApplication.translate("Seguimiento", u"Pago pendiente", None))
        self.cbox_estadopago2.setItemText(2, QCoreApplication.translate("Seguimiento", u"Pag\u00f3 adelantado", None))
        self.cbox_estadopago2.setItemText(3, QCoreApplication.translate("Seguimiento", u"Pag\u00f3 mismo d\u00eda", None))
        self.cbox_estadopago2.setItemText(4, QCoreApplication.translate("Seguimiento", u"Ayuda total", None))

        self.spin_horainicio2.setSuffix(QCoreApplication.translate("Seguimiento", u":00", None))
        self.label_51.setText(QCoreApplication.translate("Seguimiento", u"Editar sesi\u00f3n", None))
        self.label_111.setText(QCoreApplication.translate("Seguimiento", u"Tipo cita*", None))
        self.spin_horafinal2.setSuffix(QCoreApplication.translate("Seguimiento", u":59", None))
        self.datefecha_atencion2.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.cbox_centroatencion2.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_centroatencion2.setItemText(1, QCoreApplication.translate("Seguimiento", u"Centro padma", None))
        self.cbox_centroatencion2.setItemText(2, QCoreApplication.translate("Seguimiento", u"Centro m\u00e9dico", None))
        self.cbox_centroatencion2.setItemText(3, QCoreApplication.translate("Seguimiento", u"Virtual", None))

        self.label_112.setText(QCoreApplication.translate("Seguimiento", u"Hora inicio*", None))
        self.label_113.setText(QCoreApplication.translate("Seguimiento", u"Costo Asignado*", None))
        self.label_114.setText(QCoreApplication.translate("Seguimiento", u"Estado de pago*", None))
        self.label_115.setText(QCoreApplication.translate("Seguimiento", u"Medio de pago*", None))
        self.date_fechapago2.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.label_116.setText(QCoreApplication.translate("Seguimiento", u"Centro de atenci\u00f3n*", None))
        self.label_117.setText(QCoreApplication.translate("Seguimiento", u"Fecha de atenci\u00f3n*", None))
        self.label_118.setText(QCoreApplication.translate("Seguimiento", u"Duracion sesi\u00f3n*", None))
        self.cbox_mediopago2.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_mediopago2.setItemText(1, QCoreApplication.translate("Seguimiento", u"BBVA Padma", None))
        self.cbox_mediopago2.setItemText(2, QCoreApplication.translate("Seguimiento", u"BCP Carmen", None))
        self.cbox_mediopago2.setItemText(3, QCoreApplication.translate("Seguimiento", u"YAPE Carmen", None))
        self.cbox_mediopago2.setItemText(4, QCoreApplication.translate("Seguimiento", u"PLIN Padma", None))
        self.cbox_mediopago2.setItemText(5, QCoreApplication.translate("Seguimiento", u"Efectivo", None))
        self.cbox_mediopago2.setItemText(6, QCoreApplication.translate("Seguimiento", u"Convenio H&I", None))
        self.cbox_mediopago2.setItemText(7, QCoreApplication.translate("Seguimiento", u"Convenio Tejiendo sonrisas", None))

        self.line_duracion2.setText(QCoreApplication.translate("Seguimiento", u"1", None))
        self.label_119.setText(QCoreApplication.translate("Seguimiento", u"Hora final*", None))
        self.label_120.setText(QCoreApplication.translate("Seguimiento", u"Cantidad de sesiones*", None))
        self.spin_monto2.setPrefix(QCoreApplication.translate("Seguimiento", u"S/.", None))
        self.spin_monto2.setSuffix("")
        self.label_121.setText(QCoreApplication.translate("Seguimiento", u"Estado sesi\u00f3n*", None))
        self.label_122.setText(QCoreApplication.translate("Seguimiento", u"Fecha de pago*", None))
        self.label_123.setText(QCoreApplication.translate("Seguimiento", u"Obervaci\u00f3n*", None))
        self.label_124.setText(QCoreApplication.translate("Seguimiento", u"Costo Pagar*", None))
        self.cbox_estadosesion2.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_estadosesion2.setItemText(1, QCoreApplication.translate("Seguimiento", u"Pendiente", None))
        self.cbox_estadosesion2.setItemText(2, QCoreApplication.translate("Seguimiento", u"Asisti\u00f3", None))
        self.cbox_estadosesion2.setItemText(3, QCoreApplication.translate("Seguimiento", u"Tardanza", None))
        self.cbox_estadosesion2.setItemText(4, QCoreApplication.translate("Seguimiento", u"Reprogramado", None))
        self.cbox_estadosesion2.setItemText(5, QCoreApplication.translate("Seguimiento", u"Falta injustificada", None))

        self.date_fechantigua2.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.label_125.setText(QCoreApplication.translate("Seguimiento", u"Fecha Antigua*", None))
        self.date_reprogramacion2.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.label_126.setText(QCoreApplication.translate("Seguimiento", u"Fecha reprogramada*", None))
        self.line_costoasignado2.setPrefix(QCoreApplication.translate("Seguimiento", u"S/.", None))
        self.line_costoasignado2.setSuffix("")
        self.cbox_tipocita2.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_tipocita2.setItemText(1, QCoreApplication.translate("Seguimiento", u"Individual", None))
        self.cbox_tipocita2.setItemText(2, QCoreApplication.translate("Seguimiento", u"Pareja", None))
        self.cbox_tipocita2.setItemText(3, QCoreApplication.translate("Seguimiento", u"Familiar", None))
        self.cbox_tipocita2.setItemText(4, QCoreApplication.translate("Seguimiento", u"Evaluaci\u00f3n", None))
        self.cbox_tipocita2.setItemText(5, QCoreApplication.translate("Seguimiento", u"Emdr", None))

#if QT_CONFIG(tooltip)
        self.btn_actualizar_sesion.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_actualizar_sesion.setText(QCoreApplication.translate("Seguimiento", u"Actualizar sesi\u00f3n", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Seguimiento", u"Lista de sesiones", None))
#if QT_CONFIG(tooltip)
        self.btn_agregar_sesion.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_agregar_sesion.setText(QCoreApplication.translate("Seguimiento", u"Agregar sesi\u00f3n", None))
        self.label_39.setText(QCoreApplication.translate("Seguimiento", u"Lista de seguimientos", None))
        ___qtablewidgetitem = self.tabla_sesion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Seguimiento", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_sesion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Seguimiento", u"FECHA SEGUIMIENTO", None));
        ___qtablewidgetitem2 = self.tabla_sesion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Seguimiento", u"HORA ASIGNADA", None));
        ___qtablewidgetitem3 = self.tabla_sesion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Seguimiento", u"ACCIONES", None));
        ___qtablewidgetitem4 = self.tabla_sesion.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Seguimiento", u"Nueva fila", None));
        ___qtablewidgetitem5 = self.tabla_sesion.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Seguimiento", u"Nueva fila", None));
        ___qtablewidgetitem6 = self.tabla_sesion.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Seguimiento", u"Nueva fila", None));

        __sortingEnabled = self.tabla_sesion.isSortingEnabled()
        self.tabla_sesion.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tabla_sesion.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Seguimiento", u"98657", None));
        ___qtablewidgetitem8 = self.tabla_sesion.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Seguimiento", u"46", None));
        ___qtablewidgetitem9 = self.tabla_sesion.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Seguimiento", u"436", None));
        ___qtablewidgetitem10 = self.tabla_sesion.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Seguimiento", u"643", None));
        ___qtablewidgetitem11 = self.tabla_sesion.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Seguimiento", u"6436", None));
        ___qtablewidgetitem12 = self.tabla_sesion.item(1, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Seguimiento", u"643", None));
        ___qtablewidgetitem13 = self.tabla_sesion.item(1, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Seguimiento", u"4343", None));
        ___qtablewidgetitem14 = self.tabla_sesion.item(1, 3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Seguimiento", u"643", None));
        ___qtablewidgetitem15 = self.tabla_sesion.item(2, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Seguimiento", u"436", None));
        ___qtablewidgetitem16 = self.tabla_sesion.item(2, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Seguimiento", u"43643", None));
        ___qtablewidgetitem17 = self.tabla_sesion.item(2, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Seguimiento", u"643", None));
        ___qtablewidgetitem18 = self.tabla_sesion.item(2, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Seguimiento", u"643", None));
        self.tabla_sesion.setSortingEnabled(__sortingEnabled)

        self.cbox_rangosesiones.setItemText(0, QCoreApplication.translate("Seguimiento", u"5", None))
        self.cbox_rangosesiones.setItemText(1, QCoreApplication.translate("Seguimiento", u"10", None))
        self.cbox_rangosesiones.setItemText(2, QCoreApplication.translate("Seguimiento", u"20", None))
        self.cbox_rangosesiones.setItemText(3, QCoreApplication.translate("Seguimiento", u"50", None))

        self.btn_agregarses.setText(QCoreApplication.translate("Seguimiento", u"Nuevo seguimiento", None))
        self.label_44.setText(QCoreApplication.translate("Seguimiento", u"Mostrar", None))
        self.label_45.setText(QCoreApplication.translate("Seguimiento", u"sesiones", None))
        self.lbl_nombrepaciente.setText(QCoreApplication.translate("Seguimiento", u"Seguimiento", None))
#if QT_CONFIG(tooltip)
        self.btn_closeseguimiento.setToolTip(QCoreApplication.translate("Seguimiento", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeseguimiento.setText("")
        self.lbl_nombreestudiante.setText(QCoreApplication.translate("Seguimiento", u"Jose Mariano Martinez Jimenez", None))
    # retranslateUi

