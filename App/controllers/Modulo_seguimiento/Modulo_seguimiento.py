from PySide2 import QtWidgets , QtCore , QtGui
from controllers.Modulo_seguimiento.Modulo_actividad import FormularioSeguimientoEstudiante
from controllers.Modulo_seguimiento.funcion_seguimiento import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad
from PySide2.QtWidgets import QMessageBox

import re, os
from PIL import Image
from datetime import datetime


# importamos la clase de la base datos
from db.Modulo_base import BaseDatos

from views.ui_seguimiento import Ui_FormularioSeguimiento


class Seguimiento(QtWidgets.QDialog):

    def __init__(self, parent=None, id_seguimiento=None, nombre_estudiante=None):
        
        super(Seguimiento, self).__init__()
        self.seguimiento_tutor = Ui_FormularioSeguimiento()
        self.seguimiento_tutor.setupUi(self)

        # conexion con la bd
        self.conec_base = BaseDatos()

        self.parent = parent
        self.id_seguimiento = id_seguimiento
        self.nombre_estudiante = nombre_estudiante 
        self.offset = 0
        self.limit = 4
        
        if(self.parent.rol == 'Administrador'):
            self.seguimiento_tutor.btn_nuevo_seguimiento.setHidden(True)
        
        self.seguimiento_tutor.lbl_nombreestudiante.setText(str(self.nombre_estudiante))
        
        self.ventanaconfiguracion()

        evento_tabla(self)
    
        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.seguimiento_tutor.btn_close.clicked.connect(lambda: self.cerrar_ui_seguimientoadmin())


        self.seguimiento_tutor.fecha_inicio_seguimiento.dateChanged.connect(lambda: self.filtro_obtener_actividades_xfechas())
        self.seguimiento_tutor.fecha_final_seguimiento.dateChanged.connect(lambda: self.filtro_obtener_actividades_xfechas())

        self.seguimiento_tutor.btn_pag_antes_seguimiento.clicked.connect(lambda: self.prev_page('ObtenerListaSeguimientoXEstudiante', 'seguimiento', self.seguimiento_tutor.lbl_pagina_seguimiento, self.seguimiento_tutor.tabla_listado_actividades))
        self.seguimiento_tutor.btn_pag_desp_seguimiento.clicked.connect(lambda: self.next_page('ObtenerListaSeguimientoXEstudiante', 'seguimiento', self.seguimiento_tutor.lbl_pagina_seguimiento, self.seguimiento_tutor.tabla_listado_actividades))
        
        
    
        # Inicializar la tabla con la primera página
        self.llenarTabla('ObtenerListaSeguimientoXEstudiante', 'seguimiento', self.seguimiento_tutor.tabla_listado_actividades)
        self.actualizarInfoPaginacion('seguimiento', self.seguimiento_tutor.lbl_pagina_seguimiento)
        
        
        self.seguimiento_tutor.btn_nuevo_seguimiento.clicked.connect(lambda: self.abrirNuevaActividad())

        
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
            
    def abrirNuevaActividad(self):
        self.cerrar_ui_seguimientoadmin()
        self.parent.abrir_ventana_nueva_actividad()
       
    
    def llenarTabla(self, procedimiento, tabla,  tabla_diseno):
        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, [self.id_seguimiento, self.offset, self.limit])
        llenar_tabla_actividades(self, tabla_diseno, datoresultante[0])

    def next_page(self, procedimiento, tabla, labels, tabla_diseno):
        self.offset += self.limit
        datoretorno = self.conec_base.getDatosProcess_condicion(procedimiento, [self.id_seguimiento, self.offset, self.limit])
  
        if len(datoretorno[0]) > 0:
            self.llenarTabla(procedimiento, tabla, tabla_diseno)
        else:
            self.offset -= self.limit
        self.actualizarInfoPaginacion(tabla, labels)

    def prev_page(self, procedimiento, tabla, labels, tabla_diseno):
        self.offset = max(0, self.offset - self.limit)
        self.llenarTabla(procedimiento, tabla, tabla_diseno)
        self.actualizarInfoPaginacion(tabla, labels)
        
    def actualizarInfoPaginacion(self, nomnbreTabla, labels):
        total_registros = self.conec_base.getDatos(f'SELECT COUNT(*) FROM {nomnbreTabla} WHERE estudiantes_vinculacion_id = {self.id_seguimiento}')
        total_registros = total_registros[0][0] if total_registros else 0
        total_paginas = (total_registros + self.limit - 1) // self.limit 
        pagina_actual = (self.offset // self.limit) + 1 
        labels.setText(f"Página {pagina_actual} de {total_paginas}") 

    def filtro_obtener_actividades_xfechas(self):
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        fecha_inicio = self.seguimiento_tutor.fecha_inicio_seguimiento.date().toString("yyyy-MM-dd")
        fecha_final = self.seguimiento_tutor.fecha_final_seguimiento.date().toString("yyyy-MM-dd")

        if fecha_inicio > fecha_final:
            procedimiento = "ObtenerListaSeguimientoXEstudiante"
            parametros = (self.id_seguimiento, self.offset, self.limit)
            QtWidgets.QMessageBox.warning(self, 'Advertencia', 'La fecha de inicio debe ser menor o igual a la fecha final.')
            return
        else:
            total_registros = self.conec_base.getDatosProcess_condicion("contar_instituciones_SeguimientoXEstudiante", (self.id_seguimiento, fecha_inicio, fecha_final))
            total_registros = total_registros[0][0][0] if total_registros else 0

            total_paginas = (total_registros + self.limit - 1) // self.limit
            pagina_actual = min((self.offset // self.limit) + 1, total_paginas)
            self.offset = max(0, (pagina_actual - 1) * self.limit)

            procedimiento = "buscar_seguimiento_fechas"
            parametros = (self.id_seguimiento, fecha_inicio, fecha_final, self.offset, self.limit)

        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, parametros)

        if len(datoresultante[0]) > 0:
            llenar_tabla_actividades(self, self.seguimiento_tutor.tabla_listado_actividades, datoresultante[0])
        else:
            self.offset = max(0, self.offset - self.limit)
        self.actualizarInfoPaginacion('seguimiento', self.seguimiento_tutor.lbl_pagina_seguimiento)

    def ventanaconfiguracion(self):
        

        fecha_actual = QtCore.QDate.currentDate()

        self.seguimiento_tutor.fecha_inicio_seguimiento.dateChanged.connect(
            lambda: self.seguimiento_tutor.fecha_final_seguimiento.setMinimumDate(self.seguimiento_tutor.fecha_inicio_seguimiento.date()))
        
        self.seguimiento_tutor.fecha_inicio_seguimiento.setDate(fecha_actual)
      
