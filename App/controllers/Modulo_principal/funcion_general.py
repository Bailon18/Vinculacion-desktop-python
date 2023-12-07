

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
                    parent.venPri.btn_usuario]:    
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
    # tabla configuracion ---------------
    # tabla configuracion ---------------
    parent.venPri.tabla_usuario.horizontalHeader().setVisible(True)
    parent.venPri.tabla_principal.horizontalHeader().setVisible(True)

    
    # Lista de tablas
    lista_tabla=[parent.venPri.tabla_usuario, parent.venPri.tabla_principal]

    # Lista de index
    lista_index=[[0,1,2,4],[0]]

    # Lista de tamaño
    lista_tamano=[[120,120,200,120],[50]]

    for tabla,index,tamano in zip(lista_tabla,lista_index,lista_tamano):

        # verificamos si el index esta lleno
        if index:
            # insertamos tamaño al index 
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


# def crearbotoneslista(stilo,icono,tooltip):
    
#     btn_nuevo = QtWidgets.QToolButton()
    
#     btn_nuevo.setMinimumSize(QtCore.QSize(55, 54))
#     btn_nuevo.setStyleSheet(stilo)
#     btn_nuevo.setIcon(QtGui.QIcon(icono))
#     btn_nuevo.setToolTip(tooltip)
#     btn_nuevo.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))

#     return btn_nuevo

# tabla principal
def crearbotoneslista(stilo,icono,tooltip):
    
    btn_nuevo = QtWidgets.QToolButton()
    btn_nuevo.setMinimumSize(QtCore.QSize(35, 34))
    btn_nuevo.setStyleSheet(stilo)
    btn_nuevo.setIcon(QtGui.QIcon(icono))
    btn_nuevo.setToolTip(tooltip)
    btn_nuevo.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))

    return btn_nuevo

def llenar_tabla_vinculacion(parent,tabla,dato):

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

            botonpdf = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FFF0E1; border-radius:8px}
                            QToolButton:hover{background-color:#f4e6d7}""",
                icono = u':/menu/accion_exportar.png',
                tooltip = 'Exportar a PDF')
            

            botonseguimiento = crearbotoneslista(
                stilo = u"""QToolButton{background-color:  #E1F1FF; border-radius:8px}
                            QToolButton:hover{background-color:#d0dfec}""",
                icono = u':/menu/menuafiliacion.png',
                tooltip = 'Ver seguimiento')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(botoneditar)
            layout.addWidget(botoneliminar)
            layout.addWidget(botonpdf)
            layout.addWidget(botonseguimiento)

            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar(botoneditar,fila,tabla,parent)
            btn_eliminar(botoneliminar, fila,tabla,parent)
            btn_pdf(botonpdf,fila,tabla,parent)
            btn_seguimiento(botonseguimiento,fila,tabla,parent)


            tabla.setCellWidget(fila ,6,widget)

            for columna in range(len(dato[fila])):
                tabla.setItem(fila,columna, QtWidgets.QTableWidgetItem(str(dato[fila][columna])))
                tabla.item(fila,columna).setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
        
          
def btn_editar(boton,fila,tabla,parent):
    
    """eventos  del boton editar """
    boton.clicked.connect(lambda: tabla.selectRow(fila)) # selecciona filaedi (pinta)              
    boton.clicked.connect(lambda: btn_editar_acciones(fila,parent)) # acciona a realizar
    
def btn_eliminar(boton,fila,tabla,parent):
    
    """eventos  del boton eleminar """
    boton.clicked.connect(lambda: tabla.selectRow(fila)) # selecciona filaedi (pinta)              
    boton.clicked.connect(lambda: btn_eliminar_acciones(fila,parent)) # acciona a realizar
    
def btn_pdf(boton,fila,tabla,parent):
    
    """eventos  del boton pdf """
    boton.clicked.connect(lambda: tabla.selectRow(fila)) # selecciona filaedi (pinta)              
    boton.clicked.connect(lambda: btn_editar_acciones(fila,parent)) # acciona a realizar
    
def btn_seguimiento(boton,fila,tabla,parent):
    
    """eventos  del boton seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila)) # selecciona filaedi (pinta)              
    boton.clicked.connect(lambda: btn_seguimiento_acciones(fila,parent)) # acciona a realizar
    
def btn_editar_acciones(fila,parent):
    
    from controllers.Modulo_Vinculacion.Modulo_Vinculacion import Vinculacion

    vinculacion_id = parent.venPri.tabla_principal.item(fila, 0).text()
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    Vinculacion(vinculacion_id, "actualizar", parent).exec_()


def btn_eliminar_acciones(fila, parent):
    vinculacion_id = parent.venPri.tabla_principal.item(fila, 0).text()
    nombre_estudiante = parent.venPri.tabla_principal.item(fila, 2).text()

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
    nombre_estudiante = parent.venPri.tabla_principal.item(fila, 2).text()
    nombre_tutor = parent.venPri.tabla_principal.item(fila, 5).text()

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

