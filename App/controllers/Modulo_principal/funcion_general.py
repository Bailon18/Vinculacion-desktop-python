

from PySide2 import QtCore, QtWidgets , QtGui


def evento_menu(parent, parentRaiz, tr = 250):
    """ Funcion de evento de animacion del menu """
    
    # ancho actual del frame
    width = parentRaiz.frame_menu.width()
    
    
    if width == 91:
        newWidth = 220
    else:
        newWidth = 91
        
    parent.animation = QtCore.QPropertyAnimation(parentRaiz.frame_menu, b"minimumWidth")
    parent.animation.setDuration(tr)
    parent.animation.setStartValue(width)
    parent.animation.setEndValue(newWidth)
    parent.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    
    parent.animation.start()
    
def evento_hora(self):
    
    hora = QtCore.QTime.currentTime().toString("hh:mm:ss AP")
    
    hora = QtCore.QTime.currentTime().toString("hh:mm:ss")
    self.venPri.lbl_hora.setText(hora)
    
    fecha = QtCore.QDate.currentDate()
    self.venPri.lbl_fecha.setText(fecha.toString(QtCore.Qt.DefaultLocaleLongDate).title())
    
    self.venPri.hora = QtCore.QTimer(self)
    self.venPri.hora.setInterval(1000)
    self.venPri.hora.timeout.connect(lambda:Hora(self))
    self.venPri.hora.start()
    
def Hora(self):
    hora = QtCore.QTime.currentTime().toString("hh:mm:ss")
    self.venPri.lbl_hora.setText(hora)

def evento_pagina(parent,index,boton):

    """
    Funcion que recibe por parametro la clase(ventana),index(pagina),boton seleccionado(objeto)
    funcionalidad pintar y despintar la seleccion del menu
    """

    stylox="{color: white;background:#8cc0c2;border-top-left-radius:25px;border-bottom-left-radius: 25px}"

    # Despinta
    for btn in [parent.venPri.btn_afiliacion,parent.venPri.btn_home,parent.venPri.btn_reporte,
                    parent.venPri.btn_usuario, parent.venPri.btn_seguimientoo]:    
        btn.setStyleSheet(btn.styleSheet().replace("#"+btn.objectName()+ stylox,""))

    # Pinta
    boton.setStyleSheet("#"+boton.objectName()+"{color: white;background:#8cc0c2;border-top-left-radius:25px;border-bottom-left-radius: 25px}")
    parent.venPri.stackedWidget.setCurrentIndex(index)


def evento_ocultar(tol_inv,tol_vis,line,dato):
    """ 
    Esta funcion recibe por parametro los toolbutton de visible y invisible 
    para mostrar y ocultar el campo contraseña
    """
    if dato == 1:
        tol_inv.hide(),tol_vis.show()
        line.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        tol_vis.hide();tol_inv.show()
        line.setEchoMode(QtWidgets.QLineEdit.Password)

def eventorol(parent,parent2):
    """Funcion recibe por parametro clase """
    
    
    parent.listaseleccion=[]
    if(parent2.admi.isChecked()):
        parent.listaseleccion.append(3)
    if(parent2.user.isChecked()):
        parent.listaseleccion.append(4)

def evento_tabla(parent):
    """
    Funcion que recibe como paramentro la clase ventana principal
    funcionalidad es darle tamaño a las columnas 
    """

    parent.venPri.tabla_principal.horizontalHeader().setVisible(True)
    parent.venPri.tabla_principal_tutor.horizontalHeader().setVisible(True)

    
    # Lista de tablas
    lista_tabla=[parent.venPri.tabla_principal, parent.venPri.tabla_principal_tutor]

    # Lista de index
    lista_index=[[0,1,2,6], [0,1,2,5]]

    # Lista de tamaño
    lista_tamano=[[70,200,150,160], [70,300,150, 160]]

    for tabla,index,tamano in zip(lista_tabla,lista_index,lista_tamano):

        if index:
            for ind,tam in zip(index,tamano):
                tabla.setColumnWidth(ind,tam)

        tabla.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    for tabla,index in zip(lista_tabla,lista_index):
        if index:
            for ind in index:
                tabla.horizontalHeader().setSectionResizeMode(ind, QtWidgets.QHeaderView.Fixed)
            
    
def estilo(parent):
    estiloDefecto =QtWidgets.QStyleFactory.create('windowsvista')
    parent.venedit.bnt_ojoInv.setStyle(estiloDefecto)
    parent.venedit.bnt_ojoVis.setStyle(estiloDefecto)

# tabla principal
def crearbotoneslista(stilo,icono,tooltip):
    
    btn_nuevo = QtWidgets.QToolButton()
    btn_nuevo.setMinimumSize(QtCore.QSize(35, 34))
    btn_nuevo.setIconSize(QtCore.QSize(20, 20))
    btn_nuevo.setStyleSheet(stilo)
    btn_nuevo.setIcon(QtGui.QIcon(icono))
    btn_nuevo.setToolTip(tooltip)
    btn_nuevo.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))

    return btn_nuevo

