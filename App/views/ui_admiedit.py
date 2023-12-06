# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admieditvoDBoe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_AdmiEdit(object):
    def setupUi(self, AdmiEdit):
        if not AdmiEdit.objectName():
            AdmiEdit.setObjectName(u"AdmiEdit")
        AdmiEdit.resize(476, 570)
        AdmiEdit.setMinimumSize(QSize(476, 570))
        AdmiEdit.setMaximumSize(QSize(476, 570))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        AdmiEdit.setWindowIcon(icon)
        AdmiEdit.setStyleSheet(u"")
        self.gridLayout = QGridLayout(AdmiEdit)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(AdmiEdit)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.btn_closeedit.setGeometry(QRect(435, 6, 25, 25))
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
        icon1.addFile(u":/prefijoNuevo/close (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeedit.setIcon(icon1)
        self.btn_closeedit.setIconSize(QSize(13, 13))
        self.btn_closeedit.setAutoRaise(True)
        self.lbl_nombretitulo = QLabel(self.frame_2)
        self.lbl_nombretitulo.setObjectName(u"lbl_nombretitulo")
        self.lbl_nombretitulo.setGeometry(QRect(20, 7, 241, 16))
        self.lbl_nombretitulo.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 26, 47, 20))
        self.label_2.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")
        self.lbl_dnititulo = QLabel(self.frame_2)
        self.lbl_dnititulo.setObjectName(u"lbl_dnititulo")
        self.lbl_dnititulo.setGeometry(QRect(50, 27, 111, 21))
        self.lbl_dnititulo.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 23px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;}")

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

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
"/* COMBOBOX */\n"
"QComboBox{\n"
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
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"	padding: 10px 10px 10px 20px;\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color:#9CA3AF;\n"
"	font-size:14px;\n"
"	background-color: #F3F4F6;\n"
"	selection-background-color:#3A4F50;\n"
"	selection-color:#FFFFFF;\n"
"	outline: 0px;\n"
"	border: 1px solid #3A4F50;\n"
"	border-radius: 8px;\n"
"	padding: 11px ;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/prefijoNuevo/flecha_oscuro.png);\n"
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"QComboBox::focus{\n"
""
                        "background: #FFFFFF;\n"
