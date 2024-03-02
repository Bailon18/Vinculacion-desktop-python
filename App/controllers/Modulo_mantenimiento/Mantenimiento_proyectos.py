
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox

import re
from controllers.Modulo_mantenimiento.funciones import llenar_tabla_institucion


from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_proyectos import Ui_Proyectos

from db.Modulo_base import BaseDatos

class Proyectos(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', proyecto_id =  None):

        super(Proyectos, self).__init__()
        self.venProyecto = Ui_Proyectos()
        self.venProyecto.setupUi(self)
        self.control_base = BaseDatos()


        self.parent = parent
        self.modo = modo
        
    
        if(self.modo != 'Nuevo'):
            self.proyecto_id = proyecto_id
            self.venProyecto.btn_guardar.setText('Actualizar')
            self.venProyecto.lbl_titulo_ventana.setText('Editar Proyecto')
            self.llenado_datos_proyecto(int(self.proyecto_id))


        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.venProyecto.btn_closeedit.clicked.connect(lambda: self.cerrar_ventana())

        self.venProyecto.btn_guardar.clicked.connect(lambda: self.accion_boton_guardar())
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
        
    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.modifiers() & QtCore.Qt.AltModifier:
            qKeyEvent.ignore()
        elif qKeyEvent.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.focusNextChild()
            self.window().setAttribute(QtCore.Qt.WA_KeyboardFocusChange)
        else:
            super().keyPressEvent(qKeyEvent)

    def cerrar_ventana(self):
        self.parent.raizOpacidad.close()
        self.close()


    def accion_boton_guardar(self):
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        nombre_proyecto = self.venProyecto.plain_nombre_proyecto.toPlainText().strip()
        estado = self.venProyecto.cbox_estado_proyecto.currentText()

        mensaje = ""

        if nombre_proyecto == "":
            mensaje += "El campo 'Nombre' no puede estar vacío.\n"

        if estado == "":
            mensaje += "Seleccione un 'Estado del proyecto'.\n"


        if mensaje != "":
            QMessageBox.warning(self, "Error al guardar", "Se encontraron los siguientes errores:\n" + mensaje)
        else:
            if(self.modo == 'Nuevo'):
                self.control_base.setDatosProcess('InsertarProyecto', [nombre_proyecto, estado])
            else:
                self.control_base.setDatosProcess('ActualizarProyecto', [self.proyecto_id, nombre_proyecto, estado])
            
            QMessageBox.information(self, "Mensaje", "La acción se realizo correctamente!")
            self.parent.raizOpacidad.close()
            self.close()
            self.parent.llenado_proyectos('Activo')


    def llenado_datos_proyecto(self, proyecto_id):
        
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        respuesta = self.control_base.getDatosProcess_condicion('BuscarProyectoPorID', (proyecto_id,))
        if(respuesta):
            respuesta = respuesta[0][0]
            self.venProyecto.plain_nombre_proyecto.setPlainText(respuesta[1])
            self.venProyecto.cbox_estado_proyecto.setCurrentText(respuesta[2])
  


    