# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principaluyRSsR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_principal(object):
    def setupUi(self, principal):
        if not principal.objectName():
            principal.setObjectName(u"principal")
        principal.resize(1187, 640)
        principal.setMinimumSize(QSize(1187, 640))
        principal.setMaximumSize(QSize(16777215, 16777215))
        principal.setStyleSheet(u"#btn_home,#btn_afiliacion,\n"
"#btn_reporte,#btn_usuario,#btn_cerrar, #btn_seguimientoo{\n"
"background:transparent;\n"
"border: 0px;\n"
"padding-left:36px;\n"
"text-align: left;\n"
"font-family: \"Roboto\";\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 17px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;\n"
"}\n"
"\n"
"\n"
"\n"
"#btn_home:hover,#btn_afiliacion:hover,#btn_seguimientoo:hover,\n"
"#btn_reporte:hover,#btn_usuario:hover{\n"
"color: #2E5C6B;background:#8cc0c2;border-top-left-radius:25px;border-bottom-left-radius: 25px\n"
"}\n"
"\n"
"\n"
"#btn_home:disabled,#btn_almacen:disabled,#btn_seguimientoo:disabled,\n"
"#btn_reporte:disabled,#btn_usuario:disabled{\n"
"border-right: 4px solid #37464D;\n"
"color: rgb(61, 104, 118);\n"
"}\n"
"\n"
"\n"
"\n"
"#btn_cerrar:hover{\n"
"color: #2E5C6B;\n"
"}\n"
"\n"
"\n"
"#btn_cerrar{\n"
"border-top: 1.3px solid #848d95;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#frameEnca{\n"
"	background-color: #526974;\n"
"}\n"
"\n"
"#frameBoton{\n"
"	background-color: white;"
                        "\n"
"}\n"
"\n"
"#frame_usuario{ \n"
"	background-color:#fafafa;\n"
"}\n"
"\n"
"QLabel#lbl_usuario,QLabel#lbl_rol,QLabel#lbl_online{\n"
"font-family: \"Roboto\";\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 16px;\n"
"line-height: 19px;\n"
"letter-spacing: 0.02em;\n"
"color: #2E5C6B;\n"
"background-color:#fafafa;\n"
"\n"
"}\n"
"\n"
"#frame_op{\n"
"padding:0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setStyleSheet(u"")
        self.frame_principal.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_principal)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_principal)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(0, 0))
        self.frame_menu.setMaximumSize(QSize(91, 16777215))
        self.frame_menu.setStyleSheet(u"")
        self.frame_menu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameEnca = QFrame(self.frame_menu)
        self.frameEnca.setObjectName(u"frameEnca")
        self.frameEnca.setMinimumSize(QSize(0, 150))
        self.frameEnca.setMaximumSize(QSize(16777215, 150))
        self.frameEnca.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameEnca)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.frameEnca)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMinimumSize(QSize(0, 0))
        self.frame_logo.setMaximumSize(QSize(16777204, 16777204))
        self.frame_logo.setStyleSheet(u"background-color: rgb(68, 93, 94);")
        self.frame_logo.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_logo2 = QLabel(self.frame_logo)
        self.lbl_logo2.setObjectName(u"lbl_logo2")
        self.lbl_logo2.setMaximumSize(QSize(91, 80))
        self.lbl_logo2.setStyleSheet(u"")
        self.lbl_logo2.setPixmap(QPixmap(u":/menu/logito2.png"))
        self.lbl_logo2.setScaledContents(True)
        self.lbl_logo2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_logo2.setWordWrap(False)
        self.lbl_logo2.setIndent(1)
        self.lbl_logo2.setOpenExternalLinks(False)

        self.horizontalLayout_6.addWidget(self.lbl_logo2)


        self.gridLayout_2.addWidget(self.frame_logo, 1, 0, 1, 1)

        self.frame_52 = QFrame(self.frameEnca)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(16777215, 20))
        self.frame_52.setStyleSheet(u"background-color: #445d5e;")
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_52, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frameEnca)

        self.frameBoton = QFrame(self.frame_menu)
        self.frameBoton.setObjectName(u"frameBoton")
        self.frameBoton.setStyleSheet(u"")
        self.frameBoton.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frameBoton)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_op = QFrame(self.frameBoton)
        self.frame_op.setObjectName(u"frame_op")
        self.frame_op.setEnabled(True)
        self.frame_op.setFrameShape(QFrame.NoFrame)
        self.frame_op.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_op)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(0, 10, 0, 0)
        self.btn_reporte = QPushButton(self.frame_op)
        self.btn_reporte.setObjectName(u"btn_reporte")
        self.btn_reporte.setMinimumSize(QSize(0, 55))
        self.btn_reporte.setMaximumSize(QSize(220, 55))
        self.btn_reporte.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reporte.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/menu/menureport.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reporte.setIcon(icon)
        self.btn_reporte.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.btn_reporte, 8, 0, 1, 1)

        self.btn_seguimientoo = QPushButton(self.frame_op)
        self.btn_seguimientoo.setObjectName(u"btn_seguimientoo")
        self.btn_seguimientoo.setMinimumSize(QSize(0, 55))
        self.btn_seguimientoo.setMaximumSize(QSize(16777215, 55))
        icon1 = QIcon()
        icon1.addFile(u":/menu/menuseguimiento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_seguimientoo.setIcon(icon1)
        self.btn_seguimientoo.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.btn_seguimientoo, 9, 0, 1, 1)

        self.btn_afiliacion = QPushButton(self.frame_op)
        self.btn_afiliacion.setObjectName(u"btn_afiliacion")
        self.btn_afiliacion.setEnabled(True)
        self.btn_afiliacion.setMinimumSize(QSize(0, 55))
        self.btn_afiliacion.setMaximumSize(QSize(220, 55))
        self.btn_afiliacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_afiliacion.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/menu/menuafiliacion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_afiliacion.setIcon(icon2)
        self.btn_afiliacion.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.btn_afiliacion, 5, 0, 1, 1)

        self.btn_usuario = QPushButton(self.frame_op)
        self.btn_usuario.setObjectName(u"btn_usuario")
        self.btn_usuario.setMinimumSize(QSize(0, 55))
        self.btn_usuario.setMaximumSize(QSize(220, 55))
        self.btn_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_usuario.setToolTipDuration(-5)
        self.btn_usuario.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/menu/menuusuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_usuario.setIcon(icon3)
        self.btn_usuario.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.btn_usuario, 10, 0, 1, 1)

        self.btn_home = QPushButton(self.frame_op)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setEnabled(True)
        self.btn_home.setMinimumSize(QSize(0, 55))
        self.btn_home.setMaximumSize(QSize(220, 55))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/menu/menu_mantenimiento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon4)
        self.btn_home.setIconSize(QSize(33, 33))

        self.gridLayout_3.addWidget(self.btn_home, 11, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_op, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_6 = QFrame(self.frameBoton)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 100))
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(6, 0, 6, 0)
        self.btn_cerrar = QPushButton(self.frame_6)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cerrar.sizePolicy().hasHeightForWidth())
        self.btn_cerrar.setSizePolicy(sizePolicy)
        self.btn_cerrar.setMinimumSize(QSize(0, 55))
        self.btn_cerrar.setMaximumSize(QSize(220, 55))
        self.btn_cerrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cerrar.setStyleSheet(u"padding:10px 10px 0px 30px")
        icon5 = QIcon()
        icon5.addFile(u":/menu/menusalir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon5)
        self.btn_cerrar.setIconSize(QSize(27, 27))

        self.gridLayout_4.addWidget(self.btn_cerrar, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frameBoton)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_contenido = QFrame(self.frame_principal)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_contenido)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_usuario = QFrame(self.frame_contenido)
        self.frame_usuario.setObjectName(u"frame_usuario")
        self.frame_usuario.setMinimumSize(QSize(0, 85))
        self.frame_usuario.setMaximumSize(QSize(16777215, 85))
        self.frame_usuario.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_usuario)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_usuario)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"QFrame{\n"
