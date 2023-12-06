
from sys import version
from PySide2 import QtWidgets , QtCore , QtGui

from datetime import datetime
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_computador_nuevo import Ui_Computador

from controllers.Modulo_principal.funcion_general import cargatablaComputador


# importamos la clase de la base datos
from db.Modulo_base import BaseDatos


class Computador(QtWidgets.QDialog):

    def __init__(self, datos , modo , parent=None):
        
        super(Computador, self).__init__(parent)
        self.venComp = Ui_Computador()
        self.venComp.setupUi(self)
        
        self.conec_base = BaseDatos()
        
        # clase Principal
        self.parent = parent
        
        self.datos = datos
        self.modo = modo
        
            # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(parent)
        self.raizOpacidad.close()
        self.lista_validacion = []
        
        self.sede_actual = 0
        self.validacion = True
        
        self.configuracion()
        
        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.venComp.btn_closeadmi.clicked.connect(lambda: self.parent.raizOpacidad.close())
        self.venComp.btn_closeadmi.clicked.connect(lambda: self.close())
        
        self.venComp.check_fecha.clicked.connect(lambda: self.evento_fecha()) #1
        self.venComp.btn_guardar.clicked.connect(lambda: self.guardarComputador())
        
        # Evento validaciones campos serial - placa - ticket
        self.venComp.line_serial.textChanged.connect(lambda textoSerial: self.validar(textoSerial, 1))
        self.venComp.line_placa.textChanged.connect(lambda textoPlaca: self.validar(textoPlaca, 2))
        self.venComp.line_ticket.textChanged.connect(lambda textoTicket: self.validar(textoTicket, 3))
        self.venComp.line_marca.textChanged.connect(lambda textoMarca: self.validar(textoMarca, 4))
        
        

    def keyPressEvent(self, event):
        ''' 
        Metodo que detecta el boton espace y lo desabilita 
        '''
        if event.key() == QtCore.Qt.Key_Escape:
            pass
        
    def keyPressEvent(self, qKeyEvent):
        '''
        Metodo que configura para movernos de un input a otro atravez del boton enter
        '''
        if qKeyEvent.modifiers() & QtCore.Qt.AltModifier:
            qKeyEvent.ignore()
        elif qKeyEvent.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.focusNextChild()
            self.window().setAttribute(QtCore.Qt.WA_KeyboardFocusChange)
        else:
            super().keyPressEvent(qKeyEvent)
 
    def evento_fecha(self):
        
        if self.venComp.check_fecha.isChecked():
            self.venComp.fecha_registro.setDate(QtCore.QDate.fromString(self.fecha_actual, "dd-MM-yyyy"))

    def cargaEdicionCompu(self, datos):

        datos =[x for x in datos[0][0]]
        
        self.venComp.line_id.setText(str(datos[0]))
    
        self.venComp.fecha_registro.setDate(QtCore.QDate.fromString(datos[1], "dd-MM-yyyy"))
 
        self.venComp.line_serial.setText(datos[2])
        self.venComp.line_placa.setText(datos[3])
        # MODELOS {3: 'Dell', 4: 'Lenovo'}
        # modelos -> id
        self.venComp.cbox_modelo.setCurrentText(self.modelos.get(datos[4]))
        self.venComp.cbox_compania.setCurrentText(self.compania.get(datos[6]))
    
        self.venComp.line_marca.setText(datos[5])
        self.venComp.line_ticket.setText(datos[7])

    def cargaComputador(self, rango):
        
        """
        Metodo que tiene por funcion : listar el registro de computadoras condicionado por el sede
        """
        
        computadoras = self.conec_base.getDatosProcess_condicion('sp_listaComputador', [self.sede_actual,'%d-%m-%Y', rango])
        computadoras = [list(x) for x in computadoras[0]]
        return computadoras
          
    def validar(self,texto, posicion):
        
        
        
        consultas = {1:"SELECT serial FROM computador where %s in (select serial FROM computador)",
                     2:"SELECT placa FROM computador where %s in (SELECT placa FROM computador)",
                     3:"SELECT ticket FROM computador where %s in (SELECT ticket FROM computador)"}
        
        objecto = {1:self.venComp.line_serial, 2:self.venComp.line_placa, 3:self.venComp.line_ticket, 4:self.venComp.line_marca}
        lbl_errores = {1:self.venComp.lbl_serial, 2:self.venComp.lbl_placa, 3:self.venComp.lbl_ticket, 4:self.venComp.lbl_marca}
        mensajes = {1:"Número serial ingresado ya existe!", 2:"Número placa ingresado ya existe!", 3:"Número ticket ingresado ya existe!"}
        
        if texto:
        
            if posicion in [1, 2, 3,]:
                consulta =self.conec_base.getDatos_condicion(consultas.get(posicion),(texto))
        
            if(posicion != 4 and consulta):
                
                self.lista_validacion.append(False)
                objecto.get(posicion).setStyleSheet('border: 2px solid red')
                lbl_errores.get(posicion).setText(mensajes.get(posicion))
                   
            else:
                self.lista_validacion.append(True)
                lbl_errores.get(posicion).setText("")
                objecto.get(posicion).setStyleSheet('border: 2px solid green')     
        else:
            lbl_errores.get(posicion).setText("")
            objecto.get(posicion).setStyleSheet('QLineEdit::focus{background: #FFFFFF;border: 2px solid #344647;border-radius: 8px;}')
            
    def guardarComputador(self):
        
        # guardamos datos en las variables
        id = self.venComp.line_id.text()
        fecha_registro = self.venComp.fecha_registro.date().toString("yyyy-MM-dd")
        sede_id = self.sede_actual
        seriall = self.venComp.line_serial.text().strip()
        placa = self.venComp.line_placa.text().strip()
        marca = self.venComp.line_marca.text().strip()
        modelo_id = self.venComp.cbox_modelo.itemData(self.venComp.cbox_modelo.currentIndex())
        compania_id = self.venComp.cbox_compania.itemData(self.venComp.cbox_compania.currentIndex())
        ticket = self.venComp.line_ticket.text().strip()
        

        # consultas las serial , placa , ticket
        errores = True
                
        if seriall == '':
            errores = False
            self.venComp.line_serial.setStyleSheet('border: 2px solid red')
            self.venComp.lbl_serial.setText("Campo serial es obligatorio")
            
        if placa == '':
            errores = False
            self.venComp.line_placa.setStyleSheet('border: 2px solid red')
            self.venComp.lbl_placa.setText("Campo placa es obligatorio")
            
        if ticket == '':
            errores = False
            self.venComp.line_ticket.setStyleSheet('border: 2px solid red')
            self.venComp.lbl_ticket.setText("Campo ticket es obligatorio")
            
        if marca == '':
            errores = False
            self.venComp.line_marca.setStyleSheet('border: 2px solid red')
            self.venComp.lbl_marca.setText("Campo marca es obligatorio")
        
        print("VALIDACION ",self.lista_validacion)
        
        return

        if errores and self.validacion:
            
            if self.modo == 1:
                
                consulta = """
                            INSERT INTO computador(serial, marca, placa, fecha_registro, ticket, modelo_id, compania_id, sede_id)
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
                            """
                self.conec_base.setDatos(consulta, [seriall, marca, placa ,fecha_registro, ticket, modelo_id, compania_id, sede_id])
            else:
                consulta = """
                            UPDATE computador SET serial=%s, marca=%s, placa=%s, fecha_registro=%s, ticket=%s, modelo_id=%s,
                            compania_id=%s, sede_id=%s WHERE id = %s
                            """
                self.conec_base.updateDatos(consulta, [seriall, marca, placa ,fecha_registro, ticket, modelo_id, compania_id, sede_id, id])
            
            # Cargamos la tabla con el nuevo computador
            rango = self.parent.venPri.cbox_rango.currentText()
            cargatablaComputador(self.parent, self.parent.venPri.tabla_principal, self.cargaComputador(rango))
            
            QtWidgets.QMessageBox.information(self, 'Computadora', 'La computadora se guardo correctamente.')
            
            self.parent.raizOpacidad.close()
            self.close()
            
    def configuracion(self):
        self.venComp.line_id.hide()
        
        modelos , compania , sede_actual = self.conec_base.getDatosProcess_condicion('sp_cargarComputador', [self.parent.dni]) 
        
        self.sede_actual = sede_actual[0][0]
        
        self.venComp.cbox_modelo.clear()
        for dato_mode in modelos:
            self.venComp.cbox_modelo.addItem(dato_mode[1], dato_mode[0])
        
        self.venComp.cbox_compania.clear()
        for dato_comp in compania:
            self.venComp.cbox_compania.addItem(dato_comp[1], dato_comp[0])
            
        # Cargamos los modelos , companias convertimos a diccionario

        self.modelos=dict(zip([i[0] for i in modelos],[i[1] for i in modelos]))
        self.compania=dict(zip([i[0] for i in compania],[i[1] for i in compania]))
        
        fecha = datetime.now()
        self.fecha_actual = fecha.strftime('%d-%m-%Y')
        self.venComp.fecha_registro.setDate(QtCore.QDate.fromString(self.fecha_actual, "dd-MM-yyyy"))
        
        # si la ventana es edicion -> llamamos al metodo de cargar datos
        if self.modo == 2:
            self.venComp.title_computador.setText('Edición Computadora')
            self.venComp.btn_guardar.setText('Actualizar')
            self.cargaEdicionCompu(self.datos)
            

        
        
        
    