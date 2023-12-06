from PySide2 import QtCore, QtWidgets , QtGui


"""

def crearbotoneslista(stilo,icono,tooltip):
    
    btn_nuevo = QtWidgets.QToolButton()
    btn_nuevo.setMinimumSize(QtCore.QSize(35, 34))
    btn_nuevo.setStyleSheet(stilo)
    btn_nuevo.setIcon(QtGui.QIcon(icono))
    btn_nuevo.setToolTip(tooltip)
    btn_nuevo.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))

    return btn_nuevo

def cargatablaComputador(parent,tabla,dato):

    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(8)
   
        for fila in range(len(dato)):
  
            btn_editar = crearbotoneslista(
                stilo = uQToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3},   
                icono = u':/iconbar/editar.png',#'image/editar.png',
                tooltip = 'Editar Computador')


            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(btn_editar)

    
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            editar_computador(btn_editar,fila,tabla,parent)

            tabla.setCellWidget(fila ,7,widget)
            
            for columna in range(len(dato[fila])):
                
                # La columna de sedes utilizamos  el diccionario de modelo para obtener el nombre apartir del id
                if columna == 3:
                    dato[fila][columna] = parent.modelos[dato[fila][columna]]
                    
                # La columna de sedes utilizamos  el diccionario de modelo para obtener el nombre apartir del id
                if columna == 5:
                    dato[fila][columna] = parent.compania[dato[fila][columna]]
                
                tabla.setItem(fila,columna, QtWidgets.QTableWidgetItem(str(dato[fila][columna])))
                # centrar item
                tabla.item(fila,columna).setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
                
def editar_computador(btn_editar,fila,tabla,parent):
    
    btn_editar.clicked.connect(lambda:tabla.selectRow(fila)) # selecciona la fila
    btn_editar.clicked.connect(lambda:editar_computadora(parent,fila,tabla)) # Modo 


def editar_computadora(parent,fila,tabla):
    from controllers.Modulo_computador.Modulo_computador import Computador
    
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()

    # Obtenemos el serial
    serial = tabla.item(fila,1).text()
    
    computadora = parent.conec_base.getDatosProcess_condicion('sp_busquedaComputador', [parent.sede_actual,'%d-%m-%Y', serial])
    
    Computador(computadora , 2, parent).exec_()
    
    
"""