"	background-color:#465e5f;\n"
"}")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.gridLayout_64 = QGridLayout(self.frame_49)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(0, 0, 0, 0)
        self.boton_deslizable = QToolButton(self.frame_49)
        self.boton_deslizable.setObjectName(u"boton_deslizable")
        self.boton_deslizable.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.boton_deslizable.sizePolicy().hasHeightForWidth())
        self.boton_deslizable.setSizePolicy(sizePolicy1)
        self.boton_deslizable.setMinimumSize(QSize(56, 0))
        self.boton_deslizable.setStyleSheet(u"background-color: transparent;\n"
"border:0px;")
        icon6 = QIcon()
        icon6.addFile(u":/menu/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_deslizable.setIcon(icon6)
        self.boton_deslizable.setIconSize(QSize(30, 30))
        self.boton_deslizable.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.boton_deslizable.setAutoRaise(True)

        self.gridLayout_64.addWidget(self.boton_deslizable, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_49)

        self.frame = QFrame(self.frame_usuario)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 14, -1, -1)
        self.horizontalSpacer_43 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_43)

        self.lbl_hora = QLabel(self.frame)
        self.lbl_hora.setObjectName(u"lbl_hora")
        self.lbl_hora.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 24px;\n"
"line-height: 40px;\n"
"letter-spacing: 0.00em;\n"
"color: #2E5C6B")
        self.lbl_hora.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_hora)

        self.horizontalSpacer_26 = QSpacerItem(17, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_26)

        self.lbl_fecha = QLabel(self.frame)
        self.lbl_fecha.setObjectName(u"lbl_fecha")
        self.lbl_fecha.setMinimumSize(QSize(336, 0))
        self.lbl_fecha.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 24px;\n"
"line-height: 40px;\n"
"letter-spacing: 0.00em;\n"
"color: #6B7280;")

        self.horizontalLayout_3.addWidget(self.lbl_fecha)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_usuario)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(170, 0))
        self.frame_2.setMaximumSize(QSize(170, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.lbl_usuario = QLabel(self.frame_2)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setGeometry(QRect(12, 20, 212, 16))
        self.lbl_usuario.setMinimumSize(QSize(212, 0))
        self.lbl_rol = QLabel(self.frame_2)
        self.lbl_rol.setObjectName(u"lbl_rol")
        self.lbl_rol.setGeometry(QRect(12, 38, 158, 20))
        self.lbl_rol.setMinimumSize(QSize(158, 0))
        self.label_color_sesion_2 = QLabel(self.frame_2)
        self.label_color_sesion_2.setObjectName(u"label_color_sesion_2")
        self.label_color_sesion_2.setGeometry(QRect(12, 64, 10, 10))
        self.label_color_sesion_2.setMinimumSize(QSize(10, 10))
        self.label_color_sesion_2.setMaximumSize(QSize(10, 10))
        self.label_color_sesion_2.setStyleSheet(u"border: 2px solid5;\n"
"border-radius: 5px;\n"
"font-family:Roboto;\n"
"background:#41c300;\n"
"font-size:15px\n"
"")
        self.cbox_perfil = QComboBox(self.frame_2)
        self.cbox_perfil.addItem("")
        self.cbox_perfil.addItem("")
        self.cbox_perfil.setObjectName(u"cbox_perfil")
        self.cbox_perfil.setGeometry(QRect(20, 63, 121, 21))
        self.cbox_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_perfil.setStyleSheet(u"/*COMBOBOX*/\n"
"\n"
"QComboBox{\n"
"font-family: \"frutiger\";\n"
"background-color: #fafafa;\n"
"	border:0px;\n"
"	color:#a2a2a2;\n"
"	font-size: 16px;\n"
"\n"
"\n"
"combobox-popup: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: #a2a2a2;\n"
"	font-size:16px;\n"
"	padding: 11px;\n"
"background-color: #fafafa;\n"
"	selection-background-color:#fafafa;\n"
"	selection-color:black;\n"
"	outline: 0px;\n"
"	padding:10px\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/menu/contraerabajo.png);\n"
"     width: 16px;\n"
"     height: 16px;\n"
"}\n"
"")
        self.lbl_online = QLabel(self.frame_2)
        self.lbl_online.setObjectName(u"lbl_online")
        self.lbl_online.setGeometry(QRect(9, 59, 111, 21))
        self.lbl_online.setStyleSheet(u"")
        self.lbl_online.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_usuario.raise_()
        self.lbl_rol.raise_()
        self.cbox_perfil.raise_()
        self.lbl_online.raise_()
        self.label_color_sesion_2.raise_()

        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_usuario)

        self.frame_widgets = QFrame(self.frame_contenido)
        self.frame_widgets.setObjectName(u"frame_widgets")
        self.frame_widgets.setMaximumSize(QSize(16777215, 16777215))
        self.frame_widgets.setStyleSheet(u"")
        self.frame_widgets.setFrameShape(QFrame.NoFrame)
        self.frame_widgets.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_widgets)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_widgets)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.pag1 = QWidget()
        self.pag1.setObjectName(u"pag1")
        self.pag1.setStyleSheet(u"#pag1{\n"
"background-color:#f1f1f1;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.pag1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Scrollprincipal = QScrollArea(self.pag1)
        self.Scrollprincipal.setObjectName(u"Scrollprincipal")
        self.Scrollprincipal.setStyleSheet(u"")
        self.Scrollprincipal.setFrameShape(QFrame.NoFrame)
        self.Scrollprincipal.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1026, 486))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents{background-color: rgb(255, 255, 255); border-radius:10px}\n"
"\n"
"")
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frp1 = QFrame(self.scrollAreaWidgetContents)
        self.frp1.setObjectName(u"frp1")
        self.frp1.setMinimumSize(QSize(0, 0))
        self.frp1.setStyleSheet(u"")
        self.frp1.setFrameShape(QFrame.NoFrame)
        self.frp1.setFrameShadow(QFrame.Plain)
        self.gridLayout_8 = QGridLayout(self.frp1)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(9, 16, -1, -1)
        self.label_2 = QLabel(self.frp1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 22px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"\n"
"color: #000000;")

        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frp1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 60))
        self.frame_7.setMaximumSize(QSize(16777215, 60))
        self.frame_7.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"text-transform: uppercase;\n"
