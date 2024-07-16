
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox

import re

from datetime import datetime
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_entrega import Ui_EntregaUi

from db.Modulo_base import BaseDatos

class Entrega(QtWidgets.QDialog):
    
    def __init__(self, parent, modo = '', dato = []):

        super(Entrega, self).__init__()
        self.venEntrega = Ui_EntregaUi()
        self.venEntrega.setupUi(self)
        self.conec_base = BaseDatos()

        self.ventana_configuracion()

        self.parent = parent
        self.modo = modo
        self.dato = dato
        self.mes = ""
        
        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()
        self.cambioPagina()
        self.obtener_mes()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.venEntrega.btn_closeadmi_3.clicked.connect(lambda: self.cerrar_ui_perfil())
        
        self.venEntrega.fecha_informe.dateChanged.connect(lambda: self.obtener_mes())
        self.venEntrega.cbo_tipo_entrega.activated.connect(lambda: self.cambioPagina())
        self.venEntrega.btn_registrar_informe.clicked.connect(lambda: self.guardarInforme())
        self.venEntrega.btn_registrar_ficha.clicked.connect(lambda: self.guardarFicha())
        self.venEntrega.btn_registrar_memorandum.clicked.connect(lambda: self.guardarMemorandum())
        
        if(self.modo == "informe"):
            self.venEntrega.titulo_accion.setText('Entrega Informe')
            self.venEntrega.nombre_tutor.setText(self.dato[1])



    def cerrar_ui_perfil(self):
        self.parent.raizOpacidad.close()
        self.close()

    def ventana_configuracion(self):
        fecha_actual = QtCore.QDate.currentDate()
        self.venEntrega.fecha_informe.setDate(fecha_actual)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
        
    def obtener_mes(self):
        # Establecer el idioma español en la QLocale
        locale = QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Spain)
        QtCore.QLocale.setDefault(locale)
        
        fecha_seleccionada = self.venEntrega.fecha_informe.date()

        mes_texto = fecha_seleccionada.toString("MMMM")
        self.mes = mes_texto
        self.venEntrega.line_mes.setText(mes_texto)

     
    def cambioPagina(self):
        
        tipo_accion = self.venEntrega.cbo_tipo_entrega.currentText()
        
        if(tipo_accion == 'Informe'):
            self.venEntrega.stackedWidget.setCurrentIndex(0)
            self.venEntrega.titulo_accion.setText('Entrega Informe')
        elif( tipo_accion == "Ficha"):
            self.venEntrega.stackedWidget.setCurrentIndex(1)
            self.venEntrega.titulo_accion.setText('Entrega Ficha')
        else:
            self.venEntrega.stackedWidget.setCurrentIndex(2)
            self.venEntrega.titulo_accion.setText('Entrega Memorandum')
            

    def guardarInforme(self):

        fecha_informe = self.venEntrega.fecha_informe.date().toString("yyyy-MM-dd")
        tutor_id = self.dato[0]

        consulta_periodo = 'SELECT periodo_academico FROM vinculacion ORDER BY periodo_academico DESC LIMIT 1'
        periodo_academico = self.conec_base.getDatos(consulta_periodo)

        if not periodo_academico:
            QMessageBox.warning(self, "Error al guardar", "Aún no se ha iniciado ningún periodo académico")
            return

        periodo_academico = periodo_academico[0][0]
        
        consulta_validacion = 'SELECT tutor_id FROM informes WHERE tutor_id = %s AND periodo_academico = %s AND mes = %s'
        informes_existente = self.conec_base.getDatos_condicion(consulta_validacion, [tutor_id, periodo_academico, self.mes.title()])

        if len(informes_existente) > 0:
            QMessageBox.warning(self, "Error al guardar", "Ya existe un informe para este tutor en el mes seleccionado")
            return

        # Confirmar con el usuario si desea guardar el informe
        respuesta = QMessageBox.question(self, "Guardar informe", "¿Está seguro de que desea guardar el informe?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if respuesta != QMessageBox.Yes:
            return

        # Insertar el informe en la base de datos
        consulta_insertar = "INSERT INTO informes (fecha, tutor_id, mes,  periodo_academico) VALUES (%s, %s, %s, %s)"
        self.conec_base.setDatos(consulta_insertar, [fecha_informe, tutor_id,self.mes , periodo_academico])

        self.parent.llenarTabla('listar_tutores', 'tutores', self.parent.venPri.tabla_reporte_tutores)
        self.parent.actualizarInfoPaginacion('tutores', self.parent.venPri.lbl_pagina_reporte02, True )
        self.parent.configuracion_ventana()

        QMessageBox.information(self, "Mensaje", "Informe guardado exitosamente")
        self.parent.raizOpacidad.close()
        self.close()
        

    def guardarFicha(self):
        
        tutor_id = self.dato[0]

        # Obtener el periodo académico actual
        periodo_academico = self.conec_base.getDatos('SELECT periodo_academico FROM vinculacion ORDER BY periodo_academico DESC LIMIT 1')
        if not periodo_academico:
            QMessageBox.warning(self, "Error al guardar", "Aún no se ha iniciado ningún periodo académico")
            return

        periodo_academico = periodo_academico[0][0]

        # Verificar si la ficha ya existe para el tutor en el periodo académico actual
        ficha_existente = self.verificarExistenciaFicha(tutor_id, periodo_academico)

        # Confirmar con el usuario si desea guardar o actualizar la ficha
        pregunta = "¿Está seguro de actualizar la ficha?" if ficha_existente else "¿Está seguro de guardar la ficha?"
        respuesta = QMessageBox.question(self, "Guardar ficha", pregunta, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if respuesta == QMessageBox.Yes:
            # Determinar el estado de la ficha seleccionado por el usuario
            estado_ficha = self.obtenerEstadoFichaSeleccionado()

            if estado_ficha is None:
                QMessageBox.warning(self, "Mensaje", "Seleccione SI entregó ficha o NO")
                return

            if ficha_existente:
                # Actualizar ficha
                consulta_actualizar = "UPDATE fichas SET periodo_academico = %s, is_ficha = %s WHERE tutor_id = %s"
                self.conec_base.setDatos(consulta_actualizar, [periodo_academico, estado_ficha, tutor_id])
                mensaje = "Ficha actualizada exitosamente"
            else:
                # Insertar nueva ficha
                consulta_insertar = "INSERT INTO fichas (tutor_id, periodo_academico, is_ficha) VALUES (%s, %s, %s)"
                self.conec_base.setDatos(consulta_insertar, [tutor_id, periodo_academico, estado_ficha])
                mensaje = "Ficha guardada exitosamente"

            self.parent.llenarTabla('listar_tutores', 'tutores', self.parent.venPri.tabla_reporte_tutores)
            self.parent.actualizarInfoPaginacion('tutores', self.parent.venPri.lbl_pagina_reporte02, True )
            self.parent.configuracion_ventana()
            QMessageBox.information(self, "Mensaje", mensaje)
            self.parent.raizOpacidad.close()
            self.close()

    def verificarExistenciaFicha(self, tutor_id, periodo_academico):
        consulta_validacion = 'SELECT tutor_id FROM fichas WHERE tutor_id = %s AND periodo_academico = %s'
        ficha_existente = self.conec_base.getDatos_condicion(consulta_validacion, [tutor_id, periodo_academico])
        return len(ficha_existente) > 0

    def obtenerEstadoFichaSeleccionado(self):
        if self.venEntrega.rbt_si_ficha.isChecked():
            return True
        elif self.venEntrega.rbt_no_ficha.isChecked():
            return False
        return None



    def guardarMemorandum(self):
        tutor_id = self.dato[0]

        # Obtener el periodo académico actual
        periodo_academico = self.conec_base.getDatos('SELECT periodo_academico FROM vinculacion ORDER BY periodo_academico DESC LIMIT 1')
        if not periodo_academico:
            QMessageBox.warning(self, "Error al guardar", "Aún no se ha iniciado ningún periodo académico")
            return

        periodo_academico = periodo_academico[0][0]

        memorandum_existente = self.verificarExistenciaMemorandum(tutor_id, periodo_academico)

        pregunta = "¿Está seguro de actualizar la Memorandum?" if memorandum_existente else "¿Está seguro de guardar la Memorandum?"
        respuesta = QMessageBox.question(self, "Guardar Memorandum", pregunta, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if respuesta == QMessageBox.Yes:

            estado_memorandum = self.obtenerEstadoMemorandumSeleccionado()

            if estado_memorandum is None:
                QMessageBox.warning(self, "Mensaje", "Seleccione SI entregó Memorandum o NO")
                return

            if memorandum_existente:

                consulta_actualizar = "UPDATE memorandum SET periodo_academico = %s, is_memorandum = %s WHERE tutor_id = %s"
                self.conec_base.setDatos(consulta_actualizar, [periodo_academico, estado_memorandum, tutor_id])
                mensaje = "Memorandum actualizada exitosamente"
            else:

                consulta_insertar = "INSERT INTO memorandum (tutor_id, periodo_academico, is_memorandum) VALUES (%s, %s, %s)"
                self.conec_base.setDatos(consulta_insertar, [tutor_id, periodo_academico, estado_memorandum])
                mensaje = "Memorandum guardada exitosamente"


            self.parent.llenarTabla('listar_tutores', 'tutores', self.parent.venPri.tabla_reporte_tutores)
            self.parent.actualizarInfoPaginacion('tutores', self.parent.venPri.lbl_pagina_reporte02, True )
            self.parent.configuracion_ventana()
            QMessageBox.information(self, "Mensaje", mensaje)
            self.parent.raizOpacidad.close()
            self.close()

    def verificarExistenciaMemorandum(self, tutor_id, periodo_academico):
        consulta_validacion = 'SELECT tutor_id FROM memorandum WHERE tutor_id = %s AND periodo_academico = %s'
        ficha_existente = self.conec_base.getDatos_condicion(consulta_validacion, [tutor_id, periodo_academico])
        return len(ficha_existente) > 0

    def obtenerEstadoMemorandumSeleccionado(self):
        if self.venEntrega.rbt_si_memorandum.isChecked():
            return True
        elif self.venEntrega.rbt_no_memorandum.isChecked():
            return False
        return None