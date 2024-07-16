
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox

import re

from datetime import datetime
from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_usuarios import Ui_FormularioUsuario

from db.Modulo_base import BaseDatos

class Perfil(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', dato = []):

        super(Perfil, self).__init__()
        self.venPerfil = Ui_FormularioUsuario()
        self.venPerfil.setupUi(self)
        self.control_base = BaseDatos()

        self.ventana_configuracion()

        self.parent = parent
        self.modo = modo
        self.dato = []

        
        self.correo_actual = ''
        self.identificacion_actual = ''

        if(modo != 'nuevo'):
            self.dato = dato
            self.usuario_id = self.dato[0]
            self.llenar_datos_usuarios(self.usuario_id)
            self.venPerfil.lbl_titulo_ventana.setText('Editar Perfil')
            self.venPerfil.btn_guardar.setText('Actualizar')
            self.venPerfil.lbl_usuariologeado.setText(self.dato[1])

        #     if(self.parent.args[0][2]  != 'Administrador'):
        #         self.venPerfil.admi.setEnabled(False)
        #         self.venPerfil.tutor.setEnabled(False)
                
        # if(self.parent.venPri.lbl_rol.text() != 'Administrador'):
        #     self.venPerfil.admi.setEnabled(False)
            # self.venPerfil.admi.setEnabled(False)
            
        

        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.venPerfil.btn_closeedit.clicked.connect(lambda: self.cerrar_ui_perfil())
        self.venPerfil.btn_guardar.clicked.connect(lambda: self.guardar_usuario())

        # if(self.modo != 'Nuevo'):
        #     self.venPerfil.lbl_titulo_ventana.setText('Editar Perfil')
        #     self.venPerfil.btn_guardar.setText('Actualizar')
        #     self.venPerfil.lbl_usuariologeado.setText(self.dato[1])
            
        #     self.llenar_datos_usuarios()

        #     if(self.parent.rol != 'Administrador'):
        #         self.venPerfil.admi.setEnabled(False)
        #         self.venPerfil.tutor.setEnabled(False)
                
        # if(self.parent.venPri.lbl_rol.text() != 'Administrador'):
        #     self.venPerfil.admi.setEnabled(False)
        #     self.venPerfil.admi.setEnabled(False)
            



        self.STYLE_ERROR = "color: #D32F2F; font-family: Roboto; font-style: normal; font-weight: bold; font-size: 12px; visibility: visible;"
        self.STYLE_VALID = "border: 2px solid green;"
        self.STYLE_INVALID = "border: 2px solid red;"
        
        self.venPerfil.line_nombre.textChanged.connect(self.validar_nombres)
        self.venPerfil.line_apeP.textChanged.connect(self.validar_apellidos)
        self.venPerfil.line_dni.textChanged.connect(self.validar_identificacion)
        self.venPerfil.line_correo.textChanged.connect(self.validar_correo)
        self.venPerfil.line_contrasena.textChanged.connect(self.validar_contrasena)
        

        

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass

    def cerrar_ui_perfil(self):
        self.parent.raizOpacidad.close()
        self.close()

    def ventana_configuracion(self):
        fecha_actual = QtCore.QDate.currentDate()
        
    def es_texto_valido(self, texto):
        if not texto.strip():
            return "Campo vacío"
        elif not texto.replace(" ", "").isalpha():
            return "No debe contener números"
        return ""

    def consultar_existencia_identificacion(self, identificacion):
        if identificacion != self.identificacion_actual:
            consulta = "SELECT COUNT(*) FROM usuarios WHERE identificacion = %s"
            respuesta = self.control_base.getDatos_condicion(consulta, (identificacion,))
            print('respuesta ', respuesta)
            return respuesta[0][0] if respuesta else 0
        else:
            return 0
        
    def consultar_existencia_correo(self, correo):
        
        if correo != self.correo_actual:
            consulta = "SELECT COUNT(*) FROM usuarios WHERE correo_electronico = %s"
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

    def validar_nombres(self):
        nombres = self.venPerfil.line_nombre.text().strip()
        respuesta = self.es_texto_valido(nombres)
        if respuesta:
            self.venPerfil.line_nombre.setStyleSheet(self.STYLE_INVALID)
            self.venPerfil.errorNombres.setText(respuesta)
            self.venPerfil.errorNombres.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venPerfil.line_nombre.setStyleSheet(self.STYLE_VALID)
            self.venPerfil.errorNombres.setStyleSheet("")
            self.venPerfil.errorNombres.setText("")

    def validar_apellidos(self):
        apellidos = self.venPerfil.line_apeP.text().strip()
        respuesta = self.es_texto_valido(apellidos)
        if respuesta:
            self.venPerfil.line_apeP.setStyleSheet(self.STYLE_INVALID)
            self.venPerfil.errorApellidos.setText(respuesta)
            self.venPerfil.errorApellidos.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venPerfil.line_apeP.setStyleSheet(self.STYLE_VALID)
            self.venPerfil.errorApellidos.setStyleSheet("")
            self.venPerfil.errorApellidos.setText("")

    def validar_identificacion(self):
        numero_identificacion = self.venPerfil.line_dni.text().strip()
        respuesta_validacion = self.es_identificacion_valida(numero_identificacion)
        if respuesta_validacion:
            self.venPerfil.line_dni.setStyleSheet(self.STYLE_INVALID)
            self.venPerfil.errorIdentificacion.setText(respuesta_validacion)
            self.venPerfil.errorIdentificacion.setStyleSheet(self.STYLE_ERROR)
        else:
            respuesta_bd = self.consultar_existencia_identificacion(numero_identificacion)
            if respuesta_bd:
                self.venPerfil.line_dni.setStyleSheet(self.STYLE_INVALID)
                self.venPerfil.errorIdentificacion.setText("Cedula ya existe.")
                self.venPerfil.errorIdentificacion.setStyleSheet(self.STYLE_ERROR)
            else:
                self.venPerfil.line_dni.setStyleSheet(self.STYLE_VALID)
                self.venPerfil.errorIdentificacion.setStyleSheet("")
                self.venPerfil.errorIdentificacion.setText("")

    def validar_correo(self):
        correo = self.venPerfil.line_correo.text().strip()
        if not correo or not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            self.venPerfil.line_correo.setStyleSheet(self.STYLE_INVALID)
            self.venPerfil.errorCorreo.setText("Correo electrónico inválido")
            self.venPerfil.errorCorreo.setStyleSheet(self.STYLE_ERROR)
            return
        respuesta = self.consultar_existencia_correo(correo)
        if respuesta:
            self.venPerfil.line_correo.setStyleSheet(self.STYLE_INVALID)
            self.venPerfil.errorCorreo.setText("Correo ya existe.")
            self.venPerfil.errorCorreo.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venPerfil.line_correo.setStyleSheet(self.STYLE_VALID)
            self.venPerfil.errorCorreo.setStyleSheet("")
            self.venPerfil.errorCorreo.setText("")
            
    def validar_contrasena(self):
        contrasena = self.venPerfil.line_contrasena.text().strip()
        
        respuesta = self.es_valido_contrasena(contrasena)
        if respuesta:
            self.venPerfil.line_contrasena.setStyleSheet(self.STYLE_INVALID)
            self.venPerfil.errorContrasena.setText(respuesta)
            self.venPerfil.errorContrasena.setStyleSheet(self.STYLE_ERROR)
        else:
            self.venPerfil.line_contrasena.setStyleSheet(self.STYLE_VALID)
            self.venPerfil.errorContrasena.setStyleSheet("")
            self.venPerfil.errorContrasena.setText("")

    def campos_validados(self):
        return (self.venPerfil.line_nombre.styleSheet() == self.STYLE_VALID and
                self.venPerfil.line_apeP.styleSheet() == self.STYLE_VALID and
                self.venPerfil.line_dni.styleSheet() == self.STYLE_VALID and
                self.venPerfil.line_correo.styleSheet() == self.STYLE_VALID and
                self.venPerfil.line_contrasena.styleSheet() == self.STYLE_VALID
            )

    def guardar_usuario(self):
       
        nombre = self.venPerfil.line_nombre.text().strip();
        apellidos = self.venPerfil.line_apeP.text().strip();
        identificacion = self.venPerfil.line_dni.text().strip();
        estado = self.venPerfil.cbox_estado.currentText()
        correo = self.venPerfil.line_correo.text().strip();

        if self.venPerfil.admi.isChecked():
            cargo = 1
        elif self.venPerfil.tutor.isChecked():
            cargo = 2
        else:
            cargo = 0

        contrasena = self.venPerfil.line_contrasena.text().strip()
        
        self.validar_nombres()
        self.validar_apellidos()
        self.validar_identificacion()
        self.validar_correo()
        self.validar_contrasena()
        
        
        if self.campos_validados():
            try:
                if self.modo != 'nuevo':
                
                    self.control_base.setDatosProcess('actualizar_usuario', (self.usuario_id, contrasena, identificacion, cargo, nombre, apellidos, correo, estado))
                                                                        
                    QMessageBox.information(self, "Mensaje", "Los datos se han actualizado correctamente en la base de datos.")
                else:
                    self.control_base.setDatosProcess('insertar_usuario', (contrasena, identificacion, cargo, nombre, apellidos, correo, estado))
                    QMessageBox.information(self, "Mensaje", "Los datos se han validado correctamente y se han enviado a la base de datos.")

                self.parent.raizOpacidad.close()
                self.close()
                self.parent.llenarTabla('listar_usuarios', 'usuarios', self.parent.venPri.tabla_usuario)
                self.parent.actualizarInfoPaginacion('usuarios', self.parent.venPri.lbl_pagina_user, True)
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ha ocurrido un error al guardar los datos en la base de datos: {str(e)}")

    def llenar_datos_usuarios(self, id_usuario):

        if not self.control_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        respuesta = self.control_base.getDatosProcess_condicion('buscar_usuario_por_id', (id_usuario, ))

        if(len(respuesta) > 0):
            respuesta = respuesta[0][0]
            
            self.usuario_id = respuesta[0]
      
            self.venPerfil.line_contrasena.setText(respuesta[1])
            self.venPerfil.line_dni.setText(respuesta[2])

            if(respuesta[3] == 2):
                self.venPerfil.tutor.setChecked(True)
            else:
                self.venPerfil.admi.setChecked(True)

            self.venPerfil.line_nombre.setText(respuesta[4])
            self.venPerfil.line_apeP.setText(respuesta[5])
            self.venPerfil.line_correo.setText(respuesta[6])
            self.venPerfil.cbox_estado.setCurrentText(respuesta[7])
            
            self.identificacion_actual = respuesta[2]
            self.correo_actual = respuesta[6]
            
            
        