"color: #6B7280;}\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #3f5758;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #3f5758;\n"
"border-radius: 4px; }\n"
"")
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 18)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))
        self.label_4.setMaximumSize(QSize(58, 16777215))
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.cbox_rango = QComboBox(self.frame_7)
        self.cbox_rango.addItem("")
        self.cbox_rango.addItem("")
        self.cbox_rango.addItem("")
        self.cbox_rango.setObjectName(u"cbox_rango")
        self.cbox_rango.setMinimumSize(QSize(92, 38))
        self.cbox_rango.setMaximumSize(QSize(92, 38))
        self.cbox_rango.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_rango.setStyleSheet(u"\n"
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
"\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.cbox_rango)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.btn_recargar = QPushButton(self.frame_7)
        self.btn_recargar.setObjectName(u"btn_recargar")
        self.btn_recargar.setMinimumSize(QSize(59, 36))
        self.btn_recargar.setMaximumSize(QSize(59, 36))
        self.btn_recargar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recargar.setFocusPolicy(Qt.NoFocus)
        self.btn_recargar.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/menu/menuactualizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_recargar.setIcon(icon7)
        self.btn_recargar.setIconSize(QSize(20, 20))
        self.btn_recargar.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_recargar)

        self.horizontalSpacer_8 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.gridLayout_8.addWidget(self.frame_7, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.frp1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tabla_principal = QTableWidget(self.frame_5)
        if (self.tabla_principal.columnCount() < 7):
            self.tabla_principal.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tabla_principal.rowCount() < 3):
            self.tabla_principal.setRowCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_principal.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_principal.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_principal.setVerticalHeaderItem(2, __qtablewidgetitem9)
        self.tabla_principal.setObjectName(u"tabla_principal")
        self.tabla_principal.setStyleSheet(u"QTableWidget {\n"
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
        self.tabla_principal.setFrameShape(QFrame.NoFrame)
        self.tabla_principal.setAutoScrollMargin(16)
        self.tabla_principal.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_principal.setAlternatingRowColors(False)
        self.tabla_principal.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_principal.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_principal.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_principal.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_principal.setShowGrid(False)
        self.tabla_principal.setSortingEnabled(False)
        self.tabla_principal.setCornerButtonEnabled(True)
        self.tabla_principal.horizontalHeader().setVisible(False)
        self.tabla_principal.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_principal.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_principal.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_principal.horizontalHeader().setHighlightSections(False)
        self.tabla_principal.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_principal.horizontalHeader().setStretchLastSection(False)
        self.tabla_principal.verticalHeader().setVisible(False)
        self.tabla_principal.verticalHeader().setMinimumSectionSize(23)
        self.tabla_principal.verticalHeader().setDefaultSectionSize(47)
        self.tabla_principal.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_principal.verticalHeader().setStretchLastSection(False)

        self.gridLayout_7.addWidget(self.tabla_principal, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_5, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.frp1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 60))
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setStyleSheet(u"\n"
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
"}\n"
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
"padding:4px;\n"
"background: #3f5758;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #3f5758;\n"
"border-radius: 4px; }\n"
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
"}"
                        "\n"
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
"image: url(:/menu/contraerabajo.png);\n"
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
"\n"
"")
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(7, 9, 10, 12)
        self.line_busqueda = QLineEdit(self.frame_4)
        self.line_busqueda.setObjectName(u"line_busqueda")
        self.line_busqueda.setMinimumSize(QSize(0, 40))
        self.line_busqueda.setMaximumSize(QSize(16777215, 40))
        self.line_busqueda.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.line_busqueda)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_27)

        self.btn_nuevoafiliacion = QPushButton(self.frame_4)
        self.btn_nuevoafiliacion.setObjectName(u"btn_nuevoafiliacion")
        self.btn_nuevoafiliacion.setMinimumSize(QSize(180, 40))
        self.btn_nuevoafiliacion.setMaximumSize(QSize(180, 150))
        self.btn_nuevoafiliacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nuevoafiliacion.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nuevoafiliacion.setIcon(icon8)
        self.btn_nuevoafiliacion.setIconSize(QSize(15, 21))

        self.horizontalLayout_10.addWidget(self.btn_nuevoafiliacion)


        self.gridLayout_8.addWidget(self.frame_4, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frp1, 0, 0, 1, 1)

        self.Scrollprincipal.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.Scrollprincipal, 1, 1, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_28, 1, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(0, 19, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_29, 1, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.pag1)
        self.pag2 = QWidget()
        self.pag2.setObjectName(u"pag2")
        self.pag2.setStyleSheet(u"#pag2{\n"
"background-color:#f1f1f1;\n"
"}")
        self.gridLayout_17 = QGridLayout(self.pag2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalSpacer = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(19, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.Scrollprincipal_2 = QScrollArea(self.pag2)
        self.Scrollprincipal_2.setObjectName(u"Scrollprincipal_2")
        self.Scrollprincipal_2.setStyleSheet(u"#Scrollprincipal_2{\n"
"background-color:#f1f1f1;\n"
"}")
        self.Scrollprincipal_2.setFrameShape(QFrame.NoFrame)
        self.Scrollprincipal_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 393, 272))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"#scrollAreaWidgetContents_2{background-color: rgb(255, 255, 255); border-radius:10px}\n"
"\n"
"")
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frp1_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frp1_2.setObjectName(u"frp1_2")
        self.frp1_2.setMinimumSize(QSize(0, 0))
        self.frp1_2.setStyleSheet(u"")
        self.frp1_2.setFrameShape(QFrame.NoFrame)
        self.frp1_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_13 = QGridLayout(self.frp1_2)
        self.gridLayout_13.setSpacing(6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(9, 16, -1, -1)
        self.label_6 = QLabel(self.frp1_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 22px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"\n"
"color: #000000;")

        self.gridLayout_13.addWidget(self.label_6, 0, 0, 1, 1)

        self.frame_14 = QFrame(self.frp1_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 60))
        self.frame_14.setMaximumSize(QSize(16777215, 60))
        self.frame_14.setStyleSheet(u"\n"
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
"}\n"
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
"background: #3f5758;\n"
"border-radius: 8px;}\n"
"\n"
"QPushButton:hover{background: #3f5758;\n"
"border-radius: 8px; }\n"
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
"}"
                        "\n"
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
"image: url(:/menu/contraerabajo.png);\n"
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
"\n"
"")
        self.frame_14.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(7, 9, 10, 12)
        self.line_busqueda_tutor = QLineEdit(self.frame_14)
        self.line_busqueda_tutor.setObjectName(u"line_busqueda_tutor")
        self.line_busqueda_tutor.setMinimumSize(QSize(0, 45))
        self.line_busqueda_tutor.setMaximumSize(QSize(16777215, 45))
        self.line_busqueda_tutor.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.line_busqueda_tutor)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_31)


        self.gridLayout_13.addWidget(self.frame_14, 1, 0, 1, 1)

        self.frame_8 = QFrame(self.frp1_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 60))
        self.frame_8.setMaximumSize(QSize(16777215, 60))
        self.frame_8.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"text-transform: uppercase;\n"
