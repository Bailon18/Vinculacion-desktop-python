
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from controllers.Modulo_Vinculacion.Modulo_Vinculacion import Vinculacion
from controllers.Modulo_mantenimiento.Mantenimiento_instituciones import Instituciones
from controllers.Modulo_mantenimiento.Mantenimiento_proyectos import Proyectos
from controllers.Modulo_usuarios.Modulo_usuarios import Perfil
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_ventana_principal import Ui_principal


import re, os
from PIL import Image
from datetime import datetime

from controllers.Modulo_principal.funcion_general import *

from db.Modulo_base import BaseDatos

class Principal(QtWidgets.QMainWindow):

    def __init__(self, *args , parent=None):
        
        super(Principal, self).__init__(parent)
        self.venPri = Ui_principal()
        self.venPri.setupUi(self)
        
        self.conec_base = BaseDatos()

        self.configuracion_ventana()
        self.rol = args[0][2]
        self.tutor_id = args[0][0]
        self.venPri.lbl_usuario.setText(str(args[0][1]))
        self.venPri.lbl_rol.setText(str(args[0][2]))

        if(self.rol != 'Administrador'):
            self.venPri.btn_afiliacion.setHidden(True)
            self.venPri.btn_usuario.setHidden(True)
            self.venPri.btn_reporte.setHidden(True)
            self.venPri.btn_home.setHidden(True)
            self.venPri.btn_seguimientoo.setHidden(False)
            evento_pagina(self,1, self.venPri.btn_seguimientoo)
        else:
            self.venPri.btn_seguimientoo.setHidden(True)
            self.venPri.btn_home.setHidden(False)
            evento_pagina(self,0, self.venPri.btn_afiliacion)

        self.listar_vinculacion()
        self.listar_usuarios()
        
        # self.configuracion()
        self.controlSalida = True
         # clase opacidad-----------------------
        self.raizOpacidad = Clase_Opacidad(self)
        self.raizOpacidad.close()
        
        self.venPri.btn_cerrar.clicked.connect(lambda: self.cerrar_sesion())
        
        self.venPri.line_busqueda.textChanged.connect(lambda: self.busqueda_vinculacion())
        self.venPri.line_busqueda_tutor.textChanged.connect(lambda: self.busqueda_vinculacion_tutor())
        self.venPri.line_busqueda_reporte_estudiantes.textChanged.connect(lambda: self.busqueda_datos_estudiante())
        self.venPri.line_busqueda_usuario.textChanged.connect(lambda: self.busqueda_usuarios_filtro())
        self.venPri.cbox_perfil.activated.connect(lambda: self.evento_perfil())
     

 
        evento_menu(self, self.venPri, tr=0)
        evento_hora(self)
        evento_tabla(self)
        self.venPri.boton_deslizable.clicked.connect(lambda: evento_menu(self, self.venPri))

        evento_pagina_mantenimiento(self, 1, self.venPri.btn_menu_institucion)
        self.venPri.btn_menu_institucion.clicked.connect(lambda: evento_pagina_mantenimiento(self, 1, self.venPri.btn_menu_institucion))
        self.venPri.btn_menu_proyectos.clicked.connect(lambda: evento_pagina_mantenimiento(self, 0, self.venPri.btn_menu_proyectos))

        self.venPri.btn_agregar_instituto.clicked.connect(lambda: self.mostrar_formulario_instituciones())
        self.venPri.btn_agregar_proyectos.clicked.connect(lambda: self.mostrar_formulario_proyectos())

        self.llenado_instituciones('Activo')
        self.llenado_proyectos('Activo')

        self.venPri.check_estado_institucion.stateChanged.connect(lambda: self.mostrar_instituciones_estado())
        self.venPri.check_estado_proyectos.stateChanged.connect(lambda: self.mostrar_proyectos_estado())
    

        self.venPri.btn_afiliacion.clicked.connect(lambda: evento_pagina(self, 0, self.venPri.btn_afiliacion))
        self.venPri.btn_seguimientoo.clicked.connect(lambda: evento_pagina(self, 1, self.venPri.btn_seguimientoo))
        self.venPri.btn_home.clicked.connect(lambda: evento_pagina(self, 2, self.venPri.btn_home))
        self.venPri.btn_usuario.clicked.connect(lambda: evento_pagina(self, 3, self.venPri.btn_usuario))
        self.venPri.btn_reporte.clicked.connect(lambda: evento_pagina(self, 4, self.venPri.btn_reporte))
        
        
        self.venPri.btn_nuevoafiliacion.clicked.connect(lambda: self.abrir_ventana_afiliacion())
        self.venPri.btn_recargar.clicked.connect(lambda: self.listar_vinculacion())
        self.venPri.btn_agregar_usuario.clicked.connect(lambda: self.abrir_ventana_perfil())
        
        self.venPri.cbox_rango.currentIndexChanged.connect(lambda : self.mostrar_vinculacion_rango(self.venPri.cbox_rango.currentText()))
        self.venPri.cbox_rango_tutor.currentIndexChanged.connect(lambda : self.mostrar_vinculacion_rango_tutor(self.venPri.cbox_rango_tutor.currentText()))
        
        evento_seleccion_reporte(self, self.venPri.radioEstudiante, 1)
        self.venPri.radioEstudiante.clicked.connect(lambda: evento_seleccion_reporte(self, self.venPri.radioEstudiante, 1))
        self.venPri.radioTutor.clicked.connect(lambda: evento_seleccion_reporte(self, self.venPri.radioTutor, 0))

        self.listar_seguimiento_tutor()
        
        # evento reporte
        self.venPri.cbo_tutores.activated.connect(lambda: self.evento_filtro_tutores())  
        self.llenado_reporte('En Progreso',  self.venPri.tabla_reporte_tutores, 'ObtenerInfoVinculacionPorTutor', 5, self.venPri.cbo_tutores.itemData(self.venPri.cbo_tutores.currentIndex()))
        self.venPri.radioProcesoT.clicked.connect(lambda: self.filtro_reporte('En Progreso','Tutor', 'ObtenerInfoVinculacionPorTutor'))
        self.venPri.radioPendienteT.clicked.connect(lambda: self.filtro_reporte('Pendiente','Tutor', 'ObtenerInfoVinculacionPorTutor'))
        self.venPri.radioCulminadoT.clicked.connect(lambda: self.filtro_reporte('Culminado','Tutor', 'ObtenerInfoVinculacionPorTutor'))
        self.venPri.cbox_rango_reporte_tutor.activated.connect(lambda: self.evento_filtro_tutores()) 
        
        
        self.llenado_reporte('En Progreso',  self.venPri.tabla_reporte_estudiantes, 'obtenerInformacionVinculacionesConEstado', 5)
        self.venPri.check_todos_estudiantes.clicked.connect(lambda: self.evento_obtener_reporte_general())
        self.venPri.cbox_rango_estudiantes.activated.connect(lambda: self.evento_obtener_reporte_general())
        self.venPri.radioProcesoE.clicked.connect(lambda: self.filtro_reporte('En Progreso','Estudiante', 'obtenerInformacionVinculacionesConEstado'))
        self.venPri.radioPendienteE.clicked.connect(lambda: self.filtro_reporte('Pendiente','Estudiante', 'obtenerInformacionVinculacionesConEstado'))
        self.venPri.radioCulminadoE.clicked.connect(lambda: self.filtro_reporte('Culminado','Estudiante', 'obtenerInformacionVinculacionesConEstado'))
        

    def evento_perfil(self):
        
        if self.venPri.cbox_perfil.currentIndex() == 0:

            self.raizOpacidad.resize(self.width(), self.height())
            self.raizOpacidad.show()
            Perfil(self, 'Editar', [self.tutor_id, 'Jose Luna']).exec_()
        else:
            self.cerrar_sesion()

    def closeEvent(self, event):
        if self.controlSalida:
            if(QtWidgets.QMessageBox.question(self, "Mensaje", "¿Desea cerrar la aplicacíon?.", 
                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No ) == QtWidgets.QMessageBox.Yes):
                event.accept()
            else:
                event.ignore()
            
    def cerrar_sesion(self):
        from controllers.Modulo_sesion.Modulo_inicio import Login
        
        self.controlSalida = False
        if(QtWidgets.QMessageBox.question(self, "Mensaje", "¿Desea cerrar la Sesión?.", 
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No ) == QtWidgets.QMessageBox.Yes):
            
           self.close()
           self.logincito = Login()
           self.logincito.show()
           
        else:
            self.controlSalida = True

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
       
    def configuracion_ventana(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        lista_carrera, lista_institucion, lista_proyectos, lista_tutores = self.conec_base.getDatosProcess("ObtenerDatos")
        if(len(lista_tutores) > 0):
            self.llenar_combobox(self.venPri.cbo_tutores, lista_tutores, 50)
          
            
    def abrir_ventana_afiliacion(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        Vinculacion(parent = self).exec_()


    def abrir_ventana_perfil(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        Perfil(parent = self, modo ='Nuevo').exec_()

    def listar_vinculacion(self, datos=None):
        
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        limite = int(self.venPri.cbox_rango.currentText())
        
        if datos is None:
            datos = self.conec_base.getDatosProcess_condicion("ListarVinculaciones",(limite, ))

        if isinstance(datos, list) and datos:
            datos_a_insertar = datos[0]
            llenar_tabla_vinculacion(self, self.venPri.tabla_principal, datos_a_insertar)
        else:
            pass
            #print("Los datos obtenidos no son válidos o están vacíos. No se pudo llenar la tabla.")

    def busqueda_vinculacion(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        textobusqueda =  self.venPri.line_busqueda.text()
        limite = int(self.venPri.cbox_rango.currentText())
        
        lista_vinculaciones = self.conec_base.getDatosProcess_condicion("BuscarVinculaciones", (textobusqueda, limite))
        self.listar_vinculacion(lista_vinculaciones)

    def mostrar_vinculacion_rango(self, text):
        self.listar_vinculacion()

    def listar_seguimiento_tutor(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        limite = int(self.venPri.cbox_rango_tutor.currentText())

        lista_seguimiento = self.conec_base.getDatosProcess_condicion('ObtenerSeguimientosConEstudiantes', (self.tutor_id, limite))
        llenar_tabla_seguimiento(self, self.venPri.tabla_principal_tutor, lista_seguimiento[0])

    def listar_vinculacion_tutor(self, datos=None):
        
        if datos is None:
            self.listar_seguimiento_tutor()

        if isinstance(datos, list) and datos:
            datos_a_insertar = datos[0]
            llenar_tabla_seguimiento(self, self.venPri.tabla_principal_tutor, datos_a_insertar)
        else:
            pass


    def busqueda_vinculacion_tutor(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return

        textobusqueda =  self.venPri.line_busqueda_tutor.text()
        limite = int(self.venPri.cbox_rango_tutor.currentText())

        lista_vinculaciones_tutor = self.conec_base.getDatosProcess_condicion("filtrarSeguimientosConEstudiantes", (self.tutor_id, limite, textobusqueda,))
        self.listar_vinculacion_tutor(lista_vinculaciones_tutor)


    def mostrar_vinculacion_rango_tutor(self, text):
        self.listar_vinculacion_tutor()
        
    def listar_usuarios(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return

        resultado  = self.conec_base.getDatosProcess('ListarUsuarios')
        if(len(resultado) > 0):
            resultado = resultado[0]
            llenar_tabla_usuario(self, self.venPri.tabla_usuario, resultado)


    def busqueda_usuarios_filtro(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return

        texto_busqueda = self.venPri.line_busqueda_usuario.text().strip()

        resultado = self.conec_base.getDatosProcess_condicion('filtrarUsuarios', (texto_busqueda,))
        if(len(resultado) > 0):
            resultado = resultado[0]
            llenar_tabla_usuario(self, self.venPri.tabla_usuario, resultado)
        else:
            self.listar_usuarios()


    def mostrar_formulario_instituciones(self):
        
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        Instituciones(parent = self, modo='Nuevo').exec_()


    def mostrar_formulario_proyectos(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        Proyectos(parent = self, modo='Nuevo').exec_()


    def llenado_instituciones(self, estado):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        respuesta = self.conec_base.getDatosProcess_condicion('ListarInstitucionesPorEstado' , (estado, ))
        if(respuesta):
            respuesta = respuesta[0]
            llenar_tabla_institucion(self, self.venPri.tabla_intituciones, respuesta)


    def mostrar_instituciones_estado(self):

        estado = 'Inactivo' if self.venPri.check_estado_institucion.isChecked() else 'Activo'
        self.llenado_instituciones(estado)

    def llenado_proyectos(self, estado):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return

        respuesta = self.conec_base.getDatosProcess_condicion('ListarProyectosPorEstado' , (estado, ))
        if(respuesta):
            respuesta = respuesta[0]
            llenar_tabla_proyectos(self, self.venPri.tabla_proyectos, respuesta)

    def mostrar_proyectos_estado(self):

        estado = 'Inactivo' if self.venPri.check_estado_proyectos.isChecked() else 'Activo'
        self.llenado_proyectos(estado)

    def llenado_reporte(self, estado, tabla, procedimiento, limite, condicion=0):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        if(condicion != 0):
            respuesta = self.conec_base.getDatosProcess_condicion( procedimiento , (estado,limite,condicion, ))
        else:                                                                 
            respuesta = self.conec_base.getDatosProcess_condicion( procedimiento , (estado,limite ))
            
        if(respuesta):
            respuesta = respuesta[0]
            cargar_tabla(tabla, respuesta)
            
    def filtro_reporte(self, estado , tipo, consulta):
        
        if(tipo == 'Estudiante'):
            limite = int(self.venPri.cbox_rango_estudiantes.currentText())
            self.llenado_reporte(estado , self.venPri.tabla_reporte_estudiantes, consulta, limite)
        else:
            limite = int(self.venPri.cbox_rango_reporte_tutor.currentText())
            tutor_id = self.venPri.cbo_tutores.itemData(self.venPri.cbo_tutores.currentIndex());
            self.llenado_reporte(estado , self.venPri.tabla_reporte_tutores, consulta, limite, tutor_id)
            
    def evento_obtener_reporte_general(self):
        if self.venPri.check_todos_estudiantes.isChecked():
            self.venPri.radioCulminadoE.setEnabled(True)
            self.venPri.radioProcesoE.setEnabled(True)
            self.venPri.radioPendienteE.setEnabled(True)
            self.venPri.line_busqueda_reporte_estudiantes.setEnabled(False)
            estado = ''
            
            if self.venPri.radioPendienteE.isChecked():
                estado = 'Pendiente'
            elif self.venPri.radioProcesoE.isChecked():
                estado = 'En Progreso'
            else:
                estado = 'Culminado'
                
            self.filtro_reporte(estado, 'Estudiante', 'obtenerInformacionVinculacionesConEstado')
        else:
            self.venPri.line_busqueda_reporte_estudiantes.setEnabled(True)
            self.venPri.radioCulminadoE.setEnabled(False)
            self.venPri.radioProcesoE.setEnabled(False)
            self.venPri.radioPendienteE.setEnabled(False)
    
    def evento_filtro_tutores(self):
        
        estado = ''
            
        if self.venPri.radioPendienteT.isChecked():
            estado = 'Pendiente'
        elif self.venPri.radioProcesoT.isChecked():
            estado = 'En Progreso'
        else:
            estado = 'Culminado'
    
        self.filtro_reporte(estado, 'Tutor', 'ObtenerInfoVinculacionPorTutor')
            
        
        
    def busqueda_datos_estudiante(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        self.venPri.check_todos_estudiantes.setChecked(False)
        self.evento_obtener_reporte_general()
        parametro_busqueda = self.venPri.line_busqueda_reporte_estudiantes.text().strip()
        respuesta = self.conec_base.getDatosProcess_condicion( 'obtenerInformacionVinculacionesConEstadoYBusqueda' , (parametro_busqueda, ))
        if(respuesta):
            respuesta = respuesta[0]
            cargar_tabla(self.venPri.tabla_reporte_estudiantes, respuesta)
            
            
    def llenar_combobox(self, combobox, lista, longitud_maxima):
        for elemento in lista:
            id_elemento, nombre_elemento = elemento
            texto_truncado = nombre_elemento[:longitud_maxima]
            combobox.addItem(texto_truncado, userData=id_elemento)
            combobox.setItemData(combobox.count() - 1, nombre_elemento, Qt.ToolTipRole)