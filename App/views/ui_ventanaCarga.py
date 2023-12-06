# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ventanaCargaZCmcHf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_VentanaCarga(object):
    def setupUi(self, VentanaCarga):
        if not VentanaCarga.objectName():
            VentanaCarga.setObjectName(u"VentanaCarga")
        VentanaCarga.resize(619, 410)
        VentanaCarga.setStyleSheet(u"/*\n"
"#VentanaCarga{\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"*/")
        self.frameLoad = QFrame(VentanaCarga)
        self.frameLoad.setObjectName(u"frameLoad")
        self.frameLoad.setGeometry(QRect(80, 120, 471, 181))
        self.frameLoad.setStyleSheet(u"#frameLoad{\n"
"\n"
"border-radius:30px;\n"
"border:3px solid white;\n"
"\n"
"	background-color: rgb(243, 244, 246);\n"
"}\n"
"")
        self.frameLoad.setFrameShadow(QFrame.Raised)
        self.labTitu = QLabel(self.frameLoad)
        self.labTitu.setObjectName(u"labTitu")
        self.labTitu.setGeometry(QRect(20, 70, 431, 31))
        self.labTitu.setStyleSheet(u"font-size:25px;\n"
"color:#3A4F50;\n"
"font-family: \"Roboto\";\n"
"\n"
"")
        self.labTitu.setAlignment(Qt.AlignCenter)
        self.progreLoad = QProgressBar(self.frameLoad)
        self.progreLoad.setObjectName(u"progreLoad")
        self.progreLoad.setGeometry(QRect(40, 120, 391, 41))
        self.progreLoad.setStyleSheet(u"QProgressBar {\n"
"	background-color:#8A8A8C;\n"
"	color: white;\n"
"	height: 28px;\n"
"	border-radius: 15px;\n"
"	text-align: center;\n"
"	font-family: \"Roboto\";\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"background-color: #3A4F50;\n"
"\n"
"}\n"
"")
        self.progreLoad.setValue(31)
        self.progreLoad.setTextVisible(True)
        self.progreLoad.setOrientation(Qt.Horizontal)
        self.progreLoad.setTextDirection(QProgressBar.TopToBottom)
        self.labTitu_3 = QLabel(self.frameLoad)
        self.labTitu_3.setObjectName(u"labTitu_3")
        self.labTitu_3.setGeometry(QRect(10, 28, 451, 31))
        self.labTitu_3.setStyleSheet(u"font-size:25px;\n"
"color:#8A8A8C;\n"
"font-family: \"Roboto\";")
        self.labTitu_3.setAlignment(Qt.AlignCenter)

        self.retranslateUi(VentanaCarga)

        QMetaObject.connectSlotsByName(VentanaCarga)
    # setupUi

    def retranslateUi(self, VentanaCarga):
        VentanaCarga.setWindowTitle(QCoreApplication.translate("VentanaCarga", u"ReadBot Cargando", None))
        self.labTitu.setText(QCoreApplication.translate("VentanaCarga", u"Manuel Anonimo", None))
        self.labTitu_3.setText(QCoreApplication.translate("VentanaCarga", u"Bienvenido", None))
    # retranslateUi