"color: #6B7280;}\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:4px;\n"
"background: #3f5758;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #3f5758;\n"
"border-radius: 4px; }\n"
"")
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 0, 9, 18)
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(58, 16777215))
        self.label_7.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.cbox_rango_tutor = QComboBox(self.frame_8)
        self.cbox_rango_tutor.addItem("")
        self.cbox_rango_tutor.addItem("")
        self.cbox_rango_tutor.addItem("")
        self.cbox_rango_tutor.setObjectName(u"cbox_rango_tutor")
        self.cbox_rango_tutor.setMinimumSize(QSize(92, 38))
        self.cbox_rango_tutor.setMaximumSize(QSize(92, 38))
        self.cbox_rango_tutor.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_rango_tutor.setStyleSheet(u"\n"
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
"\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.cbox_rango_tutor)

        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.btn_recargar_tutor = QPushButton(self.frame_8)
        self.btn_recargar_tutor.setObjectName(u"btn_recargar_tutor")
        self.btn_recargar_tutor.setMinimumSize(QSize(59, 36))
        self.btn_recargar_tutor.setMaximumSize(QSize(59, 36))
        self.btn_recargar_tutor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recargar_tutor.setFocusPolicy(Qt.NoFocus)
        self.btn_recargar_tutor.setStyleSheet(u"")
        self.btn_recargar_tutor.setIcon(icon7)
        self.btn_recargar_tutor.setIconSize(QSize(20, 20))
        self.btn_recargar_tutor.setFlat(False)

        self.horizontalLayout_8.addWidget(self.btn_recargar_tutor)


        self.gridLayout_13.addWidget(self.frame_8, 4, 0, 1, 1)

        self.frame_9 = QFrame(self.frp1_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.gridLayout_16 = QGridLayout(self.frame_9)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.tabla_principal_tutor = QTableWidget(self.frame_9)
        if (self.tabla_principal_tutor.columnCount() < 6):
            self.tabla_principal_tutor.setColumnCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        if (self.tabla_principal_tutor.rowCount() < 3):
            self.tabla_principal_tutor.setRowCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_principal_tutor.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_principal_tutor.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_principal_tutor.setVerticalHeaderItem(2, __qtablewidgetitem18)
        self.tabla_principal_tutor.setObjectName(u"tabla_principal_tutor")
        self.tabla_principal_tutor.setStyleSheet(u"QTableWidget {\n"
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
        self.tabla_principal_tutor.setFrameShape(QFrame.NoFrame)
        self.tabla_principal_tutor.setAutoScrollMargin(16)
        self.tabla_principal_tutor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_principal_tutor.setAlternatingRowColors(False)
        self.tabla_principal_tutor.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_principal_tutor.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_principal_tutor.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_principal_tutor.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_principal_tutor.setShowGrid(False)
        self.tabla_principal_tutor.setSortingEnabled(False)
        self.tabla_principal_tutor.setCornerButtonEnabled(True)
        self.tabla_principal_tutor.horizontalHeader().setVisible(False)
        self.tabla_principal_tutor.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_principal_tutor.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_principal_tutor.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_principal_tutor.horizontalHeader().setHighlightSections(False)
        self.tabla_principal_tutor.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_principal_tutor.horizontalHeader().setStretchLastSection(False)
        self.tabla_principal_tutor.verticalHeader().setVisible(False)
        self.tabla_principal_tutor.verticalHeader().setMinimumSectionSize(23)
        self.tabla_principal_tutor.verticalHeader().setDefaultSectionSize(47)
        self.tabla_principal_tutor.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_principal_tutor.verticalHeader().setStretchLastSection(False)

        self.gridLayout_16.addWidget(self.tabla_principal_tutor, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_9, 3, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frp1_2, 0, 0, 1, 1)

        self.Scrollprincipal_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_17.addWidget(self.Scrollprincipal_2, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_6, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.pag2)
        self.pag3 = QWidget()
        self.pag3.setObjectName(u"pag3")
        self.gridLayout_21 = QGridLayout(self.pag3)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_21.addItem(self.verticalSpacer_12, 0, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_21.addItem(self.verticalSpacer_14, 2, 1, 1, 1)

        self.Scrollprincipal_3 = QScrollArea(self.pag3)
        self.Scrollprincipal_3.setObjectName(u"Scrollprincipal_3")
        self.Scrollprincipal_3.setStyleSheet(u"")
        self.Scrollprincipal_3.setFrameShape(QFrame.NoFrame)
        self.Scrollprincipal_3.setFrameShadow(QFrame.Plain)
        self.Scrollprincipal_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 304, 132))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"#scrollAreaWidgetContents_3{background-color: rgb(255, 255, 255); border-radius:10px}\n"
"\n"
"")
        self.gridLayout_18 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.frp1_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.frp1_3.setObjectName(u"frp1_3")
        self.frp1_3.setMinimumSize(QSize(0, 0))
        self.frp1_3.setStyleSheet(u"")
        self.frp1_3.setFrameShape(QFrame.NoFrame)
        self.frp1_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_19 = QGridLayout(self.frp1_3)
        self.gridLayout_19.setSpacing(6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(9, 0, -1, 0)
        self.frame_50 = QFrame(self.frp1_3)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(71, 0))
        self.frame_50.setStyleSheet(u"#frame_48{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Plain)
        self.gridLayout_66 = QGridLayout(self.frame_50)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setContentsMargins(-1, 0, -1, -1)
        self.stackedWidget_6 = QStackedWidget(self.frame_50)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.gridLayout_67 = QGridLayout(self.page_12)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.page_12)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"#frame_38{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_40.setFrameShadow(QFrame.Plain)
        self.btn_agregar_proyectos = QPushButton(self.frame_40)
        self.btn_agregar_proyectos.setObjectName(u"btn_agregar_proyectos")
        self.btn_agregar_proyectos.setGeometry(QRect(650, 0, 195, 40))
        self.btn_agregar_proyectos.setMinimumSize(QSize(195, 40))
        self.btn_agregar_proyectos.setMaximumSize(QSize(110, 40))
        self.btn_agregar_proyectos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_proyectos.setStyleSheet(u"/*  BOTON */\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #3f5758;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #3f5758;\n"
"border-radius: 4px; }\n"
"")
        self.btn_agregar_proyectos.setIcon(icon8)
        self.btn_agregar_proyectos.setIconSize(QSize(15, 21))
        self.tabla_proyectos = QTableWidget(self.frame_40)
        if (self.tabla_proyectos.columnCount() < 4):
            self.tabla_proyectos.setColumnCount(4)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        self.tabla_proyectos.setObjectName(u"tabla_proyectos")
        self.tabla_proyectos.setGeometry(QRect(10, 60, 841, 301))
        self.tabla_proyectos.setStyleSheet(u"QTableWidget {\n"
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
"color: #54bfc9;\n"
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
        self.tabla_proyectos.setFrameShape(QFrame.NoFrame)
        self.tabla_proyectos.setAutoScrollMargin(16)
        self.tabla_proyectos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_proyectos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_proyectos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_proyectos.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_proyectos.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_proyectos.setShowGrid(False)
        self.tabla_proyectos.setSortingEnabled(False)
        self.tabla_proyectos.setCornerButtonEnabled(True)
        self.tabla_proyectos.horizontalHeader().setVisible(False)
        self.tabla_proyectos.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_proyectos.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_proyectos.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_proyectos.horizontalHeader().setHighlightSections(False)
        self.tabla_proyectos.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_proyectos.horizontalHeader().setStretchLastSection(False)
        self.tabla_proyectos.verticalHeader().setVisible(False)
        self.tabla_proyectos.verticalHeader().setMinimumSectionSize(23)
        self.tabla_proyectos.verticalHeader().setDefaultSectionSize(47)
        self.tabla_proyectos.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_proyectos.verticalHeader().setStretchLastSection(False)
        self.check_estado_proyectos = QCheckBox(self.frame_40)
        self.check_estado_proyectos.setObjectName(u"check_estado_proyectos")
        self.check_estado_proyectos.setGeometry(QRect(10, 20, 131, 21))
        self.check_estado_proyectos.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;")

        self.gridLayout_67.addWidget(self.frame_40, 1, 1, 1, 1)

        self.stackedWidget_6.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.gridLayout_71 = QGridLayout(self.page_13)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.page_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.tabla_intituciones = QTableWidget(self.frame_15)
        if (self.tabla_intituciones.columnCount() < 6):
            self.tabla_intituciones.setColumnCount(6)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla_intituciones.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabla_intituciones.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_intituciones.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_intituciones.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_intituciones.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_intituciones.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        self.tabla_intituciones.setObjectName(u"tabla_intituciones")
        self.tabla_intituciones.setGeometry(QRect(0, 60, 851, 291))
        self.tabla_intituciones.setStyleSheet(u"QTableWidget {\n"
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
"color: #54bfc9;\n"
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
        self.tabla_intituciones.setFrameShape(QFrame.NoFrame)
        self.tabla_intituciones.setAutoScrollMargin(16)
        self.tabla_intituciones.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_intituciones.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_intituciones.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_intituciones.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_intituciones.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_intituciones.setShowGrid(False)
        self.tabla_intituciones.setSortingEnabled(False)
        self.tabla_intituciones.setCornerButtonEnabled(True)
        self.tabla_intituciones.horizontalHeader().setVisible(False)
        self.tabla_intituciones.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_intituciones.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_intituciones.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_intituciones.horizontalHeader().setHighlightSections(False)
        self.tabla_intituciones.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_intituciones.horizontalHeader().setStretchLastSection(False)
        self.tabla_intituciones.verticalHeader().setVisible(False)
        self.tabla_intituciones.verticalHeader().setMinimumSectionSize(23)
        self.tabla_intituciones.verticalHeader().setDefaultSectionSize(47)
        self.tabla_intituciones.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_intituciones.verticalHeader().setStretchLastSection(False)
        self.btn_agregar_instituto = QPushButton(self.frame_15)
        self.btn_agregar_instituto.setObjectName(u"btn_agregar_instituto")
        self.btn_agregar_instituto.setGeometry(QRect(650, 0, 195, 40))
        self.btn_agregar_instituto.setMinimumSize(QSize(195, 40))
        self.btn_agregar_instituto.setMaximumSize(QSize(110, 40))
        self.btn_agregar_instituto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_instituto.setStyleSheet(u"/*  BOTON */\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #3f5758;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #3f5758;\n"
"border-radius: 4px; }\n"
"")
        self.btn_agregar_instituto.setIcon(icon8)
        self.btn_agregar_instituto.setIconSize(QSize(15, 21))
        self.check_estado_institucion = QCheckBox(self.frame_15)
        self.check_estado_institucion.setObjectName(u"check_estado_institucion")
        self.check_estado_institucion.setGeometry(QRect(0, 20, 131, 21))
        self.check_estado_institucion.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;")

        self.gridLayout_71.addWidget(self.frame_15, 0, 0, 1, 1)

        self.stackedWidget_6.addWidget(self.page_13)

        self.gridLayout_66.addWidget(self.stackedWidget_6, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_50, 3, 0, 1, 1)

        self.frame_60 = QFrame(self.frp1_3)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 50))
        self.frame_60.setMaximumSize(QSize(16777215, 50))
        self.frame_60.setStyleSheet(u"QPushButton{\n"
"font-family: Roboto;\n"
"border: 0px;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"background-color: transparent;\n"
"letter-spacing: 0.10em;\n"
"color: #6B7280;\n"
"border-bottom:3px solid transparent\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"color:#445d5e;\n"
"font-weight: bold;\n"
"font-size: 14px;\n"
"border-bottom:2px solid #445d5e;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#54BFC9;\n"
"border-bottom:3px solid #54BFC9;\n"
"\n"
"}\n"
"\n"
"#frame_2{background-color:#F9FAFB ;font-size: 16px;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}\n"
"\n"
"")
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Plain)
        self.gridLayout_20 = QGridLayout(self.frame_60)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, -1, -1, -1)
        self.btn_menu_proyectos = QPushButton(self.frame_60)
        self.btn_menu_proyectos.setObjectName(u"btn_menu_proyectos")
        self.btn_menu_proyectos.setMinimumSize(QSize(114, 38))
        self.btn_menu_proyectos.setMaximumSize(QSize(16777215, 38))
        self.btn_menu_proyectos.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_20.addWidget(self.btn_menu_proyectos, 0, 1, 1, 1)

        self.btn_menu_institucion = QPushButton(self.frame_60)
        self.btn_menu_institucion.setObjectName(u"btn_menu_institucion")
        self.btn_menu_institucion.setMinimumSize(QSize(133, 38))
        self.btn_menu_institucion.setMaximumSize(QSize(16777215, 38))
        self.btn_menu_institucion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_institucion.setStyleSheet(u"")
        self.btn_menu_institucion.setFlat(True)

        self.gridLayout_20.addWidget(self.btn_menu_institucion, 0, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)


        self.gridLayout_19.addWidget(self.frame_60, 2, 0, 1, 1)

        self.label_10 = QLabel(self.frp1_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 22px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"\n"
"color: #000000;")

        self.gridLayout_19.addWidget(self.label_10, 1, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frp1_3, 0, 0, 1, 1)

        self.Scrollprincipal_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_21.addWidget(self.Scrollprincipal_3, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.pag3)
        self.pag4 = QWidget()
        self.pag4.setObjectName(u"pag4")
        self.pag4.setStyleSheet(u"#pag4{\n"
"background-color:#f1f1f1;\n"
"}")
        self.gridLayout_9 = QGridLayout(self.pag4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frp2 = QFrame(self.pag4)
        self.frp2.setObjectName(u"frp2")
        self.frp2.setMinimumSize(QSize(0, 0))
        self.frp2.setMaximumSize(QSize(16777215, 16777215))
        self.frp2.setStyleSheet(u"#frp2{background: #FFFFFF;\n"
"border-radius: 10px;}")
        self.frp2.setFrameShape(QFrame.NoFrame)
        self.frp2.setFrameShadow(QFrame.Plain)
        self.gridLayout_11 = QGridLayout(self.frp2)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frp2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.gridLayout_12 = QGridLayout(self.frame_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(12, 12, 12, 12)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShadow(QFrame.Plain)
        self.gridLayout_14 = QGridLayout(self.frame_12)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tabla_usuario = QTableWidget(self.frame_12)
        if (self.tabla_usuario.columnCount() < 8):
            self.tabla_usuario.setColumnCount(8)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(7, __qtablewidgetitem36)
        if (self.tabla_usuario.rowCount() < 3):
            self.tabla_usuario.setRowCount(3)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tabla_usuario.setVerticalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tabla_usuario.setVerticalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tabla_usuario.setVerticalHeaderItem(2, __qtablewidgetitem39)
        self.tabla_usuario.setObjectName(u"tabla_usuario")
        self.tabla_usuario.setStyleSheet(u"QTableWidget {\n"
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
        self.tabla_usuario.setFrameShape(QFrame.NoFrame)
        self.tabla_usuario.setAutoScrollMargin(16)
        self.tabla_usuario.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_usuario.setAlternatingRowColors(False)
        self.tabla_usuario.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_usuario.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_usuario.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_usuario.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_usuario.setShowGrid(False)
        self.tabla_usuario.setSortingEnabled(False)
        self.tabla_usuario.setCornerButtonEnabled(True)
        self.tabla_usuario.horizontalHeader().setVisible(False)
        self.tabla_usuario.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_usuario.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_usuario.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_usuario.horizontalHeader().setHighlightSections(False)
        self.tabla_usuario.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_usuario.horizontalHeader().setStretchLastSection(False)
        self.tabla_usuario.verticalHeader().setVisible(False)
        self.tabla_usuario.verticalHeader().setMinimumSectionSize(23)
        self.tabla_usuario.verticalHeader().setDefaultSectionSize(47)
        self.tabla_usuario.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_usuario.verticalHeader().setStretchLastSection(False)

        self.gridLayout_14.addWidget(self.tabla_usuario, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_12, 2, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_13, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"/* COMBOBOX */\n"
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
"	image: url(:/prefijoNuevo/flecha_oscuro.png);\n"
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #344647;\n"
"border-radius: 8px;\n"
"}")
        self.frame_11.setFrameShadow(QFrame.Plain)
        self.gridLayout_15 = QGridLayout(self.frame_11)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalSpacer_3 = QSpacerItem(23, 37, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_15.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Ignored)

        self.gridLayout_15.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 22px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"\n"
"color: #000000;")

        self.gridLayout_15.addWidget(self.label_9, 1, 0, 1, 1)

        self.btn_agregar_usuario = QPushButton(self.frame_11)
        self.btn_agregar_usuario.setObjectName(u"btn_agregar_usuario")
        self.btn_agregar_usuario.setMinimumSize(QSize(195, 40))
        self.btn_agregar_usuario.setMaximumSize(QSize(110, 40))
        self.btn_agregar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_usuario.setStyleSheet(u"/*  BOTON */\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #3f5758;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #3f5758;\n"
"border-radius: 4px; }\n"
"")
        self.btn_agregar_usuario.setIcon(icon8)
        self.btn_agregar_usuario.setIconSize(QSize(15, 21))

        self.gridLayout_15.addWidget(self.btn_agregar_usuario, 3, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_5, 3, 2, 1, 1)

        self.line_busqueda_usuario = QLineEdit(self.frame_11)
        self.line_busqueda_usuario.setObjectName(u"line_busqueda_usuario")
        self.line_busqueda_usuario.setMinimumSize(QSize(0, 40))
        self.line_busqueda_usuario.setMaximumSize(QSize(16777215, 40))
        self.line_busqueda_usuario.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #3f5758;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"")

        self.gridLayout_15.addWidget(self.line_busqueda_usuario, 3, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_11, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_10, 0, 1, 1, 1)

        self.frame_13 = QFrame(self.frp2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)


        self.gridLayout_11.addWidget(self.frame_13, 1, 0, 1, 2)


        self.gridLayout_9.addWidget(self.frp2, 1, 1, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_33, 1, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_10, 2, 1, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_41, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_9, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.pag4)
        self.pag6 = QWidget()
        self.pag6.setObjectName(u"pag6")
        self.gridLayout_62 = QGridLayout(self.pag6)
        self.gridLayout_62.setSpacing(0)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_65 = QFrame(self.pag6)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.gridLayout_73 = QGridLayout(self.frame_65)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.gridLayout_73.setHorizontalSpacing(15)
        self.gridLayout_73.setVerticalSpacing(9)
        self.gridLayout_73.setContentsMargins(30, 30, 30, 30)
        self.frame_48 = QFrame(self.frame_65)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(71, 0))
        self.frame_48.setStyleSheet(u"#frame_48{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_60 = QGridLayout(self.frame_48)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.frame_61 = QFrame(self.frame_48)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 50))
        self.frame_61.setMaximumSize(QSize(16777215, 50))
        self.frame_61.setStyleSheet(u"QPushButton{\n"
"font-family: Roboto;\n"
"border: 0px;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"background-color: transparent;\n"
"letter-spacing: 0.10em;\n"
"color: #6B7280;\n"
"border-bottom:3px solid transparent\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"color:#445d5e;\n"
"font-weight: bold;\n"
"font-size: 14px;\n"
"border-bottom:2px solid #445d5e;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#54BFC9;\n"
"border-bottom:3px solid #54BFC9;\n"
"\n"
"}\n"
"\n"
"#frame_2{background-color:#F9FAFB ;font-size: 16px;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;}\n"
"\n"
"")
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Plain)
        self.gridLayout_24 = QGridLayout(self.frame_61)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, -1, -1, -1)
        self.radioTutor = QPushButton(self.frame_61)
        self.radioTutor.setObjectName(u"radioTutor")
        self.radioTutor.setMinimumSize(QSize(192, 38))
        self.radioTutor.setMaximumSize(QSize(16777215, 38))
        self.radioTutor.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_24.addWidget(self.radioTutor, 0, 1, 1, 1)

        self.radioEstudiante = QPushButton(self.frame_61)
        self.radioEstudiante.setObjectName(u"radioEstudiante")
        self.radioEstudiante.setMinimumSize(QSize(246, 38))
        self.radioEstudiante.setMaximumSize(QSize(16777215, 38))
        self.radioEstudiante.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioEstudiante.setStyleSheet(u"")
        self.radioEstudiante.setFlat(True)

        self.gridLayout_24.addWidget(self.radioEstudiante, 0, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)


        self.gridLayout_60.addWidget(self.frame_61, 0, 0, 1, 1)

        self.stackedWidget_5 = QStackedWidget(self.frame_48)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_61 = QGridLayout(self.page_10)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.page_10)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"#frame_38{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_38.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.frame_38)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_20 = QFrame(self.frame_38)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 76))
        self.frame_20.setMaximumSize(QSize(16777215, 76))
        self.frame_20.setStyleSheet(u"QRadioButton{\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    color: #9CA3AF;\n"
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
""
                        "QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #3f5758;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;}")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_20)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(9, 6, -1, -1)
        self.radioProcesoT = QRadioButton(self.frame_20)
        self.radioProcesoT.setObjectName(u"radioProcesoT")
        self.radioProcesoT.setChecked(True)

        self.gridLayout_25.addWidget(self.radioProcesoT, 1, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_9, 1, 6, 1, 1)

        self.radioPendienteT = QRadioButton(self.frame_20)
        self.radioPendienteT.setObjectName(u"radioPendienteT")

        self.gridLayout_25.addWidget(self.radioPendienteT, 1, 3, 1, 1)

        self.radioCulminadoT = QRadioButton(self.frame_20)
        self.radioCulminadoT.setObjectName(u"radioCulminadoT")

        self.gridLayout_25.addWidget(self.radioCulminadoT, 1, 5, 1, 1)

        self.cbo_tutores = QComboBox(self.frame_20)
        self.cbo_tutores.setObjectName(u"cbo_tutores")
        self.cbo_tutores.setMinimumSize(QSize(300, 40))

        self.gridLayout_25.addWidget(self.cbo_tutores, 1, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_14, 1, 2, 1, 1)

        self.label = QLabel(self.frame_20)
        self.label.setObjectName(u"label")

        self.gridLayout_25.addWidget(self.label, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_38)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_21)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.tabla_reporte_tutores = QTableWidget(self.frame_21)
        if (self.tabla_reporte_tutores.columnCount() < 4):
            self.tabla_reporte_tutores.setColumnCount(4)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(3, __qtablewidgetitem43)
        if (self.tabla_reporte_tutores.rowCount() < 3):
            self.tabla_reporte_tutores.setRowCount(3)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tabla_reporte_tutores.setVerticalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tabla_reporte_tutores.setVerticalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tabla_reporte_tutores.setVerticalHeaderItem(2, __qtablewidgetitem46)
        self.tabla_reporte_tutores.setObjectName(u"tabla_reporte_tutores")
        self.tabla_reporte_tutores.setStyleSheet(u"QTableWidget {\n"
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
        self.tabla_reporte_tutores.setFrameShape(QFrame.NoFrame)
        self.tabla_reporte_tutores.setAutoScrollMargin(16)
        self.tabla_reporte_tutores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_reporte_tutores.setAlternatingRowColors(False)
        self.tabla_reporte_tutores.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_reporte_tutores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_reporte_tutores.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_tutores.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_tutores.setShowGrid(False)
        self.tabla_reporte_tutores.setSortingEnabled(False)
        self.tabla_reporte_tutores.setCornerButtonEnabled(True)
        self.tabla_reporte_tutores.horizontalHeader().setVisible(False)
        self.tabla_reporte_tutores.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_reporte_tutores.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_reporte_tutores.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_reporte_tutores.horizontalHeader().setHighlightSections(False)
        self.tabla_reporte_tutores.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_tutores.horizontalHeader().setStretchLastSection(False)
        self.tabla_reporte_tutores.verticalHeader().setVisible(False)
        self.tabla_reporte_tutores.verticalHeader().setMinimumSectionSize(23)
        self.tabla_reporte_tutores.verticalHeader().setDefaultSectionSize(47)
        self.tabla_reporte_tutores.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_tutores.verticalHeader().setStretchLastSection(False)

        self.gridLayout_23.addWidget(self.tabla_reporte_tutores, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_38)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 47))
        self.frame_22.setMaximumSize(QSize(16777215, 47))
        self.frame_22.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"text-transform: uppercase;\n"
