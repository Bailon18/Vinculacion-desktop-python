
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui
from PySide2.QtCore import Qt

from datetime import datetime
from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_vinculacion_nuevo import Ui_NuevaVinculacion




# importamos la clase de la base datos
from db.Modulo_base import BaseDatos


class Vinculacion(QtWidgets.QDialog):

    def __init__(self, datos=[] , modo="" , parent=None):
        
        super(Vinculacion, self).__init__(parent)
        self.vinculacion = Ui_NuevaVinculacion()
        self.vinculacion.setupUi(self)
        
        self.conec_base = BaseDatos()
        self.configuracion_ventana()

        self.parent = parent
        
        self.datos = datos
        self.modo = modo
        
        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(self.parent)
        self.raizOpacidad.close()

        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.vinculacion.btn_closeadmi.clicked.connect(lambda: self.cerrar_ui_vinculacion())
        
        # Para el QLineEdit line_identificacion
        # Para el QLineEdit line_identificacion
        val_identifiacion(self, self.vinculacion.line_identificacion)
        mascara_identificacion(self.vinculacion.line_identificacion)
        borrar_caracteres(self.vinculacion.line_identificacion, mascara_identificacion)


        # Para el QLineEdit line_periodoacademico
        val_periodo_academico(self, self.vinculacion.line_periodoacademico)
        mascara_periodo_academico(self.vinculacion.line_periodoacademico)
        borrar_caracteres(self.vinculacion.line_periodoacademico, mascara_periodo_academico)

        # Para el QLineEdit line_codigoies
        val_codigo_ies(self, self.vinculacion.line_codigoies)
        mascara_codigo_ies(self.vinculacion.line_codigoies)
        borrar_caracteres(self.vinculacion.line_codigoies, mascara_codigo_ies)


                

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
            
    def llenar_combobox(self, combobox, lista, longitud_maxima):
        for elemento in lista:
            id_elemento, nombre_elemento = elemento
            texto_truncado = nombre_elemento[:longitud_maxima]
            combobox.addItem(texto_truncado, userData=id_elemento)
            combobox.setItemData(combobox.count() - 1, nombre_elemento, Qt.ToolTipRole)

    def configuracion_ventana(self):
        lista_carrera, lista_institucion, lista_proyectos, lista_tutores = self.conec_base.getDatosProcess("ObtenerDatos")
        
        self.llenar_combobox(self.vinculacion.cbox_carrera, lista_carrera, 30)
        self.llenar_combobox(self.vinculacion.cbo_institucion, lista_institucion, 30)
        self.llenar_combobox(self.vinculacion.cbo_proyectos, lista_proyectos, 100)
        self.llenar_combobox(self.vinculacion.cbo_tutor, lista_tutores, 30)
        
    
        

    # def evento_fecha(self):
        
    #     if self.vinculacion.check_fecha.isChecked():
    #         self.vinculacion.fecha_registro.setDate(QtCore.QDate.fromString(self.fecha_actual, "dd-MM-yyyy"))

    # def cargaEdicionCompu(self, datos):

    #     datos =[x for x in datos[0][0]]
        
    #     self.vinculacion.line_id.setText(str(datos[0]))
    
    #     self.vinculacion.fecha_registro.setDate(QtCore.QDate.fromString(datos[1], "dd-MM-yyyy"))
 
    #     self.vinculacion.line_serial.setText(datos[2])
    #     self.vinculacion.line_placa.setText(datos[3])
    #     # MODELOS {3: 'Dell', 4: 'Lenovo'}
    #     # modelos -> id
    #     self.vinculacion.cbox_modelo.setCurrentText(self.modelos.get(datos[4]))
    #     self.vinculacion.cbox_compania.setCurrentText(self.compania.get(datos[6]))
    
    #     self.vinculacion.line_marca.setText(datos[5])
    #     self.vinculacion.line_ticket.setText(datos[7])

    # def cargaComputador(self, rango):
        
    #     """
    #     Metodo que tiene por funcion : listar el registro de computadoras condicionado por el sede
    #     """
        
    #     computadoras = self.conec_base.getDatosProcess_condicion('sp_listaComputador', [self.sede_actual,'%d-%m-%Y', rango])
    #     computadoras = [list(x) for x in computadoras[0]]
    #     return computadoras
          
    # def validar(self,texto, posicion):
        
        
        
    #     consultas = {1:"SELECT serial FROM computador where %s in (select serial FROM computador)",
    #                  2:"SELECT placa FROM computador where %s in (SELECT placa FROM computador)",
    #                  3:"SELECT ticket FROM computador where %s in (SELECT ticket FROM computador)"}
        
    #     objecto = {1:self.vinculacion.line_serial, 2:self.vinculacion.line_placa, 3:self.vinculacion.line_ticket, 4:self.vinculacion.line_marca}
    #     lbl_errores = {1:self.vinculacion.lbl_serial, 2:self.vinculacion.lbl_placa, 3:self.vinculacion.lbl_ticket, 4:self.vinculacion.lbl_marca}
    #     mensajes = {1:"Número serial ingresado ya existe!", 2:"Número placa ingresado ya existe!", 3:"Número ticket ingresado ya existe!"}
        
    #     if texto:
        
    #         if posicion in [1, 2, 3,]:
    #             consulta =self.conec_base.getDatos_condicion(consultas.get(posicion),(texto))
        
    #         if(posicion != 4 and consulta):
                
    #             self.lista_validacion.append(False)
    #             objecto.get(posicion).setStyleSheet('border: 2px solid red')
    #             lbl_errores.get(posicion).setText(mensajes.get(posicion))
                   
    #         else:
    #             self.lista_validacion.append(True)
    #             lbl_errores.get(posicion).setText("")
    #             objecto.get(posicion).setStyleSheet('border: 2px solid green')     
    #     else:
    #         lbl_errores.get(posicion).setText("")
    #         objecto.get(posicion).setStyleSheet('QLineEdit::focus{background: #FFFFFF;border: 2px solid #344647;border-radius: 8px;}')
            
    # def guardarComputador(self):
        
    #     # guardamos datos en las variables
    #     id = self.vinculacion.line_id.text()
    #     fecha_registro = self.vinculacion.fecha_registro.date().toString("yyyy-MM-dd")
    #     sede_id = self.sede_actual
    #     seriall = self.vinculacion.line_serial.text().strip()
    #     placa = self.vinculacion.line_placa.text().strip()
    #     marca = self.vinculacion.line_marca.text().strip()
    #     modelo_id = self.vinculacion.cbox_modelo.itemData(self.vinculacion.cbox_modelo.currentIndex())
    #     compania_id = self.vinculacion.cbox_compania.itemData(self.vinculacion.cbox_compania.currentIndex())
    #     ticket = self.vinculacion.line_ticket.text().strip()
        

    #     # consultas las serial , placa , ticket
    #     errores = True
                
    #     if seriall == '':
    #         errores = False
    #         self.vinculacion.line_serial.setStyleSheet('border: 2px solid red')
    #         self.vinculacion.lbl_serial.setText("Campo serial es obligatorio")
            
    #     if placa == '':
    #         errores = False
    #         self.vinculacion.line_placa.setStyleSheet('border: 2px solid red')
    #         self.vinculacion.lbl_placa.setText("Campo placa es obligatorio")
            
    #     if ticket == '':
    #         errores = False
    #         self.vinculacion.line_ticket.setStyleSheet('border: 2px solid red')
    #         self.vinculacion.lbl_ticket.setText("Campo ticket es obligatorio")
            
    #     if marca == '':
    #         errores = False
    #         self.vinculacion.line_marca.setStyleSheet('border: 2px solid red')
    #         self.vinculacion.lbl_marca.setText("Campo marca es obligatorio")
        
    #     print("VALIDACION ",self.lista_validacion)
        
    #     return

    #     if errores and self.validacion:
            
    #         if self.modo == 1:
                
    #             consulta = """
    #                         INSERT INTO computador(serial, marca, placa, fecha_registro, ticket, modelo_id, compania_id, sede_id)
    #                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    #                         """
    #             self.conec_base.setDatos(consulta, [seriall, marca, placa ,fecha_registro, ticket, modelo_id, compania_id, sede_id])
    #         else:
    #             consulta = """
    #                         UPDATE computador SET serial=%s, marca=%s, placa=%s, fecha_registro=%s, ticket=%s, modelo_id=%s,
    #                         compania_id=%s, sede_id=%s WHERE id = %s
    #                         """
    #             self.conec_base.updateDatos(consulta, [seriall, marca, placa ,fecha_registro, ticket, modelo_id, compania_id, sede_id, id])
            
    #         # Cargamos la tabla con el nuevo computador
    #         rango = self.parent.venPri.cbox_rango.currentText()
    #         cargatablaComputador(self.parent, self.parent.venPri.tabla_principal, self.cargaComputador(rango))
            
    #         QtWidgets.QMessageBox.information(self, 'Computadora', 'La computadora se guardo correctamente.')
            
    #         self.parent.raizOpacidad.close()
    #         self.close()
            
    # def configuracion(self):
    #     self.vinculacion.line_id.hide()
        
    #     modelos , compania , sede_actual = self.conec_base.getDatosProcess_condicion('sp_cargarComputador', [self.parent.dni]) 
        
    #     self.sede_actual = sede_actual[0][0]
        
    #     self.vinculacion.cbox_modelo.clear()
    #     for dato_mode in modelos:
    #         self.vinculacion.cbox_modelo.addItem(dato_mode[1], dato_mode[0])
        
    #     self.vinculacion.cbox_compania.clear()
    #     for dato_comp in compania:
    #         self.vinculacion.cbox_compania.addItem(dato_comp[1], dato_comp[0])
            
    #     # Cargamos los modelos , companias convertimos a diccionario

    #     self.modelos=dict(zip([i[0] for i in modelos],[i[1] for i in modelos]))
    #     self.compania=dict(zip([i[0] for i in compania],[i[1] for i in compania]))
        
    #     fecha = datetime.now()
    #     self.fecha_actual = fecha.strftime('%d-%m-%Y')
    #     self.vinculacion.fecha_registro.setDate(QtCore.QDate.fromString(self.fecha_actual, "dd-MM-yyyy"))
        
    #     # si la ventana es edicion -> llamamos al metodo de cargar datos
    #     if self.modo == 2:
    #         self.vinculacion.title_computador.setText('Edición Computadora')
    #         self.vinculacion.btn_guardar.setText('Actualizar')
    #         self.cargaEdicionCompu(self.datos)
            

        
        
        
    