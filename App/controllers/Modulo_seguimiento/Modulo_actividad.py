from PySide2 import QtWidgets , QtCore , QtGui
from controllers.Modulo_seguimiento.funcion_seguimiento import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad
from PySide2.QtCore import QFileInfo
from PySide2.QtWidgets import QMessageBox, QFileDialog


import re, os
from PIL import Image
from datetime import datetime

from db.Modulo_base import BaseDatos

from views.ui_formulario_seguimiento_estudiante import Ui_FormularioSeguimientoEstudiante


class FormularioSeguimientoEstudiante(QtWidgets.QDialog):

    def __init__(self, parent=None, id_actividad=None, nombre_estudiante=None):
        
        super(FormularioSeguimientoEstudiante, self).__init__()
        self.seguimiento_estudiante = Ui_FormularioSeguimientoEstudiante()
        self.seguimiento_estudiante.setupUi(self)

        # conexion con la bd
        self.conec_base = BaseDatos()
    
        self.parent = parent
        self.id_actividad = id_actividad
        self.nombre_estudiante = nombre_estudiante 
        self.offset = 0
        self.limit = 4
        
        self.archivo_actividad = None
        self.archivo_foto = None
        self.tipo_archivo = ''
        self.tipo_archivo_foto = ''
        

        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.seguimiento_estudiante.btn_closeedit.clicked.connect(lambda: self.cerrar_ui_seguimientoadmin())
        
        
        self.seguimiento_estudiante.btn_subir_archivo.clicked.connect(lambda: self.subir_archivo())
        self.seguimiento_estudiante.btn_subir_fotos.clicked.connect(lambda: self.subir_foto())
    
    
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
                # Obtener la extensión del archivo
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
                    
            self.seguimiento_estudiante.lbl_nombre_archivo_seleccionado.setText(QFileInfo(archivo).fileName())
            
            QMessageBox.information(self, "Éxito", f"La foto se ha cargado correctamente. Tipo de archivo: {self.tipo_archivo_foto}.")
        else:
            QMessageBox.information(self, "Cancelado", "No se ha seleccionado ninguna foto.")
            
            
    