# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principalbtEgez.ui'
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
        principal.resize(1393, 734)
        principal.setMinimumSize(QSize(1187, 640))
        principal.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/menu/logito2.png", QSize(), QIcon.Normal, QIcon.Off)
        principal.setWindowIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u":/menu/menureport.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reporte.setIcon(icon1)
        self.btn_reporte.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.btn_reporte, 9, 0, 1, 1)

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

        self.gridLayout_3.addWidget(self.btn_afiliacion, 6, 0, 1, 1)

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

        self.gridLayout_3.addWidget(self.btn_usuario, 11, 0, 1, 1)

        self.btn_seguimientoo = QPushButton(self.frame_op)
        self.btn_seguimientoo.setObjectName(u"btn_seguimientoo")
        self.btn_seguimientoo.setMinimumSize(QSize(0, 55))
        self.btn_seguimientoo.setMaximumSize(QSize(16777215, 55))
        icon4 = QIcon()
        icon4.addFile(u":/menu/menuseguimiento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_seguimientoo.setIcon(icon4)
        self.btn_seguimientoo.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.btn_seguimientoo, 10, 0, 1, 1)

        self.btn_home = QPushButton(self.frame_op)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setEnabled(True)
        self.btn_home.setMinimumSize(QSize(0, 55))
        self.btn_home.setMaximumSize(QSize(220, 55))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/menu/menu_mantenimiento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon5)
        self.btn_home.setIconSize(QSize(33, 33))

        self.gridLayout_3.addWidget(self.btn_home, 5, 0, 1, 1)


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
        icon6 = QIcon()
        icon6.addFile(u":/menu/menusalir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u":/menu/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_deslizable.setIcon(icon7)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1232, 580))
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
        self.gridLayout_7 = QGridLayout(self.frp1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(12)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frp1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 42))
        self.frame_7.setMaximumSize(QSize(16777215, 46))
        self.frame_7.setStyleSheet(u"/* Estilo de la Etiqueta */\n"
"QLabel {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"    margin-top: 20px; /* Incrementamos el margen superior para m\u00e1s espacio */\n"
"}\n"
"\n"
"/* Estilo Base del Bot\u00f3n de la Paginaci\u00f3n */\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 10px 20px; /* Incrementamos el padding para un mejor tama\u00f1o de bot\u00f3n */\n"
"    background: #3f5758;\n"
"    border: none; /* Eliminamos el borde por defecto */\n"
"    border-radius: 8px; /* Ajustamos el border-radius */\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Pasar el Rat\u00f3n (Hover) */\n"
"QPushButton:hover {\n"
"    background: #4a6b6c; /* Color de fondo m\u00e1s claro */\n"
"    border-r"
                        "adius: 8px;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Hacer Clic (Pressed) */\n"
"QPushButton:pressed {\n"
"    background: #2e4546; /* Color de fondo m\u00e1s oscuro */\n"
"    border-radius: 8px;\n"
"}")
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.btn_pag_antes_vinculacion = QPushButton(self.frame_7)
        self.btn_pag_antes_vinculacion.setObjectName(u"btn_pag_antes_vinculacion")
        self.btn_pag_antes_vinculacion.setMinimumSize(QSize(59, 29))
        self.btn_pag_antes_vinculacion.setMaximumSize(QSize(110, 20))
        self.btn_pag_antes_vinculacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_antes_vinculacion.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/menu/hacia-atras.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pag_antes_vinculacion.setIcon(icon8)
        self.btn_pag_antes_vinculacion.setIconSize(QSize(15, 21))

        self.horizontalLayout_5.addWidget(self.btn_pag_antes_vinculacion)

        self.lbl_pagina_vinculacion = QLabel(self.frame_7)
        self.lbl_pagina_vinculacion.setObjectName(u"lbl_pagina_vinculacion")
        self.lbl_pagina_vinculacion.setMinimumSize(QSize(45, 0))
        self.lbl_pagina_vinculacion.setStyleSheet(u"")
        self.lbl_pagina_vinculacion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lbl_pagina_vinculacion)

        self.btn_pag_desp_vinculacion = QPushButton(self.frame_7)
        self.btn_pag_desp_vinculacion.setObjectName(u"btn_pag_desp_vinculacion")
        self.btn_pag_desp_vinculacion.setMinimumSize(QSize(59, 29))
        self.btn_pag_desp_vinculacion.setMaximumSize(QSize(110, 20))
        self.btn_pag_desp_vinculacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_desp_vinculacion.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/menu/hacia-adelante.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pag_desp_vinculacion.setIcon(icon9)
        self.btn_pag_desp_vinculacion.setIconSize(QSize(15, 21))

        self.horizontalLayout_5.addWidget(self.btn_pag_desp_vinculacion)


        self.gridLayout_7.addWidget(self.frame_7, 2, 0, 1, 1)

        self.frame_5 = QFrame(self.frp1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_15 = QSpacerItem(20, 16, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_15, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 130))
        self.frame_4.setMaximumSize(QSize(16777215, 130))
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
"#groupBox_4{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_4)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(12)
        self.gridLayout_32.setVerticalSpacing(0)
        self.gridLayout_32.setContentsMargins(8, 0, 5, 0)
        self.line_filtro_estudiante = QLineEdit(self.frame_4)
        self.line_filtro_estudiante.setObjectName(u"line_filtro_estudiante")
        self.line_filtro_estudiante.setMinimumSize(QSize(346, 40))
        self.line_filtro_estudiante.setMaximumSize(QSize(16777215, 40))
        self.line_filtro_estudiante.setStyleSheet(u"")

        self.gridLayout_32.addWidget(self.line_filtro_estudiante, 2, 1, 1, 2)

        self.cbo_filtro_proyecto = QComboBox(self.frame_4)
        self.cbo_filtro_proyecto.addItem("")
        self.cbo_filtro_proyecto.setObjectName(u"cbo_filtro_proyecto")

        self.gridLayout_32.addWidget(self.cbo_filtro_proyecto, 1, 0, 1, 2)

        self.cbo_filtro_tutor = QComboBox(self.frame_4)
        self.cbo_filtro_tutor.addItem("")
        self.cbo_filtro_tutor.setObjectName(u"cbo_filtro_tutor")
        self.cbo_filtro_tutor.setMinimumSize(QSize(295, 0))

        self.gridLayout_32.addWidget(self.cbo_filtro_tutor, 2, 0, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 17))
        self.label.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 16px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;}")

        self.gridLayout_32.addWidget(self.label, 0, 0, 1, 1)

        self.cbo_filtro_periodo = QComboBox(self.frame_4)
        self.cbo_filtro_periodo.addItem("")
        self.cbo_filtro_periodo.setObjectName(u"cbo_filtro_periodo")
        self.cbo_filtro_periodo.setMaximumSize(QSize(265, 16777215))

        self.gridLayout_32.addWidget(self.cbo_filtro_periodo, 1, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_42 = QFrame(self.frame_5)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(350, 0))
        self.frame_42.setMaximumSize(QSize(177, 16777215))
        self.frame_42.setStyleSheet(u"QPushButton {\n"
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
"}")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.btn_nueva_vinculacion = QPushButton(self.frame_42)
        self.btn_nueva_vinculacion.setObjectName(u"btn_nueva_vinculacion")
        self.btn_nueva_vinculacion.setGeometry(QRect(176, 1, 171, 40))
        self.btn_nueva_vinculacion.setMinimumSize(QSize(164, 40))
        self.btn_nueva_vinculacion.setMaximumSize(QSize(171, 150))
        self.btn_nueva_vinculacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nueva_vinculacion.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/menu/botonadd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nueva_vinculacion.setIcon(icon10)
        self.btn_nueva_vinculacion.setIconSize(QSize(15, 21))

        self.gridLayout_8.addWidget(self.frame_42, 0, 1, 1, 1)

        self.tabla_vinculacion = QTableWidget(self.frame_5)
        if (self.tabla_vinculacion.columnCount() < 6):
            self.tabla_vinculacion.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_vinculacion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_vinculacion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_vinculacion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_vinculacion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_vinculacion.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_vinculacion.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabla_vinculacion.setObjectName(u"tabla_vinculacion")
        self.tabla_vinculacion.setAutoFillBackground(False)
        self.tabla_vinculacion.setStyleSheet(u"/* Estilo Base del QTableWidget */\n"
"QTableWidget {\n"
"    outline: 0px;\n"
"    border: 5px solid #f3f4f6;\n"
"    border-radius: 15px;\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    line-height: 19px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #6B7280;\n"
"    gridline-color: #e0e0e0; /* Color de las l\u00edneas de la cuadr\u00edcula */\n"
"}\n"
"\n"
"/* Estilo de las Celdas */\n"
"QTableWidget::item {\n"
"    border-bottom: 3px solid #f3f4f6;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Estilo de las Celdas Seleccionadas */\n"
"QTableWidget::item:selected {\n"
"    background: #465e5f; /* Fondo m\u00e1s claro para la celda seleccionada */\n"
"    color: #ffffff; /* Color de texto claro para las celdas seleccionadas */\n"
"}\n"
"\n"
"/* Estilo de las Celdas Deshabilitadas */\n"
"QTableWidget::disabled {\n"
"    background-color: #acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"}\n"
""
                        "\n"
