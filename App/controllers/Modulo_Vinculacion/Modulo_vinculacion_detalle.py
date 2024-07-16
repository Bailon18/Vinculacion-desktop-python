
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import QFileInfo
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QMessageBox, QFileDialog

import re

from controllers.Modulo_Vinculacion.funciona_vinculacion import *
from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_vinculacion_detalle import Ui_FormularioVinculacionDetalle

from db.Modulo_base import BaseDatos


class VinculacionDetalle(QtWidgets.QDialog):

    def __init__(self, vinculacion_id = None, parent=None):
        
        super(VinculacionDetalle, self).__init__(parent)
        self.vinculaciondetalle = Ui_FormularioVinculacionDetalle()
        self.vinculaciondetalle.setupUi(self)
        
        self.conec_base = BaseDatos()
        self.lista_id_estudiantes = []

        self.parent = parent
        self.archivo_cv = None
        self.nombretutor = ''
  
        evento_tabla_detalle(self)
        
        self.vinculacion_id = vinculacion_id 
            
        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.vinculaciondetalle.btn_close.clicked.connect(lambda: self.cerrar_ventana())
        
        self.obtener_vinculacion_y_estudiantes(self.vinculacion_id)
        self.vinculaciondetalle.btn_descargar.clicked.connect(lambda: self.descargar_archivo())
        self.vinculaciondetalle.btn_exportar_detalle.clicked.connect(lambda: self.exportar_detalle_vinculacion())
  

    def cerrar_ventana(self):
        self.parent.raizOpacidad.close()
        self.close()
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
    
    def cerrar_ui_vinculacion(self):
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
    
    
    def obtener_vinculacion_y_estudiantes(self, vinculacion_id):
            
        try:
 
            vinculacion_datos = self.conec_base.getDatosProcess_condicion("ObtenerDetalleVinculacion", (vinculacion_id, ))
            
            if not vinculacion_datos:
                QMessageBox.warning(self, "Error", "No se encontró la vinculación especificada.")
                return
            
            vinculacion = vinculacion_datos[0][0]
            
            # Detalle de vinculación
            self.vinculaciondetalle.date_fecha_inicio.setText(str(vinculacion[0]))
            self.vinculaciondetalle.line_codigo_ies.setText(vinculacion[1])
            self.vinculaciondetalle.line_campo_especifico.setText(vinculacion[2])
            self.vinculaciondetalle.line_periodo_academico.setText(vinculacion[3])
            self.vinculaciondetalle.cbo_institucion.setText(vinculacion[4])
            
            # Detalle del tutor
            self.vinculaciondetalle.line_nombres_tutor.setText(vinculacion[5])
            self.vinculaciondetalle.line_cedula_tutor.setText(vinculacion[6])
            self.vinculaciondetalle.line_telefono_tutor.setText(vinculacion[7])
            self.vinculaciondetalle.line_correo_tutor.setText(vinculacion[8])
            self.archivo_cv = vinculacion[9] 
            self.nombretutor = vinculacion[5] 
            
            # Detalle del proyecto
            self.vinculaciondetalle.line_nombre_proyecto.setText(vinculacion[10])
            

            
            consulta_estudiantes = f"""
                SELECT ev.estudiantes_id, e.nro_identificacion, concat(e.nombres,' ', e.apellidos), ev.estado_vinculacion, ev.nro_horas
                FROM estudiantes_vinculacion ev
                JOIN estudiantes e ON ev.estudiantes_id = e.id
                WHERE ev.vinculacion_id = {vinculacion_id}
            """
            estudiantes_datos = self.conec_base.getDatos(consulta_estudiantes)
   
            # Detalle de estudiantes seleccionados
            for estudiante in estudiantes_datos:
                id_estudiante, cedula_estudiante, nombre_estudiante, estado_vinculacion , nro_horas= estudiante
                self.lista_id_estudiantes.append([id_estudiante, cedula_estudiante, nombre_estudiante, estado_vinculacion, nro_horas])
                llenar_tabla_estudiantes_detalle(self, self.vinculaciondetalle.tabla_estudiante_seleccionado, self.lista_id_estudiantes)

        except Exception as e:
            QMessageBox.critical(self, "Error de Base de Datos", f"Error al obtener los datos: {str(e)}")
            
            
    def descargar_archivo(self):
        if self.archivo_cv:
            default_filename = f"{self.nombretutor}-cv.pdf"
            opciones = QFileDialog.Options()
            archivo, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar archivo",
                default_filename,  
                "Archivos PDF (*.pdf)", 
                options=opciones
            )
            
            if archivo:
                if not archivo.lower().endswith('.pdf'):
                    archivo += '.pdf' 
                else:
                    archivo = QFileInfo(archivo).absolutePath() + '/' + default_filename  
                    
                with open(archivo, 'wb') as file:
                    file.write(self.archivo_cv)
                    
                if archivo.lower().endswith('.pdf'):
                    import os
                    os.startfile(archivo)
                    
                QMessageBox.information(self, "Éxito", "El archivo se ha descargado correctamente.")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay ningún archivo para descargar.")
    
    
    def exportar_detalle_vinculacion(self):
        
        from controllers.Modulo_reporte.generarRepoInforme import FormRepoImforme
        
        
        vinculacion_datos = self.conec_base.getDatosProcess_condicion("ObtenerDetalleVinculacion", (self.vinculacion_id, ))
            
        if not vinculacion_datos:
            QMessageBox.warning(self, "Error", "No se encontró la vinculación especificada.")
            return
        
        vinculacion = vinculacion_datos[0][0]

        vinculacion_datos = [{
            'fecha_inicio': vinculacion[0],
            'codigo_ies': vinculacion[1],
            'campo_especifico': vinculacion[2],
            'periodo_academico': vinculacion[3],
            'institucion_nombre': vinculacion[4],
            'tutor_nombre': vinculacion[5],
            'tutor_identificacion': vinculacion[6],
            'tutor_telefono': vinculacion[7],
            'tutor_correo': vinculacion[8],
            'proyecto_nombre': vinculacion[10]
        }]

        estudiantes_datos = [estudiante[1:] for estudiante in self.lista_id_estudiantes]
        FormRepoImforme(vinculacion_datos=vinculacion_datos, datos=estudiantes_datos, modo='vinculacion').exec_()
 
            
        

    

  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    