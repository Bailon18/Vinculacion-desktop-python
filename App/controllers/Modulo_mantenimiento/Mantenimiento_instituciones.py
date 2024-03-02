
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox
from controllers.Modulo_mantenimiento.funciones import llenar_tabla_institucion

from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_instituciones import Ui_Institucion

from db.Modulo_base import BaseDatos

class Instituciones(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', dato = []):

        super(Instituciones, self).__init__()
        self.venInst = Ui_Institucion()
        self.venInst.setupUi(self)
        self.control_base = BaseDatos()


        self.parent = parent
        self.modo = modo

  
        if(self.modo != 'Nuevo'):
            self.institucion_id = dato[0]
            self.nombre_institucion = dato[1]
            self.venInst.btn_guardar_institiucion.setText('Actualizar')
            self.venInst.lbl_titulo_ventana.setText('Editar Institución')
            self.venInst.lbl_instituto_seleccionado.setText(str(self.nombre_institucion))
            self.llenado_datos_institucion(int(self.institucion_id))



        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.venInst.btn_closeedit.clicked.connect(lambda: self.cerrar_ventana())

        self.venInst.btn_guardar_institiucion.clicked.connect(lambda: self.accion_boton_guardar())


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

        nombre = self.venInst.line_nombre_institucion.text().strip()
        tipo_institucion = self.venInst.line_tipo_institucion.text().strip()
        estado = self.venInst.cbox_estado_intitucion.currentText()
        direccion = self.venInst.line_direccion_institucion.text().strip()

        mensaje = ""

        if nombre == "":
            mensaje += "El campo 'Nombre' no puede estar vacío.\n"

        if tipo_institucion == "":
            mensaje += "El campo 'Tipo de Institución' no puede estar vacío.\n"

        if estado == "":
            mensaje += "Seleccione un 'Estado de la Institución'.\n"

        if direccion == "":
            mensaje += "El campo 'Dirección' no puede estar vacío.\n"

        if mensaje != "":
            QMessageBox.warning(self, "Error al guardar", "Se encontraron los siguientes errores:\n" + mensaje)
        else:
            
            if(self.modo == 'Nuevo'):
                self.control_base.setDatosProcess('AgregarInstitucion', [nombre, tipo_institucion, direccion, estado])
            else:
                self.control_base.setDatosProcess('ActualizarInstitucion', [self.institucion_id, nombre, tipo_institucion, direccion, estado])
            
            QMessageBox.information(self, "Mensaje", "La acción se realizo correctamente!")
            self.parent.raizOpacidad.close()
            self.close()
            self.parent.llenado_instituciones('Activo')
            

    def llenado_datos_institucion(self, institucion_id):
        
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        respuesta = self.control_base.getDatosProcess_condicion('BuscarInstitucionPorID', (institucion_id,))
        if(respuesta):
            respuesta = respuesta[0][0]
            self.venInst.line_nombre_institucion.setText(respuesta[1])
            self.venInst.line_tipo_institucion.setText(respuesta[2])
            self.venInst.cbox_estado_intitucion.setCurrentText(respuesta[4])
            self.venInst.line_direccion_institucion.setText(respuesta[3])
           