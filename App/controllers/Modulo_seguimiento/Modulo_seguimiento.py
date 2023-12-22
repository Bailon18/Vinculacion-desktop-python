from PySide2 import QtWidgets , QtCore , QtGui
from controllers.Modulo_seguimiento.funcion_seguimiento import evento_tabla
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad
from PySide2.QtWidgets import QMessageBox

import re, os
from PIL import Image
from datetime import datetime


# importamos la clase de la base datos
from db.Modulo_base import BaseDatos

from views.ui_seguimiento import Ui_Seguimiento


class Seguimiento(QtWidgets.QDialog):

    def __init__(self, dato = [], parent=None):
        
        super(Seguimiento, self).__init__()
        self.seguimiento_tutor = Ui_Seguimiento()
        self.seguimiento_tutor.setupUi(self)

        # conexion con la bd
        self.conec_base = BaseDatos()

        self.datos_compartidos = dato
        
        self.parent = parent

        self.ventanaconfiguracion()

        evento_tabla(self)
    
        self.seguimiento_tutor.lbl_nombreestudiante.setText(str(self.datos_compartidos[1]))

        if(self.datos_compartidos[3] == 'Edit'):
            self.seguimiento_tutor.label_40.setText('Editar Seguimiento')
            self.seguimiento_tutor.btn_guardar.setText('Actualizar')
            self.llenadoSeguimiento()

  

        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.seguimiento_tutor.btn_closeseguimiento.clicked.connect(lambda: self.cerrar_ui_seguimientoadmin())


        self.seguimiento_tutor.btn_nuevo_seguimiento.clicked.connect(lambda: self.seguimiento_tutor.stack_principal.setCurrentIndex(0))
        self.seguimiento_tutor.btn_retornar_listado.clicked.connect(lambda: self.seguimiento_tutor.stack_principal.setCurrentIndex(1))

        self.seguimiento_tutor.btn_guardar.clicked.connect(lambda: self.guardarSeguimiento())
        self.seguimiento_tutor.checkhoraactual.clicked.connect(lambda: self.evento_hora_actual())                                             
        self.seguimiento_tutor.fecha_seguimiento.dateChanged.connect(lambda: self.evento_cambio_fecha())

        
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

    def ventanaconfiguracion(self):
        self.fechaactual()
        pass

    def guardarSeguimiento(self):
        
        fecha_seleccionada = self.seguimiento_tutor.fecha_seguimiento.date().toString('yyyy-MM-dd')
        hora_seguimiento = self.seguimiento_tutor.spb_numerohoras.value()
        observacion = self.seguimiento_tutor.plain_observacion.toPlainText()


        mensaje_error = ''

        if(hora_seguimiento != ''):
            mensaje_error += '- Hora asignado no puede estar vacío.\n'
        if(int(hora_seguimiento) > 1):
            mensaje_error += '- Hora asignado tiene que ser mayor a 1 hora.\n'


        if mensaje_error:
            QMessageBox.critical(self, 'Error', 'Revise los campos:\n' + mensaje_error)
        else:
            dato = [ self.datos_compartidos[0], fecha_seleccionada, observacion, self.datos_compartidos[2], int(hora_seguimiento) ]

            self.conec_base.setDatosProcess('InsertarSeguimientoTutor', (dato))
            QMessageBox.information(self, 'Correcto', 'Seguimiento registrado correctamente')
            self.seguimiento_tutor.stack_principal.setCurrentIndex(1)


    def llenadoSeguimiento(self):
        pass
    

    def listado_seguimiento(self):
        
        datos = [self.datos_compartidos[2] ,self.datos_compartidos[0]]
        resultado = self.conec_base.getDatosProcess_condicion('ObtenerSeguimientosPorTutorYEstudiante', (datos))





    def evento_hora_actual(self):
        self.fechaactual()


    def fechaactual(self):
        fecha_actual = QtCore.QDate.currentDate()
        self.seguimiento_tutor.fecha_seguimiento.setDate(fecha_actual) 

    def evento_cambio_fecha(self):

        fecha_seleccionada = self.seguimiento_tutor.fecha_seguimiento.date().toString("yyyy-MM-dd")
        fecha_actual = QtCore.QDate.currentDate()

        if fecha_seleccionada != fecha_actual.toString("yyyy-MM-dd"):
            self.seguimiento_tutor.checkhoraactual.setChecked(False) 

    
