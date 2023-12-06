# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tranferenciatQpbNc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_Transferencia(object):
    def setupUi(self, Transferencia):
        if not Transferencia.objectName():
            Transferencia.setObjectName(u"Transferencia")
        Transferencia.setEnabled(True)
        Transferencia.resize(500, 620)
        Transferencia.setMinimumSize(QSize(500, 620))
        Transferencia.setMaximumSize(QSize(500, 620))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Transferencia.setWindowIcon(icon)
        Transferencia.setStyleSheet(u"QTableWidget {\n"
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
        self.gridLayout = QGridLayout(Transferencia)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Transferencia)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"\n"
"#frame{background-color:white;border-radius:10px}\n"
"\n"
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
"	padding:"
                        " 10px 10px 10px 20px;\n"
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
"bac"
                        "kground: #F3F4F6;\n"
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
        self.cbox_sedeFinal = QComboBox(self.frame)
        self.cbox_sedeFinal.addItem("")
        self.cbox_sedeFinal.addItem("")
        self.cbox_sedeFinal.addItem("")
        self.cbox_sedeFinal.setObjectName(u"cbox_sedeFinal")
        self.cbox_sedeFinal.setGeometry(QRect(260, 94, 211, 40))
        self.cbox_sedeFinal.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_sedeFinal.setStyleSheet(u"")
        self.lbl8 = QLabel(self.frame)
        self.lbl8.setObjectName(u"lbl8")
        self.lbl8.setGeometry(QRect(24, 70, 171, 21))
        self.lbl8.setStyleSheet(u"")
        self.lbl8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.date_fecha = QDateEdit(self.frame)
        self.date_fecha.setObjectName(u"date_fecha")
        self.date_fecha.setGeometry(QRect(24, 93, 211, 40))
        self.date_fecha.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_fecha.setStyleSheet(u"/*SPINBOX*/\n"
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
"border: 2px solid #526974;\n"
"border-radius: 8px;\n"
"}")
        self.date_fecha.setCalendarPopup(False)
        self.lbl2 = QLabel(self.frame)
        self.lbl2.setObjectName(u"lbl2")
        self.lbl2.setGeometry(QRect(270, 70, 91, 21))
        self.lbl2.setStyleSheet(u"")
        self.lbl2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btn_enviar = QPushButton(self.frame)
        self.btn_enviar.setObjectName(u"btn_enviar")
        self.btn_enviar.setGeometry(QRect(140, 560, 195, 47))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_enviar.sizePolicy().hasHeightForWidth())
        self.btn_enviar.setSizePolicy(sizePolicy)
        self.btn_enviar.setSizeIncrement(QSize(0, 0))
        self.btn_enviar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar.setFocusPolicy(Qt.NoFocus)
        self.btn_enviar.setAutoFillBackground(False)
        self.btn_enviar.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/image (10).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_enviar.setIcon(icon1)
        self.btn_enviar.setIconSize(QSize(21, 21))
        self.btn_enviar.setCheckable(False)
        self.btn_enviar.setAutoRepeat(False)
        self.btn_enviar.setAutoExclusive(False)
        self.btn_enviar.setAutoDefault(False)
        self.btn_enviar.setFlat(False)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 501, 50))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 181, 27))
        self.label_3.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 22px;\n"
"line-height: 40px;\n"
"letter-spacing: 0.02em;\n"
"color:#ffffff;")
        self.btn_closeTransfe = QToolButton(self.frame_2)
        self.btn_closeTransfe.setObjectName(u"btn_closeTransfe")
        self.btn_closeTransfe.setGeometry(QRect(470, 6, 25, 25))
        self.btn_closeTransfe.setFocusPolicy(Qt.NoFocus)
        self.btn_closeTransfe.setStyleSheet(u"#btn_closeTransfe{\n"
"font-family: Roboto;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"background-color: #d5d5d8;\n"
"color: #6B7280;\n"
"border-radius:11px\n"
"}\n"
"\n"
"#btn_closeTransfe:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/close (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeTransfe.setIcon(icon2)
        self.btn_closeTransfe.setIconSize(QSize(13, 13))
        self.btn_closeTransfe.setAutoRaise(True)
        self.line_filtrar = QLineEdit(self.frame)
        self.line_filtrar.setObjectName(u"line_filtrar")
        self.line_filtrar.setGeometry(QRect(20, 160, 211, 41))
        self.list_inicio = QListWidget(self.frame)
        self.list_inicio.setObjectName(u"list_inicio")
        self.list_inicio.setGeometry(QRect(20, 210, 211, 331))
        self.list_inicio.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.list_inicio.setStyleSheet(u"")
        self.list_inicio.setFrameShape(QFrame.NoFrame)
        self.list_inicio.setAutoScrollMargin(20)
        self.list_inicio.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_inicio.setSelectionMode(QAbstractItemView.SingleSelection)
        self.list_inicio.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.list_inicio.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.list_inicio.setProperty("isWrapping", False)
        self.list_inicio.setSpacing(2)
        self.list_final = QListWidget(self.frame)
        self.list_final.setObjectName(u"list_final")
        self.list_final.setGeometry(QRect(260, 210, 211, 331))
        self.list_final.setFrameShape(QFrame.NoFrame)
        self.list_final.setTabKeyNavigation(False)
        self.list_final.setSelectionMode(QAbstractItemView.SingleSelection)
        self.list_final.setIconSize(QSize(0, 0))
        self.list_final.setSpacing(2)
        self.list_final.setSortingEnabled(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(261, 186, 211, 16))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.date_fecha, self.cbox_sedeFinal)
        QWidget.setTabOrder(self.cbox_sedeFinal, self.line_filtrar)
        QWidget.setTabOrder(self.line_filtrar, self.list_inicio)
        QWidget.setTabOrder(self.list_inicio, self.list_final)

        self.retranslateUi(Transferencia)

        self.btn_enviar.setDefault(False)


        QMetaObject.connectSlotsByName(Transferencia)
    # setupUi

    def retranslateUi(self, Transferencia):
        Transferencia.setWindowTitle(QCoreApplication.translate("Transferencia", u"Dialog", None))
        self.cbox_sedeFinal.setItemText(0, QCoreApplication.translate("Transferencia", u"Seleccionar", None))
        self.cbox_sedeFinal.setItemText(1, QCoreApplication.translate("Transferencia", u"Masculino", None))
        self.cbox_sedeFinal.setItemText(2, QCoreApplication.translate("Transferencia", u"Femenino", None))

        self.lbl8.setText(QCoreApplication.translate("Transferencia", u"Fecha", None))
        self.date_fecha.setDisplayFormat(QCoreApplication.translate("Transferencia", u"d-MM-yyyy", None))
        self.lbl2.setText(QCoreApplication.translate("Transferencia", u"sede final", None))
        self.btn_enviar.setText(QCoreApplication.translate("Transferencia", u"Enviar", None))
        self.label_3.setText(QCoreApplication.translate("Transferencia", u"Transferencia", None))
#if QT_CONFIG(tooltip)
        self.btn_closeTransfe.setToolTip(QCoreApplication.translate("Transferencia", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeTransfe.setText("")
        self.line_filtrar.setPlaceholderText(QCoreApplication.translate("Transferencia", u"buscar serial...", None))
        self.label.setText(QCoreApplication.translate("Transferencia", u"Computador Seleccionadas", None))
    # retranslateUi

