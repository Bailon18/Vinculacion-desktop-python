
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import QTimer
from PySide2.QtCore import Qt
from controllers.Modulo_Vinculacion.Modulo_Vinculacion import Vinculacion
from controllers.Modulo_administracion.Carreras_administracion import CarrerasAdmin
from controllers.Modulo_administracion.Estudiantes_administracion import EstudiantesAdmin
from controllers.Modulo_administracion.Instituciones_administracion import InstitucionesAdmin
from controllers.Modulo_administracion.Proyectos_administracion import ProyectosAdmin
from controllers.Modulo_administracion.Tutores_administracion import TutoresAdmin
from controllers.Modulo_seguimiento.Modulo_actividad import FormularioSeguimientoEstudiante
from controllers.Modulo_seguimiento.funcion_seguimiento import llenar_tabla_seguimiento_tutor
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
        
        self.configuracion_ventana()
        self.rol = args[0][2]
        self.tutor_id = args[0][0]
        self.venPri.lbl_usuario.setText(str(args[0][1])) 
        self.venPri.lbl_rol.setText(args[0][2])
        
        self.args = args
        

        self.cambioPagina()
        self.datos_inicializacion()


        if(self.rol != 'Administrador'):
            
            self.showEvent = self.customShowEvent
            self.venPri.btn_afiliacion.setHidden(True)
            self.venPri.btn_usuario.setHidden(True)
            self.venPri.btn_reporte.setHidden(True)
            self.venPri.btn_home.setHidden(True)
            #self.venPri.btn_seguimientoo.setHidden(True)
            self.venPri.cbo_filtro_tutor_seguimiento.setHidden(True)
            evento_pagina(self,1, self.venPri.btn_seguimientoo)
            
        else:
            
            #self.venPri.btn_seguimientoo.setHidden(True)
            self.venPri.btn_home.setHidden(False)
            evento_pagina(self,0, self.venPri.btn_afiliacion)
        
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
        self.venPri.btn_agregar_usuario.clicked.connect(lambda: self.abrir_ventana_usuarios())
        
        
        # filtro evento busquedas
        self.venPri.line_busqueda_estudiantes.textChanged.connect(lambda: self.filtro_estudiante())
        self.venPri.line_busqueda_tutores.textChanged.connect(lambda: self.filtro_tutores())
        self.venPri.line_busqueda_proyecto.textChanged.connect(lambda: self.filtro_proyectos())
        self.venPri.line_busqueda_carrera.textChanged.connect(lambda: self.filtro_carreras())
        self.venPri.line_busqueda_inst.textChanged.connect(lambda: self.filtro_institucion())
        self.venPri.line_busqueda_usuario.textChanged.connect(lambda: self.filtro_usuarios())
        
        
        self.venPri.cbox_perfil.activated.connect(lambda: self.evento_perfil())
     

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
        
        
    
        self.venPri.btn_afiliacion.clicked.connect(lambda: evento_pagina(self, 0, self.venPri.btn_afiliacion))
        self.venPri.btn_seguimientoo.clicked.connect(lambda: evento_pagina(self, 1, self.venPri.btn_seguimientoo))
        self.venPri.btn_home.clicked.connect(lambda: evento_pagina(self, 2, self.venPri.btn_home))
        self.venPri.btn_usuario.clicked.connect(lambda: evento_pagina(self, 3, self.venPri.btn_usuario))
        self.venPri.btn_reporte.clicked.connect(lambda: evento_pagina(self, 4, self.venPri.btn_reporte))
        
        
        
        self.venPri.check_estado_estudiantes.clicked.connect(lambda: self.mostrar_culminado_estudiantes('estado_estudiantes'))
        self.venPri.check_estado_tutores.clicked.connect(lambda: self.mostrar_inactivo_tutores('estado_tutores'))
        self.venPri.check_estado_proyecto.clicked.connect(lambda: self.mostrar_inactivo_proyectos('estado_proyectos'))
        self.venPri.check_estado_carrera.clicked.connect(lambda: self.mostrar_inactivo_carreras('estado_carreras'))
        self.venPri.check_estado_insti.clicked.connect(lambda: self.mostrar_inactivo_instituciones('estado_instituciones'))


        
        evento_seleccion_reporte(self, self.venPri.radioEstudiante, 2)
        self.venPri.radioEstudiante.clicked.connect(lambda: evento_seleccion_reporte(self, self.venPri.radioEstudiante, 2))
        self.venPri.radioTutor.clicked.connect(lambda: evento_seleccion_reporte(self, self.venPri.radioTutor, 0))
        self.venPri.radioreporteentrega.clicked.connect(lambda: evento_seleccion_reporte(self, self.venPri.radioreporteentrega, 1))
        


        self.venPri.cbo_tipo_entrega.activated.connect(lambda: self.cambioPagina())
        self.venPri.cbo_periodo_academico.activated.connect(lambda: self.eventoSeleccionPeriodo())
        
        self.venPri.btn_export.clicked.connect(lambda: self.reporte_estudiantes())
        self.venPri.btn_export_2.clicked.connect(lambda: self.generarReporte_informe())
        self.venPri.btn_export_3.clicked.connect(lambda: self.generarReporte_ficha())
        self.venPri.btn_export_4.clicked.connect(lambda: self.generarReporte_memorandum())
        
        
        self.offset = 0
        self.limit = 5
        

        self.textobusqueda = ""
        self.estudiantes_vinculacion_id = None
        self.estudiantes_vinculacion_nombre = None
        self.modo_formulario_seguimiento_estudiante = 'nuevo'
        self.id_actividad = 0

        
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
        
        self.venPri.btn_pag_antes_user.clicked.connect(lambda: self.prev_page('listar_usuarios', 'usuarios', self.venPri.lbl_pagina_user, self.venPri.tabla_usuario))
        self.venPri.btn_pag_desp_user.clicked.connect(lambda: self.next_page('listar_usuarios', 'usuarios', self.venPri.lbl_pagina_user, self.venPri.tabla_usuario))
        
    
        # Inicializar la tabla con la primera página
        self.llenarTabla('listar_estudiantes', 'estudiantes', self.venPri.tabla_estudiantes)
        self.actualizarInfoPaginacion('estudiantes', self.venPri.lbl_pagina_estudiantes, True )
        
        self.llenarTabla('listar_tutores', 'tutores', self.venPri.tabla_tutores)
        self.actualizarInfoPaginacion('tutores', self.venPri.lbl_pagina_tutores, True )
        
        self.llenarTabla('listar_proyectos', 'proyecto', self.venPri.tabla_proyecto)
        self.actualizarInfoPaginacion('proyecto', self.venPri.lbl_pagina_proyectos, True )
        
        self.llenarTabla('listar_carreras', 'carrera', self.venPri.tabla_carrera)
        self.actualizarInfoPaginacion('carrera', self.venPri.lbl_pagina_carrera, True )
        
        self.llenarTabla('listar_institucion', 'institucion', self.venPri.tabla_institucion)
        self.actualizarInfoPaginacion('institucion', self.venPri.lbl_pagina_instituto, True )
        
        self.llenarTabla('ObtenerListaVinculaciones', 'vinculacion', self.venPri.tabla_vinculacion)
        self.actualizarInfoPaginacion('vinculacion', self.venPri.lbl_pagina_vinculacion, True )
        
        self.llenarTabla('listar_usuarios', 'usuarios', self.venPri.tabla_usuario)
        self.actualizarInfoPaginacion('usuarios', self.venPri.lbl_pagina_user, True )
        
        
        self.llenarTablaReporte01('listar_estudiantes_vinculacion_por_estado', self.venPri.tabla_reporte_estudiantes, 'En proceso')
        self.actualizarInfoPaginacion_reporte(self.venPri.lbl_pagina_reporte01, 'contar_estudiantes_vinculacion_por_estado', 'En proceso')
        
        self.llenarTabla('listar_tutores', 'tutores', self.venPri.tabla_reporte_tutores)
        self.actualizarInfoPaginacion('tutores', self.venPri.lbl_pagina_reporte02, True )
       
        
        self.venPri.btn_pag_antes_reporte01.clicked.connect(lambda: self.prev_page(
                'listar_estudiantes_vinculacion_por_estado',self.venPri.lbl_pagina_reporte01, self.venPri.tabla_reporte_estudiantes, 'contar_estudiantes_vinculacion_por_estado' ))
        self.venPri.btn_pag_desp_reporte01.clicked.connect(lambda: self.next_page(
                'listar_estudiantes_vinculacion_por_estado',self.venPri.lbl_pagina_reporte01, self.venPri.tabla_reporte_estudiantes,  'contar_estudiantes_vinculacion_por_estado'))
        
        
        self.venPri.btn_pag_antes_reporte02.clicked.connect(lambda: self.prev_page('listar_tutores', 'tutores', self.venPri.lbl_pagina_reporte02, self.venPri.tabla_reporte_tutores))
        self.venPri.btn_pag_desp_reporte02.clicked.connect(lambda: self.next_page('listar_tutores', 'tutores', self.venPri.lbl_pagina_reporte02, self.venPri.tabla_reporte_tutores))
        
        self.venPri.radioProcesoE.clicked.connect(lambda: self.filtro_reporte_estudiante('En proceso'))
        self.venPri.radioPendienteE.clicked.connect(lambda: self.filtro_reporte_estudiante('Pendiente'))
        self.venPri.radioCulminadoE.clicked.connect(lambda: self.filtro_reporte_estudiante('Culminado'))
        
        
        self.venPri.line_busqueda_reporte_estudiantes.textChanged.connect(lambda: self.busqueda_datos_estudiante())
        
        # Eventos de combobox filtro en vinculacion
        self.venPri.cbo_filtro_proyecto.activated.connect(lambda: self.consultar_basedatos('proyecto'))
        self.venPri.cbo_filtro_periodo.activated.connect(lambda: self.consultar_basedatos('periodo'))
        self.venPri.cbo_filtro_tutor.activated.connect(lambda: self.consultar_basedatos('tutor'))
        self.venPri.line_filtro_estudiante.textChanged.connect(lambda: self.consultar_basedatos('estudiante'))
        
                
        self.periodo_academico = '' 

        self.venPri.cbo_filtro_tutor_seguimiento.activated.connect(lambda: self.consultar_filtro_seguimiento_tutor())
        self.venPri.cbo_filtro_periodo_seguimiento.activated.connect(lambda: self.consultar_filtro_seguimiento_periodo())
        self.venPri.cbo_filtro_proyecto_seguimiento.activated.connect(lambda: self.llenar_estudiantes_seguimientos_tutor())
        
        self.consultar_filtro_seguimiento_periodo()

        
    def customShowEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(0, self.validar_sesiones)
        

    
    def validar_sesiones(self):
        
        print('cantidasd ', self.venPri.cbo_filtro_periodo_seguimiento.count())
        if self.venPri.cbo_filtro_periodo_seguimiento.count() <= 1:
            QtWidgets.QMessageBox.warning(self, "Sin Asignación", "Usted aún no está asignado a ninguna vinculación.")
            self.venPri.cbo_filtro_periodo_seguimiento.setCurrentIndex(0)
            self.venPri.cbo_filtro_proyecto_seguimiento.setCurrentIndex(0)
        
    def evento_perfil(self):
        
        from controllers.Modulo_administracion.Tutores_administracion import TutoresAdmin
        
        if self.venPri.cbox_perfil.currentIndex() == 0:
            self.raizOpacidad.resize(self.width(), self.height())
            self.raizOpacidad.show()
            
            if(self.args[0][2] != 'Administrador'):
                TutoresAdmin(self, 'editar', self.tutor_id).exec_()    
            else:
                Perfil(self, 'Editar', [self.tutor_id, self.args[0][1]]).exec_()
            
            
           
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
        
    def abrir_ventana_nueva_actividad(self):
        
        print('Abrir ventana nueva actividad')

        if(self.estudiantes_vinculacion_id != None):
            self.raizOpacidad.resize(self.width(), self.height())
            self.raizOpacidad.show()
            FormularioSeguimientoEstudiante(self, self.id_actividad, '', self.estudiantes_vinculacion_id, self.modo_formulario_seguimiento_estudiante).exec_()
        else:
            QtWidgets.QMessageBox.information(self, 'Error', 'Debe seleccionar un estudiante para visualizar o agregar su actividad.')
            
    def abrir_ventana_seguimiento_tutor(self):
        
        from controllers.Modulo_seguimiento.Modulo_seguimiento import Seguimiento

        if(self.estudiantes_vinculacion_id != None and self.estudiantes_vinculacion_nombre!= None):
            self.raizOpacidad.resize(self.width(), self.height())
            self.raizOpacidad.show()
            Seguimiento(self, self.estudiantes_vinculacion_id, self.estudiantes_vinculacion_nombre).exec_()
        else:
            QtWidgets.QMessageBox.information(self, 'Error', 'Debe seleccionar un estudiante para visualizar su actividad.')
            
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
        Vinculacion(parent=self, modo='nuevo').exec_()

    def abrir_ventana_usuarios(self):
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        Perfil(parent=self, modo='nuevo',dato=[]).exec_()
       
    def llenarTablaFiltro(self, procedimiento, tabla_diseno, param, tipo):
        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, [tipo, param,  self.offset, self.limit])
        
        if len(datoresultante) > 0 and len(datoresultante[0]) > 0:
            llenar_tabla_vinculacion(self, tabla_diseno, datoresultante[0])
        else:
            QtWidgets.QMessageBox.warning(self, 'Información', f'No se encontró ninguna vinculación con el nombre del {tipo} seleccionado.')
            self.llenarTabla('ObtenerListaVinculaciones', 'vinculacion', self.venPri.tabla_vinculacion)
            self.actualizarInfoPaginacion('vinculacion', self.venPri.lbl_pagina_vinculacion, True)    
       
       
    def mostrar_culminado_estudiantes(self, estado_estudiantes):
        
        estado = True
        
        self.offset = 0
        
        if self.venPri.check_estado_estudiantes.isChecked():
            self.llenarTabla('listar_estudiantes_inactivos', 'estudiantes', self.venPri.tabla_estudiantes)
            estado = False

        else:
            self.llenarTabla('listar_estudiantes', 'estudiantes', self.venPri.tabla_estudiantes)
            estado = True

        self.actualizarInfoPaginacion('estudiantes', self.venPri.lbl_pagina_estudiantes, estado, estado_estudiantes)
        
    def mostrar_inactivo_tutores(self, estado_tutores):
   
        
        estado = True
        self.offset = 0
        
        if self.venPri.check_estado_tutores.isChecked():
            self.llenarTabla('listar_tutores_inactivos', 'tutores', self.venPri.tabla_tutores)
            estado = False
        else:
            self.llenarTabla('listar_tutores', 'tutores', self.venPri.tabla_tutores)
            estado = True
            
        self.actualizarInfoPaginacion('tutores', self.venPri.lbl_pagina_tutores, estado, estado_tutores)
        
    def mostrar_inactivo_proyectos(self, estado_proyectos):
        
        estado = True
        self.offset = 0
        
        if self.venPri.check_estado_proyecto.isChecked():
            self.llenarTabla('listar_proyectos_inactivos', 'proyecto', self.venPri.tabla_proyecto)
            estado = False
        else:
            self.llenarTabla('listar_proyectos', 'proyecto', self.venPri.tabla_proyecto)
            estado = True
            
        self.actualizarInfoPaginacion('proyecto', self.venPri.lbl_pagina_proyectos, estado, estado_proyectos)
        
    def mostrar_inactivo_carreras(self, estado_carreras):
        
        estado = True
        self.offset = 0
        
        if self.venPri.check_estado_carrera.isChecked():
            self.llenarTabla('listar_carreras_inactivas', 'carrera', self.venPri.tabla_carrera)
            estado = False
        else:
            self.llenarTabla('listar_carreras', 'carrera', self.venPri.tabla_carrera)
            estado = True
            
        self.actualizarInfoPaginacion('carrera', self.venPri.lbl_pagina_carrera, estado, estado_carreras)
        
    def mostrar_inactivo_instituciones(self, estado_institucion):
        
        estado = True
        self.offset = 0
        
        if self.venPri.check_estado_insti.isChecked():
            self.llenarTabla('listar_instituciones_inactivas', 'institucion', self.venPri.tabla_institucion)
            estado = False
        else:
            self.llenarTabla('listar_institucion', 'institucion', self.venPri.tabla_institucion)
            estado = True
            
        self.actualizarInfoPaginacion('institucion', self.venPri.lbl_pagina_instituto, estado, estado_institucion)
       
       
    def llenarTabla(self, procedimiento, tabla,  tabla_diseno):
        
        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, [self.offset, self.limit])

        if(tabla == 'estudiantes' and datoresultante):
            llenar_tabla_estudiantes(self, tabla_diseno, datoresultante[0])
 
        elif tabla == 'tutores' and tabla_diseno.objectName() == 'tabla_tutores' and datoresultante:
            llenar_tabla_tutores(self, tabla_diseno, datoresultante[0])
        elif tabla == 'tutores' and tabla_diseno.objectName() == 'tabla_reporte_tutores' and datoresultante:
            llenar_tabla_tutores_reportes(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'proyecto' and datoresultante):
            llenar_tabla_proyectos(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'carrera' and datoresultante):
            llenar_tabla_carreras(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'institucion' and datoresultante):
            llenar_tabla_institucion(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'vinculacion' and datoresultante):
            llenar_tabla_vinculacion(self, tabla_diseno, datoresultante[0])
        elif(tabla == 'usuarios' and datoresultante):
            llenar_tabla_usuario(self, tabla_diseno, datoresultante[0])
        # elif(tabla == 'reporte02' and datoresultante):
        #     llenar_tabla_usuario(self, tabla_diseno, datoresultante[0])
            
    def next_page(self, procedimiento, tabla, labels, tabla_diseno):
        self.offset += self.limit
        estado = True
        
        
        
        if tabla == 'estudiantes' and self.venPri.check_estado_estudiantes.isChecked():
            procedimiento = 'listar_estudiantes_inactivos'
            estado = False
            
        elif tabla == 'tutores' and self.venPri.check_estado_tutores.isChecked() and tabla_diseno.objectName() == 'tabla_tutores':
            procedimiento = 'listar_tutores_inactivos'
            estado = False
        
        elif tabla == 'tutores' and tabla_diseno.objectName() == 'tabla_reporte_tutores':
            procedimiento = procedimiento
            estado = True
            
        elif tabla == 'proyecto' and self.venPri.check_estado_proyecto.isChecked():
            procedimiento = 'listar_proyectos_inactivos'
            estado = False
            
        elif tabla == 'carrera' and self.venPri.check_estado_carrera.isChecked():
            procedimiento = 'listar_carreras_inactivas'
            estado = False
            
        elif tabla == 'institucion' and self.venPri.check_estado_insti.isChecked():
            procedimiento = 'listar_instituciones_inactivas'
            estado = False
        
        datoretorno = self.conec_base.getDatosProcess_condicion(procedimiento, [self.offset, self.limit])
    
        if len(datoretorno[0]) > 0:
            self.llenarTabla(procedimiento, tabla, tabla_diseno)
        else:
            self.offset -= self.limit 
        
        self.actualizarInfoPaginacion(tabla, labels, estado)

    def prev_page(self, procedimiento, tabla, labels, tabla_diseno):
        
        estado = True
        self.offset = max(0, self.offset - self.limit)
        
        if tabla == 'estudiantes' and self.venPri.check_estado_estudiantes.isChecked():
            procedimiento = 'listar_estudiantes_inactivos'
            estado = False
            

        elif tabla == 'tutores' and self.venPri.check_estado_tutores.isChecked() and tabla_diseno.objectName() == 'tabla_tutores':
            procedimiento = 'listar_tutores_inactivos'
            estado = False
        
        elif tabla == 'tutores' and tabla_diseno.objectName() == 'tabla_reporte_tutores':
            procedimiento = procedimiento
            estado = True
            
        elif tabla == 'proyecto' and self.venPri.check_estado_proyecto.isChecked():
            procedimiento = 'listar_proyectos_inactivos'
            estado = False
            
        elif tabla == 'carrera' and self.venPri.check_estado_carrera.isChecked():
            procedimiento = 'listar_carreras_inactivas'
            estado = False
            
        elif tabla == 'institucion' and self.venPri.check_estado_insti.isChecked():
            procedimiento = 'listar_instituciones_inactivas'
            estado = False
        
        self.llenarTabla(procedimiento, tabla, tabla_diseno)
        self.actualizarInfoPaginacion(tabla, labels, estado)
        
    def actualizarInfoPaginacion(self, nombreTabla, labels, estado, estado2 = None):
        
   
        query = f"SELECT COUNT(*) FROM {nombreTabla} WHERE estado = {estado}"
        total_registros = self.conec_base.getDatos(query)
        
  
        estadomensaje = 'Activo' if estado == True else 'Inactivo'
        
        if total_registros[0][0] == 0 and estado2 != None:
            QtWidgets.QMessageBox.warning(self, "Sin datos", f"No se encontraron datos de {nombreTabla} con el estado {estadomensaje}.")
            self.venPri.check_estado_estudiantes.setChecked(False)
            self.venPri.check_estado_tutores.setChecked(False)
            self.venPri.check_estado_proyecto.setChecked(False)
            self.venPri.check_estado_carrera.setChecked(False)
            self.venPri.check_estado_insti.setChecked(False)
            return
            
        
        total_registros = total_registros[0][0] if total_registros else 0
        
        total_paginas = (total_registros + self.limit - 1) // self.limit
        
        pagina_actual = (self.offset // self.limit) + 1
        
        if pagina_actual > total_paginas:
            pagina_actual = total_paginas
        
        if pagina_actual < 1:
            pagina_actual = 1
        
        labels.setText(f"Página {pagina_actual} de {total_paginas}")

    def llenarTablaReporte01(self, procedimiento,  tabla_diseno, condicion):

        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, [condicion, self.offset, self.limit])
        if(datoresultante):
            cargar_tabla_reporte_estudiante(tabla_diseno, datoresultante[0])

    def next_page_reporte(self, procedimiento, labels, tabla_diseno, procedimiento_count):
        
        condicion = 'Pendiente' if self.venPri.radioPendienteE.isChecked() else ('En Proceso' if self.venPri.radioProcesoE.isChecked() else 'Culminado')
        
        self.offset += self.limit

        datoretorno = self.conec_base.getDatosProcess_condicion(procedimiento, [condicion, self.offset, self.limit])
        if len(datoretorno[0]) > 0:
            self.llenarTablaReporte01(procedimiento, tabla_diseno, condicion)
        else:
            self.offset -= self.limit 
        self.actualizarInfoPaginacion_reporte(labels, procedimiento_count, condicion)

    def prev_page_reporte(self, procedimiento, labels, tabla_diseno, procedimiento_count):
        
        condicion = 'Pendiente' if self.venPri.radioPendienteE.isChecked() else ('En Proceso' if self.venPri.radioProcesoE.isChecked() else 'Culminado')
        
        print(f'condicion: {condicion}')
        
        self.offset = max(0, self.offset - self.limit)
        self.llenarTablaReporte01(procedimiento, tabla_diseno, condicion)
        self.actualizarInfoPaginacion_reporte(labels, procedimiento_count, condicion)
        
    def actualizarInfoPaginacion_reporte(self,labels, procedimiento_count  , condicion ):

        total_registros = self.conec_base.getDatosProcess_condicion(procedimiento_count, [condicion,])
     
        total_registros = total_registros[0][0] if total_registros else 0
        
        total_paginas = (total_registros[0] + self.limit - 1) // self.limit
        
        pagina_actual = (self.offset // self.limit) + 1
        
        if pagina_actual > total_paginas:
            pagina_actual = total_paginas
        
        if pagina_actual < 1:
            pagina_actual = 1
        
        labels.setText(f"Página {pagina_actual} de {total_paginas}")
        
    def filtro_reporte_estudiante(self, estado):
        
        self.venPri.line_busqueda_reporte_estudiantes.setText('')
        self.offset = 0
        
        self.llenarTablaReporte01('listar_estudiantes_vinculacion_por_estado', self.venPri.tabla_reporte_estudiantes, estado)
        self.actualizarInfoPaginacion_reporte(self.venPri.lbl_pagina_reporte01, 'contar_estudiantes_vinculacion_por_estado', estado)

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
        self.actualizarInfoPaginacion("estudiantes", self.venPri.lbl_pagina_estudiantes, True)
        
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
            llenar_tabla_tutores(self, self.venPri.tabla_tutores, datoresultante[0])
        else:
            self.offset = max(0, self.offset - self.limit)
        self.actualizarInfoPaginacion("tutores", self.venPri.lbl_pagina_tutores, True)
        
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
        self.actualizarInfoPaginacion("tutores", self.venPri.lbl_pagina_proyectos, True)
        
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
        self.actualizarInfoPaginacion("carrera", self.venPri.lbl_pagina_carrera, True)

    def filtro_institucion(self):
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        textobusqueda = self.venPri.line_busqueda_inst.text()

        if textobusqueda.strip() == "":
            procedimiento = "listar_institucion"
            parametros = (self.offset, self.limit)
        else:
            total_registros = self.conec_base.getDatosProcess_condicion("contar_instituciones", (textobusqueda,)) # id, nombre, telefono, estado 
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
        self.actualizarInfoPaginacion("institucion", self.venPri.lbl_pagina_instituto, True)
        
    def filtro_usuarios(self):
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        textobusqueda = self.venPri.line_busqueda_usuario.text()

        if textobusqueda.strip() == "":
            procedimiento = "listar_usuarios"
            parametros = (self.offset, self.limit)
        else:
            total_registros = self.conec_base.getDatosProcess_condicion("contar_usuarios", (textobusqueda,))
            total_registros = total_registros[0][0][0] if total_registros else 0

            total_paginas = (total_registros + self.limit - 1) // self.limit
            pagina_actual = min((self.offset // self.limit) + 1, total_paginas)
            self.offset = max(0, (pagina_actual - 1) * self.limit)

            procedimiento = "buscar_usuarios"
            parametros = (textobusqueda, self.offset, self.limit)

        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, parametros)

        if len(datoresultante[0]) > 0:
            llenar_tabla_usuario(self, self.venPri.tabla_usuario, datoresultante[0])
        else:
            self.offset = max(0, self.offset - self.limit)
        self.actualizarInfoPaginacion("usuarios", self.venPri.lbl_pagina_user, True)

    def datos_inicializacion(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        consulta = "SELECT t.id AS idtutor, CONCAT(t.nombres, ' ', t.apellidos) AS nombre_completo FROM tutores t JOIN vinculacion v ON t.id = v.tutores_id WHERE t.estado = TRUE;"
        respuesta_tutor = self.conec_base.getDatos(consulta)
   
        respuesta_proyecto = self.conec_base.getDatos('SELECT id, nombre FROM proyecto where estado = true')
        
        respuesta_periodoacademico = self.conec_base.getDatos('SELECT DISTINCT periodo_academico FROM vinculacion;')
        
        respuesta_tutores = self.conec_base.getDatos('SELECT id, CONCAT(nombres, " ", apellidos) AS nombres FROM tutores where estado = true')
        
        
        respuesta_filtro_periodo_seguimiento = self.conec_base.getDatos_condicion(
            "SELECT DISTINCT v.periodo_academico FROM vinculacion v WHERE v.tutores_id = %s ORDER BY v.periodo_academico;",
            (self.tutor_id,)
        )
        
        self.venPri.cbo_filtro_tutor_seguimiento.clear()
        self.venPri.cbo_filtro_tutor_seguimiento.addItem("Seleccione tutor academico", None)

        for id, nombre in respuesta_tutor:
            self.venPri.cbo_filtro_tutor_seguimiento.addItem(nombre, id)
            

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
            
            
        self.venPri.cbo_filtro_periodo_seguimiento.clear()
        self.venPri.cbo_filtro_periodo_seguimiento.addItem("Seleccione periodo academico", None)

        for nombre_tuple in respuesta_filtro_periodo_seguimiento:
            nombre = nombre_tuple[0]  
            self.venPri.cbo_filtro_periodo_seguimiento.addItem(nombre, nombre)

    def consultar_basedatos(self, tipo):
        if tipo == 'proyecto':
            proyecto_id = self.venPri.cbo_filtro_proyecto.currentData()
            if(proyecto_id):
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
            print('periodo: ' , periodo)
            if(periodo != None):
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
            if(tutor_id):
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



    def consultar_filtro_seguimiento_tutor(self):
        
        tutor_id = self.venPri.cbo_filtro_tutor_seguimiento.currentData()
        print('tutor_id ', tutor_id)
        self.tutor_id = tutor_id
   
        respuesta_filtro_periodo_seguimiento = self.conec_base.getDatos_condicion(
            "SELECT DISTINCT v.periodo_academico FROM vinculacion v WHERE v.tutores_id = %s ORDER BY v.periodo_academico;",
            (self.tutor_id,)
        )
        
        self.venPri.cbo_filtro_periodo_seguimiento.clear()
        self.venPri.cbo_filtro_periodo_seguimiento.addItem("Seleccione periodo academico", None)

        for nombre_tuple in respuesta_filtro_periodo_seguimiento:
            nombre = nombre_tuple[0]  
            self.venPri.cbo_filtro_periodo_seguimiento.addItem(nombre, nombre)
    

    def consultar_filtro_seguimiento_periodo(self):
        
        self.periodo_academico = self.venPri.cbo_filtro_periodo_seguimiento.currentData()
        
     
        resultados_proyectos = self.conec_base.getDatos_condicion(
            "SELECT p.id, p.nombre AS proyecto_nombre "
            "FROM proyecto p "
            "JOIN vinculacion v ON p.id = v.proyecto_id "
            "WHERE v.tutores_id = %s AND v.periodo_academico = %s "
            "ORDER BY p.nombre;",
            (self.tutor_id, self.periodo_academico )
        )
        
        self.venPri.cbo_filtro_proyecto_seguimiento.clear()
        self.venPri.cbo_filtro_proyecto_seguimiento.addItem("Seleccione proyecto", None)

        for id, nombre in resultados_proyectos:
            self.venPri.cbo_filtro_proyecto_seguimiento.addItem(nombre, id)
            

    def llenar_estudiantes_seguimientos_tutor(self):
      
        proyecto_id = self.venPri.cbo_filtro_proyecto_seguimiento.currentData()
        
        if(proyecto_id is not None):

            resultados_vinculaciones_estudiantes = self.conec_base.getDatos_condicion(
                "SELECT ev.id AS id_vinculacion_estudiante, "
                "CONCAT(e.nombres, ' ', e.apellidos) AS estudiante, "
                "v.fecha_inicio AS fecha_inicio_vinculacion, "
                "ev.nro_horas AS horas_vinculacion, "
                "ev.estado_vinculacion AS estado_vinculacion "
                "FROM vinculacion v "
                "JOIN estudiantes_vinculacion ev ON v.id = ev.vinculacion_id "
                "JOIN estudiantes e ON ev.estudiantes_id = e.id "
                "JOIN proyecto p ON v.proyecto_id = p.id "
                "WHERE v.tutores_id = %s "
                "AND v.periodo_academico = %s "
                "AND v.proyecto_id = %s "
                "ORDER BY v.id, e.apellidos, e.nombres;",
                (self.tutor_id, self.periodo_academico, proyecto_id)
            )
            
            #print('resultante ', resultados_vinculaciones_estudiantes)
            
            if (resultados_vinculaciones_estudiantes):
                
                llenar_tabla_seguimiento_tutor(self, self.venPri.tabla_seguimiento, resultados_vinculaciones_estudiantes)

    def busqueda_datos_estudiante(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        
        textobusqueda = self.venPri.line_busqueda_reporte_estudiantes.text()
        estado = 'Pendiente' if self.venPri.radioPendienteE.isChecked() else ('En Proceso' if self.venPri.radioProcesoE.isChecked() else 'Culminado')

        if textobusqueda.strip() == "":
            procedimiento = "listar_estudiantes_vinculacion_por_estado"
            parametros = (estado, self.offset, self.limit)
        else:
            procedimiento = "filtro_estudiantes_vinculacion_por_estado"
            parametros = (estado, self.offset, self.limit, textobusqueda)

        datoresultante = self.conec_base.getDatosProcess_condicion(procedimiento, parametros)
        
        

        if len(datoresultante[0]) > 0:
            cargar_tabla_reporte_estudiante(self.venPri.tabla_reporte_estudiantes, datoresultante[0])
        else:
            self.offset = max(0, self.offset - self.limit)
            
        total_registros = self.conec_base.getDatosProcess_condicion('filtro_estudiantes_vinculacion_por_estado_contar', [estado, textobusqueda ])
     
        total_registros = total_registros[0][0] if total_registros else 0
        
        total_paginas = (total_registros[0] + self.limit - 1) // self.limit
        
        pagina_actual = (self.offset // self.limit) + 1
        
        if pagina_actual > total_paginas:
            pagina_actual = total_paginas
        
        if pagina_actual < 1:
            pagina_actual = 1
        
        
        self.venPri.lbl_pagina_instituto.setText(f"Página {pagina_actual} de {total_paginas}")
        
        
    def reporte_estudiantes(self):
        
        from controllers.Modulo_reporte.generarRepoInforme import FormRepoImforme
        
        procedimiento = "listar_estudiantes_vinculacion_completo"
        datoresultante = self.conec_base.getDatosProcess(procedimiento)
        
        if(len( datoresultante[0]) > 0):
            
            FormRepoImforme(datos=datoresultante, modo='estudiantes').exec_()
        else:
            
            QtWidgets.QMessageBox.critical(self, "Error", "No ha realizado ningún filtro.")

 
 

    def configuracion_ventana(self):
        
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
        

        periodo_academico = self.conec_base.getDatos('SELECT DISTINCT periodo_academico FROM vinculacion ORDER BY periodo_academico DESC;')
        
        if(len(periodo_academico)):
            self.venPri.cbo_periodo_academico.clear()
            for periodo in periodo_academico:
                self.venPri.cbo_periodo_academico.addItem(periodo[0])
                
        
        self.cargaDatosEventoReporte()
        
    def cambioPagina(self):
        
        tipo_accion = self.venPri.cbo_tipo_entrega.currentText()
        
        if(tipo_accion == 'Informe'):
            self.venPri.stackedWidget_2.setCurrentIndex(0)
        else:
            self.venPri.stackedWidget_2.setCurrentIndex(1)
        
        self.cargaDatosEventoReporte()

    def cargaDatosEventoReporte(self):
        
        periodo_actual_seleccionado = self.venPri.cbo_periodo_academico.currentText()
                
        datos_informes = self.conec_base.getDatosProcess_condicion('listar_informes_por_periodo_academico', (periodo_actual_seleccionado, ))
        
        if(len(datos_informes)> 0):
            
            datos_informes = datos_informes[0]
            
            self.lista_informes_filtro = datos_informes
            
            cargar_tabla_reporte_informes(self.venPri.tabla_reporte_informe_tutor, datos_informes, periodo_actual_seleccionado, self)
            
            
        
        datos_fichas = self.conec_base.getDatosProcess_condicion('consulta_fichas', (periodo_actual_seleccionado, ))
        
        if(len(datos_fichas)> 0):
            
            datos_fichas = datos_fichas[0]
            
            self.lista_ficha_filtro = datos_fichas
            
            cargar_tabla_reporte_ficha_memorandum(self.venPri.tabla_reporte_ficha_tutor, datos_fichas, periodo_actual_seleccionado, self, 'fichas')
            
            
        datos_memorandum = self.conec_base.getDatosProcess_condicion('consulta_memorandum', (periodo_actual_seleccionado, ))
        
        if(len(datos_memorandum)> 0):
            
            datos_memorandum = datos_memorandum[0]

            self.lista_memorandun_filtro = datos_memorandum
            
            cargar_tabla_reporte_ficha_memorandum(self.venPri.tabla_reporte_memorandum_tutor, datos_memorandum, periodo_actual_seleccionado, self, 'memorandum')
        
   
    def eventoSeleccionPeriodo(self):
        
        self.cargaDatosEventoReporte()
        

    def generarReporte_informe(self):
        
        from controllers.Modulo_reporte.generarRepoInforme import FormRepoImforme
        if len(self.lista_informes_filtro) > 0:
   
            lista_sin_id = [fila[1:] for fila in self.lista_informes_filtro]

            periodo_actual_seleccionado = self.venPri.cbo_periodo_academico.currentText()
            FormRepoImforme(datos=lista_sin_id, modo='informe', periodo=periodo_actual_seleccionado).exec_()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No ha realizado ningún filtro.")

                  
    def generarReporte_ficha(self):
        from controllers.Modulo_reporte.generarRepoInforme import FormRepoImforme

        if len(self.lista_ficha_filtro) > 0:
            periodo_actual_seleccionado = self.venPri.cbo_periodo_academico.currentText()
            
            datos_sin_id = [[elemento for elemento in sublista[1:]] for sublista in self.lista_ficha_filtro]

            FormRepoImforme(datos=datos_sin_id, modo='ficha', periodo=periodo_actual_seleccionado).exec_()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No ha realizado ningún filtro.")

    def generarReporte_memorandum(self):
        from controllers.Modulo_reporte.generarRepoInforme import FormRepoImforme

        if len(self.lista_memorandun_filtro) > 0:
            periodo_actual_seleccionado = self.venPri.cbo_periodo_academico.currentText()
            
            datos_sin_id = [[elemento for elemento in sublista[1:]] for sublista in self.lista_memorandun_filtro]

            FormRepoImforme(datos=datos_sin_id, modo='memorandum', periodo=periodo_actual_seleccionado).exec_()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No ha realizado ningún filtro.")
