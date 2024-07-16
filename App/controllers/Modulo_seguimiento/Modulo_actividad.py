from PySide2 import QtWidgets , QtCore , QtGui
from controllers.Modulo_seguimiento.funcion_seguimiento import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad
from PySide2.QtCore import QFileInfo
from PySide2.QtWidgets import QMessageBox, QFileDialog
import imghdr

from PySide2.QtCore import QUrl
from PySide2.QtGui import QDesktopServices

import re, os
from PIL import Image
from datetime import datetime

from db.Modulo_base import BaseDatos

from views.ui_formulario_seguimiento_estudiante import Ui_FormularioSeguimientoEstudiante


class FormularioSeguimientoEstudiante(QtWidgets.QDialog):

    def __init__(self, parent=None, id_actividad=None, nombre_estudiante=None, id_estudiante_vinculado=None, modo='nuevo'):
        
        super(FormularioSeguimientoEstudiante, self).__init__()
        self.seguimiento_estudiante = Ui_FormularioSeguimientoEstudiante()
        self.seguimiento_estudiante.setupUi(self)


        self.parent = parent
       
        if(self.parent.rol == 'Administrador'):
            self.seguimiento_estudiante.btn_agregar_actividad.setHidden(True)
            self.seguimiento_estudiante.lbl_titulo_ventana.setText('Detalle de actividad')
            self.seguimiento_estudiante.btn_subir_fotos.setText('Evidencia foto')
            self.seguimiento_estudiante.btn_subir_archivo.setText('Evidencia archivo')
            self.seguimiento_estudiante.fecha_actividad.setEnabled(False)
            self.seguimiento_estudiante.horas_spinx.setEnabled(False)
            self.seguimiento_estudiante.btn_subir_fotos.setEnabled(False)
            self.seguimiento_estudiante.btn_subir_archivo.setEnabled(False)
            #self.seguimiento_estudiante.actividades_plain.setEnabled(False)
            #self.seguimiento_estudiante.observacion_plain.setEnabled(False)
            


        # conexion con la bd
        self.conec_base = BaseDatos()
        self.ventanaconfiguracion()
    
 
        self.id_actividad = id_actividad
        self.nombre_estudiante = nombre_estudiante 
        self.offset = 0
        self.limit = 4
        self.modo = modo
        
        self.seguimiento_estudiante.btn_descargar_foto.hide()
        self.seguimiento_estudiante.btn_descargar_archivo.hide()
        
        self.archivo_actividad = None
        self.archivo_foto = None
        self.tipo_archivo = ''
        self.tipo_archivo_foto = ''
        
        self.id_estudiante_vinculado = id_estudiante_vinculado
        
        if(self.modo != 'nuevo'):
            if(self.parent.rol == 'Tutor'):
                self.seguimiento_estudiante.lbl_titulo_ventana.setText('Editar Actividad')
                self.seguimiento_estudiante.btn_agregar_actividad.setText('Actualizar')
            self.llenar_actividad(self.id_actividad)
        
        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.seguimiento_estudiante.btn_closeedit.clicked.connect(lambda: self.cerrar_ui_seguimientoadmin())
        self.seguimiento_estudiante.cancelButton.clicked.connect(lambda: self.cerrar_ui_seguimientoadmin())
        
        
        self.seguimiento_estudiante.btn_subir_archivo.clicked.connect(lambda: self.subir_archivo())
        self.seguimiento_estudiante.btn_subir_fotos.clicked.connect(lambda: self.subir_foto())
        
        self.seguimiento_estudiante.horas_spinx.valueChanged.connect(lambda: self.validarHora())
        self.seguimiento_estudiante.actividades_plain.textChanged.connect(lambda: self.validarActividad())
        self.seguimiento_estudiante.btn_agregar_actividad.clicked.connect(lambda: self.agregar_actividad())
        
        
        self.STYLE_ERROR = "color: #D32F2F; font-family: Roboto; font-style: normal; font-weight: bold; font-size: 12px; visibility: visible;"
        self.STYLE_VALID = "border: 2px solid green;"
        self.STYLE_INVALID = "border: 2px solid red;"
        
        self.seguimiento_estudiante.btn_descargar_archivo.clicked.connect(lambda: self.descargar_archivo())
        self.seguimiento_estudiante.btn_descargar_foto.clicked.connect(lambda: self.descargar_foto())
    
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
    
    def cerrar_ui_seguimientoadmin(self):
        self.parent.raizOpacidad.close()
        self.close()
        self.parent.modo_formulario_seguimiento_estudiante = 'nuevo'
        self.parent.id_actividad = 0
        self.parent.abrir_ventana_seguimiento_tutor()

    def keyPressEvent(self, qKeyEvent):
 
        if qKeyEvent.modifiers() & QtCore.Qt.AltModifier:
            qKeyEvent.ignore()
        elif qKeyEvent.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.focusNextChild()
            self.window().setAttribute(QtCore.Qt.WA_KeyboardFocusChange)
        else:
            super().keyPressEvent(qKeyEvent)
            
    def configuracion_ventana(self):
        
        fecha_actual = QtCore.QDate.currentDate()
        self.seguimiento_estudiante.fecha_actividad.setDate(fecha_actual)
        
    def subir_archivo(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo",
            "",
            "Archivos PDF (*.pdf);;Archivos Word (*.doc *.docx);;Archivos Excel (*.xls *.xlsx);;Archivos PowerPoint (*.ppt *.pptx)",
            options=opciones
        )
        
        if archivo:
            with open(archivo, 'rb') as file:
                self.archivo_actividad = file.read()
  
                extension = QFileInfo(archivo).suffix().lower()
                # Determinar el tipo de archivo
                if extension in ['pdf']:
                    self.tipo_archivo = 'pdf'
                elif extension in ['doc', 'docx']:
                    self.tipo_archivo = 'word'
                elif extension in ['xls', 'xlsx']:
                    self.tipo_archivo = 'excel'
                elif extension in ['ppt', 'pptx']:
                    self.tipo_archivo = 'ppt'
                else:
                    self.tipo_archivo = 'desconocido'
                self.validarArchivos()
                    
            self.seguimiento_estudiante.lbl_nombre_archivo_seleccionado_2.setText(QFileInfo(archivo).fileName())
            
            
            QMessageBox.information(self, "Éxito", "El archivo se ha cargado correctamente.")
        else:
            QMessageBox.information(self, "Cancelado", "No se ha seleccionado ningún archivo.")
            
    def subir_foto(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar foto",
            "",
            "Imágenes (*.jpg *.jpeg *.png)",
            options=opciones
        )
        
        if archivo:
            with open(archivo, 'rb') as file:
                self.archivo_foto = file.read()
                extension = QFileInfo(archivo).suffix().lower()
                if extension in ['jpg', 'jpeg']:
                    self.tipo_archivo_foto = 'jpg'
                elif extension == 'png':
                    self.tipo_archivo_foto = 'png'
                else:
                    self.tipo_archivo_foto = 'desconocido'
                self.validarArchivos()
                    
            self.seguimiento_estudiante.lbl_nombre_archivo_seleccionado.setText(QFileInfo(archivo).fileName())
          
            
            QMessageBox.information(self, "Éxito", f"La foto se ha cargado correctamente. Tipo de archivo: {self.tipo_archivo_foto}.")
        else:
            QMessageBox.information(self, "Cancelado", "No se ha seleccionado ninguna foto.")
          
    def campos_validados(self):
        return (self.seguimiento_estudiante.horas_spinx.styleSheet() == self.STYLE_VALID and
                self.seguimiento_estudiante.actividades_plain.styleSheet() == self.STYLE_VALID)  
            
    def is_validar_hora(self, hora):
        if hora is None:
            return "Campo vacío"
        elif hora <= 0:
            return "Debe tener al menos 1 hora"
        return ""

    def validarActividad(self):
        actividades = self.seguimiento_estudiante.actividades_plain.toPlainText()
        if not actividades:
            self.seguimiento_estudiante.actividades_plain.setStyleSheet(self.STYLE_INVALID)
            self.seguimiento_estudiante.errorListActividades.setText("Lista actividades es obligatoria")
            self.seguimiento_estudiante.errorListActividades.setStyleSheet(self.STYLE_ERROR)
        else:
            self.seguimiento_estudiante.actividades_plain.setStyleSheet(self.STYLE_VALID)
            self.seguimiento_estudiante.errorListActividades.setStyleSheet("")
            self.seguimiento_estudiante.errorListActividades.setText("")
            
    def validarHora(self):
        hora = self.seguimiento_estudiante.horas_spinx.value()
        respuesta = self.is_validar_hora(hora)
        if respuesta:
            self.seguimiento_estudiante.horas_spinx.setStyleSheet(self.STYLE_INVALID)
            self.seguimiento_estudiante.errorHora.setText(respuesta)
            self.seguimiento_estudiante.errorHora.setStyleSheet(self.STYLE_ERROR)
        else:
            self.seguimiento_estudiante.horas_spinx.setStyleSheet(self.STYLE_VALID)
            self.seguimiento_estudiante.errorHora.setStyleSheet("")   
            self.seguimiento_estudiante.errorHora.setText("")   
            
    def validarArchivos(self):
        if self.archivo_actividad is None and self.archivo_foto is None:
            self.seguimiento_estudiante.errorEvidencias.setText('Debe guardar una evidencia de tipo foto o archivo.')
            self.seguimiento_estudiante.errorEvidencias.setStyleSheet(self.STYLE_ERROR)
        else:
            self.seguimiento_estudiante.errorEvidencias.setStyleSheet("")   
            self.seguimiento_estudiante.errorEvidencias.setText("")   
            
    def agregar_actividad(self):
       
        self.validarActividad()
        self.validarHora()
        self.validarArchivos()
        
        fecha_actividad = self.seguimiento_estudiante.fecha_actividad.date().toString("yyyy-MM-dd")
        hora_actividad = self.seguimiento_estudiante.horas_spinx.value()
        lista_actividades = self.seguimiento_estudiante.actividades_plain.toPlainText()
        observacion = self.seguimiento_estudiante.observacion_plain.toPlainText()
        
        if self.campos_validados():
            if self.modo != 'nuevo':

                query = 'UPDATE seguimiento SET fecha_actividad=%s, horas_actividad=%s, actividades=%s, observacion=%s'
                params = [fecha_actividad, hora_actividad, lista_actividades, observacion]
                
                if self.archivo_foto is not None:
                    query += ', archivo_foto=%s'
                    params.append(self.archivo_foto)
                
                # Verificar si el archivo de actividad ha cambiado
                if self.archivo_actividad is not None:
                    query += ', archivo_actividad=%s, tipo_archivo_actividad=%s'
                    params.append(self.archivo_actividad)
                    params.append(self.tipo_archivo)
                
                query += ' WHERE id=%s'
                params.append(self.id_actividad)
                
                self.conec_base.updateDatos(query, tuple(params))
                QMessageBox.information(self, "Mensaje", "Los datos se han actualizado correctamente.")
            else:
                self.conec_base.setDatosProcess('InsertarSeguimiento', (self.id_estudiante_vinculado, fecha_actividad, hora_actividad,
                                                    lista_actividades, self.archivo_foto, self.archivo_actividad, self.tipo_archivo,
                                                    observacion, fecha_actividad))
                QMessageBox.information(self, "Mensaje", "Los datos se han validado correctamente y se han enviado a la base de datos.")
                
            self.parent.raizOpacidad.close()
            self.close()
            self.parent.abrir_ventana_seguimiento_tutor()
            self.parent.llenar_estudiantes_seguimientos_tutor()
                
    def llenar_actividad(self, id_actividad):
    
        respuesta = self.conec_base.getDatos_condicion('SELECT * FROM seguimiento WHERE id = %s', (id_actividad,))
        
        if(respuesta):
            respuesta = respuesta[0]
            
            self.seguimiento_estudiante.fecha_actividad.setDate(respuesta[2])
            self.seguimiento_estudiante.horas_spinx.setValue(respuesta[3])
            self.seguimiento_estudiante.actividades_plain.setPlainText(respuesta[4])
            self.seguimiento_estudiante.observacion_plain.setPlainText(respuesta[8])
            
            self.archivo_foto = respuesta[5]
            if(self.archivo_foto != None):
                self.seguimiento_estudiante.lbl_nombre_archivo_seleccionado.setText('Descargar foto ->')
                self.seguimiento_estudiante.btn_descargar_foto.show()
            
            self.archivo_actividad = respuesta[6]
            self.tipo_archivo = respuesta[7] 
            if(self.archivo_actividad!= None):
                self.seguimiento_estudiante.lbl_nombre_archivo_seleccionado_2.setText(f'Descargar archivo {self.tipo_archivo} ->')
                self.seguimiento_estudiante.btn_descargar_archivo.show()
                
    def descargar_archivo(self):
        if self.archivo_actividad:
            opciones = QFileDialog.Options()
            extension = self.tipo_archivo.lower()
            
            if extension == 'pdf':
                filtro_archivos = "Archivos PDF (*.pdf)"
                default_filename = "archivo_actividad.pdf"
            elif extension in ['word', 'doc', 'docx']:
                filtro_archivos = "Archivos Word (*.doc *.docx)"
                default_filename = "archivo_actividad.docx"
            elif extension in ['excel', 'xls', 'xlsx']:
                filtro_archivos = "Archivos Excel (*.xls *.xlsx)"
                default_filename = "archivo_actividad.xlsx"
            elif extension in ['ppt', 'pptx']:
                filtro_archivos = "Archivos PowerPoint (*.ppt *.pptx)"
                default_filename = "archivo_actividad.pptx"
            else:
                filtro_archivos = "Todos los archivos (*)"
                default_filename = "archivo_actividad"
            
            archivo, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar archivo",
                default_filename,
                filtro_archivos,
                options=opciones
            )
            
            if archivo:
                print(f"Tamaño del archivo a descargar: {len(self.archivo_actividad)} bytes")
                
                QDesktopServices.openUrl(QUrl.fromLocalFile(archivo))
                
                with open(archivo, 'wb') as file:
                    file.write(self.archivo_actividad)
                    
                QMessageBox.information(self, "Éxito", "El archivo se ha descargado correctamente.")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay ningún archivo para descargar.")
            
    def descargar_foto(self):
        if self.archivo_foto:

            extension = imghdr.what(None, h=self.archivo_foto)
            
            if extension is None:
                QMessageBox.warning(self, "Error", "El formato de la foto no se pudo determinar.")
                return
            
            default_filename = f"foto.{extension}"
            
            opciones = QFileDialog.Options()
            filtro_archivos = "Imágenes (*.jpg *.jpeg *.png);;Todos los archivos (*)"
            
            archivo, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar foto",
                default_filename,
                filtro_archivos,
                options=opciones
            )
            
            if archivo:
                
                QDesktopServices.openUrl(QUrl.fromLocalFile(archivo))
                
                with open(archivo, 'wb') as file:
                    file.write(self.archivo_foto)
                    
                QMessageBox.information(self, "Éxito", "La foto se ha descargado correctamente.")
            else:
                QMessageBox.warning(self, "Cancelado", "No se ha seleccionado una ubicación para guardar la foto.")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay ninguna foto para descargar.")


    def ventanaconfiguracion(self):
            
        fecha_actual = QtCore.QDate.currentDate()
        self.seguimiento_estudiante.fecha_actividad.setDate(fecha_actual)