"color: #6B7280;}\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:4px;\n"
"background: #3f5758;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #3f5758;\n"
"border-radius: 4px; }\n"
"")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(198, 16, 69, 17))
        self.label_12.setStyleSheet(u"")
        self.cbox_rango_reporte_tutor = QComboBox(self.frame_22)
        self.cbox_rango_reporte_tutor.addItem("")
        self.cbox_rango_reporte_tutor.addItem("")
        self.cbox_rango_reporte_tutor.addItem("")
        self.cbox_rango_reporte_tutor.setObjectName(u"cbox_rango_reporte_tutor")
        self.cbox_rango_reporte_tutor.setGeometry(QRect(95, 6, 92, 38))
        self.cbox_rango_reporte_tutor.setMinimumSize(QSize(92, 38))
        self.cbox_rango_reporte_tutor.setMaximumSize(QSize(92, 38))
        self.cbox_rango_reporte_tutor.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_rango_reporte_tutor.setStyleSheet(u"\n"
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
"\n"
"\n"
"")
        self.label_11 = QLabel(self.frame_22)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(9, 15, 80, 17))
        self.label_11.setMinimumSize(QSize(80, 0))
        self.label_11.setMaximumSize(QSize(58, 16777215))
        self.label_11.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.frame_22)


        self.gridLayout_61.addWidget(self.frame_38, 1, 1, 1, 1)

        self.stackedWidget_5.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.gridLayout_65 = QGridLayout(self.page_11)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.page_11)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"#frame_39{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_39.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_39)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_16 = QFrame(self.frame_39)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(53, 80))
        self.frame_16.setMaximumSize(QSize(16777215, 80))
        self.frame_16.setStyleSheet(u"QRadioButton{\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    color: #9CA3AF;\n"
"}\n"
"\n"
"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;}\n"
"\n"
"#check_todos_estudiantes{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;\n"
"}")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_16)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.line_busqueda_reporte_estudiantes = QLineEdit(self.frame_16)
        self.line_busqueda_reporte_estudiantes.setObjectName(u"line_busqueda_reporte_estudiantes")
        self.line_busqueda_reporte_estudiantes.setMinimumSize(QSize(0, 40))
        self.line_busqueda_reporte_estudiantes.setMaximumSize(QSize(16777215, 40))
        self.line_busqueda_reporte_estudiantes.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #3f5758;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"")

        self.gridLayout_26.addWidget(self.line_busqueda_reporte_estudiantes, 1, 0, 1, 1)

        self.check_todos_estudiantes = QCheckBox(self.frame_16)
        self.check_todos_estudiantes.setObjectName(u"check_todos_estudiantes")
        self.check_todos_estudiantes.setChecked(True)

        self.gridLayout_26.addWidget(self.check_todos_estudiantes, 1, 2, 1, 1)

        self.label_3 = QLabel(self.frame_16)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_26.addWidget(self.label_3, 0, 0, 1, 1)

        self.radioPendienteE = QRadioButton(self.frame_16)
        self.radioPendienteE.setObjectName(u"radioPendienteE")

        self.gridLayout_26.addWidget(self.radioPendienteE, 1, 4, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_10, 1, 3, 1, 1)

        self.radioCulminadoE = QRadioButton(self.frame_16)
        self.radioCulminadoE.setObjectName(u"radioCulminadoE")

        self.gridLayout_26.addWidget(self.radioCulminadoE, 1, 7, 1, 1)

        self.radioProcesoE = QRadioButton(self.frame_16)
        self.radioProcesoE.setObjectName(u"radioProcesoE")
        self.radioProcesoE.setChecked(True)

        self.gridLayout_26.addWidget(self.radioProcesoE, 1, 5, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_7, 1, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_39)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_17)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tabla_reporte_estudiantes = QTableWidget(self.frame_17)
        if (self.tabla_reporte_estudiantes.columnCount() < 4):
            self.tabla_reporte_estudiantes.setColumnCount(4)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(3, __qtablewidgetitem50)
        if (self.tabla_reporte_estudiantes.rowCount() < 3):
            self.tabla_reporte_estudiantes.setRowCount(3)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setVerticalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setVerticalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setVerticalHeaderItem(2, __qtablewidgetitem53)
        self.tabla_reporte_estudiantes.setObjectName(u"tabla_reporte_estudiantes")
        self.tabla_reporte_estudiantes.setStyleSheet(u"QTableWidget {\n"
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
        self.tabla_reporte_estudiantes.setFrameShape(QFrame.NoFrame)
        self.tabla_reporte_estudiantes.setAutoScrollMargin(16)
        self.tabla_reporte_estudiantes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_reporte_estudiantes.setAlternatingRowColors(False)
        self.tabla_reporte_estudiantes.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_reporte_estudiantes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_reporte_estudiantes.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_estudiantes.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_estudiantes.setShowGrid(False)
        self.tabla_reporte_estudiantes.setSortingEnabled(False)
        self.tabla_reporte_estudiantes.setCornerButtonEnabled(True)
        self.tabla_reporte_estudiantes.horizontalHeader().setVisible(False)
        self.tabla_reporte_estudiantes.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_reporte_estudiantes.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_reporte_estudiantes.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_reporte_estudiantes.horizontalHeader().setHighlightSections(False)
        self.tabla_reporte_estudiantes.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_estudiantes.horizontalHeader().setStretchLastSection(False)
        self.tabla_reporte_estudiantes.verticalHeader().setVisible(False)
        self.tabla_reporte_estudiantes.verticalHeader().setMinimumSectionSize(23)
        self.tabla_reporte_estudiantes.verticalHeader().setDefaultSectionSize(47)
        self.tabla_reporte_estudiantes.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_estudiantes.verticalHeader().setStretchLastSection(False)

        self.gridLayout_22.addWidget(self.tabla_reporte_estudiantes, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_39)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 50))
        self.frame_18.setMaximumSize(QSize(16777215, 50))
        self.frame_18.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"text-transform: uppercase;\n"
