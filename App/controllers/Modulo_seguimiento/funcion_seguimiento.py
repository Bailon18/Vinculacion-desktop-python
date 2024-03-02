
from PySide2 import QtCore, QtWidgets , QtGui


def evento_tabla(parent):

    parent.seguimiento_tutor.tabla_listado_seguimiento.horizontalHeader().setVisible(True)

    index = [0, 3] 
    tamano = [70, 140]  

    for ind, tam in zip(index, tamano):
        parent.seguimiento_tutor.tabla_listado_seguimiento.setColumnWidth(ind, tam)

    parent.seguimiento_tutor.tabla_listado_seguimiento.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    for ind in index:
        parent.seguimiento_tutor.tabla_listado_seguimiento.horizontalHeader().setSectionResizeMode(ind, QtWidgets.QHeaderView.Fixed)


def crearbotoneslista(stilo,icono,tooltip):
    
    btn_nuevo = QtWidgets.QToolButton()
    btn_nuevo.setMinimumSize(QtCore.QSize(35, 34))
    btn_nuevo.setIconSize(QtCore.QSize(20, 20))
    btn_nuevo.setStyleSheet(stilo)
    btn_nuevo.setIcon(QtGui.QIcon(icono))
    btn_nuevo.setToolTip(tooltip)
    btn_nuevo.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))

    return btn_nuevo


def llenar_tabla_seguimiento_tutor(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(4)
   
        for fila in range(len(dato)):

            bton_editar_seguimiento = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                QToolButton:hover{background-color:#82b5b9}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar seguimiento')


            bton_eliminar_seguimiento = crearbotoneslista(        
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                        QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/accion_eliminar.png',
                tooltip = 'Eliminar seguimiento')



            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(bton_editar_seguimiento)
            layout.addWidget(bton_eliminar_seguimiento)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_seguimiento(bton_editar_seguimiento, fila, tabla, parent)
            btn_eliminar_seguimiento(bton_eliminar_seguimiento, fila, tabla, parent)
          
            tabla.setCellWidget(fila ,3,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


                if columna == 2:
                        if isinstance(dato[fila][columna], int) or dato[fila][columna].isdigit():
                            item.setText(f"{dato[fila][columna]} horas")


                tabla.setItem(fila, columna, item)
    else:
        tabla.setRowCount(0)
                
def btn_editar_seguimiento(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: editar_seguimiento_acccion(fila,parent)) 

                
def btn_eliminar_seguimiento(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: eliminar_seguimiento_acccion(fila,parent)) 




def editar_seguimiento_acccion(fila, parent):
    
    if not parent.conec_base.verificarConexionInternet():
        QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
        return
    
    seguimiento_id = parent.seguimiento_tutor.tabla_listado_seguimiento.item(fila, 0).text()
    resultado = parent.conec_base.getDatosProcess_condicion("ObtenerSeguimientoPorId", (seguimiento_id,))
    parent.cambiar_pagina_seguimiento('Edit', resultado )
    parent.seguimiento_seleccionado = seguimiento_id
    parent.modo_ventana = 'Edit'


def eliminar_seguimiento_acccion(fila, parent):
    
    if not parent.conec_base.verificarConexionInternet():
        QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
        return

    seguimiento_id = parent.seguimiento_tutor.tabla_listado_seguimiento.item(fila, 0).text()
    fecha = parent.seguimiento_tutor.tabla_listado_seguimiento.item(fila, 1).text()

    mensaje = f"¿Está seguro(a) de eliminar el seguimiento de {parent.datos_compartidos[1].upper()}\n Registrada en la fecha {fecha}?."

    respuesta = QtWidgets.QMessageBox.question(parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    if respuesta == QtWidgets.QMessageBox.Yes:
        consulta = 'DELETE FROM Seguimientos WHERE seguimiento_id = %s'
        parent.conec_base.deleteDatos(consulta, ( seguimiento_id))
        parent.parent.listar_vinculacion()
        parent.listado_seguimiento()
        parent.parent.listar_vinculacion_tutor()

        QtWidgets.QMessageBox.information(parent, "Mensaje", f"Seguimiento se ha eliminado exitosamente.")


