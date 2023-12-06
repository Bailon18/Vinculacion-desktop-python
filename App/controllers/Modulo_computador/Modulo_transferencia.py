
from PySide2 import QtWidgets , QtCore , QtGui
from controllers.Modulo_utils.funcion_efecto import Clase_Opacidad

from views.ui_tranferencia import Ui_Transferencia


# importamos la clase de la base datos
from db.Modulo_base import BaseDatos


class Tranferencia(QtWidgets.QDialog):

    def __init__(self , sede_actual, parent=None):
        
        super(Tranferencia, self).__init__(parent)
        self.venTransfe = Ui_Transferencia()
        self.venTransfe.setupUi(self)
        
        self.conec_base = BaseDatos()
        self.sede_actual = sede_actual # id
        print('sede actual ', self.sede_actual)
        self.parent = parent
        
        self.configuracion()
        
        # Evento Opacidad -----------------------
        self.raizOpacidad = Clase_Opacidad(parent)
        self.raizOpacidad.close()
        
        # Quitar fondo, transparencia
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.venTransfe.btn_closeTransfe.clicked.connect(lambda: self.parent.raizOpacidad.close())
        self.venTransfe.btn_closeTransfe.clicked.connect(lambda: self.close())
        
        self.llenadoLista()
        
        self.venTransfe.list_inicio.itemSelectionChanged.connect(lambda: self.pasar_seleccion())
        
        self.venTransfe.line_filtrar.textChanged.connect(lambda texto: self.evento_busqueda()
                                                           if(texto != '') else self.llenadoLista())
        self.lista = []
    
        self.venTransfe.btn_enviar.clicked.connect(lambda: self.enviarTransferencia())
    
    
    def configuracion (self):
        
        datos = self.conec_base.getDatos("SELECT * FROM sede")
        print("DATOS SEDE ", datos)
        self.venTransfe.cbox_sedeFinal.clear()
        for sede in datos:
            if sede[0] != self.sede_actual:
                self.venTransfe.cbox_sedeFinal.addItem(sede[1], sede[0])
            
    
    def seteoLista(self, lista):
        
        lista = [str(x[0]) +"  "+ x[1] for x in lista]
        self.venTransfe.list_inicio.clear()
        for item1  in lista:
            item = QtWidgets.QListWidgetItem(item1)
            item.setSizeHint(QtCore.QSize(50,25))
            item.setText(str(item1)) 
            self.venTransfe.list_inicio.addItem(item)  # listWidgetPDFlist
    
    def evento_busqueda(self):
        """
        Metodo que tiene por funcion hacer consulta en la tabla computador y retonar (ID, SERIAL)
        y respectivamente llenar con esos datos la lista apartir de un evento
        """
    
        textoBusqueda = self.venTransfe.line_filtrar.text().strip()
        consulta = """SELECT id, serial FROM computador WHERE sede_id = %s and serial LIKE %s"""
        da = self.conec_base.getDatos_condicion(consulta ,[self.sede_actual, '%'+textoBusqueda+'%'])
        
        self.seteoLista(da)

    def llenadoLista(self):
        
        """
        Metodo que tiene por funcion hacer consulta en la tabla computador y retonar (ID, SERIAL)
        y respectivamente llenar con esos datos la lista
        """
        consulta = """SELECT id, serial FROM computador WHERE sede_id = %s Order by id DESC LIMIT %s;"""
        da = self.conec_base.getDatos_condicion(consulta, (self.sede_actual, 8))
        
        self.seteoLista(da)

    def pasar_seleccion(self):
    
        seleccionado = self.venTransfe.list_inicio.selectedItems()
    
        editar = QtWidgets.QPushButton()
        editar.setMinimumSize(QtCore.QSize(0, 20))
        editar.setStyleSheet(u"QPushButton{background-color: #FBE9E9;\n"
                             "border-radius:5px}\QPushButton:hover{background-color:#ebdada}")
        editar.setIcon(QtGui.QIcon('source/image/basura1.png'))
        editar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(125,2,25,2)
        layout.addWidget(editar)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        

        for item1 in list(seleccionado):
            
            if item1.text() not in self.lista:
                
                # se agrega a la lista
                self.lista.append(item1.text())
                
                item = QtWidgets.QListWidgetItem(item1.text())
                item.setSizeHint(QtCore.QSize(50,25))
                self.venTransfe.list_final.addItem(item)
                self.venTransfe.list_final.setItemWidget(item, widget)
                self.accion_editar(editar, item)
               
    def accion_editar(self, boton, items):
        boton.clicked.connect(lambda : self.eliminar_items(items))
        
    def eliminar_items(self, items):

        if self.lista:
            for i in range(len(self.lista)):
                if self.lista[i] == items.text():
                    self.lista.remove(self.lista[i])
                    self.venTransfe.list_final.takeItem(i)
                    break


    def enviarTransferencia(self):
        
        lista = []
    
        fecha_envio  = self.venTransfe.date_fecha.date().toString("yyyy-MM-dd")
        sedeFinal_id = self.venTransfe.cbox_sedeFinal.itemData(self.venTransfe.cbox_sedeFinal.currentIndex())
       
        lista_computador = self.venTransfe.list_final.findItems('*', QtCore.Qt.MatchWildcard)
        
        if len(lista_computador) == 0:
            return
        
        if (QtWidgets.QMessageBox.question(self, "Transferencia","¿Estas segura(o) transferir los computadores seleccionados\n a"
                                           f"la sede {self.venTransfe.cbox_sedeFinal.currentText().upper()} ?",
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes):
            
            lista_computador=[i.text() for i in lista_computador]
        
            for i in lista_computador:
                id = i[0:i.index(" ")]
                lista.append(id)
            
            # actualizamos la tabla computador 
            consulta = 'UPDATE computador SET sede_id = %s WHERE id = %s'
            for i in lista:
                self.conec_base.updateDatos(consulta,[sedeFinal_id, i])
                
                
            # insertamos la transferencia realizada
            consulta = 'INSERT INTO transferencia(sede_inicial, fecha_envio, sede_final, computador_id)VALUES(%s, %s, %s, %s)'
            for i in lista:
                self.conec_base.setDatos(consulta,(self.sede_actual, fecha_envio, sedeFinal_id, i))
                
                
            rango_actual = self.parent.venPri.cbox_rango.currentText()
            self.parent.cargaCompu(rango_actual)
                
            # actualizar la tabla principal de computador sin la transferencia que hicimos
            QtWidgets.QMessageBox.information(self, "Información", "Se realizó correctamente la transferencia")
            self.parent.raizOpacidad.close()
            self.close()
    
            
        
        
        
        
        