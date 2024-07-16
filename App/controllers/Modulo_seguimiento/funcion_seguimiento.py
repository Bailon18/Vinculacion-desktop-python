
from PySide2 import QtCore, QtWidgets , QtGui


def evento_tabla(parent):

    configuraciones_columnas = {
        parent.seguimiento_tutor.tabla_listado_actividades: {0: 50, 3: 120},
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
        tabla.setColumnCount(6)

        for fila in range(len(dato)):

            bton_editar_seguimiento = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                QToolButton:hover{background-color:#82b5b9}""",
                icono = u':/menu/detalle.png',
                tooltip = 'Detalle seguimiento')


            # bton_eliminar_seguimiento = crearbotoneslista(
            #     stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
            #             QToolButton:hover{background-color:#ebdada}""",
            #     icono = u':/menu/accion_eliminar.png',
            #     tooltip = 'Eliminar seguimiento')


            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(bton_editar_seguimiento)
            # layout.addWidget(bton_eliminar_seguimiento)

            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_seguimiento(bton_editar_seguimiento, fila, tabla, parent)
            # btn_eliminar_seguimiento(bton_eliminar_seguimiento, fila, tabla, parent)

            tabla.setCellWidget(fila ,5,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


                if columna == 4:
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

                if columna == 3:
                    if isinstance(dato[fila][columna], int):
                        horas = dato[fila][columna]
                        item.setText(f"{horas} {'hora' if horas == 1 else 'horas'}")

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
    #boton.clicked.connect(lambda: eliminar_seguimiento_acccion(fila,parent))

def editar_seguimiento_acccion(fila, parent):


    from controllers.Modulo_seguimiento.Modulo_seguimiento import Seguimiento


    if not parent.conec_base.verificarConexionInternet():
        QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
        return

    seguimiento_id = parent.venPri.tabla_seguimiento.item(fila, 0).text()
    estudiante_nombre = parent.venPri.tabla_seguimiento.item(fila, 1).text()
    
    parent.estudiantes_vinculacion_id = seguimiento_id
    parent.estudiantes_vinculacion_nombre = estudiante_nombre


    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    
    Seguimiento(parent, seguimiento_id, estudiante_nombre).exec_()




    # resultado = parent.conec_base.getDatosProcess_condicion("ObtenerSeguimientoPorId", (seguimiento_id,))
    # parent.cambiar_pagina_seguimiento('Edit', resultado )
    # parent.seguimiento_seleccionado = seguimiento_id
    # parent.modo_ventana = 'Edit'


# def eliminar_seguimiento_acccion(fila, parent):

#     if not parent.conec_base.verificarConexionInternet():
#         QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
#         return

#     seguimiento_id = parent.seguimiento_tutor.tabla_listado_seguimiento.item(fila, 0).text()
#     fecha = parent.seguimiento_tutor.tabla_listado_seguimiento.item(fila, 1).text()

#     mensaje = f"¿Está seguro(a) de eliminar el seguimiento de {parent.datos_compartidos[1].upper()}\n Registrada en la fecha {fecha}?."

#     respuesta = QtWidgets.QMessageBox.question(parent, "Mensaje", mensaje,
#         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

#     if respuesta == QtWidgets.QMessageBox.Yes:
#         consulta = 'DELETE FROM Seguimientos WHERE seguimiento_id = %s'
#         parent.conec_base.deleteDatos(consulta, ( seguimiento_id))
#         parent.parent.listar_vinculacion()
#         parent.listado_seguimiento()
#         parent.parent.listar_vinculacion_tutor()

#         QtWidgets.QMessageBox.information(parent, "Mensaje", f"Seguimiento se ha eliminado exitosamente.")


# -------------------------------------------------------------------------------------------------------------------

def llenar_tabla_actividades(parent, tabla, dato):
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(4)

        for fila in range(len(dato)):
            bton_editar_actividad = crearbotoneslista(
                stilo=u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                QToolButton:hover{background-color:#82b5b9}""",
                icono=u':/menu/acccion_editar.png',
                tooltip='Editar actividad'
            )

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1, 1, 1, 1)
            layout.setSpacing(3)
            layout.addWidget(bton_editar_actividad)

            if parent.parent.rol == 'Tutor':
                bton_eliminar_actividad = crearbotoneslista(
                    stilo=u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                    icono=u':/menu/accion_eliminar.png',
                    tooltip='Eliminar seguimiento'
                )
                layout.addWidget(bton_eliminar_actividad)
                btn_eliminar_actividad(bton_eliminar_actividad, fila, tabla, parent)
            
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_actividad(bton_editar_actividad, fila, tabla, parent)

            tabla.setCellWidget(fila, 3, widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

                if columna == 2:
                    if isinstance(dato[fila][columna], int):
                        horas = dato[fila][columna]
                        item.setText(f"{horas} {'hora' if horas == 1 else 'horas'}")

                tabla.setItem(fila, columna, item)
    else:
        tabla.setRowCount(0)


def btn_editar_actividad(boton,fila,tabla,parent):

    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))
    boton.clicked.connect(lambda: editar_actividad_acccion(fila,parent))


def btn_eliminar_actividad(boton,fila,tabla,parent):

    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))
    boton.clicked.connect(lambda: eliminar_seguimiento_acccion(fila,parent))


def editar_actividad_acccion(fila, parent):


    if not parent.conec_base.verificarConexionInternet():
        QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
        return

    id_actividad = parent.seguimiento_tutor.tabla_listado_actividades.item(fila, 0).text()
    
    parent.parent.id_actividad = id_actividad
    parent.parent.modo_formulario_seguimiento_estudiante = 'editar'
    
    parent.parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.parent.raizOpacidad.show()
    parent.close()
    
    parent.parent.abrir_ventana_nueva_actividad()
    

    

def eliminar_seguimiento_acccion(fila, parent):

    from controllers.Modulo_seguimiento.Modulo_seguimiento import Seguimiento


    if not parent.conec_base.verificarConexionInternet():
        QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
        return

    id_actividad = parent.seguimiento_tutor.tabla_listado_actividades.item(fila, 0).text()
    fecha = parent.seguimiento_tutor.tabla_listado_actividades.item(fila, 1).text()
    estudiante_nombre = parent.seguimiento_tutor.lbl_nombreestudiante.text()


    mensaje = f"¿Está seguro(a) de que desea eliminar la actividad registrada en la fecha {fecha}?"


    respuesta = QtWidgets.QMessageBox.question(parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    if respuesta == QtWidgets.QMessageBox.Yes:
        consulta = 'DELETE FROM seguimiento WHERE id = %s'
        parent.conec_base.deleteDatos(consulta, ( id_actividad, ))
        
        
        QtWidgets.QMessageBox.information(parent, "Mensaje", f"Actividad se ha eliminado exitosamente.")
        
        parent.parent.estudiantes_vinculacion_id = parent.id_seguimiento
        parent.parent.estudiantes_vinculacion_nombre = estudiante_nombre
    
        parent.parent.raizOpacidad.resize(parent.width(), parent.height())
        parent.parent.raizOpacidad.show()
        parent.close()
        
        
        parent.parent.abrir_ventana_seguimiento_tutor()
        parent.parent.llenar_estudiantes_seguimientos_tutor()
        
