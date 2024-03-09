# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_VenCargaReportesuRvGEd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source.image import source

class Ui_VenCargaReportes(object):
    def setupUi(self, VenCargaReportes):
        if not VenCargaReportes.objectName():
            VenCargaReportes.setObjectName(u"VenCargaReportes")
        VenCargaReportes.resize(320, 130)
        VenCargaReportes.setMinimumSize(QSize(320, 130))
        VenCargaReportes.setMaximumSize(QSize(320, 130))
        self.label_2 = QLabel(VenCargaReportes)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 100, 151, 20))
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:11px;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.barraCarga = QProgressBar(VenCargaReportes)
        self.barraCarga.setObjectName(u"barraCarga")
        self.barraCarga.setGeometry(QRect(15, 50, 291, 41))
        self.barraCarga.setStyleSheet(u"QProgressBar{\n"
"text-align: center;}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color:#3f5758 ;}")
        self.barraCarga.setValue(0)
        self.label = QLabel(VenCargaReportes)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 151, 31))
        self.label.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:15px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(VenCargaReportes)

        QMetaObject.connectSlotsByName(VenCargaReportes)
    # setupUi

    def retranslateUi(self, VenCargaReportes):
        VenCargaReportes.setWindowTitle(QCoreApplication.translate("VenCargaReportes", u"Reporte", None))
        self.label_2.setText(QCoreApplication.translate("VenCargaReportes", u"Espere un momento.", None))
        self.label.setText(QCoreApplication.translate("VenCargaReportes", u"Generando reporte...", None))
    # retranslateUi

