
from PySide2 import QtCore, QtWidgets , QtGui
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon


def evento_tabla(parent):
    
    configuraciones_columnas = {
        parent.vinculacion.tabla_estudiante_seleccionado: {0:50, 1: 150,  3:120, 4: 120}
    }

    for tabla in configuraciones_columnas:
        header = tabla.horizontalHeader()
        header.setVisible(True)       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        for columna, ancho in configuraciones_columnas[tabla].items():
            tabla.setColumnWidth(columna, ancho)
        for i in range(1, tabla.columnCount()):
            if i not in configuraciones_columnas[tabla]:
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                
def evento_tabla_detalle(parent):
    
    configuraciones_columnas = {
        parent.vinculaciondetalle.tabla_estudiante_seleccionado: {0:50, 1: 150,  3:120, 4: 120}
    }

    for tabla in configuraciones_columnas:
        header = tabla.horizontalHeader()
        header.setVisible(True)       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        for columna, ancho in configuraciones_columnas[tabla].items():
            tabla.setColumnWidth(columna, ancho)
        for i in range(1, tabla.columnCount()):
            if i not in configuraciones_columnas[tabla]:
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                
                
def crearbotoneslista(stilo,icono,tooltip):
    
    btn_nuevo = QtWidgets.QToolButton()
    btn_nuevo.setMinimumSize(QtCore.QSize(35, 34))
    btn_nuevo.setIconSize(QtCore.QSize(22, 22))
    btn_nuevo.setStyleSheet(stilo)
    btn_nuevo.setIcon(QtGui.QIcon(icono))
    btn_nuevo.setToolTip(tooltip)
    btn_nuevo.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))

    return btn_nuevo

def llenar_tabla_estudiantes_seleccinados(parent, tabla, dato):
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(5)
   
        for fila in range(len(dato)):
            

            botoneliminar = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/accion_eliminar.png',
                tooltip = 'Eliminar estudiante seleccionado')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
    
            layout.addWidget(botoneliminar)
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_eliminar_estudiante_seleccionado(botoneliminar, fila, tabla, parent)
  
            tabla.setCellWidget(fila ,4,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
    else:
        tabla.setRowCount(0) 
          
    
def btn_eliminar_estudiante_seleccionado(boton,fila,tabla,parent):
    
    """eventos  del boton eleminar """
    boton.clicked.connect(lambda: tabla.selectRow(fila))            
    boton.clicked.connect(lambda: btn_eliminar_acciones_estudiante_seleccionado(fila,parent)) 
    


def btn_eliminar_acciones_estudiante_seleccionado(fila, parent):

    estudiante_id = int(parent.vinculacion.tabla_estudiante_seleccionado.item(fila, 0).text())
    
    print(f"Estudiante a eliminar: {estudiante_id}")
    print(f' lista {parent.lista_id_estudiantes}')
    
    for estudiante in parent.lista_id_estudiantes:
        if estudiante[0] == estudiante_id:
            parent.lista_id_estudiantes.remove(estudiante)
            break
    
    llenar_tabla_estudiantes_seleccinados(parent, parent.vinculacion.tabla_estudiante_seleccionado, parent.lista_id_estudiantes)

    
def llenar_tabla_estudiantes_detalle(parent, tabla, dato):
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(5)
   
        for fila in range(len(dato)):
            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))

                if columna == 3:
                    estado_columna = str(dato[fila][columna])
                    
                    if estado_columna == 'Pendiente':
                        color_texto = QtGui.QColor('#FFD700')  
                        texto = 'Pendiente'
                    elif estado_columna == 'En Proceso':
                        color_texto = QtGui.QColor('#008000') 
                        texto = 'En Proceso'
                    elif estado_columna == 'Culminado':
                        color_texto = QtGui.QColor('#FF0000') 
                        texto = 'Culminado'
                    else:
                        color_texto = QtGui.QColor('#000000') 
                        texto = estado_columna  

                    item.setForeground(QtGui.QBrush(color_texto))

                    font = QtGui.QFont()
                    font.setBold(True)
                    item.setFont(font)
                    
                    item.setText(texto)

                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)

    else:
        tabla.setRowCount(0)

    