def llenar_tabla_vinculacion(parent, tabla, dato):
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(7)
   
        for fila in range(len(dato)):
            botoneditar = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar vinculacion')

            botoneliminar = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/accion_eliminar.png',
                tooltip = 'Eliminar vinculacion')


            botonseguimiento = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #91cbcf; border-radius:8px}
                            QToolButton:hover{background-color:#82b5b9}""",
                icono = u':/menu/detalle.png',
                tooltip = 'Ver seguimiento')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(botoneditar)
            layout.addWidget(botoneliminar)
            layout.addWidget(botonseguimiento)

            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar(botoneditar, fila, tabla, parent)
            btn_eliminar(botoneliminar, fila, tabla, parent)
            btn_seguimiento(botonseguimiento, fila, tabla, parent)

            tabla.setCellWidget(fila ,6,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                
                if columna == 5: 
                    estado_columna = str(dato[fila][columna])
                    color_texto = QtGui.QColor('red') if estado_columna == 'Pendiente' else QtGui.QColor('green')
                    item.setForeground(QtGui.QBrush(color_texto))

                tabla.setItem(fila, columna, item)
        
          
def btn_editar(boton,fila,tabla,parent):
    
    """eventos  del boton editar """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: btn_editar_acciones(fila,parent)) 
    
def btn_eliminar(boton,fila,tabla,parent):
    
    """eventos  del boton eleminar """
    boton.clicked.connect(lambda: tabla.selectRow(fila))            
    boton.clicked.connect(lambda: btn_eliminar_acciones(fila,parent)) 
    
def btn_seguimiento(boton,fila,tabla,parent):
    
    """eventos  del boton seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))              
    boton.clicked.connect(lambda: btn_seguimiento_acciones(fila,parent)) 
    
    
def btn_editar_acciones(fila,parent):
    
    from controllers.Modulo_Vinculacion.Modulo_Vinculacion import Vinculacion

    vinculacion_id = parent.venPri.tabla_principal.item(fila, 0).text()
    nombre_estudiante = parent.venPri.tabla_principal.item(fila, 1).text()
    estado = parent.venPri.tabla_principal.item(fila, 5).text()
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    Vinculacion(vinculacion_id, nombre_estudiante,estado,  "actualizar", parent).exec_()

def btn_eliminar_acciones(fila, parent):
    vinculacion_id = parent.venPri.tabla_principal.item(fila, 0).text()
    nombre_estudiante = parent.venPri.tabla_principal.item(fila, 1).text()

    mensaje = f"¿Está seguro(a) de eliminar la vinculación de {nombre_estudiante.upper()}? Esto eliminará los datos del estudiante y sus seguimientos realizados por el tutor asociados."

    respuesta = QtWidgets.QMessageBox.question(parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    if respuesta == QtWidgets.QMessageBox.Yes:
        parent.conec_base.getDatosProcess_condicion("EliminarVinculacion", (vinculacion_id,))
        parent.listar_vinculacion()

        QtWidgets.QMessageBox.information(parent, "Mensaje", f"La vinculación de {nombre_estudiante.upper()} se ha eliminado exitosamente.")

def btn_seguimiento_acciones(fila, parent):

    from controllers.Modulo_principal.seguimiento_admin import Seguimiento_admin

    vinculacion_id = parent.venPri.tabla_principal.item(fila, 0).text()
    nombre_estudiante = parent.venPri.tabla_principal.item(fila, 1).text()
    nombre_tutor = parent.venPri.tabla_principal.item(fila, 4).text()

    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    Seguimiento_admin([nombre_estudiante, nombre_tutor, vinculacion_id],parent = parent).exec_()

def cargar_tabla(tabla,dato):
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(len(dato[0]))
   
        for fila in range(len(dato)):
            for columna in range(len(dato[fila])):
                tabla.setItem(fila,columna, QtWidgets.QTableWidgetItem(str(dato[fila][columna])))
                # centrar item
                tabla.item(fila,columna).setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)

    else:
        tabla.setRowCount(0)

def llenar_tabla_seguimiento(parent, tabla, dato):
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(6)
   
        for fila in range(len(dato)):

            boton_agregar_seguimiento = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/agregar_seguimiento.png',
                tooltip = 'Agregar seguimiento')


            bton_editar_seguimiento = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #91cbcf; border-radius:8px}
                QToolButton:hover{background-color:#82b5b9}""",
                icono = u':/menu/seguimiento_edtir.png',
                tooltip = 'Editar seguimiento')


            bton_eliminar_seguimiento = crearbotoneslista(        
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                        QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/seguimiento_eliminar.png',
                tooltip = 'Eliminar seguimiento')



            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_agregar_seguimiento)
            layout.addWidget(bton_editar_seguimiento)
            layout.addWidget(bton_eliminar_seguimiento)

            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_agregar_seguimiento(boton_agregar_seguimiento, fila, tabla, parent)
            btn_eliminar_seguimiento(bton_eliminar_seguimiento, fila, tabla, parent)
            btn_editr_seguimiento(bton_editar_seguimiento, fila, tabla, parent)

            tabla.setCellWidget(fila ,5,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                
                if columna == 3:
                    if isinstance(dato[fila][columna], int) or dato[fila][columna].isdigit():
                        item.setText(f"{dato[fila][columna]} horas")
                        
                if columna == 4: 
                    estado_columna = str(dato[fila][columna])
                    color_texto = QtGui.QColor('red') if estado_columna == 'Pendiente' else QtGui.QColor('green')
                    item.setForeground(QtGui.QBrush(color_texto))

                tabla.setItem(fila, columna, item)
                
def btn_agregar_seguimiento(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    #boton.clicked.connect(lambda: btn_editar_acciones(fila,parent)) 
    
def btn_eliminar_seguimiento(boton,fila,tabla,parent):
    
    """eventos  del boton eliminar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))            
    #boton.clicked.connect(lambda: btn_eliminar_acciones(fila,parent)) 
    
def btn_editr_seguimiento(boton,fila,tabla,parent):
    
    """eventos  del boton editar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))              
    #boton.clicked.connect(lambda: btn_seguimiento_acciones(fila,parent)) 