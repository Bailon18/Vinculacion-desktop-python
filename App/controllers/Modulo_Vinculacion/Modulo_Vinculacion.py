
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox

import re

from datetime import datetime
from controllers.Modulo_Vinculacion.funciona_vinculacion import evento_tabla, llenar_tabla_estudiantes_seleccinados
from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_vinculacion import Ui_FormularioVinculacion


# importamos la clase de la base datos
from db.Modulo_base import BaseDatos


class Vinculacion(QtWidgets.QDialog):

    def __init__(self, vinculacion_id = None , modo="" , parent=None):
        
        super(Vinculacion, self).__init__(parent)
        self.vinculacion = Ui_FormularioVinculacion()
        self.vinculacion.setupUi(self)
        
        self.conec_base = BaseDatos()
        self.vinculacion.id_estudiante_seleccionado.setVisible(False)
        
        self.lista_id_estudiantes = []
        self.lista_id_estudiantes_originales = []
        self.parent = parent
        self.id_vinculacion_editado_db = 0
        
        evento_tabla(self)
        
        self.datos_inicializacion()
        
        self.vinculacion_id = vinculacion_id 
        self.modo = modo

        if self.vinculacion_id and self.modo == "editar":
            
            self.obtener_vinculacion_y_estudiantes(self.vinculacion_id)
            self.vinculacion.lbl_titulo_ventana.setText('Editar vinculación')
            self.vinculacion.btn_agregar_vinculacion.setText('Actualizar Vinculación')

            
        # self.evento_tipo_institucion()
            
        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.vinculacion.btn_close.clicked.connect(lambda: self.cerrar_ui_vinculacion())
        self.vinculacion.cancelButton.clicked.connect(lambda: self.cerrar_ui_vinculacion())
        
        self.vinculacion.line_buscar_estudiante.textChanged.connect(self.buscar_estudiante)
        
        self.vinculacion.line_codigo_ies.textChanged.connect(self.validar_codigo_ies)
        self.vinculacion.line_campo_especifico.textChanged.connect(self.validar_campo_especifico)
        self.vinculacion.line_periodo_academico.textChanged.connect(self.validar_periodo_academico)
        self.vinculacion.cbo_institucion.currentIndexChanged.connect(self.on_validar_combobox_institucion)
        self.vinculacion.cbo_proyecto.currentIndexChanged.connect(self.on_validar_combobox_proyecto)
        self.vinculacion.cbo_tutor.currentIndexChanged.connect(self.on_validar_combobox_tutor)
        
        
        self.STYLE_ERROR = "color: #D32F2F; font-family: Roboto; font-style: normal; font-weight: bold; font-size: 12px; visibility: visible;"
        self.STYLE_VALID = "border: 2px solid green;"
        self.STYLE_INVALID = "border: 2px solid red;"
        
        self.vinculacion.btn_agregar_estu_seleccionado.clicked.connect(lambda: self.agregar_estudiante_seleccionado())
        self.vinculacion.btn_agregar_vinculacion.clicked.connect(lambda: self.guardar_vinculacion())
        

        # self.vinculacion.line_identificacion.textChanged.connect(lambda: self.vinculacion.line_identificacion.setToolTip('Formato: 10 digitos\n Ejm: 992929394-9'))
        # self.vinculacion.line_periodoacademico.textChanged.connect(lambda: self.vinculacion.line_periodoacademico.setToolTip('Ejm: P1-2023'))
        # self.vinculacion.line_codigoies.textChanged.connect(lambda: self.vinculacion.line_codigoies.setToolTip('Formato: 4 digito númericos\n Ejm: 1003'))
        # self.vinculacion.line_campoespecifico.textChanged.connect(lambda: self.vinculacion.line_campoespecifico.setToolTip('Ejm: 1-2A'))
        
        # self.vinculacion.cbo_institucion.activated.connect(lambda: self.evento_tipo_institucion())
        


        # # Validaciones y mascaras para los inputs
        # val_nombre_apellido(self, self.vinculacion.line_nombreapellidos)
        # val_identifiacion(self, self.vinculacion.line_identificacion)
        # val_periodo_academico(self, self.vinculacion.line_periodoacademico)
        # val_codigo_campoespecifico(self, self.vinculacion.line_campoespecifico)
        # val_codigo_ies(self, self.vinculacion.line_codigoies)


        # # boton guardar
        # self.vinculacion.btn_guardar.clicked.connect(lambda: self.obtener_campos_vinculacion())
        
        

                
    def actualizar_titulo_estado(self):

        if self.estado == 'En progreso':
            color_texto = 'blue'
        if self.estado == "Pendiente":
            color_texto = "red"
        elif self.estado == "Culminado":
            color_texto = "green"

        estilo = f"color: {color_texto}; font-family: Roboto; font-style: normal; font-weight: 500; font-size: 17px; line-height: 40px; letter-spacing: 0.02em;"
        self.vinculacion.vinculacion_estado.setStyleSheet(estilo)

    def keyPressEvent(self, event):
  
        if event.key() == QtCore.Qt.Key_Escape:
            pass
    
    def cerrar_ui_vinculacion(self):
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
    
    def validar_codigo_es(self, codigo_ies):
        codigo_ies_stripped = codigo_ies.strip()
        if not codigo_ies_stripped:
            return "Campo vacío"
        elif not codigo_ies_stripped.isdigit():
            return "Debe contener solo números."
        elif len(codigo_ies_stripped) != 4:
            return "Debe tener 4 dígitos."
        return ""
    
    def validar_campo_especifico_es(self,campo_especifico):
        campo_especifico_stripped = campo_especifico.strip()
        if not campo_especifico_stripped:
            return "Campo vacío"
        elif not re.match(r'^\d-\d[A-Za-z]$', campo_especifico_stripped):
            return "Formato inválido. Ejemplo: 1-2A"
        return ""
    
    def validar_periodo_academico_es(self, periodo_academico):
        campo_periodo_stripped = periodo_academico.strip()
        if not campo_periodo_stripped:
            return "Campo vacío"
        elif not re.match(r'^P[0-9]-20[0-9]{2}$', campo_periodo_stripped):
            return "Formato inválido. Ejemplo: P1-2023, P2-2023 ..."
        return ""

    def validar_codigo_ies(self):
        codigo_ies = self.vinculacion.line_codigo_ies.text()
        respuesta = self.validar_codigo_es(codigo_ies)
        if respuesta:
            self.vinculacion.line_codigo_ies.setStyleSheet(self.STYLE_INVALID)
            self.vinculacion.errorCodigoies.setText(respuesta)
            self.vinculacion.errorCodigoies.setStyleSheet(self.STYLE_ERROR)
        else:
            self.vinculacion.line_codigo_ies.setStyleSheet(self.STYLE_VALID)
            self.vinculacion.errorCodigoies.setStyleSheet("")
            self.vinculacion.errorCodigoies.setText("")
            
    def validar_campo_especifico(self):
        campo_escifico = self.vinculacion.line_campo_especifico.text()
        respuesta = self.validar_campo_especifico_es(campo_escifico)
        if respuesta:
            self.vinculacion.line_campo_especifico.setStyleSheet(self.STYLE_INVALID)
            self.vinculacion.errorCampoEspecifico.setText(respuesta)
            self.vinculacion.errorCampoEspecifico.setStyleSheet(self.STYLE_ERROR)
        else:
            self.vinculacion.line_campo_especifico.setStyleSheet(self.STYLE_VALID)
            self.vinculacion.errorCampoEspecifico.setStyleSheet("")
            self.vinculacion.errorCampoEspecifico.setText("")
            
    def validar_periodo_academico(self):
        periodo_academico = self.vinculacion.line_periodo_academico.text()
        respuesta = self.validar_periodo_academico_es(periodo_academico)
        if respuesta:
            self.vinculacion.line_periodo_academico.setStyleSheet(self.STYLE_INVALID)
            self.vinculacion.errorCampoPeriodo.setText(respuesta)
            self.vinculacion.errorCampoPeriodo.setStyleSheet(self.STYLE_ERROR)
        else:
            self.vinculacion.line_periodo_academico.setStyleSheet(self.STYLE_VALID)
            self.vinculacion.errorCampoPeriodo.setStyleSheet("")
            self.vinculacion.errorCampoPeriodo.setText("")
            
    def on_validar_combobox_institucion(self):

        codigo_institucion = self.vinculacion.cbo_institucion.currentIndex()
        if codigo_institucion == 0:
            self.vinculacion.cbo_institucion.setStyleSheet(self.STYLE_INVALID)
            self.vinculacion.errorInstitucion.setText('Debe seleccionar una institución.')
            self.vinculacion.errorInstitucion.setStyleSheet(self.STYLE_ERROR)
        else:
            self.vinculacion.cbo_institucion.setStyleSheet(self.STYLE_VALID)
            self.vinculacion.errorInstitucion.setStyleSheet("")
            self.vinculacion.errorInstitucion.setText("")
            
    def on_validar_combobox_proyecto(self):
 
        codigo_proyecto = self.vinculacion.cbo_proyecto.currentIndex()
        if codigo_proyecto == 0:
            self.vinculacion.cbo_proyecto.setStyleSheet(self.STYLE_INVALID)
            self.vinculacion.errorProyecto.setText('Debe seleccionar un proyecto.')
            self.vinculacion.errorProyecto.setStyleSheet(self.STYLE_ERROR)
        else:
            self.vinculacion.cbo_proyecto.setStyleSheet(self.STYLE_VALID)
            self.vinculacion.errorProyecto.setStyleSheet("")
            self.vinculacion.errorProyecto.setText("")
            
    def on_validar_combobox_tutor(self):
 
        codigo_tutor = self.vinculacion.cbo_tutor.currentIndex()
        
        if codigo_tutor == 0:
            self.vinculacion.cbo_tutor.setStyleSheet(self.STYLE_INVALID)
            self.vinculacion.errorTutor.setText('Debe seleccionar un tutor.')
            self.vinculacion.errorTutor.setStyleSheet(self.STYLE_ERROR)
        else:
            self.vinculacion.cbo_tutor.setStyleSheet(self.STYLE_VALID)
            self.vinculacion.errorTutor.setStyleSheet("")
            self.vinculacion.errorTutor.setText("")
        

    def datos_inicializacion(self):
        
        self.vinculacion.date_fecha_inicio.setDate(QDate.currentDate())
       
        respuestaintitucion = self.conec_base.getDatos('SELECT id, nombre FROM institucion')
        respuesta_proyecto = self.conec_base.getDatos('SELECT id, nombre FROM proyecto')
        respuesta_tutores = self.conec_base.getDatos('SELECT id, CONCAT(nombres, " ", apellidos) AS nombres FROM tutores')
    

        self.vinculacion.cbo_institucion.clear()
        self.vinculacion.cbo_institucion.addItem("Seleccione institucion practica", None)
        for id, nombre in respuestaintitucion:
            self.vinculacion.cbo_institucion.addItem(nombre, id)
            

        self.vinculacion.cbo_tutor.clear()
        self.vinculacion.cbo_tutor.addItem("Seleccione tutor", None)
        for id, nombres in respuesta_tutores:
            self.vinculacion.cbo_tutor.addItem(nombres, id)
            
            
        self.vinculacion.cbo_proyecto.clear()
        self.vinculacion.cbo_proyecto.addItem("Seleccione proyecto", None)
        for id, nombres in respuesta_proyecto:
            self.vinculacion.cbo_proyecto.addItem(nombres, id)
               
    def buscar_estudiante(self):
        search_text = self.vinculacion.line_buscar_estudiante.text().strip()
        
        if search_text:
            
            query = (
                "SELECT id, CONCAT(nombres, ' ', apellidos) AS nombre_completo, nro_identificacion "
                "FROM estudiantes "
                "WHERE (nombres LIKE %s OR apellidos LIKE %s OR nro_identificacion LIKE %s) "
                "AND NOT EXISTS ("
                "    SELECT 1 FROM estudiantes_vinculacion "
                "    WHERE estudiantes.id = estudiantes_vinculacion.estudiantes_id"
                ")"
            )
            
            search_term = f"%{search_text}%"
            
            
            
            result = self.conec_base.getDatos_condicion(query, (search_term, search_term, search_term))
        
            if result:
                self.vinculacion.line_nombre_seleccionado.setText(result[0][1])
                self.vinculacion.line_cedula_seleccionado.setText(result[0][2])
                self.vinculacion.id_estudiante_seleccionado.setText(str(result[0][0]))
                self.vinculacion.line_nombre_seleccionado.setStyleSheet(self.STYLE_VALID)
                self.vinculacion.line_cedula_seleccionado.setStyleSheet(self.STYLE_VALID)
                self.vinculacion.errorBuscar.setText("")
                self.vinculacion.line_buscar_estudiante.setStyleSheet(self.STYLE_VALID)
                self.vinculacion.errorEstudianteNoEncontrado.setText("")
            else:
                self.vinculacion.line_nombre_seleccionado.setStyleSheet(self.STYLE_INVALID)
                self.vinculacion.line_cedula_seleccionado.setStyleSheet(self.STYLE_INVALID)
                self.vinculacion.errorEstudianteNoEncontrado.setText("Estudiante no encontrado")
                self.vinculacion.line_nombre_seleccionado.clear()
                self.vinculacion.line_cedula_seleccionado.clear()
        else:
            self.vinculacion.line_nombre_seleccionado.setStyleSheet(self.STYLE_INVALID)
            self.vinculacion.line_cedula_seleccionado.setStyleSheet(self.STYLE_INVALID)
            self.vinculacion.line_buscar_estudiante.setStyleSheet(self.STYLE_INVALID)
            self.vinculacion.errorBuscar.setText("Por favor, ingrese texto para buscar")
            self.vinculacion.line_nombre_seleccionado.clear()
            self.vinculacion.line_cedula_seleccionado.clear()
                
    def agregar_estudiante_seleccionado(self):
        nombre_estudiante = self.vinculacion.line_nombre_seleccionado.text().strip()
        
        if not nombre_estudiante:
            QtWidgets.QMessageBox.warning(self, 'Advertencia', 'Debe buscar un estudiante antes de asignarlo.')
            return
        
        id_estudiante = self.vinculacion.id_estudiante_seleccionado.text()
        
        for estudiante in self.lista_id_estudiantes:
            if estudiante[0] == id_estudiante:
                QtWidgets.QMessageBox.warning(self, 'Advertencia', 'El estudiante ya está en la lista.')
                return
        
        cedula_estudiante = self.vinculacion.line_cedula_seleccionado.text().strip()
        estado_vinculacion = self.vinculacion.cbo_estado_vinculacion.currentText()
        
        self.lista_id_estudiantes.append([id_estudiante, cedula_estudiante, nombre_estudiante, estado_vinculacion])
        
        llenar_tabla_estudiantes_seleccinados(self, self.vinculacion.tabla_estudiante_seleccionado, self.lista_id_estudiantes)
        
        # Limpiar los campos y estilos después de agregar
        self.vinculacion.line_cedula_seleccionado.setText("")
        self.vinculacion.line_nombre_seleccionado.setText("")
        self.vinculacion.line_buscar_estudiante.setText("")
        self.vinculacion.line_cedula_seleccionado.setStyleSheet("")
        self.vinculacion.line_nombre_seleccionado.setStyleSheet("")
        self.vinculacion.line_buscar_estudiante.setStyleSheet("")
        self.vinculacion.errorBuscar.setText("")

    def campos_validados(self):
        return (self.vinculacion.line_codigo_ies.styleSheet() == self.STYLE_VALID and
                self.vinculacion.line_campo_especifico.styleSheet() == self.STYLE_VALID and
                self.vinculacion.line_periodo_academico.styleSheet() == self.STYLE_VALID and
                self.vinculacion.cbo_institucion.styleSheet() == self.STYLE_VALID and
                self.vinculacion.cbo_tutor.styleSheet() == self.STYLE_VALID and
                self.vinculacion.cbo_proyecto.styleSheet() == self.STYLE_VALID)
    
    def guardar_vinculacion(self):
        if not self.conec_base.verificarConexionInternet():
            QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
            
        self.validar_codigo_ies()
        self.validar_campo_especifico()
        self.validar_periodo_academico()
        self.on_validar_combobox_institucion()
        self.on_validar_combobox_proyecto()
        self.on_validar_combobox_tutor()
        
        tiene_data = self.vinculacion.tabla_estudiante_seleccionado.findItems("*", QtCore.Qt.MatchWildcard)
        if not tiene_data:
            QMessageBox.warning(self, "Error", "Debe seleccionar al menos un estudiante para vinculación.")
            return
        
        if self.campos_validados():
            
            if self.vinculacion_id == 0:
                self.guardar_nueva_vinculacion()
            else:
                self.actualizar_vinculacion()
            
            # if(self.vinculacion_id  != 0 ):
                
            #     confirmacion = QMessageBox.question(self, "Confirmar Guardar", "¿Está seguro de guardar la nueva vinculación?", QMessageBox.Yes | QMessageBox.No)
                
            
            #     if confirmacion == QMessageBox.Yes:
            
            #         fecha_inicio = self.vinculacion.date_fecha_inicio.date().toString("yyyy-MM-dd")
            #         cogido_ies = self.vinculacion.line_codigo_ies.text().strip()
            #         campo_especifico = self.vinculacion.line_campo_especifico.text().strip()
            #         periodo_academico = self.vinculacion.line_periodo_academico.text().strip()
                    
            #         intitucion_id = self.vinculacion.cbo_institucion.currentData()
            #         tutor_id = self.vinculacion.cbo_tutor.currentData()
            #         proyecto_id = self.vinculacion.cbo_proyecto.currentData()
                    
            #         data_vinculacion = (fecha_inicio, cogido_ies, campo_especifico, periodo_academico, intitucion_id, tutor_id, proyecto_id, True)
                    
            #         try:
            #             self.conec_base.setDatosProcess("guardar_vinculacion_procedure", data_vinculacion)
            #             id_vinculacion = self.conec_base.getDatos("SELECT LAST_INSERT_ID()")
                        
            #             if id_vinculacion :
            #                 datos_estudiantes_vinculados = self.preparar_datos_estudiantes(id_vinculacion[0][0])
                            
            #                 consulta_insert = (
            #                     "INSERT INTO estudiantes_vinculacion "
            #                     "(estudiantes_id, vinculacion_id, fecha_final, estado_vinculacion, nro_horas) "
            #                     "VALUES (%s, %s, %s, %s, %s)"
            #                 )
            #                 self.conec_base.setDatosListFor(consulta_insert, datos_estudiantes_vinculados)
                            
            #                 QMessageBox.information(self, "Éxito", "Vinculación guardada correctamente.")
            #                 self.parent.raizOpacidad.close()
            #                 self.close()
            #                 self.parent.llenarTabla('ObtenerListaVinculaciones', 'vinculacion', self.parent.venPri.tabla_vinculacion)
            #                 self.parent.actualizarInfoPaginacion('vinculacion', self.parent.venPri.lbl_pagina_vinculacion)

            #         except Exception as e:
            #             QMessageBox.critical(self, "Error de Base de Datos", f"Error al guardar la vinculación: {str(e)}")
                        
            # else:
            #     self.actualizar_vinculacion()
        
    def preparar_datos_estudiantes(self, id_vinculacion):
        datos_estudiantes_vinculados = []
        for estudiante in self.lista_id_estudiantes:
            datos_estudiante = [estudiante[0], id_vinculacion, None, 'Pendiente', 0]
            datos_estudiantes_vinculados.append(datos_estudiante)
        
        return datos_estudiantes_vinculados
    
    
    def obtener_vinculacion_y_estudiantes(self, vinculacion_id):
        try:
            # Paso 1: Obtener los datos de la vinculación
            consulta_vinculacion = f"SELECT * FROM vinculacion WHERE id = {vinculacion_id}"
            vinculacion_datos = self.conec_base.getDatos(consulta_vinculacion)
            
            if not vinculacion_datos:
                QMessageBox.warning(self, "Error", "No se encontró la vinculación especificada.")
                return
            
            vinculacion = vinculacion_datos[0]
            
            # print(f"Vinculación: {vinculacion}")
            # Vinculación: (5, datetime.datetime(2024, 6, 19, 3, 19, 41), datetime.date(2023, 5, 5), '1036', '1-6A', 'P1-2024', 5, 5, 5, 1)
            self.id_vinculacion_editado_db = vinculacion[0]
            self.vinculacion.date_fecha_inicio.setDate(vinculacion[2])
            self.vinculacion.line_codigo_ies.setText(vinculacion[3])
            self.vinculacion.line_campo_especifico.setText(vinculacion[4])
            self.vinculacion.line_periodo_academico.setText(vinculacion[5])
            
            self.set_combobox_by_user_data(self.vinculacion.cbo_institucion, vinculacion[6])
            self.set_combobox_by_user_data(self.vinculacion.cbo_tutor, vinculacion[7])
            self.set_combobox_by_user_data(self.vinculacion.cbo_proyecto, vinculacion[8])
            
            
        
            # Paso 2: Obtener los estudiantes vinculados
            consulta_estudiantes = f"""
                SELECT ev.estudiantes_id, e.nro_identificacion, e.nombres, ev.estado_vinculacion
                FROM estudiantes_vinculacion ev
                JOIN estudiantes e ON ev.estudiantes_id = e.id
                WHERE ev.vinculacion_id = {vinculacion_id}
            """
            estudiantes_datos = self.conec_base.getDatos(consulta_estudiantes)
            # print(f"Estudiantes vinculados: {estudiantes_datos}")
            

            # Paso 3: Formatear los datos de los estudiantes

            for estudiante in estudiantes_datos:
                id_estudiante, cedula_estudiante, nombre_estudiante, estado_vinculacion = estudiante
                self.lista_id_estudiantes.append([id_estudiante, cedula_estudiante, nombre_estudiante, estado_vinculacion])
                self.lista_id_estudiantes_originales.append([id_estudiante, cedula_estudiante, nombre_estudiante, estado_vinculacion])
                # print("lista_id_estudiantes: ", self.lista_id_estudiantes)
                # print("lista_id_estudiantes_originales: ", self.lista_id_estudiantes_originales)
                llenar_tabla_estudiantes_seleccinados(self, self.vinculacion.tabla_estudiante_seleccionado, self.lista_id_estudiantes)

        except Exception as e:
            QMessageBox.critical(self, "Error de Base de Datos", f"Error al obtener los datos: {str(e)}")
    
    def set_combobox_by_user_data(self, combobox, user_data):
        index = combobox.findData(user_data, role=Qt.UserRole) 
        if index != -1:
            combobox.setCurrentIndex(index)
    

    def guardar_nueva_vinculacion(self):
        
        confirmacion = QMessageBox.question(self, "Confirmar Guardar", "¿Está seguro de guardar la nueva vinculación?", QMessageBox.Yes | QMessageBox.No)
        if confirmacion == QMessageBox.Yes:
    
            fecha_inicio = self.vinculacion.date_fecha_inicio.date().toString("yyyy-MM-dd")
            cogido_ies = self.vinculacion.line_codigo_ies.text().strip()
            campo_especifico = self.vinculacion.line_campo_especifico.text().strip()
            periodo_academico = self.vinculacion.line_periodo_academico.text().strip()
            
            intitucion_id = self.vinculacion.cbo_institucion.currentData()
            tutor_id = self.vinculacion.cbo_tutor.currentData()
            proyecto_id = self.vinculacion.cbo_proyecto.currentData()
            
            data_vinculacion = (fecha_inicio, cogido_ies, campo_especifico, periodo_academico, intitucion_id, tutor_id, proyecto_id, True)
            
            try:
                self.conec_base.setDatosProcess("guardar_vinculacion_procedure", data_vinculacion)
                id_vinculacion = self.conec_base.getDatos("SELECT LAST_INSERT_ID()")
                
                if id_vinculacion :
                    datos_estudiantes_vinculados = self.preparar_datos_estudiantes(id_vinculacion[0][0])
                    
                    consulta_insert = (
                        "INSERT INTO estudiantes_vinculacion "
                        "(estudiantes_id, vinculacion_id, fecha_final, estado_vinculacion, nro_horas) "
                        "VALUES (%s, %s, %s, %s, %s)"
                    )
                    self.conec_base.setDatosListFor(consulta_insert, datos_estudiantes_vinculados)
                    
                    QMessageBox.information(self, "Éxito", "Vinculación guardada correctamente.")
                    self.parent.raizOpacidad.close()
                    self.close()
                    self.parent.llenarTabla('ObtenerListaVinculaciones', 'vinculacion', self.parent.venPri.tabla_vinculacion)
                    self.parent.actualizarInfoPaginacion('vinculacion', self.parent.venPri.lbl_pagina_vinculacion)

            except Exception as e:
                        QMessageBox.critical(self, "Error de Base de Datos", f"Error al guardar la vinculación: {str(e)}")

    def actualizar_vinculacion(self):
        
        confirmacion = QMessageBox.question(self, "Confirmar Actualización", "¿Está seguro de actualizar la vinculación?", QMessageBox.Yes | QMessageBox.No)
        if confirmacion == QMessageBox.Yes:
    
            try:
                # Actualizar datos de la vinculación
                fecha_inicio = self.vinculacion.date_fecha_inicio.date().toString("yyyy-MM-dd")
                cogido_ies = self.vinculacion.line_codigo_ies.text().strip()
                campo_especifico = self.vinculacion.line_campo_especifico.text().strip()
                periodo_academico = self.vinculacion.line_periodo_academico.text().strip()
                intitucion_id = self.vinculacion.cbo_institucion.currentData()
                tutor_id = self.vinculacion.cbo_tutor.currentData()
                proyecto_id = self.vinculacion.cbo_proyecto.currentData()

                consulta_update = """
                    UPDATE vinculacion SET
                    fecha_inicio = %s,
                    codigo_ies = %s,
                    campo_especifico = %s,
                    periodo_academico = %s,
                    institucion_id = %s,
                    tutores_id = %s,
                    proyecto_id = %s
                    WHERE id = %s
                """
                self.conec_base.setDatos(consulta_update, (fecha_inicio, cogido_ies, campo_especifico, periodo_academico, intitucion_id, tutor_id, proyecto_id, self.id_vinculacion_editado_db))
                
                # Identificar los estudiantes a eliminar
                estudiantes_a_eliminar = [est for est in self.lista_id_estudiantes_originales if est not in self.lista_id_estudiantes]
                for estudiante in estudiantes_a_eliminar:
                    consulta_delete = "DELETE FROM estudiantes_vinculacion WHERE vinculacion_id = %s AND estudiantes_id = %s"
                    self.conec_base.setDatos(consulta_delete, (self.id_vinculacion_editado_db, estudiante[0]))

                # Identificar los estudiantes a agregar
                estudiantes_a_agregar = [est for est in self.lista_id_estudiantes if est not in self.lista_id_estudiantes_originales]
                consulta_insert = """
                    INSERT INTO estudiantes_vinculacion (estudiantes_id, vinculacion_id, fecha_final, estado_vinculacion, nro_horas)
                    VALUES (%s, %s, %s, %s, %s)
                """
                for estudiante in estudiantes_a_agregar:
                    self.conec_base.setDatos(consulta_insert, (estudiante[0], self.id_vinculacion_editado_db, None, estudiante[3], 0))
                
                QMessageBox.information(self, "Éxito", "Vinculación actualizada correctamente.")
                self.parent.raizOpacidad.close()
                self.close()
                self.parent.llenarTabla('ObtenerListaVinculaciones', 'vinculacion', self.parent.venPri.tabla_vinculacion)
                self.parent.actualizarInfoPaginacion('vinculacion', self.parent.venPri.lbl_pagina_vinculacion)
            except Exception as e:
                QMessageBox.critical(self, "Error de Base de Datos", f"Error al actualizar la vinculación: {str(e)}")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    # def llenar_combobox(self, combobox, lista, longitud_maxima):
    #     for elemento in lista:
    #         id_elemento, nombre_elemento = elemento
    #         texto_truncado = nombre_elemento[:longitud_maxima]
    #         combobox.addItem(texto_truncado, userData=id_elemento)
    #         combobox.setItemData(combobox.count() - 1, nombre_elemento, Qt.ToolTipRole)

    # def configuracion_ventana(self):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     lista_carrera, lista_institucion, lista_proyectos, lista_tutores = self.conec_base.getDatosProcess("ObtenerDatos")
        
        
    #     self.llenar_combobox(self.vinculacion.cbox_carrera, lista_carrera, 30)
    #     self.llenar_combobox(self.vinculacion.cbo_institucion, lista_institucion, 100)
    #     self.llenar_combobox(self.vinculacion.cbo_proyectos, lista_proyectos, 700)
    #     self.llenar_combobox(self.vinculacion.cbo_tutor, lista_tutores, 30)
        
        
    #     fecha_actual = QtCore.QDate.currentDate()

    #     self.vinculacion.fecha_inicio.dateChanged.connect(
    #         lambda: self.vinculacion.fecha_final.setMinimumDate(self.vinculacion.fecha_inicio.date()))
        
    #     self.vinculacion.fecha_inicio.setDate(fecha_actual)

    # def obtener_campos_vinculacion(self):
        
    #     nombre_apellidos = self.vinculacion.line_nombreapellidos.text().strip();
    #     tipo_identificacion = self.vinculacion.cbo_tipo_identificacion.currentText();
    #     identificacion = self.vinculacion.line_identificacion.text();
    #     carrera = self.vinculacion.cbox_carrera.itemData(self.vinculacion.cbox_carrera.currentIndex()); 
    #     institucion = self.vinculacion.cbo_institucion.itemData(self.vinculacion.cbo_institucion.currentIndex()); 
    #     periodo_academico = self.vinculacion.line_periodoacademico.text()
    #     fecha_inicio = self.vinculacion.fecha_inicio.date().toString("yyyy-MM-dd")
    #     fecha_final = self.vinculacion.fecha_final.date().toString("yyyy-MM-dd")
    #     codigo_ies = self.vinculacion.line_codigoies.text()
    #     campo_especifico = self.vinculacion.line_campoespecifico.text()
    #     tutor_asignado = self.vinculacion.cbo_tutor.itemData(self.vinculacion.cbo_tutor.currentIndex())
    #     proyecto  = self.vinculacion.cbo_proyectos.itemData(self.vinculacion.cbo_proyectos.currentIndex())


    #     # Realizar las validaciones
    #     mensaje_error = ""

    #     if not nombre_apellidos:
    #         mensaje_error += "- Ingrese el nombre y apellidos.\n"

    #     if not tipo_identificacion:
    #         mensaje_error += "- Seleccione un tipo de identificación.\n"

    #     if len(identificacion) != 11 or identificacion[9] != '-':
    #         mensaje_error += "- Ingrese una identificacion válido (ejemplo: 112233456-2).\n"

    #     if not carrera:
    #         mensaje_error += "- Seleccione una carrera.\n"

    #     if not institucion:
    #         mensaje_error += "- Seleccione una institución.\n"

    #     patron_periodo_academico = re.compile(r'^P[1-9]-\d{4}$')
    #     if not periodo_academico or not patron_periodo_academico.match(periodo_academico):
    #         mensaje_error += "- Ingrese un período académico válido (ejemplo: P1-1222).\n"


    #     if not fecha_inicio:
    #         mensaje_error += "- Ingrese una fecha de inicio válida.\n"

    #     if not fecha_final:
    #         mensaje_error += "- Ingrese una fecha final válida.\n"

    #     if not codigo_ies or len(codigo_ies) != 4:
    #         mensaje_error += "- El código de IES debe tener 4 dígitos.\n"


    #     formato_correcto = re.match(r'^[1-9]?\d-[1-9]?\d[A-Z]$', campo_especifico)
    #     if not campo_especifico or not formato_correcto:
    #         mensaje_error += "- Ingrese un campo específico válido (ejemplo: 1-6A).\n"


    #     if not tutor_asignado:
    #         mensaje_error += "- Seleccione un tutor.\n"

    #     if mensaje_error:
    #         # Si hay errores, muestra el mensaje de error en un QMessageBox
    #         QMessageBox.critical(self, "Error", "Revise los campos:\n" + mensaje_error)
    #     else:

    #         datos = [tipo_identificacion, identificacion, nombre_apellidos, carrera , periodo_academico,
    #                     codigo_ies, fecha_inicio, fecha_final, campo_especifico, tutor_asignado, institucion, proyecto]

    #         if self.modo == "actualizar":
    #             # Lógica para actualizar los datos de la vinculación existente
    #             datos.append(self.vinculacion_id)
    #             self.actualizar_vinculacion(datos)
    #         else:
    #             # Lógica para crear una nueva vinculación
    #             self.crear_nueva_vinculacion(datos)


    #         # Si no hay errores, continuar con el procesamiento
    #         QMessageBox.information(self, "Correcto", "Datos válidos. Continuar con el procesamiento...")

    # def cargar_datos_vinculacion(self, vinculacion_id):

    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     datos = self.conec_base.getDatosProcess_condicion("ObtenerDatosVinculacion", (vinculacion_id,))
 
    #     if datos:
    #         datos = datos[0][0]

    #         self.vinculacion.line_nombreapellidos.setText(str(datos[0]))
    #         self.vinculacion.cbo_tipo_identificacion.setCurrentText(datos[1])
    #         self.vinculacion.line_identificacion.setText(str(datos[2]))
    #         self.vinculacion.line_periodoacademico.setText(str(datos[5]))
    #         self.vinculacion.fecha_inicio.setDate(datos[6])
    #         self.vinculacion.fecha_final.setDate(datos[7])
    #         self.vinculacion.spb_numerohoras.setValue(datos[8])
    #         self.vinculacion.line_codigoies.setText(str(datos[9]))
    #         self.vinculacion.line_campoespecifico.setText(str(datos[10]))
    #         self.vinculacion.line_tipoinstitucion.setText(str(datos[14]))

    #         # Obteniendo los identificadores de los datos
    #         codigo_carrera = datos[3]
    #         codigo_institucion = datos[4]
    #         identificacion_tutor = datos[11]
    #         id_proyecto = datos[12]

    #         # Buscando el índice correspondiente al identificador en los ComboBoxes
    #         self.set_combobox_by_user_data(self.vinculacion.cbox_carrera, codigo_carrera)
    #         self.set_combobox_by_user_data(self.vinculacion.cbo_institucion, codigo_institucion)
    #         self.set_combobox_by_user_data(self.vinculacion.cbo_tutor, identificacion_tutor)
    #         self.set_combobox_by_user_data(self.vinculacion.cbo_proyectos, id_proyecto)

    # def set_combobox_by_user_data(self, combobox, user_data):
    #     index = combobox.findData(user_data, role=Qt.UserRole) 
    #     if index != -1:
    #         combobox.setCurrentIndex(index)

    # def actualizar_vinculacion(self, dato_vinculacion):
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
    #     try:
    #         self.conec_base.setDatosProcess('ActualizarEstudianteYVinculacion', dato_vinculacion)
    #         QMessageBox.information(self, "Éxito", "Vinculación fue actualizado exitosamente.")
    #         self.parent.configuracion_ventana()
    #         self.parent.listar_vinculacion()
    #         self.parent.raizOpacidad.close()
    #         self.close()
    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"Error al actualizar vinculación: {str(e)}")
        
    # def crear_nueva_vinculacion(self, dato_vinculacion):
        
    #     if not self.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
    #         return
        
    #     try:
    #         self.conec_base.setDatosProcess('InsertarEstudianteYVinculacion', dato_vinculacion)
    #         QMessageBox.information(self, "Éxito", "Nueva vinculación creada exitosamente.")
            
    #         self.parent.configuracion_ventana()
    #         self.parent.listar_vinculacion()
    #         self.parent.raizOpacidad.close()
            
    #         self.close()
    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"Error al crear la nueva vinculación: {str(e)}")

    # def evento_tipo_institucion(self):
        
    #     valorseleccion = self.vinculacion.cbo_institucion.currentText()
        
    #     print(valorseleccion)
        
    #     if(valorseleccion):
        
    #         resultado = self.conec_base.getDatos_condicion("select tipo_institucion from instituciones_educativas where nombre_institucion = %s",(valorseleccion,))
            
    #         print(resultado)
            
    #         self.vinculacion.line_tipoinstitucion.setText(""+resultado[0][0])
        

        
        
        
    