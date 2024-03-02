
from PySide2 import QtCore, QtWidgets , QtGui

def crearbotoneslista(stilo,icono,tooltip):
    
    btn_nuevo = QtWidgets.QToolButton()
    btn_nuevo.setMinimumSize(QtCore.QSize(35, 34))
    btn_nuevo.setIconSize(QtCore.QSize(22, 22))
    btn_nuevo.setStyleSheet(stilo)
    btn_nuevo.setIcon(QtGui.QIcon(icono))
    btn_nuevo.setToolTip(tooltip)
    btn_nuevo.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))

    return btn_nuevo


def llenar_tabla_institucion(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(6)
   
        for fila in range(len(dato)):

            boton_editar_usuario = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar Instutición')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_editar_usuario)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_usuario(boton_editar_usuario, fila, tabla, parent)
          
            tabla.setCellWidget(fila ,5,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
                
def btn_editar_usuario(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_editar_acccion(fila,parent)) 
    

def ver_editar_acccion(fila, parent):
    pass