"color: #6B7280;}\n"
"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:4px;\n"
"background: #3f5758;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:hover{background: #3f5758;\n"
"border-radius: 4px; }\n"
"")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(220, 4, 704, 42))
        self.label_15.setStyleSheet(u"")
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 4, 80, 42))
        self.label_16.setMinimumSize(QSize(80, 0))
        self.label_16.setMaximumSize(QSize(58, 16777215))
        self.label_16.setStyleSheet(u"")
        self.cbox_rango_estudiantes = QComboBox(self.frame_18)
        self.cbox_rango_estudiantes.addItem("")
        self.cbox_rango_estudiantes.addItem("")
        self.cbox_rango_estudiantes.addItem("")
        self.cbox_rango_estudiantes.setObjectName(u"cbox_rango_estudiantes")
        self.cbox_rango_estudiantes.setGeometry(QRect(100, 8, 92, 38))
        self.cbox_rango_estudiantes.setMinimumSize(QSize(92, 38))
        self.cbox_rango_estudiantes.setMaximumSize(QSize(92, 38))
        self.cbox_rango_estudiantes.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_rango_estudiantes.setStyleSheet(u"\n"
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
"\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.frame_18)


        self.gridLayout_65.addWidget(self.frame_39, 2, 0, 1, 1)

        self.stackedWidget_5.addWidget(self.page_11)

        self.gridLayout_60.addWidget(self.stackedWidget_5, 1, 0, 1, 1)


        self.gridLayout_73.addWidget(self.frame_48, 1, 0, 1, 2)


        self.gridLayout_62.addWidget(self.frame_65, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.pag6)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_widgets)


        self.horizontalLayout.addWidget(self.frame_contenido)


        self.gridLayout.addWidget(self.frame_principal, 0, 0, 1, 1)

        principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(principal)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_6.setCurrentIndex(1)
        self.stackedWidget_5.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(principal)
    # setupUi

    def retranslateUi(self, principal):
        principal.setWindowTitle(QCoreApplication.translate("principal", u"UNIVERSIDAD ESTATAL DEL SUR DE MANABI", None))
        self.lbl_logo2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_reporte.setToolTip(QCoreApplication.translate("principal", u"Reportes", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reporte.setText(QCoreApplication.translate("principal", u"     Reportes", None))
#if QT_CONFIG(tooltip)
        self.btn_seguimientoo.setToolTip(QCoreApplication.translate("principal", u"Seguimiento", None))
#endif // QT_CONFIG(tooltip)
        self.btn_seguimientoo.setText(QCoreApplication.translate("principal", u"     Seguimiento", None))
#if QT_CONFIG(tooltip)
        self.btn_afiliacion.setToolTip(QCoreApplication.translate("principal", u"Paciente", None))
#endif // QT_CONFIG(tooltip)
        self.btn_afiliacion.setText(QCoreApplication.translate("principal", u"     Afiliacion", None))
#if QT_CONFIG(tooltip)
        self.btn_usuario.setToolTip(QCoreApplication.translate("principal", u"Usuarios", None))
#endif // QT_CONFIG(tooltip)
        self.btn_usuario.setText(QCoreApplication.translate("principal", u"     Usuarios", None))
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("principal", u"Inicio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText(QCoreApplication.translate("principal", u"     Mantenimiento", None))
        self.btn_cerrar.setText(QCoreApplication.translate("principal", u"    Cerrar Sesi\u00f3n", None))
        self.boton_deslizable.setText("")
        self.lbl_hora.setText(QCoreApplication.translate("principal", u"12:20:10", None))
        self.lbl_fecha.setText(QCoreApplication.translate("principal", u"sabado, 30 de enero de 2021", None))
        self.lbl_usuario.setText(QCoreApplication.translate("principal", u"Manuel", None))
        self.lbl_rol.setText(QCoreApplication.translate("principal", u"Admin", None))
        self.label_color_sesion_2.setText("")
        self.cbox_perfil.setItemText(0, QCoreApplication.translate("principal", u"Perfil", None))
        self.cbox_perfil.setItemText(1, QCoreApplication.translate("principal", u"Cerrar Sesion", None))

        self.lbl_online.setText(QCoreApplication.translate("principal", u"    Online", None))
        self.label_2.setText(QCoreApplication.translate("principal", u"  Lista de Vinculaci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("principal", u"MOSTRAR", None))
        self.cbox_rango.setItemText(0, QCoreApplication.translate("principal", u"5", None))
        self.cbox_rango.setItemText(1, QCoreApplication.translate("principal", u"10", None))
        self.cbox_rango.setItemText(2, QCoreApplication.translate("principal", u"50", None))

        self.label_5.setText(QCoreApplication.translate("principal", u"REGISTRO", None))
#if QT_CONFIG(tooltip)
        self.btn_recargar.setToolTip(QCoreApplication.translate("principal", u"Actualizar registro", None))
#endif // QT_CONFIG(tooltip)
        self.btn_recargar.setText("")
        ___qtablewidgetitem = self.tabla_principal.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_principal.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("principal", u"FECHA REGISTRO", None));
        ___qtablewidgetitem2 = self.tabla_principal.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("principal", u"ESTUDIANTE", None));
        ___qtablewidgetitem3 = self.tabla_principal.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("principal", u"FECHA AFILIACION", None));
        ___qtablewidgetitem4 = self.tabla_principal.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("principal", u"TUTOR", None));
        ___qtablewidgetitem5 = self.tabla_principal.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("principal", u"ESTADO VINCULACI\u00d3N", None));
        ___qtablewidgetitem6 = self.tabla_principal.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("principal", u"ACCIONES", None));
        ___qtablewidgetitem7 = self.tabla_principal.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem8 = self.tabla_principal.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem9 = self.tabla_principal.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.line_busqueda.setPlaceholderText(QCoreApplication.translate("principal", u"Buscar por cualquier campo", None))
        self.btn_nuevoafiliacion.setText(QCoreApplication.translate("principal", u" Nueva Vinculaci\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("principal", u"  Lista de alumnos asignados", None))
        self.line_busqueda_tutor.setPlaceholderText(QCoreApplication.translate("principal", u"Buscar por cualquier campo", None))
        self.label_7.setText(QCoreApplication.translate("principal", u"MOSTRAR", None))
        self.cbox_rango_tutor.setItemText(0, QCoreApplication.translate("principal", u"5", None))
        self.cbox_rango_tutor.setItemText(1, QCoreApplication.translate("principal", u"10", None))
        self.cbox_rango_tutor.setItemText(2, QCoreApplication.translate("principal", u"50", None))

        self.label_8.setText(QCoreApplication.translate("principal", u"REGISTRO", None))
#if QT_CONFIG(tooltip)
        self.btn_recargar_tutor.setToolTip(QCoreApplication.translate("principal", u"Actualizar registro", None))
#endif // QT_CONFIG(tooltip)
        self.btn_recargar_tutor.setText("")
        ___qtablewidgetitem10 = self.tabla_principal_tutor.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem11 = self.tabla_principal_tutor.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("principal", u"ESTUDIANTE", None));
        ___qtablewidgetitem12 = self.tabla_principal_tutor.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("principal", u"FECHA AFILIACI\u00d3N", None));
        ___qtablewidgetitem13 = self.tabla_principal_tutor.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("principal", u"HORAS SEGUIMIENTO", None));
        ___qtablewidgetitem14 = self.tabla_principal_tutor.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("principal", u"ESTADO VINCULACI\u00d3N", None));
        ___qtablewidgetitem15 = self.tabla_principal_tutor.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("principal", u"ACCIONES", None));
        ___qtablewidgetitem16 = self.tabla_principal_tutor.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem17 = self.tabla_principal_tutor.verticalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem18 = self.tabla_principal_tutor.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.btn_agregar_proyectos.setText(QCoreApplication.translate("principal", u"Lista de proyectos", None))
        ___qtablewidgetitem19 = self.tabla_proyectos.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem20 = self.tabla_proyectos.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("principal", u"NOMBRE INSTITUCIONES", None));
        ___qtablewidgetitem21 = self.tabla_proyectos.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("principal", u"ESTADO", None));
        ___qtablewidgetitem22 = self.tabla_proyectos.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("principal", u"ACCIONES", None));
        self.check_estado_proyectos.setText(QCoreApplication.translate("principal", u"Mostrar inactivos", None))
        ___qtablewidgetitem23 = self.tabla_intituciones.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem24 = self.tabla_intituciones.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("principal", u"NOMBRE INSTITUCIONES", None));
        ___qtablewidgetitem25 = self.tabla_intituciones.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("principal", u"TIPO INSTUTICION", None));
        ___qtablewidgetitem26 = self.tabla_intituciones.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("principal", u"DIRECCION", None));
        ___qtablewidgetitem27 = self.tabla_intituciones.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("principal", u"ESTADO", None));
        ___qtablewidgetitem28 = self.tabla_intituciones.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("principal", u"ACCIONES", None));
        self.btn_agregar_instituto.setText(QCoreApplication.translate("principal", u"  Agregar Instituci\u00f3n", None))
        self.check_estado_institucion.setText(QCoreApplication.translate("principal", u"Mostrar inactivos", None))
        self.btn_menu_proyectos.setText(QCoreApplication.translate("principal", u"PROYECTOS", None))
        self.btn_menu_institucion.setText(QCoreApplication.translate("principal", u"INSTITUCIONES", None))
        self.label_10.setText(QCoreApplication.translate("principal", u" Mantenimiento", None))
        ___qtablewidgetitem29 = self.tabla_usuario.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem30 = self.tabla_usuario.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("principal", u"USUARIO", None));
        ___qtablewidgetitem31 = self.tabla_usuario.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("principal", u"DOCUMENTO IDENTIDAD", None));
        ___qtablewidgetitem32 = self.tabla_usuario.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("principal", u"CARGO", None));
        ___qtablewidgetitem33 = self.tabla_usuario.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("principal", u"CORREO", None));
        ___qtablewidgetitem34 = self.tabla_usuario.horizontalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("principal", u"FECHA REGISTRO", None));
        ___qtablewidgetitem35 = self.tabla_usuario.horizontalHeaderItem(6)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("principal", u"ESTADO", None));
        ___qtablewidgetitem36 = self.tabla_usuario.horizontalHeaderItem(7)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("principal", u"ACCIONES", None));
        ___qtablewidgetitem37 = self.tabla_usuario.verticalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem38 = self.tabla_usuario.verticalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem39 = self.tabla_usuario.verticalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.label_9.setText(QCoreApplication.translate("principal", u"Lista de usuarios registrados", None))
        self.btn_agregar_usuario.setText(QCoreApplication.translate("principal", u"  Agregar usuario", None))
        self.line_busqueda_usuario.setPlaceholderText(QCoreApplication.translate("principal", u"Nombre y apellidos...", None))
        self.radioTutor.setText(QCoreApplication.translate("principal", u"REPORTE POR TUTORES", None))
        self.radioEstudiante.setText(QCoreApplication.translate("principal", u"REPORTE POR ESTUDIANTES", None))
        self.radioProcesoT.setText(QCoreApplication.translate("principal", u"Proceso", None))
        self.radioPendienteT.setText(QCoreApplication.translate("principal", u"Pendiente", None))
        self.radioCulminadoT.setText(QCoreApplication.translate("principal", u"Culminado", None))
        self.label.setText(QCoreApplication.translate("principal", u"Seleccione tutor", None))
        ___qtablewidgetitem40 = self.tabla_reporte_tutores.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("principal", u"ESTUDIANTE", None));
        ___qtablewidgetitem41 = self.tabla_reporte_tutores.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("principal", u"FECHA AFILIACI\u00d3N", None));
        ___qtablewidgetitem42 = self.tabla_reporte_tutores.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("principal", u"HORAS SEGUIMIENTO", None));
        ___qtablewidgetitem43 = self.tabla_reporte_tutores.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("principal", u"ESTADO VINCULACI\u00d3N", None));
        ___qtablewidgetitem44 = self.tabla_reporte_tutores.verticalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem45 = self.tabla_reporte_tutores.verticalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem46 = self.tabla_reporte_tutores.verticalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.label_12.setText(QCoreApplication.translate("principal", u"REGISTRO", None))
        self.cbox_rango_reporte_tutor.setItemText(0, QCoreApplication.translate("principal", u"5", None))
        self.cbox_rango_reporte_tutor.setItemText(1, QCoreApplication.translate("principal", u"10", None))
        self.cbox_rango_reporte_tutor.setItemText(2, QCoreApplication.translate("principal", u"50", None))

        self.label_11.setText(QCoreApplication.translate("principal", u"MOSTRAR", None))
        self.line_busqueda_reporte_estudiantes.setPlaceholderText(QCoreApplication.translate("principal", u"Filtrar por nombre estudiante...", None))
        self.check_todos_estudiantes.setText(QCoreApplication.translate("principal", u"Todos", None))
        self.label_3.setText(QCoreApplication.translate("principal", u"Filtrar por nombre estudiante", None))
        self.radioPendienteE.setText(QCoreApplication.translate("principal", u"Pendiente", None))
        self.radioCulminadoE.setText(QCoreApplication.translate("principal", u"Culminado", None))
        self.radioProcesoE.setText(QCoreApplication.translate("principal", u"Proceso", None))
        ___qtablewidgetitem47 = self.tabla_reporte_estudiantes.horizontalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("principal", u"ESTUDIANTE", None));
        ___qtablewidgetitem48 = self.tabla_reporte_estudiantes.horizontalHeaderItem(1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("principal", u"FECHA AFILIACION", None));
        ___qtablewidgetitem49 = self.tabla_reporte_estudiantes.horizontalHeaderItem(2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("principal", u"TUTOR", None));
        ___qtablewidgetitem50 = self.tabla_reporte_estudiantes.horizontalHeaderItem(3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("principal", u"ESTADO VINCULACI\u00d3N", None));
        ___qtablewidgetitem51 = self.tabla_reporte_estudiantes.verticalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem52 = self.tabla_reporte_estudiantes.verticalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem53 = self.tabla_reporte_estudiantes.verticalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.label_15.setText(QCoreApplication.translate("principal", u"REGISTRO", None))
        self.label_16.setText(QCoreApplication.translate("principal", u"MOSTRAR", None))
        self.cbox_rango_estudiantes.setItemText(0, QCoreApplication.translate("principal", u"5", None))
        self.cbox_rango_estudiantes.setItemText(1, QCoreApplication.translate("principal", u"10", None))
        self.cbox_rango_estudiantes.setItemText(2, QCoreApplication.translate("principal", u"50", None))

    # retranslateUi

