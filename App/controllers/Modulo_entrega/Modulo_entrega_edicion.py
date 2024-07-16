
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import QDate

import re

from datetime import datetime
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_formulario_edicion_informe import Ui_EntregaActualizacion

from db.Modulo_base import BaseDatos

class EntregaEdicion(QtWidgets.QDialog):
    
    def __init__(self, parent,dato = []):

        super(EntregaEdicion, self).__init__()
        self.venEntrega_edicion = Ui_EntregaActualizacion()
        self.venEntrega_edicion.setupUi(self)
        self.conec_base = BaseDatos()

        self.parent = parent
        self.dato = dato

        self.ventana_configuracion()
        
        self.id_seleccionado_informe = None
        self.mes = None



        
        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()


        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.venEntrega_edicion.btn_closeadmi_3.clicked.connect(lambda: self.cerrar_ui_perfil())
        
        # self.venEntrega_edicion.fecha_informe.dateChanged.connect(lambda: self.obtener_mes())
        self.venEntrega_edicion.cbo_meses_entrega.activated.connect(lambda: self.obtenerDatoMesSeleccionado())
        self.venEntrega_edicion.btn_registrar_informe.clicked.connect(lambda: self.guardarInforme())
        # self.venEntrega_edicion.btn_registrar_ficha.clicked.connect(lambda: self.guardarFicha())
        # self.venEntrega_edicion.btn_registrar_memorandum.clicked.connect(lambda: self.guardarMemorandum())
        
        # if(self.modo == "informe"):
        #     self.venEntrega_edicion.titulo_accion.setText('Entrega Informe')
        #     self.venEntrega_edicion.nombre_tutor.setText(self.dato[1])



    def cerrar_ui_perfil(self):
        self.parent.raizOpacidad.close()
        self.close()

    def ventana_configuracion(self):
    
        self.venEntrega_edicion.nombre_tutor.setText(self.dato[1])
    
        consulta = 'SELECT id, mes FROM informes WHERE periodo_academico = %s AND tutor_id = %s'
        
        periodo = self.dato[2]
        tutor_id = self.dato[0]
        
        respuesta = self.conec_base.getDatos_condicion(consulta, [periodo, tutor_id, ])
        
        self.venEntrega_edicion.cbo_meses_entrega.clear()
        self.venEntrega_edicion.cbo_meses_entrega.addItem("Seleccione mes", None)

        for id, mes in respuesta:
            self.venEntrega_edicion.cbo_meses_entrega.addItem(mes, id)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
        


    def obtenerDatoMesSeleccionado(self):
        
        id_seleccionado = self.venEntrega_edicion.cbo_meses_entrega.currentData()
        
        if id_seleccionado is not None:
            
            consulta = 'SELECT * FROM informes WHERE id=%s'
            respuesta = self.conec_base.getDatos_condicion(consulta, [id_seleccionado, ])
            
            fecha_informe_str = str(respuesta[0][1]) 
            fecha_informe = QDate.fromString(fecha_informe_str, 'yyyy-MM-dd')
            
            if not fecha_informe.isValid():
                print("Error: La fecha no es válida")
                return
            
            self.venEntrega_edicion.fecha_informe.setDate(fecha_informe)
            
            year = fecha_informe.year()
            month = fecha_informe.month()
            
            fecha_minima = QDate(year, month, 1)
            fecha_maxima = QDate(year, month, fecha_informe.daysInMonth())
            
            self.venEntrega_edicion.fecha_informe.setMinimumDate(fecha_minima)
            self.venEntrega_edicion.fecha_informe.setMaximumDate(fecha_maxima)
            
            self.id_seleccionado_informe = respuesta[0][0]
            self.mes = respuesta[0][2]


   
    def guardarInforme(self):
        
        if self.venEntrega_edicion.cbo_meses_entrega.currentIndex() == 0:
            QMessageBox.critical(self, "Error", "Seleccione el mes que necesite actualizar o eliminar entrega")
            return

        
        fecha_informe = self.venEntrega_edicion.fecha_informe.date().toString("yyyy-MM-dd")

        if self.venEntrega_edicion.rbt_si_memorandum.isChecked():
            mensaje = f"¿Está seguro de que desea actualizar la entrega del informe perteneciente al mes {self.mes}?"
            consulta = "UPDATE informes SET fecha = %s WHERE id = %s"
            parametros = [fecha_informe, self.id_seleccionado_informe]
        else:
            mensaje = f"¿Está seguro de que desea eliminar la entrega del informe perteneciente al mes {self.mes}?"
            consulta = "DELETE FROM informes WHERE id = %s"
            parametros = [self.id_seleccionado_informe]

        respuesta = QMessageBox.question(self, "Confirmación", mensaje, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if respuesta != QMessageBox.Yes:
            return

        try:
            self.conec_base.setDatos(consulta, parametros)
            mensaje_exito = "Informe actualizado exitosamente"
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Se produjo un error al guardar el informe: {e}")
            return

        self.parent.llenarTabla('listar_tutores', 'tutores', self.parent.venPri.tabla_reporte_tutores)
        self.parent.actualizarInfoPaginacion('tutores', self.parent.venPri.lbl_pagina_reporte02, True)
        self.parent.configuracion_ventana()

        QMessageBox.information(self, "Mensaje", mensaje_exito)
        self.parent.raizOpacidad.close()
        self.close()

        


