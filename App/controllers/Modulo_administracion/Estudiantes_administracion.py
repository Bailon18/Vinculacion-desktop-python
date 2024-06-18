
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox
from datetime import datetime, timedelta


from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_estudiantes import Ui_FormularioEstudiante

from db.Modulo_base import BaseDatos

class EstudiantesAdmin(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', estudiante_id =  None):

        super(EstudiantesAdmin, self).__init__()
        
        self.venEstudiante = Ui_FormularioEstudiante()
        self.venEstudiante.setupUi(self)
        self.control_base = BaseDatos()
        

        self.parent = parent
        self.modo = modo
        
        self.identificacion_actual = ''
        self.correo_actual = ''
        self.telefono_actual = ''
        
        self.data_configuracion()
        
    
        if(self.modo != 'nuevo'):
            self.estudiante_id = estudiante_id
            self.venEstudiante.btn_agregar_estudiantes.setText('Actualizar')
            self.venEstudiante.lbl_titulo_ventana.setText('Editar Estudiante')
            self.llenado_datos_estudiante(int(self.estudiante_id))
        
        self.STYLE_ERROR = "color: #D32F2F; font-family: Roboto; font-style: normal; font-weight: bold; font-size: 12px; visibility: visible;"
        self.STYLE_VALID = "border: 2px solid green;"
        self.STYLE_INVALID = "border: 2px solid red;"


        self.venEstudiante.line_nombres.textChanged.connect(self.validar_nombres)
        self.venEstudiante.line_apellidos.textChanged.connect(self.validar_apellidos)
        self.venEstudiante.line_identificacion.textChanged.connect(self.validar_identificacion)
        self.venEstudiante.line_correo.textChanged.connect(self.validar_correo)
        self.venEstudiante.line_telefono.textChanged.connect(self.validar_telefono)
        self.venEstudiante.line_direccion.textChanged.connect(self.validar_direccion)
        self.venEstudiante.date_fechaNacimiento.dateChanged.connect(self.validar_fecha_nacimiento)


        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.venEstudiante.btn_closeedit.clicked.connect(lambda: self.cerrar_ventana())
        self.venEstudiante.btn_agregar_estudiantes.clicked.connect(lambda: self.accion_boton_guardar())
        
    

        
        
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

    def data_configuracion(self):
        consulta = 'SELECT id, nombre FROM carrera'
        respuesta = self.control_base.getDatos(consulta)
        self.venEstudiante.cbo_carrera.clear()
        for id_carrera, nombre in respuesta:
            self.venEstudiante.cbo_carrera.addItem(nombre, id_carrera)

    def es_texto_valido(self, texto):
        if not texto.strip():
            return "Campo vacío"
        elif not texto.replace(" ", "").isalpha():
            return "No debe contener números"
        return ""

    def consultar_existencia_identificacion(self, identificacion):
        if identificacion != self.identificacion_actual:
            consulta = "SELECT COUNT(*) FROM estudiantes WHERE nro_identificacion = %s"
            respuesta = self.control_base.getDatos_condicion(consulta, (identificacion,))
            return respuesta[0][0] if respuesta else 0
        else:
            return 0

    def consultar_existencia_telefono(self, telefono):
        if telefono != self.telefono_actual:
            consulta = "SELECT COUNT(*) FROM estudiantes WHERE telefono = %s"
            respuesta = self.control_base.getDatos_condicion(consulta, (telefono,))
            return respuesta[0][0] if respuesta else 0
        else:
            return 0

    def consultar_existencia_correo(self, correo):
        
        print('correo ', correo)
        print('correo_actual ', self.correo_actual)
        if correo != self.correo_actual:
            consulta = "SELECT COUNT(*) FROM estudiantes WHERE correo = %s"
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
        nombres = self.venEstudiante.line_nombres.text().strip()
        respuesta = self.es_texto_valido(nombres)
        if respuesta:
            self.venEstudiante.line_nombres.setStyleSheet(self.STYLE_INVALID)
            self.venEstudiante.errorNombres.setText(respuesta)
            self.venEstudiante.errorNombres.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venEstudiante.line_nombres.setStyleSheet(self.STYLE_VALID)
            self.venEstudiante.errorNombres.setStyleSheet("")
            self.venEstudiante.errorNombres.setText("")

    def validar_apellidos(self):
        apellidos = self.venEstudiante.line_apellidos.text().strip()
        respuesta = self.es_texto_valido(apellidos)
        if respuesta:
            self.venEstudiante.line_apellidos.setStyleSheet(self.STYLE_INVALID)
            self.venEstudiante.errorApellidos.setText(respuesta)
            self.venEstudiante.errorApellidos.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venEstudiante.line_apellidos.setStyleSheet(self.STYLE_VALID)
            self.venEstudiante.errorApellidos.setStyleSheet("")
            self.venEstudiante.errorApellidos.setText("")

    def validar_identificacion(self):
        numero_identificacion = self.venEstudiante.line_identificacion.text().strip()
        respuesta_validacion = self.es_identificacion_valida(numero_identificacion)
        if respuesta_validacion:
            self.venEstudiante.line_identificacion.setStyleSheet(self.STYLE_INVALID)
            self.venEstudiante.errorIdentificacion.setText(respuesta_validacion)
            self.venEstudiante.errorIdentificacion.setStyleSheet(self.STYLE_ERROR)
        else:
            respuesta_bd = self.consultar_existencia_identificacion(numero_identificacion)
            if respuesta_bd:
                self.venEstudiante.line_identificacion.setStyleSheet(self.STYLE_INVALID)
                self.venEstudiante.errorIdentificacion.setText("Cedula ya existe.")
                self.venEstudiante.errorIdentificacion.setStyleSheet(self.STYLE_ERROR)
            else:
                self.venEstudiante.line_identificacion.setStyleSheet(self.STYLE_VALID)
                self.venEstudiante.errorIdentificacion.setStyleSheet("")
                self.venEstudiante.errorIdentificacion.setText("")

    def validar_correo(self):
        correo = self.venEstudiante.line_correo.text().strip()
        if not correo or not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            self.venEstudiante.line_correo.setStyleSheet(self.STYLE_INVALID)
            self.venEstudiante.errorCorreo.setText("Correo electrónico inválido")
            self.venEstudiante.errorCorreo.setStyleSheet(self.STYLE_ERROR)
            return
        respuesta = self.consultar_existencia_correo(correo)
        if respuesta:
            self.venEstudiante.line_correo.setStyleSheet(self.STYLE_INVALID)
            self.venEstudiante.errorCorreo.setText("Correo ya existe.")
            self.venEstudiante.errorCorreo.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venEstudiante.line_correo.setStyleSheet(self.STYLE_VALID)
            self.venEstudiante.errorCorreo.setStyleSheet("")
            self.venEstudiante.errorCorreo.setText("")
            
    def validar_telefono(self):
        telefono = self.venEstudiante.line_telefono.text().strip()
        respuesta_validacion = self.es_identificacion_valida(telefono)
        if respuesta_validacion:
            self.venEstudiante.line_telefono.setStyleSheet(self.STYLE_INVALID)
            self.venEstudiante.errorTelefono.setText(respuesta_validacion)
            self.venEstudiante.errorTelefono.setStyleSheet(self.STYLE_ERROR)
        else:
            respuesta_bd = self.consultar_existencia_telefono(telefono)
            if respuesta_bd:
                self.venEstudiante.line_telefono.setStyleSheet(self.STYLE_INVALID)
                self.venEstudiante.errorTelefono.setText("Teléfono ya existe.")
                self.venEstudiante.errorTelefono.setStyleSheet(self.STYLE_ERROR)
            else:
                self.venEstudiante.line_telefono.setStyleSheet(self.STYLE_VALID)
                self.venEstudiante.errorTelefono.setStyleSheet("")
                self.venEstudiante.errorTelefono.setText("")

    def validar_direccion(self):
        direccion = self.venEstudiante.line_direccion.text().strip()
        if not direccion:
            self.venEstudiante.line_direccion.setStyleSheet(self.STYLE_INVALID)
            self.venEstudiante.errorDireccion.setText("Dirección es obligatoria")
            self.venEstudiante.errorDireccion.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venEstudiante.line_direccion.setStyleSheet(self.STYLE_VALID)
            self.venEstudiante.errorDireccion.setStyleSheet("")
            self.venEstudiante.errorDireccion.setText("")

    def validar_fecha_nacimiento(self):
        fecha_nacimiento = self.venEstudiante.date_fechaNacimiento.date().toString("yyyy-MM-dd")
        respuesta = self.es_mayor_de_edad(fecha_nacimiento)
        if respuesta:
            self.venEstudiante.date_fechaNacimiento.setStyleSheet(self.STYLE_INVALID)
            self.venEstudiante.errorFechaNacimiento.setText(respuesta)
            self.venEstudiante.errorFechaNacimiento.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venEstudiante.date_fechaNacimiento.setStyleSheet(self.STYLE_VALID)
            self.venEstudiante.errorFechaNacimiento.setStyleSheet("")   
            self.venEstudiante.errorFechaNacimiento.setText("")   
        
    def campos_validados(self):
        return (self.venEstudiante.line_nombres.styleSheet() == self.STYLE_VALID and
                self.venEstudiante.line_apellidos.styleSheet() == self.STYLE_VALID and
                self.venEstudiante.line_identificacion.styleSheet() == self.STYLE_VALID and
                self.venEstudiante.line_correo.styleSheet() == self.STYLE_VALID and
                self.venEstudiante.line_telefono.styleSheet() == self.STYLE_VALID and
                self.venEstudiante.line_direccion.styleSheet() == self.STYLE_VALID and
                self.venEstudiante.date_fechaNacimiento.styleSheet() == self.STYLE_VALID)
        
    def accion_boton_guardar(self):
        
        if not self.control_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        nombres = self.venEstudiante.line_nombres.text().strip()
        apellidos = self.venEstudiante.line_apellidos.text().strip()
        tipo_identificacion = self.venEstudiante.cbo_tipoIdentificacion.currentText().strip()
        numero_identifiacion = self.venEstudiante.line_identificacion.text().strip()
        fecha_nacimiento = self.venEstudiante.date_fechaNacimiento.date().toString("yyyy-MM-dd")
        genero_texto = self.venEstudiante.cbo_genero.currentText()
        genero = 'M' if genero_texto == 'Masculino' else 'F' if genero_texto == 'Femenino' else 'Otro'
        correo = self.venEstudiante.line_correo.text()
        telefono = self.venEstudiante.line_telefono.text()
        direccion = self.venEstudiante.line_direccion.text()
        carrera_id = self.venEstudiante.cbo_carrera.currentData()

        self.validar_nombres()
        self.validar_apellidos()
        self.validar_identificacion()
        self.validar_correo()
        self.validar_telefono()
        self.validar_direccion()
        self.validar_fecha_nacimiento()

        if self.campos_validados():
            try:
                if self.modo != 'nuevo':
                    self.control_base.setDatosProcess('actualizar_estudiante', (self.estudiante_id, nombres, apellidos, tipo_identificacion,
                                                                                numero_identifiacion, fecha_nacimiento,
                                                                                genero, correo, telefono, direccion,
                                                                                carrera_id))
                    QMessageBox.information(self, "Mensaje", "Los datos se han actualizado correctamente en la base de datos.")
                else:
                    self.control_base.setDatosProcess('agregar_estudiante', (nombres, apellidos, tipo_identificacion,
                                                                            numero_identifiacion, fecha_nacimiento,
                                                                            genero, correo, telefono, direccion,
                                                                            carrera_id))
                    QMessageBox.information(self, "Mensaje", "Los datos se han validado correctamente y se han enviado a la base de datos.")

                self.parent.raizOpacidad.close()
                self.close()
                self.parent.llenarTabla('listar_estudiantes', 'estudiantes', self.parent.venPri.tabla_estudiantes)
                self.parent.actualizarInfoPaginacion('estudiantes', self.parent.venPri.lbl_pagina_estudiantes)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ha ocurrido un error al guardar los datos en la base de datos: {str(e)}")

  
    def llenado_datos_estudiante(self, estudiante_id):
        
        estudiante_data = self.control_base.getDatosProcess_condicion('buscar_estudiante_por_id', (estudiante_id, ))
        
        if estudiante_data:
            estudiante = estudiante_data[0][0] 
            self.venEstudiante.line_nombres.setText(estudiante[1])  
            self.venEstudiante.line_apellidos.setText(estudiante[2]) 
            self.venEstudiante.cbo_tipoIdentificacion.setCurrentText(estudiante[3]) 
            self.venEstudiante.line_identificacion.setText(estudiante[4])  
            self.venEstudiante.date_fechaNacimiento.setDate(estudiante[5])  
            if estudiante[6] == 'M':
                self.venEstudiante.cbo_genero.setCurrentText('Masculino') 
            elif estudiante[6] == 'F':
                self.venEstudiante.cbo_genero.setCurrentText('Femenino')  
            else:
                self.venEstudiante.cbo_genero.setCurrentText('Otro')  
            self.venEstudiante.line_correo.setText(estudiante[7]) 
            self.venEstudiante.line_telefono.setText(estudiante[8])  
            self.venEstudiante.line_direccion.setText(estudiante[9])  
            
            self.set_combobox_by_user_data(self.venEstudiante.cbo_carrera, estudiante[10])
            
            
            self.identificacion_actual = estudiante[4]
            self.correo_actual = estudiante[7]
            print('self.correo_actual ', self.correo_actual)
            self.telefono_actual = estudiante[8]
            
        else:
            print("No se encontraron datos para el estudiante con ID:", estudiante_id)
            
    def set_combobox_by_user_data(self, combobox, user_data):
        index = combobox.findData(user_data, role=Qt.UserRole) 
        if index != -1:
            combobox.setCurrentIndex(index)

        


    