"border: 2px solid #3A4F50;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox {combobox-popup: 0}\n"
"\n"
"QCheckBox{font-family: Roboto;\n"
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
        self.btn_guardar = QPushButton(self.frame_3)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(140, 447, 195, 47))
        self.btn_guardar.setMinimumSize(QSize(195, 47))
        self.btn_guardar.setMaximumSize(QSize(110, 47))
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
"QPushButton:hover{background: #344748;\n"
"border-radius: 8px; }\n"
"")
        self.btn_guardar.setIconSize(QSize(15, 21))
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 461, 431))
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.lbl5 = QLabel(self.frame_4)
        self.lbl5.setObjectName(u"lbl5")
        self.lbl5.setGeometry(QRect(10, 93, 151, 21))
        self.lbl5.setStyleSheet(u"")
        self.lbl5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_dni = QLineEdit(self.frame_4)
        self.line_dni.setObjectName(u"line_dni")
        self.line_dni.setEnabled(False)
        self.line_dni.setGeometry(QRect(10, 36, 205, 40))
        self.line_dni.setStyleSheet(u"")
        self.line_dni.setMaxLength(8)
        self.line_dni.setFrame(True)
        self.line_dni.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl11 = QLabel(self.frame_4)
        self.lbl11.setObjectName(u"lbl11")
        self.lbl11.setGeometry(QRect(10, 10, 171, 21))
        self.lbl11.setStyleSheet(u"")
        self.lbl11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl9 = QLabel(self.frame_4)
        self.lbl9.setObjectName(u"lbl9")
        self.lbl9.setGeometry(QRect(240, 10, 81, 21))
        self.lbl9.setStyleSheet(u"")
        self.lbl9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_nombre = QLineEdit(self.frame_4)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setEnabled(False)
        self.line_nombre.setGeometry(QRect(240, 36, 205, 40))
        self.line_nombre.setStyleSheet(u"")
        self.line_nombre.setMaxLength(100)
        self.line_nombre.setFrame(True)
        self.line_nombre.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_nombre.setClearButtonEnabled(False)
        self.line_apeP = QLineEdit(self.frame_4)
        self.line_apeP.setObjectName(u"line_apeP")
        self.line_apeP.setEnabled(False)
        self.line_apeP.setGeometry(QRect(10, 118, 205, 40))
        self.line_apeP.setStyleSheet(u"")
        self.line_apeP.setMaxLength(100)
        self.line_apeP.setFrame(True)
        self.line_apeP.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl2 = QLabel(self.frame_4)
        self.lbl2.setObjectName(u"lbl2")
        self.lbl2.setGeometry(QRect(10, 177, 91, 21))
        self.lbl2.setStyleSheet(u"")
        self.lbl2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl8 = QLabel(self.frame_4)
        self.lbl8.setObjectName(u"lbl8")
        self.lbl8.setGeometry(QRect(240, 93, 181, 21))
        self.lbl8.setStyleSheet(u"")
        self.lbl8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.date_naci = QDateEdit(self.frame_4)
        self.date_naci.setObjectName(u"date_naci")
        self.date_naci.setEnabled(False)
        self.date_naci.setGeometry(QRect(240, 118, 205, 40))
        self.date_naci.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_naci.setStyleSheet(u"/*SPINBOX*/\n"
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
"border: 2px solid #54BFC9;\n"
"border-radius: 8px;\n"
"}")
        self.date_naci.setCalendarPopup(False)
        self.cbox_genero = QComboBox(self.frame_4)
        self.cbox_genero.addItem("")
        self.cbox_genero.addItem("")
        self.cbox_genero.addItem("")
        self.cbox_genero.setObjectName(u"cbox_genero")
        self.cbox_genero.setEnabled(False)
        self.cbox_genero.setGeometry(QRect(10, 200, 205, 40))
        self.cbox_genero.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_genero.setStyleSheet(u"")
        self.lbl10 = QLabel(self.frame_4)
        self.lbl10.setObjectName(u"lbl10")
        self.lbl10.setGeometry(QRect(320, 260, 82, 21))
        self.lbl10.setStyleSheet(u"")
        self.lbl10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl3 = QLabel(self.frame_4)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setGeometry(QRect(10, 260, 151, 21))
        self.lbl3.setStyleSheet(u"")
        self.lbl3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_correo = QLineEdit(self.frame_4)
        self.line_correo.setObjectName(u"line_correo")
        self.line_correo.setEnabled(True)
        self.line_correo.setGeometry(QRect(10, 284, 291, 40))
        self.line_correo.setStyleSheet(u"")
        self.line_correo.setMaxLength(100)
        self.line_correo.setFrame(True)
        self.line_correo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_20 = QFrame(self.frame_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(10, 368, 291, 40))
        self.frame_20.setStyleSheet(u"#frame_20{background: #F3F4F6;\n"
"border: 1px solid  #F3F4F6; ;\n"
"border-radius: 11px;}\n"
"")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line_contrasena = QLineEdit(self.frame_20)
        self.line_contrasena.setObjectName(u"line_contrasena")
        self.line_contrasena.setEnabled(False)
        self.line_contrasena.setMinimumSize(QSize(0, 0))
        self.line_contrasena.setMaximumSize(QSize(16777215, 16777215))
        self.line_contrasena.setStyleSheet(u"")
        self.line_contrasena.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.line_contrasena)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(43, 0))
        self.frame_21.setStyleSheet(u"background-color: rgb(243, 244, 246);")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.bnt_ojoVis = QPushButton(self.frame_21)
        self.bnt_ojoVis.setObjectName(u"bnt_ojoVis")
        self.bnt_ojoVis.setEnabled(False)
        self.bnt_ojoVis.setGeometry(QRect(11, 5, 29, 25))
        self.bnt_ojoVis.setMinimumSize(QSize(29, 25))
        self.bnt_ojoVis.setFocusPolicy(Qt.NoFocus)
        self.bnt_ojoVis.setStyleSheet(u"background-color: Transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/ojo2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_ojoVis.setIcon(icon2)
        self.bnt_ojoVis.setIconSize(QSize(25, 25))
        self.bnt_ojoInv = QPushButton(self.frame_21)
        self.bnt_ojoInv.setObjectName(u"bnt_ojoInv")
        self.bnt_ojoInv.setEnabled(False)
        self.bnt_ojoInv.setGeometry(QRect(10, 5, 29, 25))
        self.bnt_ojoInv.setMinimumSize(QSize(29, 25))
        self.bnt_ojoInv.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_ojoInv.setFocusPolicy(Qt.NoFocus)
        self.bnt_ojoInv.setStyleSheet(u"background-color: Transparent;")
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/invi2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_ojoInv.setIcon(icon3)
        self.bnt_ojoInv.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.frame_21)

        self.lbl6_2 = QLabel(self.frame_4)
        self.lbl6_2.setObjectName(u"lbl6_2")
        self.lbl6_2.setGeometry(QRect(10, 342, 151, 21))
        self.lbl6_2.setStyleSheet(u"")
        self.lbl6_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lbl6_3 = QLabel(self.frame_4)
        self.lbl6_3.setObjectName(u"lbl6_3")
        self.lbl6_3.setGeometry(QRect(242, 175, 81, 21))
        self.lbl6_3.setStyleSheet(u"")
        self.lbl6_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbox_estado = QComboBox(self.frame_4)
        self.cbox_estado.addItem("")
        self.cbox_estado.addItem("")
        self.cbox_estado.setObjectName(u"cbox_estado")
        self.cbox_estado.setGeometry(QRect(240, 200, 205, 40))
        self.cbox_estado.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_estado.setStyleSheet(u"")
        self.admi = QCheckBox(self.frame_4)
        self.admi.setObjectName(u"admi")
        self.admi.setEnabled(True)
        self.admi.setGeometry(QRect(320, 286, 131, 17))
        self.user = QCheckBox(self.frame_4)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(320, 308, 111, 17))

        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.line_dni, self.line_nombre)
        QWidget.setTabOrder(self.line_nombre, self.line_apeP)
        QWidget.setTabOrder(self.line_apeP, self.date_naci)
        QWidget.setTabOrder(self.date_naci, self.cbox_genero)
        QWidget.setTabOrder(self.cbox_genero, self.cbox_estado)
        QWidget.setTabOrder(self.cbox_estado, self.line_correo)
        QWidget.setTabOrder(self.line_correo, self.admi)
        QWidget.setTabOrder(self.admi, self.user)
        QWidget.setTabOrder(self.user, self.line_contrasena)

        self.retranslateUi(AdmiEdit)

        self.cbox_estado.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(AdmiEdit)
    # setupUi

    def retranslateUi(self, AdmiEdit):
        AdmiEdit.setWindowTitle(QCoreApplication.translate("AdmiEdit", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.btn_closeedit.setToolTip(QCoreApplication.translate("AdmiEdit", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closeedit.setText("")
        self.lbl_nombretitulo.setText(QCoreApplication.translate("AdmiEdit", u"Bailon Paucar", None))
        self.label_2.setText(QCoreApplication.translate("AdmiEdit", u"Dni", None))
        self.lbl_dnititulo.setText(QCoreApplication.translate("AdmiEdit", u"47094589", None))
        self.btn_guardar.setText(QCoreApplication.translate("AdmiEdit", u"Actualizar", None))
        self.lbl5.setText(QCoreApplication.translate("AdmiEdit", u"Apellidos*", None))
        self.line_dni.setPlaceholderText(QCoreApplication.translate("AdmiEdit", u"Ingrese n\u00famero de DNI", None))
        self.lbl11.setText(QCoreApplication.translate("AdmiEdit", u"Documento Identidad*", None))
        self.lbl9.setText(QCoreApplication.translate("AdmiEdit", u"Nombre*", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("AdmiEdit", u"Ingrese nombre", None))
        self.line_apeP.setPlaceholderText(QCoreApplication.translate("AdmiEdit", u"Ingrese apellido paterno", None))
        self.lbl2.setText(QCoreApplication.translate("AdmiEdit", u"Genero", None))
        self.lbl8.setText(QCoreApplication.translate("AdmiEdit", u"Fecha de nacimiento*", None))
        self.date_naci.setDisplayFormat(QCoreApplication.translate("AdmiEdit", u"yyyy-MM-d", None))
        self.cbox_genero.setItemText(0, QCoreApplication.translate("AdmiEdit", u"Seleccionar", None))
        self.cbox_genero.setItemText(1, QCoreApplication.translate("AdmiEdit", u"Masculino", None))
        self.cbox_genero.setItemText(2, QCoreApplication.translate("AdmiEdit", u"Femenino", None))

        self.lbl10.setText(QCoreApplication.translate("AdmiEdit", u"Cargo*", None))
        self.lbl3.setText(QCoreApplication.translate("AdmiEdit", u"Correo electronico*", None))
        self.line_correo.setPlaceholderText(QCoreApplication.translate("AdmiEdit", u"Ingrese correo", None))
        self.line_contrasena.setPlaceholderText(QCoreApplication.translate("AdmiEdit", u"Ingrese contrase\u00f1a", None))
        self.bnt_ojoVis.setText("")
        self.bnt_ojoInv.setText("")
        self.lbl6_2.setText(QCoreApplication.translate("AdmiEdit", u"Contrase\u00f1a*", None))
        self.lbl6_3.setText(QCoreApplication.translate("AdmiEdit", u"Estado*", None))
        self.cbox_estado.setItemText(0, QCoreApplication.translate("AdmiEdit", u"Inactivo", None))
        self.cbox_estado.setItemText(1, QCoreApplication.translate("AdmiEdit", u"Activo", None))

        self.admi.setText(QCoreApplication.translate("AdmiEdit", u"Administrador", None))
        self.user.setText(QCoreApplication.translate("AdmiEdit", u"Usuario", None))
    # retranslateUi

