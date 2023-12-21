from PySide2 import QtWidgets , QtCore , QtGui
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

import re, os
from PIL import Image
from datetime import datetime


# importamos la clase de la base datos
from db.Modulo_base import BaseDatos

from views.ui_seguimiento_nuevo import Ui_SeguimientoNuevo


class Seguimiento(QtWidgets.QDialog):

    def __init__(self, dato = [], parent=None):
        
        super(Seguimiento, self).__init__()
        self.seguimiento_tutor = Ui_SeguimientoNuevo()
        self.seguimiento_tutor.setupUi(self)

        # conexion con la bd
        self.conec_base = BaseDatos()
        
        self.parent = parent

    
        self.seguimiento_tutor.lbl_nombreestudiante.setText(dato[0])

        self.llenar_seguimiento(dato[2])

        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.seguimiento_tutor.btn_closeseguimiento.clicked.connect(lambda: self.cerrar_ui_seguimientoadmin())

        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
    
    def cerrar_ui_seguimientoadmin(self):
        self.parent.raizOpacidad.close()
        self.close()
        
    def keyPressEvent(self, qKeyEvent):
 
        if qKeyEvent.modifiers() & QtCore.Qt.AltModifier:
            qKeyEvent.ignore()
        elif qKeyEvent.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.focusNextChild()
            self.window().setAttribute(QtCore.Qt.WA_KeyboardFocusChange)
        else:
            super().keyPressEvent(qKeyEvent)