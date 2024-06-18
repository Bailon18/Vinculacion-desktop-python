
from sys import version
import os
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import QFileInfo
from PySide2.QtWidgets import QMessageBox, QFileDialog

from datetime import datetime, timedelta

from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_tutores import Ui_FormularioTutor

from db.Modulo_base import BaseDatos

class TutoresAdmin(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', tutor_id =  None):

        super(TutoresAdmin, self).__init__()
        
        self.venTutores = Ui_FormularioTutor()
        self.venTutores.setupUi(self)
        self.control_base = BaseDatos()
        

        self.parent = parent
        self.modo = modo
        
        self.identificacion_actual = ''
        self.correo_actual = ''
        self.telefono_actual = ''
        self.archivo_cv = None
        self.nombretutor = ''
        
    
        if(self.modo != 'nuevo'):
            self.tutor_id = tutor_id
            self.venTutores.btn_agregar_tutor.setText('Actualizar')
            self.venTutores.lbl_titulo_ventana.setText('Editar Tutor')
            self.venTutores.btn_subir_cv.setText('Actualizar cv de PDF')
            self.llenado_datos_tutor(int(self.tutor_id))
        else:
            self.venTutores.btn_descargar_archivo.hide()


        self.STYLE_ERROR = "color: #D32F2F; font-family: Roboto; font-style: normal; font-weight: bold; font-size: 12px; visibility: visible;"
        self.STYLE_VALID = "border: 2px solid green;"
        self.STYLE_INVALID = "border: 2px solid red;"
        
        
        self.venTutores.line_nombres.textChanged.connect(self.validar_nombres)
        self.venTutores.line_apellidos.textChanged.connect(self.validar_apellidos)
        self.venTutores.line_identificacion.textChanged.connect(self.validar_identificacion)
        self.venTutores.line_correo.textChanged.connect(self.validar_correo)
        self.venTutores.line_telefono.textChanged.connect(self.validar_telefono)
        self.venTutores.line_direccion.textChanged.connect(self.validar_direccion)
        self.venTutores.date_fechaNacimiento.dateChanged.connect(self.validar_fecha_nacimiento)
        self.venTutores.line_contrasena.textChanged.connect(self.validar_contrasena)

        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.venTutores.btn_close.clicked.connect(lambda: self.cerrar_ventana())
        self.venTutores.btn_agregar_tutor.clicked.connect(lambda: self.accion_boton_guardar())
        self.venTutores.btn_subir_cv.clicked.connect(lambda: self.subir_cv())
        self.venTutores.btn_descargar_archivo.clicked.connect(lambda: self.descargar_archivo())
        self.venTutores.cancelButton.clicked.connect(lambda: self.cerrar_ventana())

 
        
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

    def consultar_existencia_identificacion(self, identificacion):
        if identificacion != self.identificacion_actual:
            consulta = "SELECT COUNT(*) FROM tutores WHERE nro_identificacion = %s"
            respuesta = self.control_base.getDatos_condicion(consulta, (identificacion,))
            return respuesta[0][0] if respuesta else 0
        else:
            return 0
        
    def consultar_existencia_telefono(self, telefono):
        if telefono != self.telefono_actual:
            consulta = "SELECT COUNT(*) FROM tutores WHERE telefono = %s"
            respuesta = self.control_base.getDatos_condicion(consulta, (telefono,))
            return respuesta[0][0] if respuesta else 0
        else:
            return 0

    def consultar_existencia_correo(self, correo):
        
        print('correo ', correo)
        print('correo_actual ', self.correo_actual)
        if correo != self.correo_actual:
            consulta = "SELECT COUNT(*) FROM tutores WHERE correo = %s"
            respuesta = self.control_base.getDatos_condicion(consulta, (correo,))
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
    
    def es_valido_contrasena(self, contrasena):
        contrasena_stripped = contrasena.strip()
        if not contrasena_stripped:
            return "Campo vacío"
        elif len(contrasena_stripped) <= 5:
            return "Debe tener más de 5 caracteres."
        return ""

    def es_mayor_de_edad(self, fecha_nacimiento):
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            fecha_actual = datetime.now()
            edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            if edad < 18:
                return "Debe ser mayor de edad."
            return ""
        except ValueError:
            return "Formato de fecha inválido. Utilice el formato YYYY-MM-DD."
        
    def validar_nombres(self):
        nombres = self.venTutores.line_nombres.text().strip()
        respuesta = self.es_texto_valido(nombres)
        if respuesta:
            self.venTutores.line_nombres.setStyleSheet(self.STYLE_INVALID)
            self.venTutores.errorNombres.setText(respuesta)
            self.venTutores.errorNombres.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venTutores.line_nombres.setStyleSheet(self.STYLE_VALID)
            self.venTutores.errorNombres.setStyleSheet("")
            self.venTutores.errorNombres.setText("")

    def validar_apellidos(self):
        apellidos = self.venTutores.line_apellidos.text().strip()
        respuesta = self.es_texto_valido(apellidos)
        if respuesta:
            self.venTutores.line_apellidos.setStyleSheet(self.STYLE_INVALID)
            self.venTutores.errorApellidos.setText(respuesta)
            self.venTutores.errorApellidos.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venTutores.line_apellidos.setStyleSheet(self.STYLE_VALID)
            self.venTutores.errorApellidos.setStyleSheet("")
            self.venTutores.errorApellidos.setText("")

    def validar_identificacion(self):
        numero_identificacion = self.venTutores.line_identificacion.text().strip()
        respuesta_validacion = self.es_identificacion_valida(numero_identificacion)
        if respuesta_validacion:
            self.venTutores.line_identificacion.setStyleSheet(self.STYLE_INVALID)
            self.venTutores.errorIdentificacion.setText(respuesta_validacion)
            self.venTutores.errorIdentificacion.setStyleSheet(self.STYLE_ERROR)
        else:
            respuesta_bd = self.consultar_existencia_identificacion(numero_identificacion)
            if respuesta_bd:
                self.venTutores.line_identificacion.setStyleSheet(self.STYLE_INVALID)
                self.venTutores.errorIdentificacion.setText("Cedula ya existe.")
                self.venTutores.errorIdentificacion.setStyleSheet(self.STYLE_ERROR)
            else:
                self.venTutores.line_identificacion.setStyleSheet(self.STYLE_VALID)
                self.venTutores.errorIdentificacion.setStyleSheet("")
                self.venTutores.errorIdentificacion.setText("")

    def validar_correo(self):
        correo = self.venTutores.line_correo.text().strip()
        if not correo or not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            self.venTutores.line_correo.setStyleSheet(self.STYLE_INVALID)
            self.venTutores.errorCorreo.setText("Correo electrónico inválido")
            self.venTutores.errorCorreo.setStyleSheet(self.STYLE_ERROR)
            return
        respuesta = self.consultar_existencia_correo(correo)
        if respuesta:
            self.venTutores.line_correo.setStyleSheet(self.STYLE_INVALID)
            self.venTutores.errorCorreo.setText("Correo ya existe.")
            self.venTutores.errorCorreo.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venTutores.line_correo.setStyleSheet(self.STYLE_VALID)
            self.venTutores.errorCorreo.setStyleSheet("")
            self.venTutores.errorCorreo.setText("")
            
    def validar_telefono(self):
        telefono = self.venTutores.line_telefono.text().strip()
        respuesta_validacion = self.es_identificacion_valida(telefono)
        if respuesta_validacion:
            self.venTutores.line_telefono.setStyleSheet(self.STYLE_INVALID)
            self.venTutores.errorTelefono.setText(respuesta_validacion)
            self.venTutores.errorTelefono.setStyleSheet(self.STYLE_ERROR)
        else:
            respuesta_bd = self.consultar_existencia_telefono(telefono)
            if respuesta_bd:
                self.venTutores.line_telefono.setStyleSheet(self.STYLE_INVALID)
                self.venTutores.errorTelefono.setText("Teléfono ya existe.")
                self.venTutores.errorTelefono.setStyleSheet(self.STYLE_ERROR)
            else:
                self.venTutores.line_telefono.setStyleSheet(self.STYLE_VALID)
                self.venTutores.errorTelefono.setStyleSheet("")
                self.venTutores.errorTelefono.setText("")

    def validar_direccion(self):
        direccion = self.venTutores.line_direccion.text().strip()
        if not direccion:
            self.venTutores.line_direccion.setStyleSheet(self.STYLE_INVALID)
            self.venTutores.errorDireccion.setText("Dirección es obligatoria")
            self.venTutores.errorDireccion.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venTutores.line_direccion.setStyleSheet(self.STYLE_VALID)
            self.venTutores.errorDireccion.setStyleSheet("")
            self.venTutores.errorDireccion.setText("")

    def validar_fecha_nacimiento(self):
        fecha_nacimiento = self.venTutores.date_fechaNacimiento.date().toString("yyyy-MM-dd")
        respuesta = self.es_mayor_de_edad(fecha_nacimiento)
        if respuesta:
            self.venTutores.date_fechaNacimiento.setStyleSheet(self.STYLE_INVALID)
            self.venTutores.errorFechaNacimiento.setText(respuesta)
            self.venTutores.errorFechaNacimiento.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venTutores.date_fechaNacimiento.setStyleSheet(self.STYLE_VALID)
            self.venTutores.errorFechaNacimiento.setStyleSheet("")   
            self.venTutores.errorFechaNacimiento.setText("")  
            
    def validar_contrasena(self):
        contrasena = self.venTutores.line_contrasena.text().strip()
        
        respuesta = self.es_valido_contrasena(contrasena)
        if respuesta:
            self.venTutores.line_contrasena.setStyleSheet(self.STYLE_INVALID)
            self.venTutores.errorContrasena.setText(respuesta)
            self.venTutores.errorContrasena.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venTutores.line_contrasena.setStyleSheet(self.STYLE_VALID)
            self.venTutores.errorContrasena.setStyleSheet("")
            self.venTutores.errorContrasena.setText("")

    def campos_validados(self):
        return (self.venTutores.line_nombres.styleSheet() == self.STYLE_VALID and
                self.venTutores.line_apellidos.styleSheet() == self.STYLE_VALID and
                self.venTutores.line_identificacion.styleSheet() == self.STYLE_VALID and
                self.venTutores.line_correo.styleSheet() == self.STYLE_VALID and
                self.venTutores.line_telefono.styleSheet() == self.STYLE_VALID and
                self.venTutores.line_direccion.styleSheet() == self.STYLE_VALID and
                self.venTutores.line_contrasena.styleSheet() == self.STYLE_VALID and
                self.venTutores.date_fechaNacimiento.styleSheet() == self.STYLE_VALID)


    def accion_boton_guardar(self):
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        

        nombres = self.venTutores.line_nombres.text().strip()
        apellidos = self.venTutores.line_apellidos.text().strip()
        tipo_identificacion = self.venTutores.cbo_tipoIdentificacion.currentText().strip()
        numero_identifiacion = self.venTutores.line_identificacion.text().strip()
        contrasena = self.venTutores.line_contrasena.text().strip()
        fecha_nacimiento = self.venTutores.date_fechaNacimiento.date().toString("yyyy-MM-dd")
        genero_texto = self.venTutores.cbo_genero.currentText()
        genero = 'M' if genero_texto == 'Masculino' else 'F' if genero_texto == 'Femenino' else 'Otro'
        correo = self.venTutores.line_correo.text()
        telefono = self.venTutores.line_telefono.text()
        direccion = self.venTutores.line_direccion.text()
        carrera = self.venTutores.cbo_carrera.currentText()

        self.validar_nombres()
        self.validar_apellidos()
        self.validar_identificacion()
        self.validar_correo()
        self.validar_telefono()
        self.validar_direccion()
        self.validar_fecha_nacimiento()
        self.validar_contrasena()
        
        if self.campos_validados():
            try:
                if self.modo != 'nuevo':
                    if self.archivo_cv is not None:
                        self.control_base.setDatosProcess('actualizar_tutor', (self.tutor_id, nombres, apellidos, tipo_identificacion,
                                                                                numero_identifiacion, fecha_nacimiento,
                                                                                genero, correo, telefono, direccion,
                                                                                carrera, contrasena, self.archivo_cv))
                    else:
                        self.control_base.setDatosProcess('actualizar_tutor_sin_archivo', (self.tutor_id, nombres, apellidos, tipo_identificacion,
                                                                                            numero_identifiacion, fecha_nacimiento,
                                                                                            genero, correo, telefono, direccion,
                                                                                            carrera, contrasena))
                    QMessageBox.information(self, "Mensaje", "Los datos se han actualizado correctamente en la base de datos.")
                else:
                    self.control_base.setDatosProcess('agregar_tutor', (nombres, apellidos, tipo_identificacion,
                                                                        numero_identifiacion, fecha_nacimiento,
                                                                        genero, correo, telefono, direccion,
                                                                        carrera,contrasena , self.archivo_cv))
                    QMessageBox.information(self, "Mensaje", "Los datos se han validado correctamente y se han enviado a la base de datos.")

                self.parent.raizOpacidad.close()
                self.close()
                self.parent.llenarTabla('listar_estudiantes', 'estudiantes', self.parent.venPri.tabla_estudiantes)
                self.parent.actualizarInfoPaginacion('estudiantes', self.parent.venPri.lbl_pagina_estudiantes)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ha ocurrido un error al guardar los datos en la base de datos: {str(e)}")


    def subir_cv(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo",
            "",
            "Archivos PDF (*.pdf)",
            options=opciones
        )
        
        if archivo:
            with open(archivo, 'rb') as file:
                self.archivo_cv = file.read()
                
            self.venTutores.lbl_nombre_archivo_seleccionado.setText(QFileInfo(archivo).fileName())
            
            QMessageBox.information(self, "Éxito", "El archivo se ha cargado correctamente.")
        else:
            QMessageBox.information(self, "Cancelado", "No se ha seleccionado ningún archivo.")



    def llenado_datos_tutor(self, tutor_id):
        
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        respuesta = self.control_base.getDatosProcess_condicion('buscar_tutor_por_id', (tutor_id,))

        if respuesta:
            tutor = respuesta[0][0]
            
            self.venTutores.line_nombres.setText(tutor[1])
            self.venTutores.line_apellidos.setText(tutor[2])
            self.venTutores.cbo_tipoIdentificacion.setCurrentText(tutor[3])
            self.venTutores.line_identificacion.setText(tutor[4])
            self.venTutores.line_contrasena.setText(tutor[8])
            self.venTutores.date_fechaNacimiento.setDate(tutor[5])
            
            if tutor[6] == 'M':
                self.venTutores.cbo_genero.setCurrentText('Masculino')
            elif tutor[6] == 'F':
                self.venTutores.cbo_genero.setCurrentText('Femenino')
            else:
                self.venTutores.cbo_genero.setCurrentText('Otro')
            
            self.venTutores.line_correo.setText(tutor[7])
            self.venTutores.line_telefono.setText(tutor[9])
            self.venTutores.line_direccion.setText(tutor[10])
            # Asignar carrera
            self.venTutores.cbo_carrera.setCurrentText(tutor[11])
            
            self.identificacion_actual = tutor[4]
            self.correo_actual = tutor[7]
            print('self.correo_actual ', self.correo_actual)
            self.telefono_actual = tutor[9]
            
            # Asignar nombre de archivo si existe
            if tutor[12]:
            
                self.archivo_cv = tutor[12]
                self.nombretutor = tutor[1] + ' ' + tutor[2]
                self.venTutores.lbl_nombre_archivo_seleccionado.setText("Descargar archivo -->")
           
            else:
                self.venTutores.lbl_nombre_archivo_seleccionado.setText("Ningún archivo seleccionado")
            
        else:
            QMessageBox.warning(None, "Error", "No se encontraron datos para el tutor con el ID proporcionado.")

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
                    # Si es un archivo PDF, abrir automáticamente
                    import os
                    os.startfile(archivo)
                    
                QMessageBox.information(self, "Éxito", "El archivo se ha descargado correctamente.")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay ningún archivo para descargar.")