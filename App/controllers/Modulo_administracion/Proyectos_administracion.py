
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox


from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_proyectos import Ui_FormularioProyectos

from db.Modulo_base import BaseDatos

class ProyectosAdmin(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', proyecto_id =  None):

        super(ProyectosAdmin, self).__init__()
        
        self.venProyecto = Ui_FormularioProyectos()
        self.venProyecto.setupUi(self)
        self.control_base = BaseDatos()
        

        self.parent = parent
        self.modo = modo
        
        self.nombre_actual = ''

        
        if(self.modo != 'nuevo'):
            self.proyecto_id = proyecto_id
            self.venProyecto.btn_agregar_proyecto.setText('Actualizar')
            self.venProyecto.lbl_titulo_ventana.setText('Editar Proyecto')
            self.llenado_datos_proyecto(int(self.proyecto_id))

    

        self.STYLE_ERROR = "color: #D32F2F; font-family: Roboto; font-style: normal; font-weight: bold; font-size: 12px; visibility: visible;"
        self.STYLE_VALID = "border: 2px solid green;"
        self.STYLE_INVALID = "border: 2px solid red;"
        
        self.venProyecto.line_nombre.textChanged.connect(self.validar_nombre)

        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.venProyecto.btn_close.clicked.connect(lambda: self.cerrar_ventana())
        self.venProyecto.btn_agregar_proyecto.clicked.connect(lambda: self.accion_boton_guardar())
        self.venProyecto.cancelButton.clicked.connect(lambda: self.cerrar_ventana())
        
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
            consulta = "SELECT COUNT(*) FROM proyecto WHERE LOWER(nombre) = LOWER(%s)"
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
        nombre = self.venProyecto.line_nombre.toPlainText()
        respuesta_validacion = self.es_valida_texto(nombre)
        if respuesta_validacion:
            self.venProyecto.line_nombre.setStyleSheet(self.STYLE_INVALID)
            self.venProyecto.errorNombre.setText(respuesta_validacion)
            self.venProyecto.errorNombre.setStyleSheet(self.STYLE_ERROR)
        else:
            respuesta_bd = self.consultar_existencia_nombre(nombre)
            if respuesta_bd:
                self.venProyecto.line_nombre.setStyleSheet(self.STYLE_INVALID)
                self.venProyecto.errorNombre.setText("Nombre proyecto ya existe.")
                self.venProyecto.errorNombre.setStyleSheet(self.STYLE_ERROR)
            else:
                self.venProyecto.line_nombre.setStyleSheet(self.STYLE_VALID)
                self.venProyecto.errorNombre.setStyleSheet("")
                self.venProyecto.errorNombre.setText("")
                
        
    def campos_validados(self):
        return (self.venProyecto.line_nombre.styleSheet() == self.STYLE_VALID)
        
        
    def accion_boton_guardar(self):
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        nombre_proyecto = self.venProyecto.line_nombre.toPlainText().strip()
        descripcion = self.venProyecto.plain_descripcion.toPlainText()
        estado = True if self.venProyecto.cbo_estado.currentText() == 'Activo' else False
        
        self.validar_nombre()

        if self.campos_validados():
            try:
                if self.modo != 'nuevo':

                    self.control_base.setDatosProcess('actualizar_proyecto', (self.proyecto_id, nombre_proyecto, descripcion, estado))

                    QMessageBox.information(self, "Mensaje", "Los datos se han actualizado correctamente en la base de datos.")
                else:
                    self.control_base.setDatosProcess('agregar_proyecto', (nombre_proyecto, descripcion, estado))
                    
                    QMessageBox.information(self, "Mensaje", "Los datos se han validado correctamente y se han enviado a la base de datos.")

                self.parent.raizOpacidad.close()
                self.close()
                self.parent.offset = 0
                self.parent.llenarTabla('listar_proyectos', 'proyecto', self.parent.venPri.tabla_proyecto)
                self.parent.venPri.check_estado_proyecto.setChecked(False)
                self.parent.actualizarInfoPaginacion('proyecto', self.parent.venPri.lbl_pagina_proyectos, True)
                self.parent.datos_inicializacion()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ha ocurrido un error al guardar los datos en la base de datos: {str(e)}")


    def llenado_datos_proyecto(self, proyecto_id):
        
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        respuesta = self.control_base.getDatosProcess_condicion('buscar_proyecto_por_id', (proyecto_id,))
        if(respuesta):
            respuesta = respuesta[0][0]
            self.venProyecto.line_nombre.setPlainText(respuesta[0])
            self.venProyecto.plain_descripcion.setPlainText(respuesta[1])
            estado = 'Activo' if respuesta[2] == True else 'Inactivo'
            self.venProyecto.cbo_estado.setCurrentText(estado)
            self.nombre_actual = respuesta[0]
  


    