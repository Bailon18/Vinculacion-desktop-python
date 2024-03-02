# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario_institucioneszbHlXc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_Institucion(object):
    def setupUi(self, Institucion):
        if not Institucion.objectName():
            Institucion.setObjectName(u"Institucion")
        Institucion.resize(476, 406)
        Institucion.setMinimumSize(QSize(476, 406))
        Institucion.setMaximumSize(QSize(476, 406))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Institucion.setWindowIcon(icon)
        Institucion.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Institucion)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Institucion)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"background-color: rgb(255, 255, 255);\n"
"border-Bottom-left-radius: 10px;\n"
"border-Bottom-right-radius: 10px;\n"
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
"border: 2px solid #3A4F50;\n"
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
"    w"
                        "idth:15px;\n"
"    height:15px;\n"
"padding:13px 20px 10px 10px;\n"
"}\n"
"\n"
"QDateEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #3A4F50;\n"
"border-radius: 8px;\n"
"}\n"
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
"     hei"
                        "ght: 11px;\n"
"}\n"
"\n"
"QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox {combobox-popup: 0}\n"
"\n"
"QRadioButton{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"color:#9CA3AF}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_guardar_institiucion = QPushButton(self.frame_3)
        self.btn_guardar_institiucion.setObjectName(u"btn_guardar_institiucion")
        self.btn_guardar_institiucion.setGeometry(QRect(330, 300, 120, 40))
        self.btn_guardar_institiucion.setMinimumSize(QSize(120, 40))
        self.btn_guardar_institiucion.setMaximumSize(QSize(120, 40))
        self.btn_guardar_institiucion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_guardar_institiucion.setFocusPolicy(Qt.NoFocus)
        self.btn_guardar_institiucion.setStyleSheet(u"/*  BOTON */\n"
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
"QPushButton:hover{background: #344748;\n"
"border-radius: 8px; }\n"
"")
        self.btn_guardar_institiucion.setIconSize(QSize(15, 21))
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 461, 271))
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.lbl5 = QLabel(self.frame_4)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(10, 93, 151, 21))
        self.lbl5.setStyleSheet(u"")
        self.lbl5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_nombre_institucion = QLineEdit(self.frame_4)
        self.line_nombre_institucion.setObjectName(u"line_nombre_institucion")
        self.line_nombre_institucion.setEnabled(True)
        self.line_nombre_institucion.setGeometry(QRect(10, 36, 431, 40))
        self.line_nombre_institucion.setStyleSheet(u"")
        self.line_nombre_institucion.setMaxLength(102)
        self.line_nombre_institucion.setFrame(True)
        self.line_nombre_institucion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.frame_4)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(10, 10, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_tipo_institucion = QLineEdit(self.frame_4)
        self.line_tipo_institucion.setObjectName(u"line_tipo_institucion")
        self.line_tipo_institucion.setEnabled(True)
        self.line_tipo_institucion.setGeometry(QRect(10, 118, 205, 40))
        self.line_tipo_institucion.setStyleSheet(u"")
        self.line_tipo_institucion.setMaxLength(100)
        self.line_tipo_institucion.setFrame(True)
        self.line_tipo_institucion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl3 = QLabel(self.frame_4)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setGeometry(QRect(10, 180, 151, 21))
        self.lbl3.setStyleSheet(u"")
        self.lbl3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_direccion_institucion = QLineEdit(self.frame_4)
        self.line_direccion_institucion.setObjectName(u"line_direccion_institucion")
        self.line_direccion_institucion.setEnabled(True)
        self.line_direccion_institucion.setGeometry(QRect(10, 204, 431, 40))
        self.line_direccion_institucion.setStyleSheet(u"")
        self.line_direccion_institucion.setMaxLength(100)
        self.line_direccion_institucion.setFrame(True)
        self.line_direccion_institucion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl6_3 = QLabel(self.frame_4)
        self.lbl6_3.setObjectName(u"lbl6_3")
        self.lbl6_3.setGeometry(QRect(242, 95, 81, 21))
        self.lbl6_3.setStyleSheet(u"")
        self.lbl6_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbox_estado_intitucion = QComboBox(self.frame_4)
        self.cbox_estado_intitucion.addItem("")
        self.cbox_estado_intitucion.addItem("")
        self.cbox_estado_intitucion.setObjectName(u"cbox_estado_intitucion")
        self.cbox_estado_intitucion.setGeometry(QRect(240, 120, 205, 40))
        self.cbox_estado_intitucion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estado_intitucion.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"#frame_2{background: #3A4F50 ;border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_closeedit = QToolButton(self.frame_2)
        self.btn_closeedit.setObjectName(u"btn_closeedit")
        self.btn_closeedit.setGeometry(QRect(445, 6, 25, 25))
        self.btn_closeedit.setFocusPolicy(Qt.NoFocus)
        self.btn_closeedit.setStyleSheet(u"#btn_closeedit{\n"
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
"#btn_closeedit:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeedit.setIcon(icon1)
        self.btn_closeedit.setIconSize(QSize(13, 13))
        self.btn_closeedit.setAutoRaise(True)
        self.lbl_titulo_ventana = QLabel(self.frame_2)
        self.lbl_titulo_ventana.setObjectName(u"lbl_titulo_ventana")
        self.lbl_titulo_ventana.setGeometry(QRect(19, 4, 241, 19))
        self.lbl_titulo_ventana.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")
        self.lbl_instituto_seleccionado = QLabel(self.frame_2)
        self.lbl_instituto_seleccionado.setObjectName(u"lbl_instituto_seleccionado")
        self.lbl_instituto_seleccionado.setGeometry(QRect(20, 27, 411, 21))
        self.lbl_instituto_seleccionado.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.line_nombre_institucion, self.line_tipo_institucion)
        QWidget.setTabOrder(self.line_tipo_institucion, self.cbox_estado_intitucion)
        QWidget.setTabOrder(self.cbox_estado_intitucion, self.line_direccion_institucion)

        self.retranslateUi(Institucion)

        self.cbox_estado_intitucion.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Institucion)
    # setupUi

    def retranslateUi(self, Institucion):
        Institucion.setWindowTitle(QCoreApplication.translate("Institucion", u"Dialog", None))
        self.btn_guardar_institiucion.setText(QCoreApplication.translate("Institucion", u"Guardar", None))
        self.lbl5.setText(QCoreApplication.translate("Institucion", u"Tipo de instituci\u00f3n*", None))
        self.line_nombre_institucion.setPlaceholderText(QCoreApplication.translate("Institucion", u"Ingrese nombre de la instituci\u00f3n", None))
        self.lbl11.setText(QCoreApplication.translate("Institucion", u"Nombre instituci\u00f3n*", None))
        self.line_tipo_institucion.setPlaceholderText(QCoreApplication.translate("Institucion", u"Ingrese tipo de institucion", None))
        self.lbl3.setText(QCoreApplication.translate("Institucion", u"Direcci\u00f3n*", None))
        self.line_direccion_institucion.setPlaceholderText(QCoreApplication.translate("Institucion", u"Ingrese la direcci\u00f3n ", None))
        self.lbl6_3.setText(QCoreApplication.translate("Institucion", u"Estado*", None))
        self.cbox_estado_intitucion.setItemText(0, QCoreApplication.translate("Institucion", u"Inactivo", None))
        self.cbox_estado_intitucion.setItemText(1, QCoreApplication.translate("Institucion", u"Activo", None))

#if QT_CONFIG(tooltip)
        self.btn_closeedit.setToolTip(QCoreApplication.translate("Institucion", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeedit.setText("")
        self.lbl_titulo_ventana.setText(QCoreApplication.translate("Institucion", u"Nueva Instituci\u00f3n", None))
        self.lbl_instituto_seleccionado.setText("")
    # retranslateUi

