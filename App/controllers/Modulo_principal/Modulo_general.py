
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from controllers.Modulo_Vinculacion.Modulo_Vinculacion import Vinculacion
from controllers.Modulo_administracion.Carreras_administracion import CarrerasAdmin
from controllers.Modulo_administracion.Estudiantes_administracion import EstudiantesAdmin
from controllers.Modulo_administracion.Instituciones_administracion import InstitucionesAdmin
from controllers.Modulo_administracion.Proyectos_administracion import ProyectosAdmin
from controllers.Modulo_administracion.Tutores_administracion import TutoresAdmin
from controllers.Modulo_usuarios.Modulo_usuarios import Perfil
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_ventana_principal import Ui_principal


import re, os
from datetime import datetime

from controllers.Modulo_principal.funcion_general import *

from db.Modulo_base import BaseDatos

class Principal(QtWidgets.QMainWindow):

    def __init__(self, *args , parent=None):
        
        super(Principal, self).__init__(parent)
        self.venPri = Ui_principal()
        self.venPri.setupUi(self)
        
        self.conec_base = BaseDatos()

        
        #self.configuracion_ventana()
        self.rol = 'Administrador' # args[0][2]
        self.tutor_id = 1 # args[0][0]
        self.venPri.lbl_usuario.setText("Bailon Paucar") # str(args[0][1])
        self.venPri.lbl_rol.setText("Administrador") # str(args[0][2])
        
        # self.lista_estudiante_filtro = []
        # self.lista_informes_filtro =[]
        # self.lista_ficha_filtro = []
        # self.lista_memorandun_filtro = []
        
        # self.cambioPagina()
        self.datos_inicializacion()
        

        

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

        # self.listar_vinculacion()
        # self.listar_usuarios()
        
        self.controlSalida = True
         # clase opacidad-----------------------
        self.raizOpacidad = Clase_Opacidad(self)
        self.raizOpacidad.close()
        
        self.venPri.btn_cerrar.clicked.connect(lambda: self.cerrar_sesion())
        
        # abrir vemtamas model
        self.venPri.btn_agregar_estudiantes_admin.clicked.connect(lambda: self.abrir_ventana_estudiantes())
        self.venPri.btn_agregar_tutores.clicked.connect(lambda: self.abrir_ventana_tutores())
        self.venPri.btn_agregar_proyectos.clicked.connect(lambda: self.abrir_ventana_proyectos())
        self.venPri.btn_agregar_carrera.clicked.connect(lambda: self.abrir_ventana_carreras())
        self.venPri.btn_agregar_insti.clicked.connect(lambda: self.abrir_ventana_instituciones())
        self.venPri.btn_nueva_vinculacion.clicked.connect(lambda: self.abrir_ventana_vinculacion())
        
        
        # filtro evento busquedas
        self.venPri.line_busqueda_estudiantes.textChanged.connect(lambda: self.filtro_estudiante())
        self.venPri.line_busqueda_tutores.textChanged.connect(lambda: self.filtro_tutores())
        self.venPri.line_busqueda_proyecto.textChanged.connect(lambda: self.filtro_proyectos())
        self.venPri.line_busqueda_carrera.textChanged.connect(lambda: self.filtro_carreras())
        self.venPri.line_busqueda_inst.textChanged.connect(lambda: self.filtro_institucion())
        # self.venPri.line_busqueda_tutor.textChanged.connect(lambda: self.busqueda_vinculacion_tutor())
        # self.venPri.line_busqueda_reporte_estudiantes.textChanged.connect(lambda: self.busqueda_datos_estudiante())
        # self.venPri.line_busqueda_usuario.textChanged.connect(lambda: self.busqueda_usuarios_filtro())
        # self.venPri.cbox_perfil.activated.connect(lambda: self.evento_perfil())
     

 
        #evento_menu(self, self.venPri, tr=0)
        evento_menu(self, self.venPri, tr=200, imagen=self.venPri.lbl_logo2)
        evento_hora(self)
        evento_tabla(self)
        self.venPri.boton_deslizable.clicked.connect(lambda: evento_menu(self, self.venPri))

        evento_pagina_mantenimiento(self, 0, self.venPri.btn_menu_estudiantes)
        self.venPri.btn_menu_estudiantes.clicked.connect(lambda: evento_pagina_mantenimiento(self, 0, self.venPri.btn_menu_estudiantes))
        self.venPri.btn_menu_tutores.clicked.connect(lambda: evento_pagina_mantenimiento(self, 1, self.venPri.btn_menu_tutores))
        self.venPri.btn_menu_proyectos.clicked.connect(lambda: evento_pagina_mantenimiento(self, 2, self.venPri.btn_menu_proyectos))
        self.venPri.btn_menu_carreras.clicked.connect(lambda: evento_pagina_mantenimiento(self, 3, self.venPri.btn_menu_carreras))
        self.venPri.btn_menu_instituciones.clicked.connect(lambda: evento_pagina_mantenimiento(self, 4, self.venPri.btn_menu_instituciones))
        
        
        

        # self.venPri.btn_agregar_instituto.clicked.connect(lambda: self.mostrar_formulario_instituciones())
        # self.venPri.btn_agregar_proyectos.clicked.connect(lambda: self.mostrar_formulario_proyectos())

        # self.llenado_instituciones('Activo')
        # self.llenado_proyectos('Activo')

        # self.venPri.check_estado_institucion.stateChanged.connect(lambda: self.mostrar_instituciones_estado())
        # self.venPri.check_estado_proyectos.stateChanged.connect(lambda: self.mostrar_proyectos_estado())
    

        self.venPri.btn_afiliacion.clicked.connect(lambda: evento_pagina(self, 0, self.venPri.btn_afiliacion))
        self.venPri.btn_seguimientoo.clicked.connect(lambda: evento_pagina(self, 1, self.venPri.btn_seguimientoo))
        self.venPri.btn_home.clicked.connect(lambda: evento_pagina(self, 2, self.venPri.btn_home))
        self.venPri.btn_usuario.clicked.connect(lambda: evento_pagina(self, 3, self.venPri.btn_usuario))
        self.venPri.btn_reporte.clicked.connect(lambda: evento_pagina(self, 4, self.venPri.btn_reporte))
        
        
        # self.venPri.btn_nuevoafiliacion.clicked.connect(lambda: self.abrir_ventana_afiliacion())
        # self.venPri.btn_recargar.clicked.connect(lambda: self.listar_vinculacion())
        # self.venPri.btn_agregar_usuario.clicked.connect(lambda: self.abrir_ventana_perfil())
        
        # self.venPri.cbox_rango.currentIndexChanged.connect(lambda : self.mostrar_vinculacion_rango(self.venPri.cbox_rango.currentText()))
        # self.venPri.cbox_rango_tutor.currentIndexChanged.connect(lambda : self.mostrar_vinculacion_rango_tutor(self.venPri.cbox_rango_tutor.currentText()))
        
        # evento_seleccion_reporte(self, self.venPri.radioEstudiante, 2)
        # self.venPri.radioEstudiante.clicked.connect(lambda: evento_seleccion_reporte(self, self.venPri.radioEstudiante, 2))
        # self.venPri.radioTutor.clicked.connect(lambda: evento_seleccion_reporte(self, self.venPri.radioTutor, 0))
        # self.venPri.radioreporteentrega.clicked.connect(lambda: evento_seleccion_reporte(self, self.venPri.radioreporteentrega, 1))
        

        # self.listar_seguimiento_tutor()
        
        # # evento reporte
        # self.venPri.cbox_rango_reporte_tutor.activated.connect(lambda: self.evento_obtener_tutores_limite())
        # self.venPri.line_busqueda_reporte_tutor.textChanged.connect(lambda: self.busqueda_tutor_reporte())

        
        # self.llenado_reporte('En Progreso',  self.venPri.tabla_reporte_estudiantes, 'obtenerInformacionVinculacionesConEstado', 5)
        # self.venPri.check_todos_estudiantes.clicked.connect(lambda: self.evento_obtener_reporte_general())
        # self.venPri.cbox_rango_estudiantes.activated.connect(lambda: self.evento_obtener_reporte_general())
        # self.venPri.radioProcesoE.clicked.connect(lambda: self.filtro_reporte('En Progreso','Estudiante', 'obtenerInformacionVinculacionesConEstado'))
        # self.venPri.radioPendienteE.clicked.connect(lambda: self.filtro_reporte('Pendiente','Estudiante', 'obtenerInformacionVinculacionesConEstado'))
        # self.venPri.radioCulminadoE.clicked.connect(lambda: self.filtro_reporte('Culminado','Estudiante', 'obtenerInformacionVinculacionesConEstado'))
        
        # self.venPri.cbo_tipo_entrega.activated.connect(lambda: self.cambioPagina())
        # self.venPri.cbo_periodo_academico.activated.connect(lambda: self.eventoSeleccionPeriodo())
        
        # self.venPri.btn_export.clicked.connect(lambda: self.reporte_estudiantes())
        # self.venPri.btn_export_2.clicked.connect(lambda: self.generarReporte_informe())
        # self.venPri.btn_export_3.clicked.connect(lambda: self.generarReporte_ficha())
        # self.venPri.btn_export_4.clicked.connect(lambda: self.generarReporte_memorandum())
        
        
        self.offset = 0
        self.limit = 5
        self.textobusqueda = ""
        
        self.venPri.btn_pag_antes_estu.clicked.connect(lambda: self.prev_page('listar_estudiantes', 'estudiantes', self.venPri.lbl_pagina_estudiantes, self.venPri.tabla_estudiantes))
        self.venPri.btn_pag_desp_estu.clicked.connect(lambda: self.next_page('listar_estudiantes', 'estudiantes', self.venPri.lbl_pagina_estudiantes, self.venPri.tabla_estudiantes))
        
        self.venPri.btn_pag_antes_tutor.clicked.connect(lambda: self.prev_page('listar_tutores', 'tutores', self.venPri.lbl_pagina_tutores, self.venPri.tabla_tutores))
        self.venPri.btn_pag_desp_tutor.clicked.connect(lambda: self.next_page('listar_tutores', 'tutores', self.venPri.lbl_pagina_tutores, self.venPri.tabla_tutores))
        
        self.venPri.btn_pag_antes_proyecto.clicked.connect(lambda: self.prev_page('listar_proyectos', 'proyecto', self.venPri.lbl_pagina_proyectos, self.venPri.tabla_proyecto))
        self.venPri.btn_pag_desp_proyecto.clicked.connect(lambda: self.next_page('listar_proyectos', 'proyecto', self.venPri.lbl_pagina_proyectos, self.venPri.tabla_proyecto))
        
        self.venPri.btn_pag_antes_carrera.clicked.connect(lambda: self.prev_page('listar_carreras', 'carrera', self.venPri.lbl_pagina_carrera, self.venPri.tabla_carrera))
        self.venPri.btn_pag_desp_carrera.clicked.connect(lambda: self.next_page('listar_carreras', 'carrera', self.venPri.lbl_pagina_carrera, self.venPri.tabla_carrera))
        
        self.venPri.btn_pag_antes_inst.clicked.connect(lambda: self.prev_page('listar_institucion', 'institucion', self.venPri.lbl_pagina_instituto, self.venPri.tabla_institucion))
        self.venPri.btn_pag_desp_inst.clicked.connect(lambda: self.next_page('listar_institucion', 'institucion', self.venPri.lbl_pagina_instituto, self.venPri.tabla_institucion))
        
        self.venPri.btn_pag_antes_vinculacion.clicked.connect(lambda: self.prev_page('ObtenerListaVinculaciones', 'vinculacion', self.venPri.lbl_pagina_vinculacion, self.venPri.tabla_vinculacion))
        self.venPri.btn_pag_desp_vinculacion.clicked.connect(lambda: self.next_page('ObtenerListaVinculaciones', 'vinculacion', self.venPri.lbl_pagina_vinculacion, self.venPri.tabla_vinculacion))
        
        
    
        # Inicializar la tabla con la primera página
        self.llenarTabla('listar_estudiantes', 'estudiantes', self.venPri.tabla_estudiantes)
        self.actualizarInfoPaginacion('estudiantes', self.venPri.lbl_pagina_estudiantes)
        
        self.llenarTabla('listar_tutores', 'tutores', self.venPri.tabla_tutores)
        self.actualizarInfoPaginacion('tutores', self.venPri.lbl_pagina_tutores)
        
        self.llenarTabla('listar_proyectos', 'proyecto', self.venPri.tabla_proyecto)
        self.actualizarInfoPaginacion('proyecto', self.venPri.lbl_pagina_proyectos)
        
        self.llenarTabla('listar_carreras', 'carrera', self.venPri.tabla_carrera)
        self.actualizarInfoPaginacion('carrera', self.venPri.lbl_pagina_carrera)
        
        self.llenarTabla('listar_institucion', 'institucion', self.venPri.tabla_institucion)
        self.actualizarInfoPaginacion('institucion', self.venPri.lbl_pagina_instituto)
        
        self.llenarTabla('ObtenerListaVinculaciones', 'vinculacion', self.venPri.tabla_vinculacion)
        self.actualizarInfoPaginacion('vinculacion', self.venPri.lbl_pagina_vinculacion)
        
        
        # Eventos de combobox filtro en vinculacion
        self.venPri.cbo_filtro_proyecto.currentIndexChanged.connect(lambda: self.consultar_basedatos('proyecto'))
        self.venPri.cbo_filtro_periodo.currentIndexChanged.connect(lambda: self.consultar_basedatos('periodo'))
        self.venPri.cbo_filtro_tutor.currentIndexChanged.connect(lambda: self.consultar_basedatos('tutor'))
        self.venPri.line_filtro_estudiante.textChanged.connect(lambda: self.consultar_basedatos('estudiante'))


        

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
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
          
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
       
    def abrir_ventana_estudiantes(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        EstudiantesAdmin(self, 'nuevo', 0).exec_()
        
    def abrir_ventana_tutores(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        TutoresAdmin(self, 'nuevo', 0).exec_()
        
    def abrir_ventana_proyectos(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        ProyectosAdmin(self, 'nuevo', 0).exec_()
        
    def abrir_ventana_carreras(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        CarrerasAdmin(self, 'nuevo', 0).exec_()
        
    def abrir_ventana_instituciones(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        InstitucionesAdmin(self, 'nuevo', 0).exec_()
        
    def abrir_ventana_vinculacion(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        Vinculacion(parent=self).exec_()
       
       
    def llenarTabla(self, procedimiento, tabla,  tabla_diseno):
        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, [self.offset, self.limit])

        if(tabla == 'estudiantes' and datoresultante):
            llenar_tabla_estudiantes(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'tutores' and datoresultante):
            lenar_tabla_tutores(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'proyecto' and datoresultante):
            llenar_tabla_proyectos(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'carrera' and datoresultante):
            llenar_tabla_carreras(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'institucion' and datoresultante):
            llenar_tabla_institucion(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'vinculacion' and datoresultante):
            llenar_tabla_vinculacion(self, tabla_diseno, datoresultante[0])
            
    def llenarTablaFiltro(self, procedimiento, tabla_diseno, param, tipo):
        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, [tipo, param,  self.offset, self.limit])
        
        if len(datoresultante) > 0 and len(datoresultante[0]) > 0:
            llenar_tabla_vinculacion(self, tabla_diseno, datoresultante[0])
        else:
            QtWidgets.QMessageBox.warning(self, 'Información', f'No se encontró ninguna vinculación con el nombre del {tipo} seleccionado.')
            self.llenarTabla('ObtenerListaVinculaciones', 'vinculacion', self.venPri.tabla_vinculacion)
            self.actualizarInfoPaginacion('vinculacion', self.venPri.lbl_pagina_vinculacion)

          
    def next_page(self, procedimiento, tabla, labels, tabla_diseno):
        self.offset += self.limit
        datoretorno = self.conec_base.getDatosProcess_condicion(procedimiento, [self.offset, self.limit])
  
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
        total_registros = self.conec_base.getDatos('SELECT COUNT(*) FROM '+ nomnbreTabla)
        total_registros = total_registros[0][0] if total_registros else 0
        total_paginas = (total_registros + self.limit - 1) // self.limit 
        pagina_actual = (self.offset // self.limit) + 1 
        labels.setText(f"Página {pagina_actual} de {total_paginas}") 

    def filtro_estudiante(self):
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        textobusqueda = self.venPri.line_busqueda_estudiantes.text()

        if textobusqueda.strip() == "":
            procedimiento = "listar_estudiantes"
            parametros = (self.offset, self.limit)
        else:
            total_registros = self.conec_base.getDatosProcess_condicion("contar_estudiantes", (textobusqueda,))
            total_registros = total_registros[0][0][0] if total_registros else 0

            total_paginas = (total_registros + self.limit - 1) // self.limit
            pagina_actual = min((self.offset // self.limit) + 1, total_paginas)
            self.offset = max(0, (pagina_actual - 1) * self.limit)

            procedimiento = "buscar_estudiantes"
            parametros = (textobusqueda, self.offset, self.limit)

        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, parametros)

        if len(datoresultante[0]) > 0:
            llenar_tabla_estudiantes(self, self.venPri.tabla_estudiantes, datoresultante[0])
        else:
            self.offset = max(0, self.offset - self.limit)
        self.actualizarInfoPaginacion("estudiantes", self.venPri.lbl_pagina_estudiantes)
        
    def filtro_tutores(self):
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        textobusqueda = self.venPri.line_busqueda_tutores.text()

        if textobusqueda.strip() == "":
            procedimiento = "listar_tutores"
            parametros = (self.offset, self.limit)
        else:
            total_registros = self.conec_base.getDatosProcess_condicion("contar_tutores", (textobusqueda,))
            total_registros = total_registros[0][0][0] if total_registros else 0

            total_paginas = (total_registros + self.limit - 1) // self.limit
            pagina_actual = min((self.offset // self.limit) + 1, total_paginas)
            self.offset = max(0, (pagina_actual - 1) * self.limit)

            procedimiento = "buscar_tutores"
            parametros = (textobusqueda, self.offset, self.limit)

        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, parametros)

        if len(datoresultante[0]) > 0:
            lenar_tabla_tutores(self, self.venPri.tabla_tutores, datoresultante[0])
        else:
            self.offset = max(0, self.offset - self.limit)
        self.actualizarInfoPaginacion("tutores", self.venPri.lbl_pagina_tutores)
        
    def filtro_proyectos(self):
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        textobusqueda = self.venPri.line_busqueda_proyecto.text()

        if textobusqueda.strip() == "":
            procedimiento = "listar_proyectos"
            parametros = (self.offset, self.limit)
        else:
            total_registros = self.conec_base.getDatosProcess_condicion("contar_proyectos", (textobusqueda,))
            total_registros = total_registros[0][0][0] if total_registros else 0

            total_paginas = (total_registros + self.limit - 1) // self.limit
            pagina_actual = min((self.offset // self.limit) + 1, total_paginas)
            self.offset = max(0, (pagina_actual - 1) * self.limit)

            procedimiento = "buscar_proyectos"
            parametros = (textobusqueda, self.offset, self.limit)

        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, parametros)

        if len(datoresultante[0]) > 0:
            llenar_tabla_proyectos(self, self.venPri.tabla_proyecto, datoresultante[0])
        else:
            self.offset = max(0, self.offset - self.limit)
        self.actualizarInfoPaginacion("tutores", self.venPri.lbl_pagina_proyectos)
        
    def filtro_carreras(self):
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        textobusqueda = self.venPri.line_busqueda_carrera.text()

        if textobusqueda.strip() == "":
            procedimiento = "listar_carreras"
            parametros = (self.offset, self.limit)
        else:
            total_registros = self.conec_base.getDatosProcess_condicion("contar_carreras", (textobusqueda,))
            total_registros = total_registros[0][0][0] if total_registros else 0

            total_paginas = (total_registros + self.limit - 1) // self.limit
            pagina_actual = min((self.offset // self.limit) + 1, total_paginas)
            self.offset = max(0, (pagina_actual - 1) * self.limit)

            procedimiento = "buscar_carreras"
            parametros = (textobusqueda, self.offset, self.limit)

        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, parametros)

        if len(datoresultante[0]) > 0:
            llenar_tabla_carreras(self, self.venPri.tabla_carrera, datoresultante[0])
        else:
            self.offset = max(0, self.offset - self.limit)
        self.actualizarInfoPaginacion("carrera", self.venPri.lbl_pagina_carrera)

    def filtro_institucion(self):
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        textobusqueda = self.venPri.line_busqueda_inst.text()

        if textobusqueda.strip() == "":
            procedimiento = "listar_institucion"
            parametros = (self.offset, self.limit)
        else:
            total_registros = self.conec_base.getDatosProcess_condicion("contar_instituciones", (textobusqueda,))
            total_registros = total_registros[0][0][0] if total_registros else 0

            total_paginas = (total_registros + self.limit - 1) // self.limit
            pagina_actual = min((self.offset // self.limit) + 1, total_paginas)
            self.offset = max(0, (pagina_actual - 1) * self.limit)

            procedimiento = "buscar_instituciones"
            parametros = (textobusqueda, self.offset, self.limit)

        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, parametros)

        if len(datoresultante[0]) > 0:
            llenar_tabla_institucion(self, self.venPri.tabla_institucion, datoresultante[0])
        else:
            self.offset = max(0, self.offset - self.limit)
        self.actualizarInfoPaginacion("institucion", self.venPri.lbl_pagina_instituto)

    def datos_inicializacion(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
   
        respuesta_proyecto = self.conec_base.getDatos('SELECT id, nombre FROM proyecto')
        respuesta_periodoacademico = self.conec_base.getDatos('SELECT COALESCE((SELECT DISTINCT periodo_academico FROM vinculacion),"P1-2023") AS periodo_academico;')
        respuesta_tutores = self.conec_base.getDatos('SELECT id, CONCAT(nombres, " ", apellidos) AS nombres FROM tutores')


        self.venPri.cbo_filtro_proyecto.clear()
        self.venPri.cbo_filtro_proyecto.addItem("Seleccione proyecto", None)

        for id, nombre in respuesta_proyecto:
            self.venPri.cbo_filtro_proyecto.addItem(nombre, id)

        self.venPri.cbo_filtro_periodo.clear()
        self.venPri.cbo_filtro_periodo.addItem("Seleccione periodo academico", "P1-2023")

        for nombre_tuple in respuesta_periodoacademico:
            nombre = nombre_tuple[0]  
            self.venPri.cbo_filtro_periodo.addItem(nombre, nombre)


        self.venPri.cbo_filtro_tutor.clear()
        self.venPri.cbo_filtro_tutor.addItem("Seleccione tutor", None)

        for id, nombres in respuesta_tutores:
            self.venPri.cbo_filtro_tutor.addItem(nombres, id)

    def consultar_basedatos(self, tipo):
        if tipo == 'proyecto':
            proyecto_id = self.venPri.cbo_filtro_proyecto.currentData()
            self.llenarTablaFiltro('ObtenerListaVinculacionesPorFiltro', self.venPri.tabla_vinculacion, proyecto_id, 'proyecto')
            self.venPri.cbo_filtro_periodo.blockSignals(True)
            self.venPri.cbo_filtro_tutor.blockSignals(True)
            self.venPri.line_filtro_estudiante.blockSignals(True)
            self.venPri.cbo_filtro_periodo.setCurrentIndex(0)
            self.venPri.cbo_filtro_tutor.setCurrentIndex(0)
            self.venPri.line_filtro_estudiante.setText('')
            self.venPri.cbo_filtro_periodo.blockSignals(False)
            self.venPri.cbo_filtro_tutor.blockSignals(False)
            self.venPri.line_filtro_estudiante.blockSignals(False)
        elif tipo == 'periodo':
            periodo = self.venPri.cbo_filtro_periodo.currentData()
            print('periodo ', periodo)
            self.llenarTablaFiltro('ObtenerListaVinculacionesPorFiltro', self.venPri.tabla_vinculacion, periodo, 'periodo')
            self.venPri.cbo_filtro_proyecto.blockSignals(True)
            self.venPri.cbo_filtro_tutor.blockSignals(True)
            self.venPri.line_filtro_estudiante.blockSignals(True)
            self.venPri.cbo_filtro_proyecto.setCurrentIndex(0)
            self.venPri.cbo_filtro_tutor.setCurrentIndex(0)
            self.venPri.line_filtro_estudiante.setText('')
            self.venPri.cbo_filtro_proyecto.blockSignals(False)
            self.venPri.cbo_filtro_tutor.blockSignals(False)
            self.venPri.line_filtro_estudiante.blockSignals(False)
        elif tipo == 'tutor':
            tutor_id = self.venPri.cbo_filtro_tutor.currentData()
            self.llenarTablaFiltro('ObtenerListaVinculacionesPorFiltro', self.venPri.tabla_vinculacion, tutor_id, 'tutor')
            self.venPri.cbo_filtro_proyecto.blockSignals(True)
            self.venPri.cbo_filtro_periodo.blockSignals(True)
            self.venPri.line_filtro_estudiante.blockSignals(True)
            self.venPri.cbo_filtro_proyecto.setCurrentIndex(0)
            self.venPri.cbo_filtro_periodo.setCurrentIndex(0)
            self.venPri.line_filtro_estudiante.setText('')
            self.venPri.cbo_filtro_proyecto.blockSignals(False)
            self.venPri.cbo_filtro_periodo.blockSignals(False)
            self.venPri.line_filtro_estudiante.blockSignals(False)
        elif tipo == 'estudiante':
            text_param = self.venPri.line_filtro_estudiante.text().strip()
            self.llenarTablaFiltro('ObtenerListaVinculacionesPorEstudiante', self.venPri.tabla_vinculacion, text_param, 'estudiante')
            self.venPri.cbo_filtro_proyecto.blockSignals(True)
            self.venPri.cbo_filtro_periodo.blockSignals(True)
            self.venPri.cbo_filtro_tutor.blockSignals(True)
            self.venPri.cbo_filtro_proyecto.setCurrentIndex(0)
            self.venPri.cbo_filtro_periodo.setCurrentIndex(0)
            self.venPri.cbo_filtro_tutor.setCurrentIndex(0)
            self.venPri.cbo_filtro_proyecto.blockSignals(False)
            self.venPri.cbo_filtro_periodo.blockSignals(False)
            self.venPri.cbo_filtro_tutor.blockSignals(False)

    # def configuracion_ventana(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     limite = int(self.venPri.cbox_rango_reporte_tutor.currentText())
        
    #     lista_tutores = self.conec_base.getDatosProcess_condicion("listar_usuarios_tutor", (limite, ))
        
    #     if(len(lista_tutores)> 0):
    #         llenar_tabla_tutores(self, self.venPri.tabla_reporte_tutores, lista_tutores[0])
        
    #     periodo_academico = self.conec_base.getDatos('SELECT DISTINCT periodo_academico FROM ( SELECT periodo_academico FROM vinculaciones ORDER BY fecha_registro DESC ) AS subconsulta;')
        
    #     if(len(periodo_academico)):
    #         self.venPri.cbo_periodo_academico.clear()
    #         for periodo in periodo_academico:
    #             self.venPri.cbo_periodo_academico.addItem(periodo[0])
                
        
    #     self.cargaDatosEventoReporte()
        
    # def abrir_ventana_afiliacion(self):
    #     self.raizOpacidad.resize(self.width(), self.height())
    #     self.raizOpacidad.show()
    #     Vinculacion(parent = self).exec_()

    # def abrir_ventana_perfil(self):
    #     self.raizOpacidad.resize(self.width(), self.height())
    #     self.raizOpacidad.show()
    #     Perfil(parent = self, modo ='Nuevo').exec_()

    # def listar_vinculacion(self, datos=None):
        
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     limite = int(self.venPri.cbox_rango.currentText())
        
    #     if datos is None:
    #         datos = self.conec_base.getDatosProcess_condicion("ListarVinculaciones",(limite, ))

    #     if isinstance(datos, list) and datos:
    #         datos_a_insertar = datos[0]
    #         llenar_tabla_vinculacion(self, self.venPri.tabla_principal, datos_a_insertar)
    #     else:
    #         pass
    #         #print("Los datos obtenidos no son válidos o están vacíos. No se pudo llenar la tabla.")

    # def busqueda_vinculacion(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     textobusqueda =  self.venPri.line_busqueda.text()
    #     limite = int(self.venPri.cbox_rango.currentText())
        
    #     lista_vinculaciones = self.conec_base.getDatosProcess_condicion("BuscarVinculaciones", (textobusqueda, limite))
    #     self.listar_vinculacion(lista_vinculaciones)

    # def mostrar_vinculacion_rango(self, text):
    #     self.listar_vinculacion()

    # def listar_seguimiento_tutor(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     limite = int(self.venPri.cbox_rango_tutor.currentText())

    #     lista_seguimiento = self.conec_base.getDatosProcess_condicion('ObtenerSeguimientosConEstudiantes', (self.tutor_id, limite))
    #     llenar_tabla_seguimiento(self, self.venPri.tabla_principal_tutor, lista_seguimiento[0])

    # def listar_vinculacion_tutor(self, datos=None):
        
    #     if datos is None:
    #         self.listar_seguimiento_tutor()

    #     if isinstance(datos, list) and datos:
    #         datos_a_insertar = datos[0]
    #         llenar_tabla_seguimiento(self, self.venPri.tabla_principal_tutor, datos_a_insertar)
    #     else:
    #         pass


    # def busqueda_vinculacion_tutor(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return

    #     textobusqueda =  self.venPri.line_busqueda_tutor.text()
    #     limite = int(self.venPri.cbox_rango_tutor.currentText())

    #     lista_vinculaciones_tutor = self.conec_base.getDatosProcess_condicion("filtrarSeguimientosConEstudiantes", (self.tutor_id, limite, textobusqueda,))
    #     self.listar_vinculacion_tutor(lista_vinculaciones_tutor)


    # def mostrar_vinculacion_rango_tutor(self, text):
    #     self.listar_vinculacion_tutor()
        
    # def listar_usuarios(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return

    #     resultado  = self.conec_base.getDatosProcess('ListarUsuarios')
    #     if(len(resultado) > 0):
    #         resultado = resultado[0]
    #         llenar_tabla_usuario(self, self.venPri.tabla_usuario, resultado)


    # def busqueda_usuarios_filtro(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return

    #     texto_busqueda = self.venPri.line_busqueda_usuario.text().strip()

    #     resultado = self.conec_base.getDatosProcess_condicion('filtrarUsuarios', (texto_busqueda,))
    #     if(len(resultado) > 0):
    #         resultado = resultado[0]
    #         llenar_tabla_usuario(self, self.venPri.tabla_usuario, resultado)
    #     else:
    #         self.listar_usuarios()


    # def mostrar_formulario_instituciones(self):
        
    #     self.raizOpacidad.resize(self.width(), self.height())
    #     self.raizOpacidad.show()
    #     Instituciones(parent = self, modo='Nuevo').exec_()


    # def mostrar_formulario_proyectos(self):
    #     self.raizOpacidad.resize(self.width(), self.height())
    #     self.raizOpacidad.show()
    #     Proyectos(parent = self, modo='Nuevo').exec_()


    # def llenado_instituciones(self, estado):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     respuesta = self.conec_base.getDatosProcess_condicion('ListarInstitucionesPorEstado' , (estado, ))
    #     if(respuesta):
    #         respuesta = respuesta[0]
    #         llenar_tabla_institucion(self, self.venPri.tabla_intituciones, respuesta)


    # def mostrar_instituciones_estado(self):

    #     estado = 'Inactivo' if self.venPri.check_estado_institucion.isChecked() else 'Activo'
    #     self.llenado_instituciones(estado)

    # def llenado_proyectos(self, estado):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return

    #     respuesta = self.conec_base.getDatosProcess_condicion('ListarProyectosPorEstado' , (estado, ))
    #     if(respuesta):
    #         respuesta = respuesta[0]
    #         llenar_tabla_proyectos(self, self.venPri.tabla_proyectos, respuesta)

    # def mostrar_proyectos_estado(self):

    #     estado = 'Inactivo' if self.venPri.check_estado_proyectos.isChecked() else 'Activo'
    #     self.llenado_proyectos(estado)

    # def llenado_reporte(self, estado, tabla, procedimiento, limite, condicion=0):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     if(condicion != 0):
    #         respuesta = self.conec_base.getDatosProcess_condicion( procedimiento , (estado,limite,condicion, ))
    #     else:                                                                 
    #         respuesta = self.conec_base.getDatosProcess_condicion( procedimiento , (estado,limite ))
            
  
    #     if(respuesta):
    #         respuesta = respuesta[0]
    #         self.lista_estudiante_filtro = respuesta
            
    #         cargar_tabla(tabla, respuesta)
            
    # def filtro_reporte(self, estado , tipo, consulta):
        
    #     if(tipo == 'Estudiante'):
    #         limite = int(self.venPri.cbox_rango_estudiantes.currentText())
    #         self.llenado_reporte(estado , self.venPri.tabla_reporte_estudiantes, consulta, limite)

    # def evento_obtener_reporte_general(self):
    #     if self.venPri.check_todos_estudiantes.isChecked():
    #         self.venPri.radioCulminadoE.setEnabled(True)
    #         self.venPri.radioProcesoE.setEnabled(True)
    #         self.venPri.radioPendienteE.setEnabled(True)
    #         self.venPri.line_busqueda_reporte_estudiantes.setEnabled(False)
    #         estado = ''
    #         self.venPri.line_busqueda_reporte_estudiantes.setText('')
            
    #         if self.venPri.radioPendienteE.isChecked():
    #             estado = 'Pendiente'
    #         elif self.venPri.radioProcesoE.isChecked():
    #             estado = 'En Progreso'
    #         else:
    #             estado = 'Culminado'
                
    #         self.filtro_reporte(estado, 'Estudiante', 'obtenerInformacionVinculacionesConEstado')
    #     else:
    #         self.venPri.line_busqueda_reporte_estudiantes.setEnabled(True)
    #         self.venPri.radioCulminadoE.setEnabled(False)
    #         self.venPri.radioProcesoE.setEnabled(False)
    #         self.venPri.radioPendienteE.setEnabled(False)
    
    # def busqueda_datos_estudiante(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     self.venPri.check_todos_estudiantes.setChecked(False)
    #     self.evento_obtener_reporte_general()
    #     parametro_busqueda = self.venPri.line_busqueda_reporte_estudiantes.text().strip()
    #     respuesta = self.conec_base.getDatosProcess_condicion( 'obtenerInformacionVinculacionesConEstadoYBusqueda' , (parametro_busqueda, ))
        
  
        
    #     if(respuesta):
        
    #         respuesta = respuesta[0]
            
    #         self.lista_estudiante_filtro = respuesta
            
    #         cargar_tabla(self.venPri.tabla_reporte_estudiantes, respuesta)
            
    # def llenar_combobox(self, combobox, lista, longitud_maxima):
    #     for elemento in lista:
    #         id_elemento, nombre_elemento = elemento
    #         texto_truncado = nombre_elemento[:longitud_maxima]
    #         combobox.addItem(texto_truncado, userData=id_elemento)
    #         combobox.setItemData(combobox.count() - 1, nombre_elemento, Qt.ToolTipRole)
            
    # def evento_obtener_tutores_limite(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
        
    #     limite = int(self.venPri.cbox_rango_reporte_tutor.currentText())
        
    #     lista_tutores = self.conec_base.getDatosProcess_condicion("listar_usuarios_tutor", (limite, ))
        
    #     if(len(lista_tutores)> 0):
            
    #         llenar_tabla_tutores(self, self.venPri.tabla_reporte_tutores, lista_tutores[0])
            

    # def busqueda_tutor_reporte(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return

    #     textobusqueda = self.venPri.line_busqueda_reporte_tutor.text()
    #     limite = int(self.venPri.cbox_rango_reporte_tutor.currentText())

    #     if textobusqueda:
    #         lista_tutor = self.conec_base.getDatosProcess_condicion("buscar_tutor_criterio", (textobusqueda,))
    #     else:
    #         lista_tutor = self.conec_base.getDatosProcess_condicion("listar_usuarios_tutor", (limite,))
            
    #     if not lista_tutor:
    #         QtWidgets.QMessageBox.information(self, "Información", "No se encontraron resultados.")
    #         return
        
    #     llenar_tabla_tutores(self, self.venPri.tabla_reporte_tutores, lista_tutor[0])

        
    # def cambioPagina(self):
        
    #     tipo_accion = self.venPri.cbo_tipo_entrega.currentText()
        
    #     if(tipo_accion == 'Informe'):
    #         self.venPri.stackedWidget_2.setCurrentIndex(0)
    #     else:
    #         self.venPri.stackedWidget_2.setCurrentIndex(1)
        
    #     self.cargaDatosEventoReporte()

            
    # def cargaDatosEventoReporte(self):
        
    #     periodo_actual_seleccionado = self.venPri.cbo_periodo_academico.currentText()
                
    #     datos_informes = self.conec_base.getDatosProcess_condicion('listar_informes_por_periodo_academico', (periodo_actual_seleccionado, ))
        
    #     if(len(datos_informes)> 0):
            
    #         datos_informes = datos_informes[0]
            
    #         self.lista_informes_filtro = datos_informes
            
    #         cargar_tabla_reporte_informes(self.venPri.tabla_reporte_informe_tutor, datos_informes)
            
            
        
    #     datos_fichas = self.conec_base.getDatosProcess_condicion('consulta_fichas', (periodo_actual_seleccionado, ))
        
    #     if(len(datos_fichas)> 0):
            
    #         datos_fichas = datos_fichas[0]
            
    #         self.lista_ficha_filtro = datos_fichas
            
    #         cargar_tabla_reporte_ficha_memorandum(self.venPri.tabla_reporte_ficha_tutor, datos_fichas)
            
            
    #     datos_memorandum = self.conec_base.getDatosProcess_condicion('consulta_memorandum', (periodo_actual_seleccionado, ))
        
    #     if(len(datos_memorandum)> 0):
            
    #         datos_memorandum = datos_memorandum[0]

    #         self.lista_memorandun_filtro = datos_memorandum
            
    #         cargar_tabla_reporte_ficha_memorandum(self.venPri.tabla_reporte_memorandum_tutor, datos_memorandum)
            
    # def eventoSeleccionPeriodo(self):
        
    #     self.cargaDatosEventoReporte()
        
    # def reporte_estudiantes(self):
        
    #     from controllers.Modulo_reporte.generarRepoInforme import FormRepoImforme
        
        
    #     if(len(self.lista_estudiante_filtro)> 0):
            
    #         print(self.lista_estudiante_filtro)
        
    #         FormRepoImforme(self.lista_estudiante_filtro, 'estudiantes', '').exec_()
            
    #     else:
            
    #         QtWidgets.QMessageBox.critical(self, "Error", "No ha realizado ningún filtro.")
            
    
    # def generarReporte_informe(self):
        
    #     from controllers.Modulo_reporte.generarRepoInforme import FormRepoImforme
        
        
    #     if(len(self.lista_informes_filtro)> 0):
            
    #         periodo_actual_seleccionado = self.venPri.cbo_periodo_academico.currentText()
    #         FormRepoImforme(self.lista_informes_filtro, 'informe', periodo_actual_seleccionado).exec_()
            
    #     else:
            
    #         QtWidgets.QMessageBox.critical(self, "Error", "No ha realizado ningún filtro.")
            
            
    # def generarReporte_ficha(self):
        
    #     from controllers.Modulo_reporte.generarRepoInforme import FormRepoImforme
        
        
    #     if(len(self.lista_ficha_filtro)> 0):
            
    #         periodo_actual_seleccionado = self.venPri.cbo_periodo_academico.currentText()
            
    #         FormRepoImforme(self.lista_ficha_filtro, 'ficha', periodo_actual_seleccionado).exec_()
            
    #     else:
            
    #         QtWidgets.QMessageBox.critical(self, "Error", "No ha realizado ningún filtro.")
            
    # def generarReporte_memorandum(self):
        
        # from controllers.Modulo_reporte.generarRepoInforme import FormRepoImforme
        
        
        # if(len(self.lista_memorandun_filtro)> 0):
            
        #     periodo_actual_seleccionado = self.venPri.cbo_periodo_academico.currentText()
            
        #     FormRepoImforme(self.lista_memorandun_filtro, 'memorandum', periodo_actual_seleccionado).exec_()
            
        # else:
            
        #     QtWidgets.QMessageBox.critical(self, "Error", "No ha realizado ningún filtro.")