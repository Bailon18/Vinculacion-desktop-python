# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seguimientolDPSEW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_Seguimiento(object):
    def setupUi(self, Seguimiento):
        if not Seguimiento.objectName():
            Seguimiento.setObjectName(u"Seguimiento")
        Seguimiento.resize(620, 582)
        Seguimiento.setMinimumSize(QSize(620, 582))
        Seguimiento.setMaximumSize(QSize(620, 582))
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
        self.page_4.setMinimumSize(QSize(0, 522))
        self.gridLayout_9 = QGridLayout(self.page_4)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.page_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMinimumSize(QSize(0, 599))
        self.scrollArea_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 603, 448))
        self.scrollAreaWidgetContents_4.setMaximumSize(QSize(16777215, 448))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 665))
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
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 700))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Sunken)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 10, 911, 700))
        self.frame_13.setMinimumSize(QSize(0, 700))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Sunken)
        self.stack_formulario = QStackedWidget(self.frame_13)
        self.stack_formulario.setObjectName(u"stack_formulario")
        self.stack_formulario.setGeometry(QRect(0, 10, 911, 741))
        self.stack_formulario.setMinimumSize(QSize(0, 709))
        self.stack_formulario.setMaximumSize(QSize(16777215, 624))
        self.stack_formulario.setStyleSheet(u"QLabel{\n"
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
"QSpinBox::up-button {\n"
"min-width: 25px; min-height: 12px; backgroun"
                        "d-color: #F3F4F6; \n"
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
"min-width: 25px; min-height: 12px; background-color: #F3F4F6; \n"
"border-radius: 6px;}\n"
"\n"
"QDateEdi"
                        "t::up-arrow{\n"
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
        self.pag_agregarSesion = QWidget()
        self.pag_agregarSesion.setObjectName(u"pag_agregarSesion")
        self.pag_agregarSesion.setMinimumSize(QSize(0, 691))
        self.pag_agregarSesion.setMaximumSize(QSize(16777215, 16777215))
        self.pag_agregarSesion.setStyleSheet(u"#pag_agregarSesion{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
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
""
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
"min-width: 25px; min-height: 1"
                        "2px; background-color: #F3F4F6; \n"
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
        self.datefecha_atencion = QDateEdit(self.pag_agregarSesion)
        self.datefecha_atencion.setObjectName(u"datefecha_atencion")
        self.datefecha_atencion.setGeometry(QRect(620, 69, 280, 47))
        self.datefecha_atencion.setMinimumSize(QSize(0, 40))
        self.datefecha_atencion.setCursor(QCursor(Qt.PointingHandCursor))
        self.datefecha_atencion.setStyleSheet(u"")
        self.datefecha_atencion.setCalendarPopup(False)
        self.label_79 = QLabel(self.pag_agregarSesion)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(620, 140, 133, 21))
        self.line_duracion = QLineEdit(self.pag_agregarSesion)
        self.line_duracion.setObjectName(u"line_duracion")
        self.line_duracion.setEnabled(False)
        self.line_duracion.setGeometry(QRect(620, 164, 280, 47))
        self.line_duracion.setMinimumSize(QSize(0, 40))
        self.label_89 = QLabel(self.pag_agregarSesion)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(620, 39, 151, 31))
        self.label_91 = QLabel(self.pag_agregarSesion)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(620, 250, 181, 31))
        self.spin_monto = QDoubleSpinBox(self.pag_agregarSesion)
        self.spin_monto.setObjectName(u"spin_monto")
        self.spin_monto.setEnabled(False)
        self.spin_monto.setGeometry(QRect(620, 280, 280, 47))
        self.spin_monto.setMinimumSize(QSize(0, 40))
        self.spin_monto.setCursor(QCursor(Qt.PointingHandCursor))
        self.spin_monto.setStyleSheet(u"")
        self.label_97 = QLabel(self.pag_agregarSesion)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(620, 340, 151, 31))
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
        self.fecha_seguimiento = QDateEdit(self.pag_agregarSesion)
        self.fecha_seguimiento.setObjectName(u"fecha_seguimiento")
        self.fecha_seguimiento.setGeometry(QRect(10, 88, 230, 40))
        self.fecha_seguimiento.setCursor(QCursor(Qt.PointingHandCursor))
        self.fecha_seguimiento.setStyleSheet(u"")
        self.fecha_seguimiento.setCalendarPopup(False)
        self.spb_numerohoras = QSpinBox(self.pag_agregarSesion)
        self.spb_numerohoras.setObjectName(u"spb_numerohoras")
        self.spb_numerohoras.setEnabled(True)
        self.spb_numerohoras.setGeometry(QRect(320, 88, 71, 41))
        self.label_96 = QLabel(self.pag_agregarSesion)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(10, 48, 201, 31))
        self.label_98 = QLabel(self.pag_agregarSesion)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(10, 158, 161, 31))
        self.plain_observacion = QPlainTextEdit(self.pag_agregarSesion)
        self.plain_observacion.setObjectName(u"plain_observacion")
        self.plain_observacion.setGeometry(QRect(10, 200, 561, 221))
        self.lbl5 = QLabel(self.pag_agregarSesion)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(320, 48, 101, 31))
        self.lbl5.setStyleSheet(u"")
        self.checkhoraactual = QCheckBox(self.pag_agregarSesion)
        self.checkhoraactual.setObjectName(u"checkhoraactual")
        self.checkhoraactual.setGeometry(QRect(250, 100, 70, 17))
        self.checkhoraactual.setStyleSheet(u"QCheckBox {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    color: #9CA3AF;\n"
"}\n"
"\n"
"\n"
"")
        self.label_40 = QLabel(self.pag_agregarSesion)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 0, 291, 31))
        self.label_40.setStyleSheet(u"QLabel{\n"
"font-family: Roboto ;\n"
"font-style: bold;\n"
"font-weight: 480;\n"
"font-size: 21px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"color: #374151}")
        self.stack_formulario.addWidget(self.pag_agregarSesion)

        self.verticalLayout.addWidget(self.frame_11)


        self.gridLayout_10.addWidget(self.frame_10, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_9.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.page_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 61))
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
        self.btn_guardar = QPushButton(self.frame_9)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(470, 10, 110, 40))
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
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #344647;\n"
"border-radius: 4px; }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guardar.setIcon(icon1)
        self.btn_guardar.setIconSize(QSize(15, 21))
        self.btn_retornar_listado = QPushButton(self.frame_9)
        self.btn_retornar_listado.setObjectName(u"btn_retornar_listado")
        self.btn_retornar_listado.setGeometry(QRect(280, 10, 180, 40))
        self.btn_retornar_listado.setMinimumSize(QSize(180, 40))
        self.btn_retornar_listado.setMaximumSize(QSize(110, 40))
        self.btn_retornar_listado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_retornar_listado.setFocusPolicy(Qt.NoFocus)
        self.btn_retornar_listado.setStyleSheet(u"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    color: #FFFFF;\n"
"    padding: 8px 16px;\n"
"    background-color: #b3b3b3;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #919191;\n"
"    border-color: #BBBBBB;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/menu/retornar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_retornar_listado.setIcon(icon2)
        self.btn_retornar_listado.setIconSize(QSize(15, 21))

        self.gridLayout_9.addWidget(self.frame_9, 1, 0, 1, 1)

        self.stack_principal.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"#page_2{background-color: #ffffff;\n"
"border-bottom-right-radius: 10;\n"
"border-bottom-left-radius: 10;}\n"
"\n"
"")
        self.label_39 = QLabel(self.page_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(20, 100, 241, 31))
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
        self.frame_17.setGeometry(QRect(14, 140, 591, 291))
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
        self.tabla_listado_seguimiento = QTableWidget(self.frame_17)
        if (self.tabla_listado_seguimiento.columnCount() < 4):
            self.tabla_listado_seguimiento.setColumnCount(4)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setForeground(brush);
        self.tabla_listado_seguimiento.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_listado_seguimiento.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_listado_seguimiento.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_listado_seguimiento.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabla_listado_seguimiento.setObjectName(u"tabla_listado_seguimiento")
        self.tabla_listado_seguimiento.setStyleSheet(u"QTableWidget {\n"
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
        self.tabla_listado_seguimiento.setFrameShape(QFrame.NoFrame)
        self.tabla_listado_seguimiento.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_listado_seguimiento.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_listado_seguimiento.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_listado_seguimiento.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_listado_seguimiento.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_listado_seguimiento.setShowGrid(False)
        self.tabla_listado_seguimiento.setSortingEnabled(False)
        self.tabla_listado_seguimiento.horizontalHeader().setMinimumSectionSize(39)
        self.tabla_listado_seguimiento.horizontalHeader().setHighlightSections(False)
        self.tabla_listado_seguimiento.verticalHeader().setVisible(False)
        self.tabla_listado_seguimiento.verticalHeader().setMinimumSectionSize(23)
        self.tabla_listado_seguimiento.verticalHeader().setDefaultSectionSize(41)

        self.gridLayout_30.addWidget(self.tabla_listado_seguimiento, 0, 0, 1, 1)

        self.cbox_rangoseguimiento = QComboBox(self.page_2)
        self.cbox_rangoseguimiento.addItem("")
        self.cbox_rangoseguimiento.addItem("")
        self.cbox_rangoseguimiento.addItem("")
        self.cbox_rangoseguimiento.addItem("")
        self.cbox_rangoseguimiento.setObjectName(u"cbox_rangoseguimiento")
        self.cbox_rangoseguimiento.setGeometry(QRect(90, 460, 81, 38))
        self.cbox_rangoseguimiento.setMinimumSize(QSize(0, 0))
        self.cbox_rangoseguimiento.setMaximumSize(QSize(92, 38))
        self.cbox_rangoseguimiento.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_rangoseguimiento.setStyleSheet(u"QComboBox{\n"
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
"	selection-background-color:#3f5758;\n"
"	selection-color:#ffffff;\n"
"	outline: 0px;\n"
"   border: 1px solid #3f5758;\n"
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
"border: 2px solid #3f5758;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QComboBox {combobox-popup: 0}")
        self.btn_nuevo_seguimiento = QPushButton(self.page_2)
        self.btn_nuevo_seguimiento.setObjectName(u"btn_nuevo_seguimiento")
        self.btn_nuevo_seguimiento.setGeometry(QRect(440, 30, 161, 40))
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
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #3A4F50;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #344647;\n"
"border-radius: 4px; }\n"
"")
        self.btn_nuevo_seguimiento.setIcon(icon1)
        self.btn_nuevo_seguimiento.setIconSize(QSize(12, 38))
        self.btn_nuevo_seguimiento.setCheckable(False)
        self.btn_nuevo_seguimiento.setAutoRepeat(False)
        self.btn_nuevo_seguimiento.setAutoExclusive(False)
        self.btn_nuevo_seguimiento.setAutoDefault(False)
        self.btn_nuevo_seguimiento.setFlat(False)
        self.label_44 = QLabel(self.page_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(20, 461, 61, 31))
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
        self.label_45.setGeometry(QRect(190, 460, 101, 31))
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
        self.line_busqueda_seguimiento = QLineEdit(self.page_2)
        self.line_busqueda_seguimiento.setObjectName(u"line_busqueda_seguimiento")
        self.line_busqueda_seguimiento.setGeometry(QRect(20, 30, 331, 45))
        self.line_busqueda_seguimiento.setMinimumSize(QSize(0, 45))
        self.line_busqueda_seguimiento.setMaximumSize(QSize(16777215, 45))
        self.line_busqueda_seguimiento.setStyleSheet(u"\n"
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
"\n"
"QLineEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #3f5758;\n"
"border-radius: 8px;\n"
"}")
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

        QWidget.setTabOrder(self.datefecha_atencion, self.line_duracion)
        QWidget.setTabOrder(self.line_duracion, self.spin_monto)
        QWidget.setTabOrder(self.spin_monto, self.cbox_mediopago)
        QWidget.setTabOrder(self.cbox_mediopago, self.scrollArea_4)
        QWidget.setTabOrder(self.scrollArea_4, self.tabla_listado_seguimiento)
        QWidget.setTabOrder(self.tabla_listado_seguimiento, self.cbox_rangoseguimiento)

        self.retranslateUi(Seguimiento)

        self.stack_principal.setCurrentIndex(0)
        self.stack_formulario.setCurrentIndex(0)
        self.btn_nuevo_seguimiento.setDefault(False)


        QMetaObject.connectSlotsByName(Seguimiento)
    # setupUi

    def retranslateUi(self, Seguimiento):
        Seguimiento.setWindowTitle(QCoreApplication.translate("Seguimiento", u"Sesiones", None))
        self.datefecha_atencion.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.label_79.setText(QCoreApplication.translate("Seguimiento", u"Duracion sesi\u00f3n*", None))
        self.line_duracion.setText(QCoreApplication.translate("Seguimiento", u"1", None))
        self.label_89.setText(QCoreApplication.translate("Seguimiento", u"Fecha de atenci\u00f3n*", None))
        self.label_91.setText(QCoreApplication.translate("Seguimiento", u"Costo Pagar*", None))
        self.spin_monto.setPrefix(QCoreApplication.translate("Seguimiento", u"S/.", None))
        self.spin_monto.setSuffix("")
        self.label_97.setText(QCoreApplication.translate("Seguimiento", u"Medio de pago*", None))
        self.cbox_mediopago.setItemText(0, QCoreApplication.translate("Seguimiento", u"Seleccionar", None))
        self.cbox_mediopago.setItemText(1, QCoreApplication.translate("Seguimiento", u"BBVA Padma", None))
        self.cbox_mediopago.setItemText(2, QCoreApplication.translate("Seguimiento", u"BCP Carmen", None))
        self.cbox_mediopago.setItemText(3, QCoreApplication.translate("Seguimiento", u"YAPE Carmen", None))
        self.cbox_mediopago.setItemText(4, QCoreApplication.translate("Seguimiento", u"PLIN Carmen", None))
        self.cbox_mediopago.setItemText(5, QCoreApplication.translate("Seguimiento", u"Efectivo", None))
        self.cbox_mediopago.setItemText(6, QCoreApplication.translate("Seguimiento", u"Convenio H&I", None))
        self.cbox_mediopago.setItemText(7, QCoreApplication.translate("Seguimiento", u"Convenio Tejiendo sonrisas", None))

        self.fecha_seguimiento.setDisplayFormat(QCoreApplication.translate("Seguimiento", u"d-MM-yyyy", None))
        self.label_96.setText(QCoreApplication.translate("Seguimiento", u"Fecha seguimiento*", None))
        self.label_98.setText(QCoreApplication.translate("Seguimiento", u"Observaciones*", None))
        self.lbl5.setText(QCoreApplication.translate("Seguimiento", u"N\u00b0 horas", None))
        self.checkhoraactual.setText(QCoreApplication.translate("Seguimiento", u"Hoy", None))
        self.label_40.setText(QCoreApplication.translate("Seguimiento", u"Nuevo  Seguimiento", None))
        self.btn_guardar.setText(QCoreApplication.translate("Seguimiento", u"Guardar", None))
        self.btn_retornar_listado.setText(QCoreApplication.translate("Seguimiento", u" Listado seguimiento", None))
        self.label_39.setText(QCoreApplication.translate("Seguimiento", u"Lista de seguimientos", None))
        ___qtablewidgetitem = self.tabla_listado_seguimiento.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Seguimiento", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_listado_seguimiento.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Seguimiento", u"FECHA SEGUIMIENTO", None));
        ___qtablewidgetitem2 = self.tabla_listado_seguimiento.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Seguimiento", u"HORA ASIGNADA", None));
        ___qtablewidgetitem3 = self.tabla_listado_seguimiento.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Seguimiento", u"ACCIONES", None));
        self.cbox_rangoseguimiento.setItemText(0, QCoreApplication.translate("Seguimiento", u"5", None))
        self.cbox_rangoseguimiento.setItemText(1, QCoreApplication.translate("Seguimiento", u"10", None))
        self.cbox_rangoseguimiento.setItemText(2, QCoreApplication.translate("Seguimiento", u"20", None))
        self.cbox_rangoseguimiento.setItemText(3, QCoreApplication.translate("Seguimiento", u"50", None))

        self.btn_nuevo_seguimiento.setText(QCoreApplication.translate("Seguimiento", u"Nuevo seguimiento", None))
        self.label_44.setText(QCoreApplication.translate("Seguimiento", u"Mostrar", None))
        self.label_45.setText(QCoreApplication.translate("Seguimiento", u"Seguimientos", None))
        self.line_busqueda_seguimiento.setPlaceholderText(QCoreApplication.translate("Seguimiento", u"Buscar por cualquier campo", None))
        self.lbl_nombrepaciente.setText(QCoreApplication.translate("Seguimiento", u"Seguimiento", None))
#if QT_CONFIG(tooltip)
        self.btn_closeseguimiento.setToolTip(QCoreApplication.translate("Seguimiento", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeseguimiento.setText("")
        self.lbl_nombreestudiante.setText(QCoreApplication.translate("Seguimiento", u"Jose Mariano Martinez Jimenez", None))
    # retranslateUi

