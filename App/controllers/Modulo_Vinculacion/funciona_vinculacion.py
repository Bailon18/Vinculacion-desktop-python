
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

    estudiante_id = parent.vinculacion.tabla_estudiante_seleccionado.item(fila, 0).text()
    
    for estudiante in parent.lista_id_estudiantes:
        if estudiante[0] == estudiante_id:
            parent.lista_id_estudiantes.remove(estudiante)
            break
    
    llenar_tabla_estudiantes_seleccinados(parent, parent.vinculacion.tabla_estudiante_seleccionado, parent.lista_id_estudiantes)

    
    
    
    
    
    # nombre_estudiante = parent.venPri.tabla_principal.item(fila, 6).text()

    # mensaje = f"¿Está seguro(a) de eliminar la vinculación de {nombre_estudiante.upper()}? Esto eliminará los datos del estudiante y sus seguimientos realizados por el tutor asociados."

    # respuesta = QtWidgets.QMessageBox.question(parent, "Mensaje", mensaje,
    #     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    # if respuesta == QtWidgets.QMessageBox.Yes:
        
    #     if not parent.conec_base.verificarConexionInternet():
    #         QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
    #         return
        
    #     parent.conec_base.getDatosProcess_condicion("EliminarVinculacion", (vinculacion_id,))
    #     parent.listar_vinculacion()

    #     QtWidgets.QMessageBox.information(parent, "Mensaje", f"La vinculación de {nombre_estudiante.upper()} se ha eliminado exitosamente.")