"/* Estilo de las Secciones de la Cabecera */\n"
"QHeaderView::section {\n"
"    background-color: #f1f2f3;\n"
"    border-style: none;\n"
"    height: 40px;\n"
"    font-family: \"Roboto\";\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"}\n"
"\n"
"/* Estilo de las Secciones Horizontales de la Cabecera */\n"
"QHeaderView::section:horizontal {\n"
"    font-size: 14px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"   text-transform: uppercase; /* Convertir texto a may\u00fasculas */;\n"
"    color: #212529;\n"
"    border-bottom: 2px solid #e0e0e0; /* Separador inferior */\n"
"}\n"
"")
        self.tabla_vinculacion.setFrameShape(QFrame.Panel)
        self.tabla_vinculacion.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabla_vinculacion.setAutoScroll(True)
        self.tabla_vinculacion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_vinculacion.setAlternatingRowColors(False)
        self.tabla_vinculacion.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_vinculacion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_vinculacion.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tabla_vinculacion.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_vinculacion.setShowGrid(False)
        self.tabla_vinculacion.setSortingEnabled(False)
        self.tabla_vinculacion.setWordWrap(True)
        self.tabla_vinculacion.setCornerButtonEnabled(False)
        self.tabla_vinculacion.horizontalHeader().setVisible(False)
        self.tabla_vinculacion.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_vinculacion.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_vinculacion.horizontalHeader().setDefaultSectionSize(170)
        self.tabla_vinculacion.horizontalHeader().setHighlightSections(False)
        self.tabla_vinculacion.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_vinculacion.horizontalHeader().setStretchLastSection(False)
        self.tabla_vinculacion.verticalHeader().setVisible(False)
        self.tabla_vinculacion.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_vinculacion.verticalHeader().setMinimumSectionSize(23)
        self.tabla_vinculacion.verticalHeader().setDefaultSectionSize(47)
        self.tabla_vinculacion.verticalHeader().setHighlightSections(True)
        self.tabla_vinculacion.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_vinculacion.verticalHeader().setStretchLastSection(False)

        self.gridLayout_8.addWidget(self.tabla_vinculacion, 2, 0, 2, 2)


        self.gridLayout_7.addWidget(self.frame_5, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frp1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 22px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"\n"
"color: #000000;")

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)


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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1234, 575))
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
        icon11 = QIcon()
        icon11.addFile(u":/menu/menuactualizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_recargar_tutor.setIcon(icon11)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_principal_tutor.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        if (self.tabla_principal_tutor.rowCount() < 3):
            self.tabla_principal_tutor.setRowCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_principal_tutor.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_principal_tutor.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_principal_tutor.setVerticalHeaderItem(2, __qtablewidgetitem14)
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

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.Scrollprincipal_3 = QScrollArea(self.pag3)
        self.Scrollprincipal_3.setObjectName(u"Scrollprincipal_3")
        self.Scrollprincipal_3.setStyleSheet(u"")
        self.Scrollprincipal_3.setFrameShape(QFrame.NoFrame)
        self.Scrollprincipal_3.setFrameShadow(QFrame.Plain)
        self.Scrollprincipal_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1232, 579))
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
        self.stacked_administracion = QStackedWidget(self.frame_50)
        self.stacked_administracion.setObjectName(u"stacked_administracion")
        self.page_estudiantes = QWidget()
        self.page_estudiantes.setObjectName(u"page_estudiantes")
        self.gridLayout_67 = QGridLayout(self.page_estudiantes)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.page_estudiantes)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"#frame_38{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_40.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_40)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_25 = QFrame(self.frame_40)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 57))
        self.frame_25.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
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
"")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, -1, -1)
        self.line_busqueda_estudiantes = QLineEdit(self.frame_25)
        self.line_busqueda_estudiantes.setObjectName(u"line_busqueda_estudiantes")
        self.line_busqueda_estudiantes.setMinimumSize(QSize(0, 43))
        self.line_busqueda_estudiantes.setMaximumSize(QSize(16777215, 40))
        self.line_busqueda_estudiantes.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.line_busqueda_estudiantes)

        self.horizontalSpacer_18 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)

        self.check_estado_estudiantes = QCheckBox(self.frame_25)
        self.check_estado_estudiantes.setObjectName(u"check_estado_estudiantes")
        self.check_estado_estudiantes.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;")

        self.horizontalLayout_13.addWidget(self.check_estado_estudiantes)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_19)

        self.btn_agregar_estudiantes_admin = QPushButton(self.frame_25)
        self.btn_agregar_estudiantes_admin.setObjectName(u"btn_agregar_estudiantes_admin")
        self.btn_agregar_estudiantes_admin.setMinimumSize(QSize(195, 40))
        self.btn_agregar_estudiantes_admin.setMaximumSize(QSize(110, 40))
        self.btn_agregar_estudiantes_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_estudiantes_admin.setStyleSheet(u"")
        self.btn_agregar_estudiantes_admin.setIcon(icon10)
        self.btn_agregar_estudiantes_admin.setIconSize(QSize(15, 21))

        self.horizontalLayout_13.addWidget(self.btn_agregar_estudiantes_admin)


        self.verticalLayout_6.addWidget(self.frame_25)

        self.tabla_estudiantes = QTableWidget(self.frame_40)
        if (self.tabla_estudiantes.columnCount() < 6):
            self.tabla_estudiantes.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_estudiantes.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_estudiantes.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_estudiantes.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_estudiantes.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_estudiantes.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_estudiantes.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        if (self.tabla_estudiantes.rowCount() < 2):
            self.tabla_estudiantes.setRowCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_estudiantes.setVerticalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_estudiantes.setVerticalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(0, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(0, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(0, 2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(0, 3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(0, 4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(1, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(1, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(1, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(1, 3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabla_estudiantes.setItem(1, 4, __qtablewidgetitem32)
        self.tabla_estudiantes.setObjectName(u"tabla_estudiantes")
        self.tabla_estudiantes.setStyleSheet(u"/* Estilo Base del QTableWidget */\n"
"QTableWidget {\n"
"    outline: 0px;\n"
"    border: 5px solid #f3f4f6;\n"
"    border-radius: 15px;\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    line-height: 19px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #6B7280;\n"
"    gridline-color: #e0e0e0; /* Color de las l\u00edneas de la cuadr\u00edcula */\n"
"}\n"
"\n"
"/* Estilo de las Celdas */\n"
"QTableWidget::item {\n"
"    border-bottom: 3px solid #f3f4f6;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Estilo de las Celdas Seleccionadas */\n"
"QTableWidget::item:selected {\n"
"    background: #465e5f; /* Fondo m\u00e1s claro para la celda seleccionada */\n"
"    color: #ffffff; /* Color de texto claro para las celdas seleccionadas */\n"
"}\n"
"\n"
"/* Estilo de las Celdas Deshabilitadas */\n"
"QTableWidget::disabled {\n"
"    background-color: #acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"}\n"
""
                        "\n"
"/* Estilo de las Secciones de la Cabecera */\n"
"QHeaderView::section {\n"
"    background-color: #f1f2f3;\n"
"    border-style: none;\n"
"    height: 40px;\n"
"    font-family: \"Roboto\";\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"}\n"
"\n"
"/* Estilo de las Secciones Horizontales de la Cabecera */\n"
"QHeaderView::section:horizontal {\n"
"    font-size: 14px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"   text-transform: uppercase; /* Convertir texto a may\u00fasculas */;\n"
"    color: #212529;\n"
"    border-bottom: 2px solid #e0e0e0; /* Separador inferior */\n"
"}\n"
"")
        self.tabla_estudiantes.setFrameShape(QFrame.NoFrame)
        self.tabla_estudiantes.setAutoScroll(True)
        self.tabla_estudiantes.setAutoScrollMargin(16)
        self.tabla_estudiantes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_estudiantes.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_estudiantes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_estudiantes.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_estudiantes.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_estudiantes.setShowGrid(False)
        self.tabla_estudiantes.setSortingEnabled(False)
        self.tabla_estudiantes.setCornerButtonEnabled(True)
        self.tabla_estudiantes.horizontalHeader().setVisible(False)
        self.tabla_estudiantes.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_estudiantes.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_estudiantes.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_estudiantes.horizontalHeader().setHighlightSections(False)
        self.tabla_estudiantes.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_estudiantes.horizontalHeader().setStretchLastSection(False)
        self.tabla_estudiantes.verticalHeader().setVisible(False)
        self.tabla_estudiantes.verticalHeader().setMinimumSectionSize(23)
        self.tabla_estudiantes.verticalHeader().setDefaultSectionSize(47)
        self.tabla_estudiantes.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_estudiantes.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_6.addWidget(self.tabla_estudiantes)

        self.frame_26 = QFrame(self.frame_40)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 47))
        self.frame_26.setStyleSheet(u"/* Estilo de la Etiqueta */\n"
"QLabel {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"    margin-top: 20px; /* Incrementamos el margen superior para m\u00e1s espacio */\n"
"}\n"
"\n"
"/* Estilo Base del Bot\u00f3n de la Paginaci\u00f3n */\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 10px 20px; /* Incrementamos el padding para un mejor tama\u00f1o de bot\u00f3n */\n"
"    background: #3f5758;\n"
"    border: none; /* Eliminamos el borde por defecto */\n"
"    border-radius: 8px; /* Ajustamos el border-radius */\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Pasar el Rat\u00f3n (Hover) */\n"
"QPushButton:hover {\n"
"    background: #4a6b6c; /* Color de fondo m\u00e1s claro */\n"
"    border-r"
                        "adius: 8px;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Hacer Clic (Pressed) */\n"
"QPushButton:pressed {\n"
"    background: #2e4546; /* Color de fondo m\u00e1s oscuro */\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_26)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_20, 0, 0, 1, 1)

        self.btn_pag_desp_estu = QPushButton(self.frame_26)
        self.btn_pag_desp_estu.setObjectName(u"btn_pag_desp_estu")
        self.btn_pag_desp_estu.setMinimumSize(QSize(29, 29))
        self.btn_pag_desp_estu.setMaximumSize(QSize(110, 20))
        self.btn_pag_desp_estu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_desp_estu.setStyleSheet(u"")
        self.btn_pag_desp_estu.setIcon(icon9)
        self.btn_pag_desp_estu.setIconSize(QSize(15, 21))

        self.gridLayout_20.addWidget(self.btn_pag_desp_estu, 0, 3, 1, 1)

        self.lbl_pagina_estudiantes = QLabel(self.frame_26)
        self.lbl_pagina_estudiantes.setObjectName(u"lbl_pagina_estudiantes")
        self.lbl_pagina_estudiantes.setStyleSheet(u"")
        self.lbl_pagina_estudiantes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.lbl_pagina_estudiantes, 0, 2, 1, 1)

        self.btn_pag_antes_estu = QPushButton(self.frame_26)
        self.btn_pag_antes_estu.setObjectName(u"btn_pag_antes_estu")
        self.btn_pag_antes_estu.setMinimumSize(QSize(29, 29))
        self.btn_pag_antes_estu.setMaximumSize(QSize(110, 20))
        self.btn_pag_antes_estu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_antes_estu.setStyleSheet(u"")
        self.btn_pag_antes_estu.setIcon(icon8)
        self.btn_pag_antes_estu.setIconSize(QSize(15, 21))

        self.gridLayout_20.addWidget(self.btn_pag_antes_estu, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_26)


        self.gridLayout_67.addWidget(self.frame_40, 1, 1, 1, 1)

        self.stacked_administracion.addWidget(self.page_estudiantes)
        self.page_tutores = QWidget()
        self.page_tutores.setObjectName(u"page_tutores")
        self.gridLayout_71 = QGridLayout(self.page_tutores)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.page_tutores)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_27 = QFrame(self.frame_15)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 57))
        self.frame_27.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
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
"\n"
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
"")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, -1, -1)
        self.line_busqueda_tutores = QLineEdit(self.frame_27)
        self.line_busqueda_tutores.setObjectName(u"line_busqueda_tutores")
        self.line_busqueda_tutores.setMinimumSize(QSize(0, 43))
        self.line_busqueda_tutores.setMaximumSize(QSize(16777215, 40))
        self.line_busqueda_tutores.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.line_busqueda_tutores)

        self.horizontalSpacer_24 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_24)

        self.check_estado_tutores = QCheckBox(self.frame_27)
        self.check_estado_tutores.setObjectName(u"check_estado_tutores")
        self.check_estado_tutores.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;")

        self.horizontalLayout_15.addWidget(self.check_estado_tutores)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_25)

        self.btn_agregar_tutores = QPushButton(self.frame_27)
        self.btn_agregar_tutores.setObjectName(u"btn_agregar_tutores")
        self.btn_agregar_tutores.setMinimumSize(QSize(195, 40))
        self.btn_agregar_tutores.setMaximumSize(QSize(110, 40))
        self.btn_agregar_tutores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_tutores.setStyleSheet(u"")
        self.btn_agregar_tutores.setIcon(icon10)
        self.btn_agregar_tutores.setIconSize(QSize(15, 21))

        self.horizontalLayout_15.addWidget(self.btn_agregar_tutores)


        self.verticalLayout_9.addWidget(self.frame_27)

        self.tabla_tutores = QTableWidget(self.frame_15)
        if (self.tabla_tutores.columnCount() < 6):
            self.tabla_tutores.setColumnCount(6)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tabla_tutores.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabla_tutores.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tabla_tutores.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabla_tutores.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tabla_tutores.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tabla_tutores.setHorizontalHeaderItem(5, __qtablewidgetitem38)
        if (self.tabla_tutores.rowCount() < 2):
            self.tabla_tutores.setRowCount(2)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tabla_tutores.setVerticalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tabla_tutores.setVerticalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tabla_tutores.setItem(0, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tabla_tutores.setItem(0, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tabla_tutores.setItem(0, 2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tabla_tutores.setItem(0, 3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tabla_tutores.setItem(0, 4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tabla_tutores.setItem(1, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tabla_tutores.setItem(1, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tabla_tutores.setItem(1, 2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tabla_tutores.setItem(1, 3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tabla_tutores.setItem(1, 4, __qtablewidgetitem50)
        self.tabla_tutores.setObjectName(u"tabla_tutores")
        self.tabla_tutores.setStyleSheet(u"/* Estilo Base del QTableWidget */\n"
"QTableWidget {\n"
"    outline: 0px;\n"
"    border: 5px solid #f3f4f6;\n"
"    border-radius: 15px;\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    line-height: 19px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #6B7280;\n"
"    gridline-color: #e0e0e0; /* Color de las l\u00edneas de la cuadr\u00edcula */\n"
"}\n"
"\n"
"/* Estilo de las Celdas */\n"
"QTableWidget::item {\n"
"    border-bottom: 3px solid #f3f4f6;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Estilo de las Celdas Seleccionadas */\n"
"QTableWidget::item:selected {\n"
"    background: #465e5f; /* Fondo m\u00e1s claro para la celda seleccionada */\n"
"    color: #ffffff; /* Color de texto claro para las celdas seleccionadas */\n"
"}\n"
"\n"
"/* Estilo de las Celdas Deshabilitadas */\n"
"QTableWidget::disabled {\n"
"    background-color: #acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"}\n"
""
                        "\n"
"/* Estilo de las Secciones de la Cabecera */\n"
"QHeaderView::section {\n"
"    background-color: #f1f2f3;\n"
"    border-style: none;\n"
"    height: 40px;\n"
"    font-family: \"Roboto\";\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"}\n"
"\n"
"/* Estilo de las Secciones Horizontales de la Cabecera */\n"
"QHeaderView::section:horizontal {\n"
"    font-size: 14px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"   text-transform: uppercase; /* Convertir texto a may\u00fasculas */;\n"
"    color: #212529;\n"
"    border-bottom: 2px solid #e0e0e0; /* Separador inferior */\n"
"}\n"
"")
        self.tabla_tutores.setFrameShape(QFrame.NoFrame)
        self.tabla_tutores.setAutoScroll(True)
        self.tabla_tutores.setAutoScrollMargin(16)
        self.tabla_tutores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_tutores.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_tutores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_tutores.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_tutores.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_tutores.setShowGrid(False)
        self.tabla_tutores.setSortingEnabled(False)
        self.tabla_tutores.setCornerButtonEnabled(True)
        self.tabla_tutores.horizontalHeader().setVisible(False)
        self.tabla_tutores.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_tutores.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_tutores.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_tutores.horizontalHeader().setHighlightSections(False)
        self.tabla_tutores.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_tutores.horizontalHeader().setStretchLastSection(False)
        self.tabla_tutores.verticalHeader().setVisible(False)
        self.tabla_tutores.verticalHeader().setMinimumSectionSize(23)
        self.tabla_tutores.verticalHeader().setDefaultSectionSize(47)
        self.tabla_tutores.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_tutores.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_9.addWidget(self.tabla_tutores)

        self.frame_28 = QFrame(self.frame_15)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 47))
        self.frame_28.setStyleSheet(u"/* Estilo de la Etiqueta */\n"
"QLabel {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"    margin-top: 20px; /* Incrementamos el margen superior para m\u00e1s espacio */\n"
"}\n"
"\n"
"/* Estilo Base del Bot\u00f3n de la Paginaci\u00f3n */\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 10px 20px; /* Incrementamos el padding para un mejor tama\u00f1o de bot\u00f3n */\n"
"    background: #3f5758;\n"
"    border: none; /* Eliminamos el borde por defecto */\n"
"    border-radius: 8px; /* Ajustamos el border-radius */\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Pasar el Rat\u00f3n (Hover) */\n"
"QPushButton:hover {\n"
"    background: #4a6b6c; /* Color de fondo m\u00e1s claro */\n"
"    border-r"
                        "adius: 8px;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Hacer Clic (Pressed) */\n"
"QPushButton:pressed {\n"
"    background: #2e4546; /* Color de fondo m\u00e1s oscuro */\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_28)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_33.addItem(self.horizontalSpacer_30, 0, 0, 1, 1)

        self.btn_pag_antes_tutor = QPushButton(self.frame_28)
        self.btn_pag_antes_tutor.setObjectName(u"btn_pag_antes_tutor")
        self.btn_pag_antes_tutor.setMinimumSize(QSize(29, 29))
        self.btn_pag_antes_tutor.setMaximumSize(QSize(110, 20))
        self.btn_pag_antes_tutor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_antes_tutor.setStyleSheet(u"")
        self.btn_pag_antes_tutor.setIcon(icon8)
        self.btn_pag_antes_tutor.setIconSize(QSize(15, 21))

        self.gridLayout_33.addWidget(self.btn_pag_antes_tutor, 0, 1, 1, 1)

        self.btn_pag_desp_tutor = QPushButton(self.frame_28)
        self.btn_pag_desp_tutor.setObjectName(u"btn_pag_desp_tutor")
        self.btn_pag_desp_tutor.setMinimumSize(QSize(29, 29))
        self.btn_pag_desp_tutor.setMaximumSize(QSize(110, 20))
        self.btn_pag_desp_tutor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_desp_tutor.setStyleSheet(u"")
        self.btn_pag_desp_tutor.setIcon(icon9)
        self.btn_pag_desp_tutor.setIconSize(QSize(15, 21))

        self.gridLayout_33.addWidget(self.btn_pag_desp_tutor, 0, 3, 1, 1)

        self.lbl_pagina_tutores = QLabel(self.frame_28)
        self.lbl_pagina_tutores.setObjectName(u"lbl_pagina_tutores")
        self.lbl_pagina_tutores.setStyleSheet(u"")
        self.lbl_pagina_tutores.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_33.addWidget(self.lbl_pagina_tutores, 0, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_28)


        self.gridLayout_71.addWidget(self.frame_15, 0, 0, 1, 1)

        self.stacked_administracion.addWidget(self.page_tutores)
        self.page_proyectos = QWidget()
        self.page_proyectos.setObjectName(u"page_proyectos")
        self.gridLayout_36 = QGridLayout(self.page_proyectos)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.page_proyectos)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"")
        self.frame_29.setFrameShadow(QFrame.Plain)
        self.gridLayout_35 = QGridLayout(self.frame_29)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 57))
        self.frame_30.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
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
"\n"
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
"")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.line_busqueda_proyecto = QLineEdit(self.frame_30)
        self.line_busqueda_proyecto.setObjectName(u"line_busqueda_proyecto")
        self.line_busqueda_proyecto.setMinimumSize(QSize(0, 43))
        self.line_busqueda_proyecto.setMaximumSize(QSize(16777215, 40))
        self.line_busqueda_proyecto.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.line_busqueda_proyecto)

        self.horizontalSpacer_32 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_32)

        self.check_estado_proyecto = QCheckBox(self.frame_30)
        self.check_estado_proyecto.setObjectName(u"check_estado_proyecto")
        self.check_estado_proyecto.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;")

        self.horizontalLayout_16.addWidget(self.check_estado_proyecto)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_34)

        self.btn_agregar_proyectos = QPushButton(self.frame_30)
        self.btn_agregar_proyectos.setObjectName(u"btn_agregar_proyectos")
        self.btn_agregar_proyectos.setMinimumSize(QSize(195, 40))
        self.btn_agregar_proyectos.setMaximumSize(QSize(110, 40))
        self.btn_agregar_proyectos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_proyectos.setStyleSheet(u"")
        self.btn_agregar_proyectos.setIcon(icon10)
        self.btn_agregar_proyectos.setIconSize(QSize(15, 21))

        self.horizontalLayout_16.addWidget(self.btn_agregar_proyectos)


        self.gridLayout_35.addWidget(self.frame_30, 0, 0, 1, 1)

        self.tabla_proyecto = QTableWidget(self.frame_29)
        if (self.tabla_proyecto.columnCount() < 4):
            self.tabla_proyecto.setColumnCount(4)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tabla_proyecto.setHorizontalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tabla_proyecto.setHorizontalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tabla_proyecto.setHorizontalHeaderItem(2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tabla_proyecto.setHorizontalHeaderItem(3, __qtablewidgetitem54)
        if (self.tabla_proyecto.rowCount() < 2):
            self.tabla_proyecto.setRowCount(2)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tabla_proyecto.setVerticalHeaderItem(0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tabla_proyecto.setVerticalHeaderItem(1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tabla_proyecto.setItem(0, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tabla_proyecto.setItem(0, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tabla_proyecto.setItem(1, 0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tabla_proyecto.setItem(1, 1, __qtablewidgetitem60)
        self.tabla_proyecto.setObjectName(u"tabla_proyecto")
        self.tabla_proyecto.setStyleSheet(u"/* Estilo Base del QTableWidget */\n"
"QTableWidget {\n"
"    outline: 0px;\n"
"    border: 5px solid #f3f4f6;\n"
"    border-radius: 15px;\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    line-height: 19px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #6B7280;\n"
"    gridline-color: #e0e0e0; /* Color de las l\u00edneas de la cuadr\u00edcula */\n"
"}\n"
"\n"
"/* Estilo de las Celdas */\n"
"QTableWidget::item {\n"
"    border-bottom: 3px solid #f3f4f6;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Estilo de las Celdas Seleccionadas */\n"
"QTableWidget::item:selected {\n"
"    background: #465e5f; /* Fondo m\u00e1s claro para la celda seleccionada */\n"
"    color: #ffffff; /* Color de texto claro para las celdas seleccionadas */\n"
"}\n"
"\n"
"/* Estilo de las Celdas Deshabilitadas */\n"
"QTableWidget::disabled {\n"
"    background-color: #acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"}\n"
""
                        "\n"
"/* Estilo de las Secciones de la Cabecera */\n"
"QHeaderView::section {\n"
"    background-color: #f1f2f3;\n"
"    border-style: none;\n"
"    height: 40px;\n"
"    font-family: \"Roboto\";\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"}\n"
"\n"
"/* Estilo de las Secciones Horizontales de la Cabecera */\n"
"QHeaderView::section:horizontal {\n"
"    font-size: 14px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"   text-transform: uppercase; /* Convertir texto a may\u00fasculas */;\n"
"    color: #212529;\n"
"    border-bottom: 2px solid #e0e0e0; /* Separador inferior */\n"
"}\n"
"")
        self.tabla_proyecto.setFrameShape(QFrame.NoFrame)
        self.tabla_proyecto.setAutoScroll(True)
        self.tabla_proyecto.setAutoScrollMargin(16)
        self.tabla_proyecto.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_proyecto.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_proyecto.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_proyecto.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_proyecto.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_proyecto.setShowGrid(False)
        self.tabla_proyecto.setSortingEnabled(False)
        self.tabla_proyecto.setCornerButtonEnabled(True)
        self.tabla_proyecto.horizontalHeader().setVisible(False)
        self.tabla_proyecto.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_proyecto.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_proyecto.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_proyecto.horizontalHeader().setHighlightSections(False)
        self.tabla_proyecto.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_proyecto.horizontalHeader().setStretchLastSection(False)
        self.tabla_proyecto.verticalHeader().setVisible(False)
        self.tabla_proyecto.verticalHeader().setMinimumSectionSize(23)
        self.tabla_proyecto.verticalHeader().setDefaultSectionSize(47)
        self.tabla_proyecto.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_proyecto.verticalHeader().setStretchLastSection(False)

        self.gridLayout_35.addWidget(self.tabla_proyecto, 1, 0, 1, 1)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 47))
        self.frame_31.setStyleSheet(u"/* Estilo de la Etiqueta */\n"
"QLabel {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"    margin-top: 20px; /* Incrementamos el margen superior para m\u00e1s espacio */\n"
"}\n"
"\n"
"/* Estilo Base del Bot\u00f3n de la Paginaci\u00f3n */\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 10px 20px; /* Incrementamos el padding para un mejor tama\u00f1o de bot\u00f3n */\n"
"    background: #3f5758;\n"
"    border: none; /* Eliminamos el borde por defecto */\n"
"    border-radius: 8px; /* Ajustamos el border-radius */\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Pasar el Rat\u00f3n (Hover) */\n"
"QPushButton:hover {\n"
"    background: #4a6b6c; /* Color de fondo m\u00e1s claro */\n"
"    border-r"
                        "adius: 8px;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Hacer Clic (Pressed) */\n"
"QPushButton:pressed {\n"
"    background: #2e4546; /* Color de fondo m\u00e1s oscuro */\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_31)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_35, 0, 0, 1, 1)

        self.lbl_pagina_proyectos = QLabel(self.frame_31)
        self.lbl_pagina_proyectos.setObjectName(u"lbl_pagina_proyectos")
        self.lbl_pagina_proyectos.setStyleSheet(u"")
        self.lbl_pagina_proyectos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_34.addWidget(self.lbl_pagina_proyectos, 0, 2, 1, 1)

        self.btn_pag_desp_proyecto = QPushButton(self.frame_31)
        self.btn_pag_desp_proyecto.setObjectName(u"btn_pag_desp_proyecto")
        self.btn_pag_desp_proyecto.setMinimumSize(QSize(29, 29))
        self.btn_pag_desp_proyecto.setMaximumSize(QSize(110, 20))
        self.btn_pag_desp_proyecto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_desp_proyecto.setStyleSheet(u"")
        self.btn_pag_desp_proyecto.setIcon(icon9)
        self.btn_pag_desp_proyecto.setIconSize(QSize(15, 21))

        self.gridLayout_34.addWidget(self.btn_pag_desp_proyecto, 0, 3, 1, 1)

        self.btn_pag_antes_proyecto = QPushButton(self.frame_31)
        self.btn_pag_antes_proyecto.setObjectName(u"btn_pag_antes_proyecto")
        self.btn_pag_antes_proyecto.setMinimumSize(QSize(29, 29))
        self.btn_pag_antes_proyecto.setMaximumSize(QSize(110, 20))
        self.btn_pag_antes_proyecto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_antes_proyecto.setStyleSheet(u"")
        self.btn_pag_antes_proyecto.setIcon(icon8)
        self.btn_pag_antes_proyecto.setIconSize(QSize(15, 21))

        self.gridLayout_34.addWidget(self.btn_pag_antes_proyecto, 0, 1, 1, 1)


        self.gridLayout_35.addWidget(self.frame_31, 2, 0, 1, 1)


        self.gridLayout_36.addWidget(self.frame_29, 0, 0, 1, 1)

        self.stacked_administracion.addWidget(self.page_proyectos)
        self.page_carreras = QWidget()
        self.page_carreras.setObjectName(u"page_carreras")
        self.gridLayout_39 = QGridLayout(self.page_carreras)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.page_carreras)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"")
        self.frame_32.setFrameShadow(QFrame.Plain)
        self.gridLayout_37 = QGridLayout(self.frame_32)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 57))
        self.frame_33.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
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
" \n"
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
"")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, -1, -1, -1)
        self.line_busqueda_carrera = QLineEdit(self.frame_33)
        self.line_busqueda_carrera.setObjectName(u"line_busqueda_carrera")
        self.line_busqueda_carrera.setMinimumSize(QSize(0, 43))
        self.line_busqueda_carrera.setMaximumSize(QSize(16777215, 40))
        self.line_busqueda_carrera.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.line_busqueda_carrera)

        self.horizontalSpacer_36 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_36)

        self.check_estado_carrera = QCheckBox(self.frame_33)
        self.check_estado_carrera.setObjectName(u"check_estado_carrera")
        self.check_estado_carrera.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;")

        self.horizontalLayout_17.addWidget(self.check_estado_carrera)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_37)

        self.btn_agregar_carrera = QPushButton(self.frame_33)
        self.btn_agregar_carrera.setObjectName(u"btn_agregar_carrera")
        self.btn_agregar_carrera.setMinimumSize(QSize(195, 40))
        self.btn_agregar_carrera.setMaximumSize(QSize(110, 40))
        self.btn_agregar_carrera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_carrera.setStyleSheet(u"")
        self.btn_agregar_carrera.setIcon(icon10)
        self.btn_agregar_carrera.setIconSize(QSize(15, 21))

        self.horizontalLayout_17.addWidget(self.btn_agregar_carrera)


        self.gridLayout_37.addWidget(self.frame_33, 0, 0, 1, 1)

        self.tabla_carrera = QTableWidget(self.frame_32)
        if (self.tabla_carrera.columnCount() < 4):
            self.tabla_carrera.setColumnCount(4)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tabla_carrera.setHorizontalHeaderItem(0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tabla_carrera.setHorizontalHeaderItem(1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tabla_carrera.setHorizontalHeaderItem(2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tabla_carrera.setHorizontalHeaderItem(3, __qtablewidgetitem64)
        if (self.tabla_carrera.rowCount() < 2):
            self.tabla_carrera.setRowCount(2)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tabla_carrera.setVerticalHeaderItem(0, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tabla_carrera.setVerticalHeaderItem(1, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tabla_carrera.setItem(0, 0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tabla_carrera.setItem(0, 1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tabla_carrera.setItem(0, 2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tabla_carrera.setItem(1, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tabla_carrera.setItem(1, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tabla_carrera.setItem(1, 2, __qtablewidgetitem72)
        self.tabla_carrera.setObjectName(u"tabla_carrera")
        self.tabla_carrera.setStyleSheet(u"/* Estilo Base del QTableWidget */\n"
"QTableWidget {\n"
"    outline: 0px;\n"
"    border: 5px solid #f3f4f6;\n"
"    border-radius: 15px;\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    line-height: 19px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #6B7280;\n"
"    gridline-color: #e0e0e0; /* Color de las l\u00edneas de la cuadr\u00edcula */\n"
"}\n"
"\n"
"/* Estilo de las Celdas */\n"
"QTableWidget::item {\n"
"    border-bottom: 3px solid #f3f4f6;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Estilo de las Celdas Seleccionadas */\n"
"QTableWidget::item:selected {\n"
"    background: #465e5f; /* Fondo m\u00e1s claro para la celda seleccionada */\n"
"    color: #ffffff; /* Color de texto claro para las celdas seleccionadas */\n"
"}\n"
"\n"
"/* Estilo de las Celdas Deshabilitadas */\n"
"QTableWidget::disabled {\n"
"    background-color: #acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"}\n"
""
                        "\n"
"/* Estilo de las Secciones de la Cabecera */\n"
"QHeaderView::section {\n"
"    background-color: #f1f2f3;\n"
"    border-style: none;\n"
"    height: 40px;\n"
"    font-family: \"Roboto\";\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"}\n"
"\n"
"/* Estilo de las Secciones Horizontales de la Cabecera */\n"
"QHeaderView::section:horizontal {\n"
"    font-size: 14px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"   text-transform: uppercase; /* Convertir texto a may\u00fasculas */;\n"
"    color: #212529;\n"
"    border-bottom: 2px solid #e0e0e0; /* Separador inferior */\n"
"}\n"
"")
        self.tabla_carrera.setFrameShape(QFrame.NoFrame)
        self.tabla_carrera.setAutoScroll(True)
        self.tabla_carrera.setAutoScrollMargin(16)
        self.tabla_carrera.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_carrera.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_carrera.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_carrera.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_carrera.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_carrera.setShowGrid(False)
        self.tabla_carrera.setSortingEnabled(False)
        self.tabla_carrera.setCornerButtonEnabled(True)
        self.tabla_carrera.horizontalHeader().setVisible(False)
        self.tabla_carrera.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_carrera.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_carrera.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_carrera.horizontalHeader().setHighlightSections(False)
        self.tabla_carrera.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_carrera.horizontalHeader().setStretchLastSection(False)
        self.tabla_carrera.verticalHeader().setVisible(False)
        self.tabla_carrera.verticalHeader().setMinimumSectionSize(23)
        self.tabla_carrera.verticalHeader().setDefaultSectionSize(47)
        self.tabla_carrera.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_carrera.verticalHeader().setStretchLastSection(False)

        self.gridLayout_37.addWidget(self.tabla_carrera, 1, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 47))
        self.frame_34.setStyleSheet(u"/* Estilo de la Etiqueta */\n"
"QLabel {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"    margin-top: 20px; /* Incrementamos el margen superior para m\u00e1s espacio */\n"
"}\n"
"\n"
"/* Estilo Base del Bot\u00f3n de la Paginaci\u00f3n */\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 10px 20px; /* Incrementamos el padding para un mejor tama\u00f1o de bot\u00f3n */\n"
"    background: #3f5758;\n"
"    border: none; /* Eliminamos el borde por defecto */\n"
"    border-radius: 8px; /* Ajustamos el border-radius */\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Pasar el Rat\u00f3n (Hover) */\n"
"QPushButton:hover {\n"
"    background: #4a6b6c; /* Color de fondo m\u00e1s claro */\n"
"    border-r"
                        "adius: 8px;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Hacer Clic (Pressed) */\n"
"QPushButton:pressed {\n"
"    background: #2e4546; /* Color de fondo m\u00e1s oscuro */\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_34)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.btn_pag_antes_carrera = QPushButton(self.frame_34)
        self.btn_pag_antes_carrera.setObjectName(u"btn_pag_antes_carrera")
        self.btn_pag_antes_carrera.setMinimumSize(QSize(29, 29))
        self.btn_pag_antes_carrera.setMaximumSize(QSize(110, 20))
        self.btn_pag_antes_carrera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_antes_carrera.setStyleSheet(u"")
        self.btn_pag_antes_carrera.setIcon(icon8)
        self.btn_pag_antes_carrera.setIconSize(QSize(15, 21))

        self.gridLayout_38.addWidget(self.btn_pag_antes_carrera, 0, 1, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_38, 0, 0, 1, 1)

        self.btn_pag_desp_carrera = QPushButton(self.frame_34)
        self.btn_pag_desp_carrera.setObjectName(u"btn_pag_desp_carrera")
        self.btn_pag_desp_carrera.setMinimumSize(QSize(29, 29))
        self.btn_pag_desp_carrera.setMaximumSize(QSize(110, 20))
        self.btn_pag_desp_carrera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_desp_carrera.setStyleSheet(u"")
        self.btn_pag_desp_carrera.setIcon(icon9)
        self.btn_pag_desp_carrera.setIconSize(QSize(15, 21))

        self.gridLayout_38.addWidget(self.btn_pag_desp_carrera, 0, 3, 1, 1)

        self.lbl_pagina_carrera = QLabel(self.frame_34)
        self.lbl_pagina_carrera.setObjectName(u"lbl_pagina_carrera")
        self.lbl_pagina_carrera.setStyleSheet(u"")
        self.lbl_pagina_carrera.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_38.addWidget(self.lbl_pagina_carrera, 0, 2, 1, 1)


        self.gridLayout_37.addWidget(self.frame_34, 2, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_32, 0, 0, 1, 1)

        self.stacked_administracion.addWidget(self.page_carreras)
        self.page_intituciones = QWidget()
        self.page_intituciones.setObjectName(u"page_intituciones")
        self.gridLayout_42 = QGridLayout(self.page_intituciones)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.page_intituciones)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"")
        self.frame_35.setFrameShadow(QFrame.Plain)
        self.gridLayout_40 = QGridLayout(self.frame_35)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 57))
        self.frame_36.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
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
"\n"
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
"")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, -1, -1)
        self.line_busqueda_inst = QLineEdit(self.frame_36)
        self.line_busqueda_inst.setObjectName(u"line_busqueda_inst")
        self.line_busqueda_inst.setMinimumSize(QSize(0, 43))
        self.line_busqueda_inst.setMaximumSize(QSize(16777215, 40))
        self.line_busqueda_inst.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.line_busqueda_inst)

        self.horizontalSpacer_39 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_39)

        self.check_estado_insti = QCheckBox(self.frame_36)
        self.check_estado_insti.setObjectName(u"check_estado_insti")
        self.check_estado_insti.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;")

        self.horizontalLayout_18.addWidget(self.check_estado_insti)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_40)

        self.btn_agregar_insti = QPushButton(self.frame_36)
        self.btn_agregar_insti.setObjectName(u"btn_agregar_insti")
        self.btn_agregar_insti.setMinimumSize(QSize(195, 40))
        self.btn_agregar_insti.setMaximumSize(QSize(110, 40))
        self.btn_agregar_insti.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_insti.setStyleSheet(u"")
        self.btn_agregar_insti.setIcon(icon10)
        self.btn_agregar_insti.setIconSize(QSize(15, 21))

        self.horizontalLayout_18.addWidget(self.btn_agregar_insti)


        self.gridLayout_40.addWidget(self.frame_36, 0, 0, 1, 1)

        self.tabla_institucion = QTableWidget(self.frame_35)
        if (self.tabla_institucion.columnCount() < 5):
            self.tabla_institucion.setColumnCount(5)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tabla_institucion.setHorizontalHeaderItem(0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tabla_institucion.setHorizontalHeaderItem(1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tabla_institucion.setHorizontalHeaderItem(2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tabla_institucion.setHorizontalHeaderItem(3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tabla_institucion.setHorizontalHeaderItem(4, __qtablewidgetitem77)
        if (self.tabla_institucion.rowCount() < 2):
            self.tabla_institucion.setRowCount(2)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tabla_institucion.setVerticalHeaderItem(0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tabla_institucion.setVerticalHeaderItem(1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tabla_institucion.setItem(0, 0, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tabla_institucion.setItem(0, 1, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tabla_institucion.setItem(0, 3, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tabla_institucion.setItem(1, 0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tabla_institucion.setItem(1, 1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tabla_institucion.setItem(1, 3, __qtablewidgetitem85)
        self.tabla_institucion.setObjectName(u"tabla_institucion")
        self.tabla_institucion.setStyleSheet(u"/* Estilo Base del QTableWidget */\n"
"QTableWidget {\n"
"    outline: 0px;\n"
"    border: 5px solid #f3f4f6;\n"
"    border-radius: 15px;\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    line-height: 19px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #6B7280;\n"
"    gridline-color: #e0e0e0; /* Color de las l\u00edneas de la cuadr\u00edcula */\n"
"}\n"
"\n"
"/* Estilo de las Celdas */\n"
"QTableWidget::item {\n"
"    border-bottom: 3px solid #f3f4f6;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"/* Estilo de las Celdas Seleccionadas */\n"
"QTableWidget::item:selected {\n"
"    background: #465e5f; /* Fondo m\u00e1s claro para la celda seleccionada */\n"
"    color: #ffffff; /* Color de texto claro para las celdas seleccionadas */\n"
"}\n"
"\n"
"/* Estilo de las Celdas Deshabilitadas */\n"
"QTableWidget::disabled {\n"
"    background-color: #acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
""
                        "}\n"
"\n"
"/* Estilo de las Secciones de la Cabecera */\n"
"QHeaderView::section {\n"
"    background-color: #f1f2f3;\n"
"    border-style: none;\n"
"    height: 40px;\n"
"    font-family: \"Roboto\";\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"}\n"
"\n"
"/* Estilo de las Secciones Horizontales de la Cabecera */\n"
"QHeaderView::section:horizontal {\n"
"    font-size: 14px; /* Tama\u00f1o de la letra de la cabecera */\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"   text-transform: uppercase; /* Convertir texto a may\u00fasculas */;\n"
"    color: #212529;\n"
"    border-bottom: 2px solid #e0e0e0; /* Separador inferior */\n"
"}\n"
"")
        self.tabla_institucion.setFrameShape(QFrame.NoFrame)
        self.tabla_institucion.setAutoScroll(True)
        self.tabla_institucion.setAutoScrollMargin(16)
        self.tabla_institucion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_institucion.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_institucion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_institucion.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_institucion.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_institucion.setShowGrid(False)
        self.tabla_institucion.setSortingEnabled(False)
        self.tabla_institucion.setCornerButtonEnabled(True)
        self.tabla_institucion.horizontalHeader().setVisible(False)
        self.tabla_institucion.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_institucion.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_institucion.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_institucion.horizontalHeader().setHighlightSections(False)
        self.tabla_institucion.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_institucion.horizontalHeader().setStretchLastSection(False)
        self.tabla_institucion.verticalHeader().setVisible(False)
        self.tabla_institucion.verticalHeader().setMinimumSectionSize(23)
        self.tabla_institucion.verticalHeader().setDefaultSectionSize(47)
        self.tabla_institucion.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_institucion.verticalHeader().setStretchLastSection(False)

        self.gridLayout_40.addWidget(self.tabla_institucion, 1, 0, 1, 1)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 47))
        self.frame_37.setStyleSheet(u"/* Estilo de la Etiqueta */\n"
"QLabel {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    line-height: 14px;\n"
"    letter-spacing: 0.04em;\n"
"    color: #6B7280;\n"
"    margin-top: 20px; /* Incrementamos el margen superior para m\u00e1s espacio */\n"
"}\n"
"\n"
"/* Estilo Base del Bot\u00f3n de la Paginaci\u00f3n */\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white;\n"
"    padding: 10px 20px; /* Incrementamos el padding para un mejor tama\u00f1o de bot\u00f3n */\n"
"    background: #3f5758;\n"
"    border: none; /* Eliminamos el borde por defecto */\n"
"    border-radius: 8px; /* Ajustamos el border-radius */\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Pasar el Rat\u00f3n (Hover) */\n"
"QPushButton:hover {\n"
"    background: #4a6b6c; /* Color de fondo m\u00e1s claro */\n"
"    border-r"
                        "adius: 8px;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n de la Paginaci\u00f3n al Hacer Clic (Pressed) */\n"
"QPushButton:pressed {\n"
"    background: #2e4546; /* Color de fondo m\u00e1s oscuro */\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_37)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.lbl_pagina_instituto = QLabel(self.frame_37)
        self.lbl_pagina_instituto.setObjectName(u"lbl_pagina_instituto")
        self.lbl_pagina_instituto.setStyleSheet(u"")
        self.lbl_pagina_instituto.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.lbl_pagina_instituto, 0, 2, 1, 1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_42, 0, 0, 1, 1)

        self.btn_pag_desp_inst = QPushButton(self.frame_37)
        self.btn_pag_desp_inst.setObjectName(u"btn_pag_desp_inst")
        self.btn_pag_desp_inst.setMinimumSize(QSize(29, 29))
        self.btn_pag_desp_inst.setMaximumSize(QSize(110, 20))
        self.btn_pag_desp_inst.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_desp_inst.setStyleSheet(u"")
        self.btn_pag_desp_inst.setIcon(icon9)
        self.btn_pag_desp_inst.setIconSize(QSize(15, 21))

        self.gridLayout_41.addWidget(self.btn_pag_desp_inst, 0, 3, 1, 1)

        self.btn_pag_antes_inst = QPushButton(self.frame_37)
        self.btn_pag_antes_inst.setObjectName(u"btn_pag_antes_inst")
        self.btn_pag_antes_inst.setMinimumSize(QSize(29, 29))
        self.btn_pag_antes_inst.setMaximumSize(QSize(110, 20))
        self.btn_pag_antes_inst.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pag_antes_inst.setStyleSheet(u"")
        self.btn_pag_antes_inst.setIcon(icon8)
        self.btn_pag_antes_inst.setIconSize(QSize(15, 21))

        self.gridLayout_41.addWidget(self.btn_pag_antes_inst, 0, 1, 1, 1)


        self.gridLayout_40.addWidget(self.frame_37, 2, 0, 1, 1)


        self.gridLayout_42.addWidget(self.frame_35, 0, 0, 1, 1)

        self.stacked_administracion.addWidget(self.page_intituciones)

        self.gridLayout_66.addWidget(self.stacked_administracion, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_50, 2, 0, 1, 1)

        self.frame_60 = QFrame(self.frp1_3)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 50))
        self.frame_60.setMaximumSize(QSize(16777215, 50))
        self.frame_60.setStyleSheet(u"/* Estilo Base del Bot\u00f3n */\n"
"QPushButton {\n"
"    font-family: Roboto;\n"
"    border: 0px;\n"
"    font-weight: normal;\n"
"    font-size: 14px;\n"
"    background-color: transparent;\n"
"    letter-spacing: 0.10em;\n"
"    color: #6B7280;\n"
"    border-bottom: 3px solid transparent;\n"
"    padding: 10px 20px;\n"
"	text-transform: uppercase; /* Convertir texto a may\u00fasculas */\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n al Pasar el Rat\u00f3n (Hover) */\n"
"QPushButton:hover {\n"
"    color: #445d5e;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"    border-bottom: 2px solid #445d5e;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n Deshabilitado */\n"
"QPushButton:disabled {\n"
"    color: #54BFC9;\n"
"    border-bottom: 3px solid #54BFC9;\n"
"}\n"
"\n"
"/* Estilo del Bot\u00f3n Activo (Pesta\u00f1a Activa) */\n"
"QPushButton:checked, QPushButton:focus {\n"
"    color: #000000; /* Puedes ajustar el color para que destaque m\u00e1s */\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"    borde"
                        "r-bottom: 3px solid #3f5758; /* Color que indique claramente la pesta\u00f1a activa */\n"
"}\n"
"\n"
"/* Estilo del Contenedor del Marco */\n"
"#frame_60 {\n"
"    background-color: #F9FAFB;\n"
"    font-size: 16px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"")
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_menu_estudiantes = QPushButton(self.frame_60)
        self.btn_menu_estudiantes.setObjectName(u"btn_menu_estudiantes")
        self.btn_menu_estudiantes.setMinimumSize(QSize(150, 38))
        self.btn_menu_estudiantes.setMaximumSize(QSize(16777215, 38))
        self.btn_menu_estudiantes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_estudiantes.setStyleSheet(u"")
        self.btn_menu_estudiantes.setFlat(True)

        self.horizontalLayout_11.addWidget(self.btn_menu_estudiantes)

        self.btn_menu_tutores = QPushButton(self.frame_60)
        self.btn_menu_tutores.setObjectName(u"btn_menu_tutores")
        self.btn_menu_tutores.setMinimumSize(QSize(150, 38))
        self.btn_menu_tutores.setMaximumSize(QSize(16777215, 38))
        self.btn_menu_tutores.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_menu_tutores)

        self.btn_menu_proyectos = QPushButton(self.frame_60)
        self.btn_menu_proyectos.setObjectName(u"btn_menu_proyectos")
        self.btn_menu_proyectos.setMinimumSize(QSize(150, 38))
        self.btn_menu_proyectos.setMaximumSize(QSize(16777215, 38))
        self.btn_menu_proyectos.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_menu_proyectos)

        self.btn_menu_carreras = QPushButton(self.frame_60)
        self.btn_menu_carreras.setObjectName(u"btn_menu_carreras")
        self.btn_menu_carreras.setMinimumSize(QSize(150, 38))
        self.btn_menu_carreras.setMaximumSize(QSize(16777215, 38))
        self.btn_menu_carreras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_carreras.setStyleSheet(u"")
        self.btn_menu_carreras.setFlat(True)

        self.horizontalLayout_11.addWidget(self.btn_menu_carreras)

        self.btn_menu_instituciones = QPushButton(self.frame_60)
        self.btn_menu_instituciones.setObjectName(u"btn_menu_instituciones")
        self.btn_menu_instituciones.setMinimumSize(QSize(246, 38))
        self.btn_menu_instituciones.setMaximumSize(QSize(16777215, 38))
        self.btn_menu_instituciones.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_instituciones.setStyleSheet(u"")
        self.btn_menu_instituciones.setFlat(True)

        self.horizontalLayout_11.addWidget(self.btn_menu_instituciones)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.gridLayout_19.addWidget(self.frame_60, 1, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frp1_3, 0, 0, 1, 1)

        self.Scrollprincipal_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_21.addWidget(self.Scrollprincipal_3, 1, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_21.addItem(self.verticalSpacer_14, 2, 1, 1, 1)

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
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(2, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(3, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(4, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(5, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(6, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tabla_usuario.setHorizontalHeaderItem(7, __qtablewidgetitem93)
        if (self.tabla_usuario.rowCount() < 3):
            self.tabla_usuario.setRowCount(3)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tabla_usuario.setVerticalHeaderItem(0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tabla_usuario.setVerticalHeaderItem(1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tabla_usuario.setVerticalHeaderItem(2, __qtablewidgetitem96)
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
        self.btn_agregar_usuario.setIcon(icon10)
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
        self.radioEstudiante = QPushButton(self.frame_61)
        self.radioEstudiante.setObjectName(u"radioEstudiante")
        self.radioEstudiante.setMinimumSize(QSize(246, 38))
        self.radioEstudiante.setMaximumSize(QSize(16777215, 38))
        self.radioEstudiante.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioEstudiante.setStyleSheet(u"")
        self.radioEstudiante.setFlat(True)

        self.gridLayout_24.addWidget(self.radioEstudiante, 0, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_13, 0, 3, 1, 1)

        self.radioTutor = QPushButton(self.frame_61)
        self.radioTutor.setObjectName(u"radioTutor")
        self.radioTutor.setMinimumSize(QSize(241, 38))
        self.radioTutor.setMaximumSize(QSize(16777215, 38))
        self.radioTutor.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_24.addWidget(self.radioTutor, 0, 1, 1, 1)

        self.radioreporteentrega = QPushButton(self.frame_61)
        self.radioreporteentrega.setObjectName(u"radioreporteentrega")
        self.radioreporteentrega.setMinimumSize(QSize(224, 38))
        self.radioreporteentrega.setMaximumSize(QSize(16777215, 38))
        self.radioreporteentrega.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_24.addWidget(self.radioreporteentrega, 0, 2, 1, 1)


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
        self.line_busqueda_reporte_tutor = QLineEdit(self.frame_20)
        self.line_busqueda_reporte_tutor.setObjectName(u"line_busqueda_reporte_tutor")
        self.line_busqueda_reporte_tutor.setMinimumSize(QSize(0, 40))
        self.line_busqueda_reporte_tutor.setMaximumSize(QSize(16777215, 40))
        self.line_busqueda_reporte_tutor.setStyleSheet(u"QLineEdit{\n"
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

        self.gridLayout_25.addWidget(self.line_busqueda_reporte_tutor, 0, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_38)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_21)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.tabla_reporte_tutores = QTableWidget(self.frame_21)
        if (self.tabla_reporte_tutores.columnCount() < 6):
            self.tabla_reporte_tutores.setColumnCount(6)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(0, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(1, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(2, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(3, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(4, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tabla_reporte_tutores.setHorizontalHeaderItem(5, __qtablewidgetitem102)
        if (self.tabla_reporte_tutores.rowCount() < 3):
            self.tabla_reporte_tutores.setRowCount(3)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tabla_reporte_tutores.setVerticalHeaderItem(0, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tabla_reporte_tutores.setVerticalHeaderItem(1, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tabla_reporte_tutores.setVerticalHeaderItem(2, __qtablewidgetitem105)
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
"font-weight: 700;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
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
"\n"
"/*bordes internos*/\n"
"QTab"
                        "leWidget::item {\n"
"	border-bottom: 3px solid #f3f4f6;\n"
"\n"
"}\n"
"\n"
"QTableWidget:item:selected{\n"
"	background:white;/*color-seleccion*/\n"
"color: #2c3d3e;\n"
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
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_29 = QGridLayout(self.page)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.frame_41 = QFrame(self.page)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"#frame_41{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_41.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame_41)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.frame_23 = QFrame(self.frame_41)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 55))
        self.frame_23.setMaximumSize(QSize(16777215, 55))
        self.frame_23.setStyleSheet(u"QRadioButton{\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
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
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_23)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(9, 6, -1, -1)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_15, 0, 5, 1, 1)

        self.cbo_periodo_academico = QComboBox(self.frame_23)
        self.cbo_periodo_academico.setObjectName(u"cbo_periodo_academico")
        self.cbo_periodo_academico.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbo_periodo_academico.setStyleSheet(u"")
        self.cbo_periodo_academico.setMaxVisibleItems(67)

        self.gridLayout_27.addWidget(self.cbo_periodo_academico, 0, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(17, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)

        self.cbo_tipo_entrega = QComboBox(self.frame_23)
        self.cbo_tipo_entrega.addItem("")
        self.cbo_tipo_entrega.addItem("")
        self.cbo_tipo_entrega.setObjectName(u"cbo_tipo_entrega")
        self.cbo_tipo_entrega.setMinimumSize(QSize(200, 0))
        self.cbo_tipo_entrega.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbo_tipo_entrega.setStyleSheet(u"")
        self.cbo_tipo_entrega.setMaxVisibleItems(67)

        self.gridLayout_27.addWidget(self.cbo_tipo_entrega, 0, 1, 1, 1)

        self.lbl9_3 = QLabel(self.frame_23)
        self.lbl9_3.setObjectName(u"lbl9_3")
        self.lbl9_3.setStyleSheet(u"")
        self.lbl9_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.lbl9_3, 0, 0, 1, 1)

        self.lbl9_4 = QLabel(self.frame_23)
        self.lbl9_4.setObjectName(u"lbl9_4")
        self.lbl9_4.setStyleSheet(u"")
        self.lbl9_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.lbl9_4, 0, 3, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_41)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_24)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, -1)
        self.stackedWidget_2 = QStackedWidget(self.frame_24)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"QLabel{font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: #6B7280;}")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_30 = QGridLayout(self.page_2)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_17, 1, 0, 1, 1)

        self.tabla_reporte_informe_tutor = QTableWidget(self.page_2)
        if (self.tabla_reporte_informe_tutor.columnCount() < 13):
            self.tabla_reporte_informe_tutor.setColumnCount(13)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(0, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(1, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(2, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(3, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(4, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(5, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(6, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(7, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(8, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(9, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(10, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(11, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setHorizontalHeaderItem(12, __qtablewidgetitem118)
        if (self.tabla_reporte_informe_tutor.rowCount() < 3):
            self.tabla_reporte_informe_tutor.setRowCount(3)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setVerticalHeaderItem(0, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setVerticalHeaderItem(1, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tabla_reporte_informe_tutor.setVerticalHeaderItem(2, __qtablewidgetitem121)
        self.tabla_reporte_informe_tutor.setObjectName(u"tabla_reporte_informe_tutor")
        self.tabla_reporte_informe_tutor.setStyleSheet(u"QTableWidget {\n"
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
"font-weight: 700;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
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
"\n"
"/*bordes internos*/\n"
"QTab"
                        "leWidget::item {\n"
"	border-bottom: 3px solid #f3f4f6;\n"
"\n"
"}\n"
"\n"
"QTableWidget:item:selected{\n"
"	background:white;/*color-seleccion*/\n"
"color: #2c3d3e;\n"
"}\n"
"\n"
"")
        self.tabla_reporte_informe_tutor.setFrameShape(QFrame.NoFrame)
        self.tabla_reporte_informe_tutor.setAutoScroll(True)
        self.tabla_reporte_informe_tutor.setAutoScrollMargin(16)
        self.tabla_reporte_informe_tutor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_reporte_informe_tutor.setAlternatingRowColors(False)
        self.tabla_reporte_informe_tutor.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_reporte_informe_tutor.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_reporte_informe_tutor.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_informe_tutor.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_informe_tutor.setShowGrid(False)
        self.tabla_reporte_informe_tutor.setSortingEnabled(False)
        self.tabla_reporte_informe_tutor.setCornerButtonEnabled(True)
        self.tabla_reporte_informe_tutor.horizontalHeader().setVisible(False)
        self.tabla_reporte_informe_tutor.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_reporte_informe_tutor.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_reporte_informe_tutor.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_reporte_informe_tutor.horizontalHeader().setHighlightSections(False)
        self.tabla_reporte_informe_tutor.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_informe_tutor.horizontalHeader().setStretchLastSection(False)
        self.tabla_reporte_informe_tutor.verticalHeader().setVisible(False)
        self.tabla_reporte_informe_tutor.verticalHeader().setMinimumSectionSize(23)
        self.tabla_reporte_informe_tutor.verticalHeader().setDefaultSectionSize(47)
        self.tabla_reporte_informe_tutor.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_informe_tutor.verticalHeader().setStretchLastSection(False)

        self.gridLayout_30.addWidget(self.tabla_reporte_informe_tutor, 3, 0, 1, 2)

        self.btn_export_2 = QPushButton(self.page_2)
        self.btn_export_2.setObjectName(u"btn_export_2")
        self.btn_export_2.setMinimumSize(QSize(146, 35))
        self.btn_export_2.setMaximumSize(QSize(160, 35))
        self.btn_export_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_2.setStyleSheet(u"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 450;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;\n"
"background: #f78f91;\n"
"border-radius: 8px;}\n"
"\n"
"QPushButton:hover{background: #e38487;\n"
"border-radius: 8px; }")
        icon12 = QIcon()
        icon12.addFile(u":/menu/exportar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_2.setIcon(icon12)

        self.gridLayout_30.addWidget(self.btn_export_2, 1, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_30.addItem(self.verticalSpacer_11, 2, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_31 = QGridLayout(self.page_3)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.frame_19 = QFrame(self.page_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 45))
        self.frame_19.setMaximumSize(QSize(16777215, 45))
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, 0)
        self.lbl9_6 = QLabel(self.frame_19)
        self.lbl9_6.setObjectName(u"lbl9_6")
        self.lbl9_6.setStyleSheet(u"")
        self.lbl9_6.setFrameShadow(QFrame.Raised)
        self.lbl9_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lbl9_6)

        self.btn_export_4 = QPushButton(self.frame_19)
        self.btn_export_4.setObjectName(u"btn_export_4")
        self.btn_export_4.setMinimumSize(QSize(146, 35))
        self.btn_export_4.setMaximumSize(QSize(160, 35))
        self.btn_export_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_4.setStyleSheet(u"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 450;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;\n"
"background: #f78f91;\n"
"border-radius: 8px;}\n"
"\n"
"QPushButton:hover{background: #e38487;\n"
"border-radius: 8px; }")
        self.btn_export_4.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.btn_export_4)


        self.gridLayout_31.addWidget(self.frame_19, 0, 1, 1, 1)

        self.tabla_reporte_memorandum_tutor = QTableWidget(self.page_3)
        if (self.tabla_reporte_memorandum_tutor.columnCount() < 3):
            self.tabla_reporte_memorandum_tutor.setColumnCount(3)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tabla_reporte_memorandum_tutor.setHorizontalHeaderItem(0, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tabla_reporte_memorandum_tutor.setHorizontalHeaderItem(1, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tabla_reporte_memorandum_tutor.setHorizontalHeaderItem(2, __qtablewidgetitem124)
        if (self.tabla_reporte_memorandum_tutor.rowCount() < 3):
            self.tabla_reporte_memorandum_tutor.setRowCount(3)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tabla_reporte_memorandum_tutor.setVerticalHeaderItem(0, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tabla_reporte_memorandum_tutor.setVerticalHeaderItem(1, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tabla_reporte_memorandum_tutor.setVerticalHeaderItem(2, __qtablewidgetitem127)
        self.tabla_reporte_memorandum_tutor.setObjectName(u"tabla_reporte_memorandum_tutor")
        self.tabla_reporte_memorandum_tutor.setStyleSheet(u"QTableWidget {\n"
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
"font-weight: 700;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
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
"\n"
"/*bordes internos*/\n"
"QTab"
                        "leWidget::item {\n"
"	border-bottom: 3px solid #f3f4f6;\n"
"\n"
"}\n"
"\n"
"QTableWidget:item:selected{\n"
"	background:white;/*color-seleccion*/\n"
"color: #2c3d3e;\n"
"}\n"
"\n"
"")
        self.tabla_reporte_memorandum_tutor.setFrameShape(QFrame.NoFrame)
        self.tabla_reporte_memorandum_tutor.setAutoScroll(True)
        self.tabla_reporte_memorandum_tutor.setAutoScrollMargin(16)
        self.tabla_reporte_memorandum_tutor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_reporte_memorandum_tutor.setAlternatingRowColors(False)
        self.tabla_reporte_memorandum_tutor.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_reporte_memorandum_tutor.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_reporte_memorandum_tutor.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_memorandum_tutor.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_memorandum_tutor.setShowGrid(False)
        self.tabla_reporte_memorandum_tutor.setSortingEnabled(False)
        self.tabla_reporte_memorandum_tutor.setCornerButtonEnabled(True)
        self.tabla_reporte_memorandum_tutor.horizontalHeader().setVisible(False)
        self.tabla_reporte_memorandum_tutor.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_reporte_memorandum_tutor.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_reporte_memorandum_tutor.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_reporte_memorandum_tutor.horizontalHeader().setHighlightSections(False)
        self.tabla_reporte_memorandum_tutor.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_memorandum_tutor.horizontalHeader().setStretchLastSection(False)
        self.tabla_reporte_memorandum_tutor.verticalHeader().setVisible(False)
        self.tabla_reporte_memorandum_tutor.verticalHeader().setMinimumSectionSize(23)
        self.tabla_reporte_memorandum_tutor.verticalHeader().setDefaultSectionSize(47)
        self.tabla_reporte_memorandum_tutor.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_memorandum_tutor.verticalHeader().setStretchLastSection(False)

        self.gridLayout_31.addWidget(self.tabla_reporte_memorandum_tutor, 1, 1, 1, 1)

        self.tabla_reporte_ficha_tutor = QTableWidget(self.page_3)
        if (self.tabla_reporte_ficha_tutor.columnCount() < 3):
            self.tabla_reporte_ficha_tutor.setColumnCount(3)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tabla_reporte_ficha_tutor.setHorizontalHeaderItem(0, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tabla_reporte_ficha_tutor.setHorizontalHeaderItem(1, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tabla_reporte_ficha_tutor.setHorizontalHeaderItem(2, __qtablewidgetitem130)
        if (self.tabla_reporte_ficha_tutor.rowCount() < 3):
            self.tabla_reporte_ficha_tutor.setRowCount(3)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tabla_reporte_ficha_tutor.setVerticalHeaderItem(0, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tabla_reporte_ficha_tutor.setVerticalHeaderItem(1, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tabla_reporte_ficha_tutor.setVerticalHeaderItem(2, __qtablewidgetitem133)
        self.tabla_reporte_ficha_tutor.setObjectName(u"tabla_reporte_ficha_tutor")
        self.tabla_reporte_ficha_tutor.setStyleSheet(u"QTableWidget {\n"
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
"font-weight: 700;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
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
"\n"
"/*bordes internos*/\n"
"QTab"
                        "leWidget::item {\n"
"	border-bottom: 3px solid #f3f4f6;\n"
"\n"
"}\n"
"\n"
"QTableWidget:item:selected{\n"
"	background:white;/*color-seleccion*/\n"
"color: #2c3d3e;\n"
"}\n"
"\n"
"")
        self.tabla_reporte_ficha_tutor.setFrameShape(QFrame.NoFrame)
        self.tabla_reporte_ficha_tutor.setAutoScroll(True)
        self.tabla_reporte_ficha_tutor.setAutoScrollMargin(16)
        self.tabla_reporte_ficha_tutor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_reporte_ficha_tutor.setAlternatingRowColors(False)
        self.tabla_reporte_ficha_tutor.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_reporte_ficha_tutor.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_reporte_ficha_tutor.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_ficha_tutor.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_reporte_ficha_tutor.setShowGrid(False)
        self.tabla_reporte_ficha_tutor.setSortingEnabled(False)
        self.tabla_reporte_ficha_tutor.setCornerButtonEnabled(True)
        self.tabla_reporte_ficha_tutor.horizontalHeader().setVisible(False)
        self.tabla_reporte_ficha_tutor.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_reporte_ficha_tutor.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_reporte_ficha_tutor.horizontalHeader().setDefaultSectionSize(100)
        self.tabla_reporte_ficha_tutor.horizontalHeader().setHighlightSections(False)
        self.tabla_reporte_ficha_tutor.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_ficha_tutor.horizontalHeader().setStretchLastSection(False)
        self.tabla_reporte_ficha_tutor.verticalHeader().setVisible(False)
        self.tabla_reporte_ficha_tutor.verticalHeader().setMinimumSectionSize(23)
        self.tabla_reporte_ficha_tutor.verticalHeader().setDefaultSectionSize(47)
        self.tabla_reporte_ficha_tutor.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_reporte_ficha_tutor.verticalHeader().setStretchLastSection(False)

        self.gridLayout_31.addWidget(self.tabla_reporte_ficha_tutor, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.page_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 45))
        self.frame_3.setMaximumSize(QSize(16777215, 45))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.lbl9_5 = QLabel(self.frame_3)
        self.lbl9_5.setObjectName(u"lbl9_5")
        self.lbl9_5.setStyleSheet(u"")
        self.lbl9_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl9_5)

        self.btn_export_3 = QPushButton(self.frame_3)
        self.btn_export_3.setObjectName(u"btn_export_3")
        self.btn_export_3.setMinimumSize(QSize(146, 35))
        self.btn_export_3.setMaximumSize(QSize(160, 35))
        self.btn_export_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_3.setStyleSheet(u"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 450;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;\n"
"background: #f78f91;\n"
"border-radius: 8px;}\n"
"\n"
"QPushButton:hover{background: #e38487;\n"
"border-radius: 8px; }")
        self.btn_export_3.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.btn_export_3)


        self.gridLayout_31.addWidget(self.frame_3, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_3)

        self.gridLayout_28.addWidget(self.stackedWidget_2, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_24)


        self.gridLayout_29.addWidget(self.frame_41, 0, 0, 1, 1)

        self.stackedWidget_5.addWidget(self.page)
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
        self.radioProcesoE = QRadioButton(self.frame_16)
        self.radioProcesoE.setObjectName(u"radioProcesoE")
        self.radioProcesoE.setChecked(True)

        self.gridLayout_26.addWidget(self.radioProcesoE, 1, 5, 1, 1)

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

        self.radioPendienteE = QRadioButton(self.frame_16)
        self.radioPendienteE.setObjectName(u"radioPendienteE")

        self.gridLayout_26.addWidget(self.radioPendienteE, 1, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_7, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_10, 1, 3, 1, 1)

        self.btn_export = QPushButton(self.frame_16)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setMinimumSize(QSize(146, 35))
        self.btn_export.setMaximumSize(QSize(160, 35))
        self.btn_export.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export.setStyleSheet(u"\n"
"QPushButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: 450;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color: #FFFFFF;\n"
"background: #f78f91;\n"
"border-radius: 8px;}\n"
"\n"
"QPushButton:hover{background: #e38487;\n"
"border-radius: 8px; }")
        self.btn_export.setIcon(icon12)

        self.gridLayout_26.addWidget(self.btn_export, 1, 9, 1, 1)

        self.check_todos_estudiantes = QCheckBox(self.frame_16)
        self.check_todos_estudiantes.setObjectName(u"check_todos_estudiantes")
        self.check_todos_estudiantes.setChecked(True)

        self.gridLayout_26.addWidget(self.check_todos_estudiantes, 1, 2, 1, 1)

        self.radioCulminadoE = QRadioButton(self.frame_16)
        self.radioCulminadoE.setObjectName(u"radioCulminadoE")

        self.gridLayout_26.addWidget(self.radioCulminadoE, 1, 7, 1, 1)

        self.label_3 = QLabel(self.frame_16)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_26.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_16, 1, 8, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_39)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_17)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tabla_reporte_estudiantes = QTableWidget(self.frame_17)
        if (self.tabla_reporte_estudiantes.columnCount() < 16):
            self.tabla_reporte_estudiantes.setColumnCount(16)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(0, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(1, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(2, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(3, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(4, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(5, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(6, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(7, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(8, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(9, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(10, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(11, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(12, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(13, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(14, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tabla_reporte_estudiantes.setHorizontalHeaderItem(15, __qtablewidgetitem149)
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
"font-weight: 700;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
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
"\n"
"/*bordes internos*/\n"
"QTab"
                        "leWidget::item {\n"
"	border-bottom: 3px solid #f3f4f6;\n"
"\n"
"}\n"
"\n"
"QTableWidget:item:selected{\n"
"	background:white;/*color-seleccion*/\n"
"color: #2c3d3e;\n"
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
        self.stacked_administracion.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(1)


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
        self.btn_afiliacion.setToolTip(QCoreApplication.translate("principal", u"Paciente", None))
#endif // QT_CONFIG(tooltip)
        self.btn_afiliacion.setText(QCoreApplication.translate("principal", u"     Vinculaci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btn_usuario.setToolTip(QCoreApplication.translate("principal", u"Usuarios", None))
#endif // QT_CONFIG(tooltip)
        self.btn_usuario.setText(QCoreApplication.translate("principal", u"     Usuarios", None))
#if QT_CONFIG(tooltip)
        self.btn_seguimientoo.setToolTip(QCoreApplication.translate("principal", u"Seguimiento", None))
#endif // QT_CONFIG(tooltip)
        self.btn_seguimientoo.setText(QCoreApplication.translate("principal", u"     Seguimiento", None))
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("principal", u"Inicio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText(QCoreApplication.translate("principal", u"     Administracion", None))
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
        self.btn_pag_antes_vinculacion.setText("")
        self.lbl_pagina_vinculacion.setText(QCoreApplication.translate("principal", u"2000", None))
        self.btn_pag_desp_vinculacion.setText("")
        self.line_filtro_estudiante.setPlaceholderText(QCoreApplication.translate("principal", u"Buscar estudiante por nombre - apellidos - cedula", None))
        self.cbo_filtro_proyecto.setItemText(0, QCoreApplication.translate("principal", u"Seleccione proyecto", None))

        self.cbo_filtro_tutor.setItemText(0, QCoreApplication.translate("principal", u"Seleccione tutor", None))

        self.label.setText(QCoreApplication.translate("principal", u"Filtro", None))
        self.cbo_filtro_periodo.setItemText(0, QCoreApplication.translate("principal", u"Seleccione periodo academico", None))

        self.btn_nueva_vinculacion.setText(QCoreApplication.translate("principal", u" Nueva asignaci\u00f3n", None))
        ___qtablewidgetitem = self.tabla_vinculacion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_vinculacion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("principal", u"NOMBRE PROYECTO", None));
        ___qtablewidgetitem2 = self.tabla_vinculacion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("principal", u"FECHA INICIO", None));
        ___qtablewidgetitem3 = self.tabla_vinculacion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("principal", u"PERIODO ACADEMICO", None));
        ___qtablewidgetitem4 = self.tabla_vinculacion.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("principal", u"NRO ESTUDIANTES", None));
        ___qtablewidgetitem5 = self.tabla_vinculacion.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("principal", u"ACCIONES", None));
        self.label_2.setText(QCoreApplication.translate("principal", u"  Lista de Vinculaci\u00f3n", None))
        self.label_7.setText(QCoreApplication.translate("principal", u"MOSTRAR", None))
        self.cbox_rango_tutor.setItemText(0, QCoreApplication.translate("principal", u"5", None))
        self.cbox_rango_tutor.setItemText(1, QCoreApplication.translate("principal", u"10", None))
        self.cbox_rango_tutor.setItemText(2, QCoreApplication.translate("principal", u"50", None))

        self.label_8.setText(QCoreApplication.translate("principal", u"REGISTRO", None))
#if QT_CONFIG(tooltip)
        self.btn_recargar_tutor.setToolTip(QCoreApplication.translate("principal", u"Actualizar registro", None))
#endif // QT_CONFIG(tooltip)
        self.btn_recargar_tutor.setText("")
        ___qtablewidgetitem6 = self.tabla_principal_tutor.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem7 = self.tabla_principal_tutor.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("principal", u"ESTUDIANTE", None));
        ___qtablewidgetitem8 = self.tabla_principal_tutor.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("principal", u"FECHA AFILIACI\u00d3N", None));
        ___qtablewidgetitem9 = self.tabla_principal_tutor.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("principal", u"HORAS SEGUIMIENTO", None));
        ___qtablewidgetitem10 = self.tabla_principal_tutor.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("principal", u"ESTADO VINCULACI\u00d3N", None));
        ___qtablewidgetitem11 = self.tabla_principal_tutor.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("principal", u"ACCIONES", None));
        ___qtablewidgetitem12 = self.tabla_principal_tutor.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem13 = self.tabla_principal_tutor.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem14 = self.tabla_principal_tutor.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.line_busqueda_tutor.setPlaceholderText(QCoreApplication.translate("principal", u"Buscar por cualquier campo", None))
        self.label_6.setText(QCoreApplication.translate("principal", u"  Lista de alumnos asignados", None))
        self.line_busqueda_estudiantes.setPlaceholderText(QCoreApplication.translate("principal", u"buscar por nombre - apellido - cedula ", None))
        self.check_estado_estudiantes.setText(QCoreApplication.translate("principal", u"Mostrar inactivos", None))
        self.btn_agregar_estudiantes_admin.setText(QCoreApplication.translate("principal", u"Registrar estudiante", None))
        ___qtablewidgetitem15 = self.tabla_estudiantes.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("principal", u"Id", None));
        ___qtablewidgetitem16 = self.tabla_estudiantes.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("principal", u"Nombres", None));
        ___qtablewidgetitem17 = self.tabla_estudiantes.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("principal", u"Apellidos", None));
        ___qtablewidgetitem18 = self.tabla_estudiantes.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("principal", u"Cedula", None));
        ___qtablewidgetitem19 = self.tabla_estudiantes.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("principal", u"Correo electronico", None));
        ___qtablewidgetitem20 = self.tabla_estudiantes.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("principal", u"Acciones", None));
        ___qtablewidgetitem21 = self.tabla_estudiantes.verticalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem22 = self.tabla_estudiantes.verticalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("principal", u"Nueva fila", None));

        __sortingEnabled = self.tabla_estudiantes.isSortingEnabled()
        self.tabla_estudiantes.setSortingEnabled(False)
        ___qtablewidgetitem23 = self.tabla_estudiantes.item(0, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem24 = self.tabla_estudiantes.item(0, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem25 = self.tabla_estudiantes.item(0, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem26 = self.tabla_estudiantes.item(0, 3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("principal", u"qsq", None));
        ___qtablewidgetitem27 = self.tabla_estudiantes.item(0, 4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem28 = self.tabla_estudiantes.item(1, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem29 = self.tabla_estudiantes.item(1, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("principal", u"qsq", None));
        ___qtablewidgetitem30 = self.tabla_estudiantes.item(1, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem31 = self.tabla_estudiantes.item(1, 3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem32 = self.tabla_estudiantes.item(1, 4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("principal", u"qsqs", None));
        self.tabla_estudiantes.setSortingEnabled(__sortingEnabled)

        self.btn_pag_desp_estu.setText("")
        self.lbl_pagina_estudiantes.setText(QCoreApplication.translate("principal", u"Pagina 1 de", None))
        self.btn_pag_antes_estu.setText("")
        self.line_busqueda_tutores.setPlaceholderText(QCoreApplication.translate("principal", u"buscar por nombre - apellido - cedula ", None))
        self.check_estado_tutores.setText(QCoreApplication.translate("principal", u"Mostrar inactivos", None))
        self.btn_agregar_tutores.setText(QCoreApplication.translate("principal", u"Registrar tutor", None))
        ___qtablewidgetitem33 = self.tabla_tutores.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("principal", u"Id", None));
        ___qtablewidgetitem34 = self.tabla_tutores.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("principal", u"Nombres", None));
        ___qtablewidgetitem35 = self.tabla_tutores.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("principal", u"Apellidos", None));
        ___qtablewidgetitem36 = self.tabla_tutores.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("principal", u"Cedula", None));
        ___qtablewidgetitem37 = self.tabla_tutores.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("principal", u"Correo electronico", None));
        ___qtablewidgetitem38 = self.tabla_tutores.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("principal", u"Acciones", None));
        ___qtablewidgetitem39 = self.tabla_tutores.verticalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem40 = self.tabla_tutores.verticalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("principal", u"Nueva fila", None));

        __sortingEnabled1 = self.tabla_tutores.isSortingEnabled()
        self.tabla_tutores.setSortingEnabled(False)
        ___qtablewidgetitem41 = self.tabla_tutores.item(0, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem42 = self.tabla_tutores.item(0, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem43 = self.tabla_tutores.item(0, 2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem44 = self.tabla_tutores.item(0, 3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("principal", u"qsq", None));
        ___qtablewidgetitem45 = self.tabla_tutores.item(0, 4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem46 = self.tabla_tutores.item(1, 0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem47 = self.tabla_tutores.item(1, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("principal", u"qsq", None));
        ___qtablewidgetitem48 = self.tabla_tutores.item(1, 2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem49 = self.tabla_tutores.item(1, 3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem50 = self.tabla_tutores.item(1, 4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("principal", u"qsqs", None));
        self.tabla_tutores.setSortingEnabled(__sortingEnabled1)

        self.btn_pag_antes_tutor.setText("")
        self.btn_pag_desp_tutor.setText("")
        self.lbl_pagina_tutores.setText(QCoreApplication.translate("principal", u"Pagina 1 de", None))
        self.line_busqueda_proyecto.setPlaceholderText(QCoreApplication.translate("principal", u"buscar por nombre", None))
        self.check_estado_proyecto.setText(QCoreApplication.translate("principal", u"Mostrar inactivos", None))
        self.btn_agregar_proyectos.setText(QCoreApplication.translate("principal", u"Registrar proyecto", None))
        ___qtablewidgetitem51 = self.tabla_proyecto.horizontalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("principal", u"Id", None));
        ___qtablewidgetitem52 = self.tabla_proyecto.horizontalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("principal", u"Nombre", None));
        ___qtablewidgetitem53 = self.tabla_proyecto.horizontalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("principal", u"Estado", None));
        ___qtablewidgetitem54 = self.tabla_proyecto.horizontalHeaderItem(3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("principal", u"Acciones", None));
        ___qtablewidgetitem55 = self.tabla_proyecto.verticalHeaderItem(0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem56 = self.tabla_proyecto.verticalHeaderItem(1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("principal", u"Nueva fila", None));

        __sortingEnabled2 = self.tabla_proyecto.isSortingEnabled()
        self.tabla_proyecto.setSortingEnabled(False)
        ___qtablewidgetitem57 = self.tabla_proyecto.item(0, 0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem58 = self.tabla_proyecto.item(0, 1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem59 = self.tabla_proyecto.item(1, 0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem60 = self.tabla_proyecto.item(1, 1)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("principal", u"qsq", None));
        self.tabla_proyecto.setSortingEnabled(__sortingEnabled2)

        self.lbl_pagina_proyectos.setText(QCoreApplication.translate("principal", u"2000", None))
        self.btn_pag_desp_proyecto.setText("")
        self.btn_pag_antes_proyecto.setText("")
        self.line_busqueda_carrera.setPlaceholderText(QCoreApplication.translate("principal", u"buscar por nombre", None))
        self.check_estado_carrera.setText(QCoreApplication.translate("principal", u"Mostrar inactivos", None))
        self.btn_agregar_carrera.setText(QCoreApplication.translate("principal", u"Registrar carrera", None))
        ___qtablewidgetitem61 = self.tabla_carrera.horizontalHeaderItem(0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("principal", u"Id", None));
        ___qtablewidgetitem62 = self.tabla_carrera.horizontalHeaderItem(1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("principal", u"Nombre carrera", None));
        ___qtablewidgetitem63 = self.tabla_carrera.horizontalHeaderItem(2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("principal", u"Estado", None));
        ___qtablewidgetitem64 = self.tabla_carrera.horizontalHeaderItem(3)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("principal", u"Acciones", None));
        ___qtablewidgetitem65 = self.tabla_carrera.verticalHeaderItem(0)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem66 = self.tabla_carrera.verticalHeaderItem(1)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("principal", u"Nueva fila", None));

        __sortingEnabled3 = self.tabla_carrera.isSortingEnabled()
        self.tabla_carrera.setSortingEnabled(False)
        ___qtablewidgetitem67 = self.tabla_carrera.item(0, 0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem68 = self.tabla_carrera.item(0, 1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem69 = self.tabla_carrera.item(0, 2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("principal", u"qsq", None));
        ___qtablewidgetitem70 = self.tabla_carrera.item(1, 0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem71 = self.tabla_carrera.item(1, 1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem72 = self.tabla_carrera.item(1, 2)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("principal", u"qsqs", None));
        self.tabla_carrera.setSortingEnabled(__sortingEnabled3)

        self.btn_pag_antes_carrera.setText("")
        self.btn_pag_desp_carrera.setText("")
        self.lbl_pagina_carrera.setText(QCoreApplication.translate("principal", u"2000", None))
        self.line_busqueda_inst.setPlaceholderText(QCoreApplication.translate("principal", u"buscar por nombre", None))
        self.check_estado_insti.setText(QCoreApplication.translate("principal", u"Mostrar inactivos", None))
        self.btn_agregar_insti.setText(QCoreApplication.translate("principal", u"Registrar instituci\u00f3n", None))
        ___qtablewidgetitem73 = self.tabla_institucion.horizontalHeaderItem(0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("principal", u"Id", None));
        ___qtablewidgetitem74 = self.tabla_institucion.horizontalHeaderItem(1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("principal", u"Nombre", None));
        ___qtablewidgetitem75 = self.tabla_institucion.horizontalHeaderItem(2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("principal", u"Telefono", None));
        ___qtablewidgetitem76 = self.tabla_institucion.horizontalHeaderItem(3)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("principal", u"Estado", None));
        ___qtablewidgetitem77 = self.tabla_institucion.horizontalHeaderItem(4)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("principal", u"Acciones", None));
        ___qtablewidgetitem78 = self.tabla_institucion.verticalHeaderItem(0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem79 = self.tabla_institucion.verticalHeaderItem(1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("principal", u"Nueva fila", None));

        __sortingEnabled4 = self.tabla_institucion.isSortingEnabled()
        self.tabla_institucion.setSortingEnabled(False)
        ___qtablewidgetitem80 = self.tabla_institucion.item(0, 0)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem81 = self.tabla_institucion.item(0, 1)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem82 = self.tabla_institucion.item(0, 3)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("principal", u"qsq", None));
        ___qtablewidgetitem83 = self.tabla_institucion.item(1, 0)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("principal", u"qsqs", None));
        ___qtablewidgetitem84 = self.tabla_institucion.item(1, 1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("principal", u"sqs", None));
        ___qtablewidgetitem85 = self.tabla_institucion.item(1, 3)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("principal", u"qsqs", None));
        self.tabla_institucion.setSortingEnabled(__sortingEnabled4)

        self.lbl_pagina_instituto.setText(QCoreApplication.translate("principal", u"2000", None))
        self.btn_pag_desp_inst.setText("")
        self.btn_pag_antes_inst.setText("")
        self.btn_menu_estudiantes.setText(QCoreApplication.translate("principal", u"Estudiantes", None))
        self.btn_menu_tutores.setText(QCoreApplication.translate("principal", u"Tutores", None))
        self.btn_menu_proyectos.setText(QCoreApplication.translate("principal", u"Proyectos", None))
        self.btn_menu_carreras.setText(QCoreApplication.translate("principal", u"Carreras", None))
        self.btn_menu_instituciones.setText(QCoreApplication.translate("principal", u"Instituciones practica", None))
        ___qtablewidgetitem86 = self.tabla_usuario.horizontalHeaderItem(0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem87 = self.tabla_usuario.horizontalHeaderItem(1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("principal", u"USUARIO", None));
        ___qtablewidgetitem88 = self.tabla_usuario.horizontalHeaderItem(2)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("principal", u"DOCUMENTO IDENTIDAD", None));
        ___qtablewidgetitem89 = self.tabla_usuario.horizontalHeaderItem(3)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("principal", u"CARGO", None));
        ___qtablewidgetitem90 = self.tabla_usuario.horizontalHeaderItem(4)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("principal", u"CORREO", None));
        ___qtablewidgetitem91 = self.tabla_usuario.horizontalHeaderItem(5)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("principal", u"FECHA REGISTRO", None));
        ___qtablewidgetitem92 = self.tabla_usuario.horizontalHeaderItem(6)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("principal", u"ESTADO", None));
        ___qtablewidgetitem93 = self.tabla_usuario.horizontalHeaderItem(7)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("principal", u"ACCIONES", None));
        ___qtablewidgetitem94 = self.tabla_usuario.verticalHeaderItem(0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem95 = self.tabla_usuario.verticalHeaderItem(1)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem96 = self.tabla_usuario.verticalHeaderItem(2)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.label_9.setText(QCoreApplication.translate("principal", u"Lista de usuarios registrados", None))
        self.btn_agregar_usuario.setText(QCoreApplication.translate("principal", u"  Agregar usuario", None))
        self.line_busqueda_usuario.setPlaceholderText(QCoreApplication.translate("principal", u"Nombre y apellidos...", None))
        self.radioEstudiante.setText(QCoreApplication.translate("principal", u"REPORTE POR ESTUDIANTES", None))
        self.radioTutor.setText(QCoreApplication.translate("principal", u"REGISTRO ENTREGA TUTORES", None))
        self.radioreporteentrega.setText(QCoreApplication.translate("principal", u"REPORTE ENTREGA TUTORES", None))
        self.line_busqueda_reporte_tutor.setPlaceholderText(QCoreApplication.translate("principal", u"Buscar por cualquier campo....", None))
        ___qtablewidgetitem97 = self.tabla_reporte_tutores.horizontalHeaderItem(0)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem98 = self.tabla_reporte_tutores.horizontalHeaderItem(1)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("principal", u"TUTOR", None));
        ___qtablewidgetitem99 = self.tabla_reporte_tutores.horizontalHeaderItem(2)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("principal", u"CEDULA", None));
        ___qtablewidgetitem100 = self.tabla_reporte_tutores.horizontalHeaderItem(3)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("principal", u"CARGO", None));
        ___qtablewidgetitem101 = self.tabla_reporte_tutores.horizontalHeaderItem(4)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("principal", u"CORREO", None));
        ___qtablewidgetitem102 = self.tabla_reporte_tutores.horizontalHeaderItem(5)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("principal", u"ACCIONES", None));
        ___qtablewidgetitem103 = self.tabla_reporte_tutores.verticalHeaderItem(0)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem104 = self.tabla_reporte_tutores.verticalHeaderItem(1)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem105 = self.tabla_reporte_tutores.verticalHeaderItem(2)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.label_12.setText(QCoreApplication.translate("principal", u"REGISTRO", None))
        self.cbox_rango_reporte_tutor.setItemText(0, QCoreApplication.translate("principal", u"5", None))
        self.cbox_rango_reporte_tutor.setItemText(1, QCoreApplication.translate("principal", u"10", None))
        self.cbox_rango_reporte_tutor.setItemText(2, QCoreApplication.translate("principal", u"50", None))

        self.label_11.setText(QCoreApplication.translate("principal", u"MOSTRAR", None))
        self.cbo_tipo_entrega.setItemText(0, QCoreApplication.translate("principal", u"Informe", None))
        self.cbo_tipo_entrega.setItemText(1, QCoreApplication.translate("principal", u"Ficha - Memorandum", None))

        self.lbl9_3.setText(QCoreApplication.translate("principal", u"Tipo entrega", None))
        self.lbl9_4.setText(QCoreApplication.translate("principal", u"Periodo Academico", None))
        ___qtablewidgetitem106 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(0)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("principal", u"TUTOR", None));
        ___qtablewidgetitem107 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(1)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("principal", u"ENERO", None));
        ___qtablewidgetitem108 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(2)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("principal", u"FEBRERO", None));
        ___qtablewidgetitem109 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(3)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("principal", u"MARZO", None));
        ___qtablewidgetitem110 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(4)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("principal", u"ABRIL", None));
        ___qtablewidgetitem111 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(5)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("principal", u"MAYO", None));
        ___qtablewidgetitem112 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(6)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("principal", u"JUNIO", None));
        ___qtablewidgetitem113 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(7)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("principal", u"JULIO", None));
        ___qtablewidgetitem114 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(8)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("principal", u"AGOSTO", None));
        ___qtablewidgetitem115 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(9)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("principal", u"SETIEMBRE", None));
        ___qtablewidgetitem116 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(10)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("principal", u"OCTUBRE", None));
        ___qtablewidgetitem117 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(11)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("principal", u"NOVIEMBRE", None));
        ___qtablewidgetitem118 = self.tabla_reporte_informe_tutor.horizontalHeaderItem(12)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("principal", u"DICIEMBRE", None));
        ___qtablewidgetitem119 = self.tabla_reporte_informe_tutor.verticalHeaderItem(0)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem120 = self.tabla_reporte_informe_tutor.verticalHeaderItem(1)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem121 = self.tabla_reporte_informe_tutor.verticalHeaderItem(2)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.btn_export_2.setText(QCoreApplication.translate("principal", u" Exportar a PDF", None))
        self.lbl9_6.setText(QCoreApplication.translate("principal", u"Memorandum", None))
        self.btn_export_4.setText(QCoreApplication.translate("principal", u" Exportar a PDF", None))
        ___qtablewidgetitem122 = self.tabla_reporte_memorandum_tutor.horizontalHeaderItem(0)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("principal", u"TUTOR", None));
        ___qtablewidgetitem123 = self.tabla_reporte_memorandum_tutor.horizontalHeaderItem(1)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("principal", u"SI", None));
        ___qtablewidgetitem124 = self.tabla_reporte_memorandum_tutor.horizontalHeaderItem(2)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("principal", u"NO", None));
        ___qtablewidgetitem125 = self.tabla_reporte_memorandum_tutor.verticalHeaderItem(0)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem126 = self.tabla_reporte_memorandum_tutor.verticalHeaderItem(1)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem127 = self.tabla_reporte_memorandum_tutor.verticalHeaderItem(2)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem128 = self.tabla_reporte_ficha_tutor.horizontalHeaderItem(0)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("principal", u"TUTOR", None));
        ___qtablewidgetitem129 = self.tabla_reporte_ficha_tutor.horizontalHeaderItem(1)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("principal", u"SI", None));
        ___qtablewidgetitem130 = self.tabla_reporte_ficha_tutor.horizontalHeaderItem(2)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("principal", u"NO", None));
        ___qtablewidgetitem131 = self.tabla_reporte_ficha_tutor.verticalHeaderItem(0)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem132 = self.tabla_reporte_ficha_tutor.verticalHeaderItem(1)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        ___qtablewidgetitem133 = self.tabla_reporte_ficha_tutor.verticalHeaderItem(2)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("principal", u"Nueva fila", None));
        self.lbl9_5.setText(QCoreApplication.translate("principal", u"Ficha", None))
        self.btn_export_3.setText(QCoreApplication.translate("principal", u" Exportar a PDF", None))
        self.radioProcesoE.setText(QCoreApplication.translate("principal", u"Proceso", None))
        self.line_busqueda_reporte_estudiantes.setPlaceholderText(QCoreApplication.translate("principal", u"Filtrar por cualquier campo...", None))
        self.radioPendienteE.setText(QCoreApplication.translate("principal", u"Pendiente", None))
        self.btn_export.setText(QCoreApplication.translate("principal", u" Exportar a PDF", None))
        self.check_todos_estudiantes.setText(QCoreApplication.translate("principal", u"Todos", None))
        self.radioCulminadoE.setText(QCoreApplication.translate("principal", u"Culminado", None))
        self.label_3.setText(QCoreApplication.translate("principal", u"Filtrar por nombre estudiante", None))
        ___qtablewidgetitem134 = self.tabla_reporte_estudiantes.horizontalHeaderItem(0)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("principal", u"ID", None));
        ___qtablewidgetitem135 = self.tabla_reporte_estudiantes.horizontalHeaderItem(1)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("principal", u"PERIODO ACADEMICO", None));
        ___qtablewidgetitem136 = self.tabla_reporte_estudiantes.horizontalHeaderItem(2)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("principal", u"ESTADO VINCULACION", None));
        ___qtablewidgetitem137 = self.tabla_reporte_estudiantes.horizontalHeaderItem(3)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("principal", u"CODIGO IES", None));
        ___qtablewidgetitem138 = self.tabla_reporte_estudiantes.horizontalHeaderItem(4)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("principal", u"TIPO IDENTIFICACION", None));
        ___qtablewidgetitem139 = self.tabla_reporte_estudiantes.horizontalHeaderItem(5)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("principal", u"IDENT. ESTUDIANTE", None));
        ___qtablewidgetitem140 = self.tabla_reporte_estudiantes.horizontalHeaderItem(6)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("principal", u"ESTUDIANTE", None));
        ___qtablewidgetitem141 = self.tabla_reporte_estudiantes.horizontalHeaderItem(7)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("principal", u"INSTITUCI\u00d3N", None));
        ___qtablewidgetitem142 = self.tabla_reporte_estudiantes.horizontalHeaderItem(8)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("principal", u"TIPO INSTITUCI\u00d3N", None));
        ___qtablewidgetitem143 = self.tabla_reporte_estudiantes.horizontalHeaderItem(9)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("principal", u"COD. CARRERA", None));
        ___qtablewidgetitem144 = self.tabla_reporte_estudiantes.horizontalHeaderItem(10)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("principal", u"FECHA INICIO", None));
        ___qtablewidgetitem145 = self.tabla_reporte_estudiantes.horizontalHeaderItem(11)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("principal", u"FECHA FIN", None));
        ___qtablewidgetitem146 = self.tabla_reporte_estudiantes.horizontalHeaderItem(12)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("principal", u"N\u00daMEROS HORAS", None));
        ___qtablewidgetitem147 = self.tabla_reporte_estudiantes.horizontalHeaderItem(13)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("principal", u"CAMPO ESPECIFICO", None));
        ___qtablewidgetitem148 = self.tabla_reporte_estudiantes.horizontalHeaderItem(14)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("principal", u"IDENT. TUTOR", None));
        ___qtablewidgetitem149 = self.tabla_reporte_estudiantes.horizontalHeaderItem(15)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("principal", u"TUTOR", None));
        self.label_15.setText(QCoreApplication.translate("principal", u"REGISTRO", None))
        self.label_16.setText(QCoreApplication.translate("principal", u"MOSTRAR", None))
        self.cbox_rango_estudiantes.setItemText(0, QCoreApplication.translate("principal", u"5", None))
        self.cbox_rango_estudiantes.setItemText(1, QCoreApplication.translate("principal", u"10", None))
        self.cbox_rango_estudiantes.setItemText(2, QCoreApplication.translate("principal", u"50", None))

    # retranslateUi

