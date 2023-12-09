# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seguimiento_adminJujYeP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_SeguimientoAdmin(object):
    def setupUi(self, SeguimientoAdmin):
        if not SeguimientoAdmin.objectName():
            SeguimientoAdmin.setObjectName(u"SeguimientoAdmin")
        SeguimientoAdmin.setEnabled(True)
        SeguimientoAdmin.resize(580, 550)
        SeguimientoAdmin.setMinimumSize(QSize(580, 550))
        SeguimientoAdmin.setMaximumSize(QSize(580, 550))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        SeguimientoAdmin.setWindowIcon(icon)
        SeguimientoAdmin.setStyleSheet(u"QTableWidget {\n"
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
        self.gridLayout = QGridLayout(SeguimientoAdmin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(SeguimientoAdmin)
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
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
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
"	padding: 1"
                        "0px 10px 10px 20px;\n"
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
"	image: url(:/prefijoNuevo/flecha_oscuro.png);\n"
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
"background: #3A4F50;\n"
"border-radius: 8px;}\n"
"\n"
"QPushButton:hover{background: #2e3e3f;\n"
"border-radius: 8px; }\n"
"\n"
"\n"
"/* LISTA */\n"
"\n"
"\n"
"QListWidget{\n"
"font-family: Roboto;\n"
"font-size: 13px;\n"
"backg"
                        "round: #F3F4F6;\n"
"color:#9CA3AF;\n"
"padding:8px;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"\n"
"\n"
"QListWidget::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #3A4F50;\n"
"border-radius: 8px;\n"
"\n"
"}\n"
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
        self.frame_2.setGeometry(QRect(0, 0, 581, 50))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lbl_nombre_estudiante = QLabel(self.frame_2)
        self.lbl_nombre_estudiante.setObjectName(u"lbl_nombre_estudiante")
        self.lbl_nombre_estudiante.setGeometry(QRect(20, 10, 521, 27))
        self.lbl_nombre_estudiante.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 17px;\n"
"line-height: 40px;\n"
"letter-spacing: 0.02em;\n"
"color:#ffffff;")
        self.btn_closeseguimiento = QToolButton(self.frame_2)
        self.btn_closeseguimiento.setObjectName(u"btn_closeseguimiento")
        self.btn_closeseguimiento.setGeometry(QRect(550, 10, 25, 25))
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
        self.lbl_nombretutor = QLabel(self.frame)
        self.lbl_nombretutor.setObjectName(u"lbl_nombretutor")
        self.lbl_nombretutor.setGeometry(QRect(20, 100, 491, 16))
        self.tabla_admiseguimiento = QTableWidget(self.frame)
        if (self.tabla_admiseguimiento.columnCount() < 2):
            self.tabla_admiseguimiento.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_admiseguimiento.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_admiseguimiento.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tabla_admiseguimiento.setObjectName(u"tabla_admiseguimiento")
        self.tabla_admiseguimiento.setGeometry(QRect(20, 170, 541, 341))
        self.tabla_admiseguimiento.setStyleSheet(u"QTableWidget {\n"
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
"\n"
"")
        self.tabla_admiseguimiento.setFrameShape(QFrame.NoFrame)
        self.tabla_admiseguimiento.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_admiseguimiento.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_admiseguimiento.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_admiseguimiento.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_admiseguimiento.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_admiseguimiento.setShowGrid(False)
        self.tabla_admiseguimiento.horizontalHeader().setVisible(True)
        self.tabla_admiseguimiento.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_admiseguimiento.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_admiseguimiento.horizontalHeader().setHighlightSections(False)
        self.tabla_admiseguimiento.horizontalHeader().setStretchLastSection(False)
        self.tabla_admiseguimiento.verticalHeader().setVisible(False)
        self.tabla_admiseguimiento.verticalHeader().setDefaultSectionSize(47)
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

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(SeguimientoAdmin)

        QMetaObject.connectSlotsByName(SeguimientoAdmin)
    # setupUi

    def retranslateUi(self, SeguimientoAdmin):
        SeguimientoAdmin.setWindowTitle(QCoreApplication.translate("SeguimientoAdmin", u"Seguimiento detalle", None))
        self.lbl8.setText(QCoreApplication.translate("SeguimientoAdmin", u"Tutor asignado", None))
        self.lbl_nombre_estudiante.setText(QCoreApplication.translate("SeguimientoAdmin", u"Seguimiento", None))
#if QT_CONFIG(tooltip)
        self.btn_closeseguimiento.setToolTip(QCoreApplication.translate("SeguimientoAdmin", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeseguimiento.setText("")
        self.lbl_nombretutor.setText(QCoreApplication.translate("SeguimientoAdmin", u"tutor asignado", None))
        ___qtablewidgetitem = self.tabla_admiseguimiento.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SeguimientoAdmin", u"Fecha de seguimiento", None));
        ___qtablewidgetitem1 = self.tabla_admiseguimiento.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SeguimientoAdmin", u"Observaciones", None));
        self.lbl8_2.setText(QCoreApplication.translate("SeguimientoAdmin", u"Lista de seguimientos", None))
    # retranslateUi

