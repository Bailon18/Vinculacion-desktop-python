
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox

import re

from datetime import datetime
from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_perfil import Ui_Perfil

from db.Modulo_base import BaseDatos

class Perfil(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', dato = []):

        super(Perfil, self).__init__()
        self.venPerfil = Ui_Perfil()
        self.venPerfil.setupUi(self)
        self.control_perfil = BaseDatos()

        self.ventana_configuracion()

        self.parent = parent
        self.modo = modo
        self.dato = dato
        

        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.venPerfil.btn_closeedit.clicked.connect(lambda: self.cerrar_ui_perfil())
        self.venPerfil.btn_guardar.clicked.connect(lambda: self.guardar_usuario())

        if(self.modo != 'Nuevo'):
            self.venPerfil.lbl_titulo_ventana.setText('Editar Perfil')
            self.venPerfil.btn_guardar.setText('Actualizar')
            self.venPerfil.lbl_usuariologeado.setText(self.dato[1])
            
            self.llenar_datos_usuarios()

            if(self.parent.rol != 'Administrador'):
                self.venPerfil.admi.setEnabled(False)
                self.venPerfil.tutor.setEnabled(False)
                
        if(self.parent.venPri.lbl_rol.text() != 'Administrador'):
            self.venPerfil.admi.setEnabled(False)
            self.venPerfil.admi.setEnabled(False)
            

        # Validaciones y mascaras para los inputs
        val_nombre_apellido(self, self.venPerfil.line_nombre)
        val_nombre_apellido(self, self.venPerfil.line_apeP)
        val_identifiacion(self, self.venPerfil.line_dni)

        

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass

    def cerrar_ui_perfil(self):
        self.parent.raizOpacidad.close()
        self.close()

    def ventana_configuracion(self):
        fecha_actual = QtCore.QDate.currentDate()

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

        mensaje_error = ""

        if not nombre:
            mensaje_error += "- Ingrese el nombre \n"

        if not apellidos:
            mensaje_error += "- Ingrese los apellidos \n"

        if not validar_correo_electronico(correo):
            mensaje_error += "- Correo no tiene el formato correcto \n"

        if len(identificacion) != 11 or identificacion[9] != '-':
            mensaje_error += "- Ingrese una identificacion válido (ejemplo: 112233456-2).\n"

        if not contrasena:
            mensaje_error += "- Ingrese contraseñaa.\n"

        if cargo == 0:
            mensaje_error += "- Seleccione un rol.\n"


        if mensaje_error:

            QMessageBox.critical(self, "Error", "Revise los campos:\n" + mensaje_error)
        else:

            datos = [contrasena, identificacion, cargo, nombre, apellidos, correo, estado]

            if self.modo == "Editar":
                datos.append(self.dato[0])
                self.actualizar_usuario(datos)
            else:
                self.crear_nueva_usuario(datos)

            self.parent.listar_usuarios()
            self.parent.raizOpacidad.close()
            self.close()

    def llenar_datos_usuarios(self):

        if not self.control_perfil.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        respuesta = self.control_perfil.getDatosProcess_condicion('BuscarUsuarioPorID', (self.dato[0], ))

        if(len(respuesta) > 0):
            respuesta = respuesta[0][0]
      
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
            
    def actualizar_usuario(self , datos):
        
        if not self.control_perfil.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        self.control_perfil.setDatosProcess('ActualizarUsuario', (datos))
        QMessageBox.information(self, "Correcto", "Perfil actualizado correctamente")
  
    def crear_nueva_usuario(self, datos):
        
        if not self.control_perfil.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        self.control_perfil.setDatosProcess('InsertarUsuario', (datos))
        QMessageBox.information(self, "Correcto", "Perfil registrado correctamente")

        