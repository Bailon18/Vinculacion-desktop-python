

from PySide2 import QtWidgets , QtCore , QtGui
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

import re, os
from PIL import Image
from datetime import datetime

from controllers.Modulo_principal.funcion_general import *

# importamos la clase de la base datos
from db.Modulo_base import BaseDatos

from views.ui_seguimiento_admin import Ui_SeguimientoAdmin


class Seguimiento_admin(QtWidgets.QDialog):

    def __init__(self, dato = [], parent=None):
        
        super(Seguimiento_admin, self).__init__()
        self.seguimiento = Ui_SeguimientoAdmin()
        self.seguimiento.setupUi(self)

        # columnas de tabla a elastica (Stretch)
        #self.seguimiento.tabla_admiseguimiento.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) 

        # Establecer el ancho fijo para la primera columna
        self.seguimiento.tabla_admiseguimiento.setColumnWidth(0, 170)  # Cambiar 100 al ancho deseado

        # Establecer el ancho fijo para la segunda columna
        self.seguimiento.tabla_admiseguimiento.setColumnWidth(1, 300)  # Cambiar 200 al ancho deseado


        # conexion con la bd
        self.conec_base = BaseDatos()
        
        self.parent = parent

        self.seguimiento.lbl_nombre_estudiante.setText('Lista de seguimiento: ' + str(dato[0]).capitalize())
        self.seguimiento.lbl_nombretutor.setText(dato[1])

        self.llenar_seguimiento(dato[2])

        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.seguimiento.btn_closeseguimiento.clicked.connect(lambda: self.cerrar_ui_seguimientoadmin())

        
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

    def llenar_seguimiento(self, vinculacion_id):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        datos = self.conec_base.getDatosProcess_condicion("ObtenerSeguimientosPorVinculacionId", (vinculacion_id,))
        if len(datos) > 0:
            cargar_tabla(self.seguimiento.tabla_admiseguimiento, datos[0])

            