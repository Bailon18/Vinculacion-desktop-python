
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox

import re

from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_carreras import Ui_FormularioCarreras

from db.Modulo_base import BaseDatos

class CarrerasAdmin(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', carrera_id =  None):

        super(CarrerasAdmin, self).__init__()
        
        self.venCarreras = Ui_FormularioCarreras()
        self.venCarreras.setupUi(self)
        self.control_base = BaseDatos()
        

        self.parent = parent
        self.modo = modo
        
    
        self.nombre_actual = ''

        
        if(self.modo != 'nuevo'):
            self.carrera_id = carrera_id
            self.venCarreras.btn_agregar_carrera.setText('Actualizar')
            self.venCarreras.lbl_titulo_ventana.setText('Editar Carrera')
            self.llenado_datos_carreras(int(self.carrera_id))
            
            
        self.STYLE_ERROR = "color: #D32F2F; font-family: Roboto; font-style: normal; font-weight: bold; font-size: 12px; visibility: visible;"
        self.STYLE_VALID = "border: 2px solid green;"
        self.STYLE_INVALID = "border: 2px solid red;"
        
        self.venCarreras.line_nombre.textChanged.connect(self.validar_nombre)

        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.venCarreras.btn_close.clicked.connect(lambda: self.cerrar_ventana())
        self.venCarreras.btn_agregar_carrera.clicked.connect(lambda: self.accion_boton_guardar())
        self.venCarreras.cancelButton.clicked.connect(lambda: self.cerrar_ventana())

 
        
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
        
    def consultar_existencia_nombre(self, nombre):
        if nombre != self.nombre_actual:
            consulta = "SELECT COUNT(*) FROM carrera WHERE LOWER(nombre) = LOWER(%s)"
            respuesta = self.control_base.getDatos_condicion(consulta, (nombre,))
            return respuesta[0][0] if respuesta else 0
        else:
            return 0
        
    def es_valida_texto(self, nombre):
        identificacion_stripped = nombre.strip()
        if not identificacion_stripped:
            return "Campo vacío"
        return ""
        

    def validar_nombre(self):
        nombre = self.venCarreras.line_nombre.text()
        respuesta_validacion = self.es_valida_texto(nombre)
        if respuesta_validacion:
            self.venCarreras.line_nombre.setStyleSheet(self.STYLE_INVALID)
            self.venCarreras.errorNombre.setText(respuesta_validacion)
            self.venCarreras.errorNombre.setStyleSheet(self.STYLE_ERROR)
        else:
            respuesta_bd = self.consultar_existencia_nombre(nombre)
            if respuesta_bd:
                self.venCarreras.line_nombre.setStyleSheet(self.STYLE_INVALID)
                self.venCarreras.errorNombre.setText("Nombre proyecto ya existe.")
                self.venCarreras.errorNombre.setStyleSheet(self.STYLE_ERROR)
            else:
                self.venCarreras.line_nombre.setStyleSheet(self.STYLE_VALID)
                self.venCarreras.errorNombre.setStyleSheet("")
                self.venCarreras.errorNombre.setText("")

    def campos_validados(self):
        return (self.venCarreras.line_nombre.styleSheet() == self.STYLE_VALID)


    def accion_boton_guardar(self):
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        nombre_carrera = self.venCarreras.line_nombre.text().strip()
        descripcion = self.venCarreras.plain_descripcion.toPlainText()
        estado = True if self.venCarreras.cbo_estado.currentText() == 'Activo' else False
        
        self.validar_nombre()

        if self.campos_validados():
            try:
                if self.modo != 'nuevo':

                    self.control_base.setDatosProcess('actualizar_carrera', (self.carrera_id, nombre_carrera, descripcion, estado))

                    QMessageBox.information(self, "Mensaje", "Los datos se han actualizado correctamente en la base de datos.")
                else:
                    self.control_base.setDatosProcess('agregar_carrera', (nombre_carrera, descripcion, estado))
                    
                    QMessageBox.information(self, "Mensaje", "Los datos se han validado correctamente y se han enviado a la base de datos.")

                self.parent.raizOpacidad.close()
                self.close()
                self.parent.llenarTabla('listar_carreras', 'carrera', self.parent.venPri.tabla_carrera)
                self.parent.actualizarInfoPaginacion('carrera', self.parent.venPri.lbl_pagina_carrera)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ha ocurrido un error al guardar los datos en la base de datos: {str(e)}")

    
    def llenado_datos_carreras(self, carrera_id):
        
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        respuesta = self.control_base.getDatosProcess_condicion('buscar_carrera_por_id', (carrera_id,))
        if(respuesta):
            respuesta = respuesta[0][0]
            self.venCarreras.line_nombre.setText(respuesta[0])
            self.venCarreras.plain_descripcion.setPlainText(respuesta[1])
            estado = 'Activo' if respuesta[2] == True else 'Inactivo'
            self.venCarreras.cbo_estado.setCurrentText(estado)
            self.nombre_actual = respuesta[0]
  
  


    