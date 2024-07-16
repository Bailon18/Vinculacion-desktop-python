
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QMessageBox, QFileDialog
import imghdr
import os
from PySide2.QtCore import QUrl
from PySide2.QtGui import QDesktopServices


from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad
from PySide2.QtCore import QFileInfo

from views.ui_formulario_instituciones import Ui_FormularioInstitucion

from db.Modulo_base import BaseDatos

class InstitucionesAdmin(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', institucion_id =  None):

        super(InstitucionesAdmin, self).__init__()
        
        self.venInstituciones = Ui_FormularioInstitucion()
        self.venInstituciones.setupUi(self)
        self.control_base = BaseDatos()
        

        self.parent = parent
        self.modo = modo
        self.telefono_actual = ''
        self.nombre_actual = ''
        
        self.archivo_convenio = None
        self.tipo_archivo = ''
        self.venInstituciones.btn_descargar_archivo.hide()
    
        if(self.modo != 'nuevo'):
            self.institucion_id = institucion_id
            self.venInstituciones.btn_guardar_institiucion.setText('Actualizar')
            self.venInstituciones.lbl_titulo_ventana.setText('Editar Institución')
            self.llenado_datos_institucion(int(self.institucion_id))

        self.STYLE_ERROR = "color: #D32F2F; font-family: Roboto; font-style: normal; font-weight: bold; font-size: 12px; visibility: visible;"
        self.STYLE_VALID = "border: 2px solid green;"
        self.STYLE_INVALID = "border: 2px solid red;"


        self.venInstituciones.line_nombre_institucion.textChanged.connect(self.validar_nombre)
        self.venInstituciones.line_telefono.textChanged.connect(self.validar_telefono)

        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.venInstituciones.btn_close.clicked.connect(lambda: self.cerrar_ventana())
        self.venInstituciones.btn_guardar_institiucion.clicked.connect(lambda: self.accion_boton_guardar())
        self.venInstituciones.cancelButton.clicked.connect(lambda: self.cerrar_ventana())
        self.venInstituciones.btn_subir_cv.clicked.connect(lambda: self.subir_convenio())
        self.venInstituciones.btn_descargar_archivo.clicked.connect(lambda: self.descargar_archivo())
        
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

    def es_texto_valido(self, texto):
        if not texto.strip():
            return "Campo vacío"
        elif not texto.replace(" ", "").isalpha():
            return "No debe contener números"
        return ""

    def consultar_existencia_telefono(self, telefono):
        if telefono != self.telefono_actual:
            consulta = "SELECT COUNT(*) FROM institucion WHERE telefono = %s"
            respuesta = self.control_base.getDatos_condicion(consulta, (telefono,))
            return respuesta[0][0] if respuesta else 0
        else:
            return 0
        
    def es_identificacion_valida(self, identificacion):
        identificacion_stripped = identificacion.strip()
        if not identificacion_stripped:
            return "Campo vacío"
        elif not identificacion_stripped.isdigit():
            return "Debe contener solo números."
        elif len(identificacion_stripped) != 10:
            return "Debe tener 10 dígitos."
        return ""
        
    def consultar_existencia_nombre(self, nombre):
        if nombre != self.nombre_actual:
            consulta = "SELECT COUNT(*) FROM institucion WHERE LOWER(nombre) = LOWER(%s)"
            respuesta = self.control_base.getDatos_condicion(consulta, (nombre,))
            return respuesta[0][0] if respuesta else 0
        else:
            return 0


    def validar_nombre(self):
        nombre = self.venInstituciones.line_nombre_institucion.text()
        respuesta_validacion = self.es_texto_valido(nombre)
        if respuesta_validacion:
            self.venInstituciones.line_nombre_institucion.setStyleSheet(self.STYLE_INVALID)
            self.venInstituciones.errorNombre.setText(respuesta_validacion)
            self.venInstituciones.errorNombre.setStyleSheet(self.STYLE_ERROR)
        else:
            respuesta_bd = self.consultar_existencia_nombre(nombre)
            if respuesta_bd:
                self.venInstituciones.line_nombre_institucion.setStyleSheet(self.STYLE_INVALID)
                self.venInstituciones.errorNombre.setText("Nombre instituto ya existe.")
                self.venInstituciones.errorNombre.setStyleSheet(self.STYLE_ERROR)
            else:
                self.venInstituciones.line_nombre_institucion.setStyleSheet(self.STYLE_VALID)
                self.venInstituciones.errorNombre.setStyleSheet("")
                self.venInstituciones.errorNombre.setText("")
                
    def validar_telefono(self):
        telefono = self.venInstituciones.line_telefono.text()
        respuesta_validacion = self.es_identificacion_valida(telefono)
        if respuesta_validacion:
            self.venInstituciones.line_telefono.setStyleSheet(self.STYLE_INVALID)
            self.venInstituciones.errorTelefono.setText(respuesta_validacion)
            self.venInstituciones.errorTelefono.setStyleSheet(self.STYLE_ERROR)
        else:
            respuesta_bd = self.consultar_existencia_telefono(telefono)
            if respuesta_bd:
                self.venInstituciones.line_telefono.setStyleSheet(self.STYLE_INVALID)
                self.venInstituciones.errorTelefono.setText("Teléfono ya existe.")
                self.venInstituciones.errorTelefono.setStyleSheet(self.STYLE_ERROR)
            else:
                self.venInstituciones.line_telefono.setStyleSheet(self.STYLE_VALID)
                self.venInstituciones.errorTelefono.setStyleSheet("")
                self.venInstituciones.errorTelefono.setText("")

    def campos_validados(self):
        return (self.venInstituciones.line_nombre_institucion.styleSheet() == self.STYLE_VALID and
                self.venInstituciones.line_telefono.styleSheet() == self.STYLE_VALID)

    def accion_boton_guardar(self):
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        nombre_proyecto = self.venInstituciones.line_nombre_institucion.text().strip()
        telefono = self.venInstituciones.line_telefono.text().strip()
        tipo_institucion = self.venInstituciones.cbo_tipoIdentificacion.currentText()
        estado = True if self.venInstituciones.cbox_estado_intitucion.currentText() == 'Activo' else False
        direccion = self.venInstituciones.line_direccion_institucion.text().strip()

        self.validar_nombre()
        self.validar_telefono()

        if self.campos_validados():
            try:
                if self.modo != 'nuevo':

                    self.control_base.setDatosProcess('actualizar_institucion', (self.institucion_id, nombre_proyecto, tipo_institucion, estado, direccion, telefono, self.archivo_convenio, self.tipo_archivo ))

                    QMessageBox.information(self, "Mensaje", "Los datos se han actualizado correctamente en la base de datos.")
                else:
                    self.control_base.setDatosProcess('agregar_institucion', ( nombre_proyecto, tipo_institucion, estado, direccion, telefono, self.archivo_convenio, self.tipo_archivo))
                    
                    QMessageBox.information(self, "Mensaje", "Los datos se han validado correctamente y se han enviado a la base de datos.")

                self.parent.raizOpacidad.close()
                self.close()
                self.parent.offset = 0
                self.parent.llenarTabla('listar_institucion', 'institucion', self.parent.venPri.tabla_institucion)
                self.parent.venPri.check_estado_insti.setChecked(False)
                self.parent.actualizarInfoPaginacion('institucion', self.parent.venPri.lbl_pagina_instituto, True)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ha ocurrido un error al guardar los datos en la base de datos: {str(e)}")


    def llenado_datos_institucion(self, proyecto_id):
        
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        respuesta = self.control_base.getDatosProcess_condicion('buscar_institucion_por_id', (proyecto_id,))
        if(respuesta):
            respuesta = respuesta[0][0]
            self.venInstituciones.line_nombre_institucion.setText(respuesta[0])
            self.venInstituciones.cbo_tipoIdentificacion.setCurrentText(respuesta[1])
            estado = 'Activo' if respuesta[2] == True else 'Inactivo'
            self.venInstituciones.cbox_estado_intitucion.setCurrentText(estado)
            self.venInstituciones.line_direccion_institucion.setText(respuesta[3])
            self.venInstituciones.line_telefono.setText(respuesta[4])
            self.nombre_actual = respuesta[0]
            self.telefono_actual = respuesta[4]
            
            self.archivo_convenio = respuesta[5]
            self.tipo_archivo = respuesta[6] 
            if(self.archivo_convenio!= None):
                self.venInstituciones.lbl_nombre_archivo_seleccionado.setText(f'Descargar archivo {self.tipo_archivo} ->')
                self.venInstituciones.btn_descargar_archivo.show()
  

    def subir_convenio(self):
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
                self.archivo_convenio = file.read()
  
                extension = QFileInfo(archivo).suffix().lower()

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
               
                QDesktopServices.openUrl(QUrl.fromLocalFile(archivo))
            self.venInstituciones.lbl_nombre_archivo_seleccionado.setText(QFileInfo(archivo).fileName())
            
            
            QMessageBox.information(self, "Éxito", "El archivo se ha cargado correctamente.")
        else:
            QMessageBox.information(self, "Cancelado", "No se ha seleccionado ningún archivo.")
    
    def descargar_archivo(self):
        if self.archivo_convenio:
            opciones = QFileDialog.Options()
            extension = self.tipo_archivo.lower()
            
            if extension == 'pdf':
                filtro_archivos = "Archivos PDF (*.pdf)"
                default_filename = "archivo_convenio.pdf"
            elif extension in ['word', 'doc', 'docx']:
                filtro_archivos = "Archivos Word (*.doc *.docx)"
                default_filename = "archivo_convenio.docx"
            elif extension in ['excel', 'xls', 'xlsx']:
                filtro_archivos = "Archivos Excel (*.xls *.xlsx)"
                default_filename = "archivo_convenio.xlsx"
            elif extension in ['ppt', 'pptx']:
                filtro_archivos = "Archivos PowerPoint (*.ppt *.pptx)"
                default_filename = "archivo_convenio.pptx"
            else:
                filtro_archivos = "Todos los archivos (*)"
                default_filename = "archivo_convenio"
            
            archivo, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar archivo",
                default_filename,
                filtro_archivos,
                options=opciones
            )
            
            if archivo:
                try:
                    with open(archivo, 'wb') as file:
                        file.write(self.archivo_convenio)
                    
                    # Abrir vista previa del archivo
                    if os.path.isfile(archivo):
                        QDesktopServices.openUrl(QUrl.fromLocalFile(archivo))
                    else:
                        QMessageBox.warning(self, "Advertencia", "No se pudo abrir el archivo guardado.")
                    
                    QMessageBox.information(self, "Éxito", "El archivo se ha descargado correctamente.")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Ha ocurrido un error al guardar el archivo: {str(e)}")
            else:
                QMessageBox.warning(self, "Advertencia", "No se ha especificado una ruta para guardar el archivo.")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay ningún archivo para descargar.")