

from PySide2 import QtCore, QtWidgets , QtGui
from PySide2 import QtWidgets


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
    
    self.venPri.lbl_hora.setText(hora)
    fecha = QtCore.QDate.currentDate()
    
    fecha_formateada = fecha.toString("dddd d 'de' MMMM  yyyy")
    
    # Establecer la fecha en el QLabel lbl_fecha
    self.venPri.lbl_fecha.setText(fecha_formateada.capitalize())

    
    self.venPri.hora = QtCore.QTimer(self)
    self.venPri.hora.setInterval(1000)
    self.venPri.hora.timeout.connect(lambda:Hora(self))
    self.venPri.hora.start()
    
def Hora(self):
    hora = QtCore.QTime.currentTime().toString("hh:mm:ss")
    self.venPri.lbl_hora.setText(hora)

def evento_pagina_mantenimiento(parent, index, boton):
    # Estilo deseado para el botón cuando se hace clic
    estilo_clic = """
        QPushButton {
            color: #445d5e;
            font-weight: bold;
            font-size: 14px;
            border-bottom: 2px solid #445d5e;
        }
    """

    # Establecer el estilo al botón
    boton.setStyleSheet(estilo_clic)

    # Restablecer el estilo de los otros botones si es necesario
    for btn in [parent.venPri.btn_menu_institucion, parent.venPri.btn_menu_proyectos]:
        if btn != boton:
            btn.setStyleSheet("")  # Establecer un estilo vacío o inicial si es necesario

    # Cambiar la página actual
    parent.venPri.stackedWidget_6.setCurrentIndex(index)



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
        
def evento_seleccion_reporte(parent, boton, index):
    
    estilo_clic = """
        QPushButton {
            color: #445d5e;
            font-weight: bold;
            font-size: 14px;
            border-bottom: 2px solid #445d5e;
        }
    """

    boton.setStyleSheet(estilo_clic)

    for btn in [parent.venPri.radioEstudiante, parent.venPri.radioTutor]:
        if btn != boton:
            btn.setStyleSheet("")  


    parent.venPri.stackedWidget_5.setCurrentIndex(index)

        
def evento_tabla(parent):
    """
    Funcion que recibe como paramentro la clase ventana principal
    funcionalidad es darle tamaño a las columnas 
    """

    parent.venPri.tabla_principal.horizontalHeader().setVisible(True)
    parent.venPri.tabla_principal_tutor.horizontalHeader().setVisible(True)
    parent.venPri.tabla_usuario.horizontalHeader().setVisible(True)
    parent.venPri.tabla_intituciones.horizontalHeader().setVisible(True)
    parent.venPri.tabla_proyectos.horizontalHeader().setVisible(True)
    parent.venPri.tabla_reporte_tutores.horizontalHeader().setVisible(True)
    parent.venPri.tabla_reporte_estudiantes.horizontalHeader().setVisible(True)

    
    # Lista de tablas
    lista_tabla=[parent.venPri.tabla_principal, parent.venPri.tabla_principal_tutor,
                  parent.venPri.tabla_usuario, parent.venPri.tabla_intituciones, parent.venPri.tabla_proyectos,
                  parent.venPri.tabla_reporte_tutores, parent.venPri.tabla_reporte_estudiantes
                  ]

    # Lista de index
    lista_index=[[0,6], [0,5], [0,7],[0,5], [0,2,3], [3], [3]]

    # Lista de tamaño
    lista_tamano=[[70,160], [70, 160], [70, 120],[70,100], [70,80,100], [200], [200]]

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
    btn_nuevo.setIconSize(QtCore.QSize(22, 22))
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
                    color_texto = QtGui.QColor('red') if estado_columna == 'Pendiente' else \
                                QtGui.QColor('blue') if estado_columna == 'En progreso' else \
                                QtGui.QColor('green')
                    item.setForeground(QtGui.QBrush(color_texto))

                    # Establecer negrita (bold) para los estados
                    font = QtGui.QFont()
                    font.setBold(True)
                    item.setFont(font)

                tabla.setItem(fila, columna, item)


    else:
        tabla.setRowCount(0) 
          
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
    nombre_estudiante = parent.venPri.tabla_principal.item(fila, 2).text()
    estado = parent.venPri.tabla_principal.item(fila, 5).text()
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    Vinculacion(vinculacion_id, nombre_estudiante,estado,  "actualizar", parent).exec_()

def btn_eliminar_acciones(fila, parent):
    vinculacion_id = parent.venPri.tabla_principal.item(fila, 0).text()
    nombre_estudiante = parent.venPri.tabla_principal.item(fila, 2).text()

    mensaje = f"¿Está seguro(a) de eliminar la vinculación de {nombre_estudiante.upper()}? Esto eliminará los datos del estudiante y sus seguimientos realizados por el tutor asociados."

    respuesta = QtWidgets.QMessageBox.question(parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    if respuesta == QtWidgets.QMessageBox.Yes:
        
        if not parent.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        parent.conec_base.getDatosProcess_condicion("EliminarVinculacion", (vinculacion_id,))
        parent.listar_vinculacion()

        QtWidgets.QMessageBox.information(parent, "Mensaje", f"La vinculación de {nombre_estudiante.upper()} se ha eliminado exitosamente.")

def btn_seguimiento_acciones(fila, parent):

    from controllers.Modulo_principal.seguimiento_admin import Seguimiento_admin

    vinculacion_id = parent.venPri.tabla_principal.item(fila, 0).text()
    nombre_estudiante = parent.venPri.tabla_principal.item(fila, 2).text()
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
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                
                if columna == 3: 
                    estado_columna = str(dato[fila][columna])
                    color_texto = QtGui.QColor('red') if estado_columna == 'Pendiente' else \
                                QtGui.QColor('blue') if estado_columna == 'En progreso' else \
                                QtGui.QColor('green')
                    item.setForeground(QtGui.QBrush(color_texto))

                    # Establecer negrita (bold) para los estados
                    font = QtGui.QFont()
                    font.setBold(True)
                    item.setFont(font)
                    
                tabla.setItem(fila, columna, item)

    else:
        tabla.setRowCount(0)

def llenar_tabla_seguimiento(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(6)
   
        for fila in range(len(dato)):

            boton_ver_seguimiento = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/visualizar_seguimiento.png',
                tooltip = 'ver seguimiento')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_ver_seguimiento)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_ver_seguimiento(boton_ver_seguimiento, fila, tabla, parent)
          
            tabla.setCellWidget(fila ,5,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                
                if columna == 3:
                    if isinstance(dato[fila][columna], int) or dato[fila][columna].isdigit():
                        item.setText(f"{dato[fila][columna]} horas")
                        
                if columna == 4: 
                    estado_columna = str(dato[fila][columna])
                    color_texto = QtGui.QColor('red') if estado_columna == 'Pendiente' else \
                                QtGui.QColor('blue') if estado_columna == 'En progreso' else \
                                QtGui.QColor('green')  
                    item.setForeground(QtGui.QBrush(color_texto))

                    font = QtGui.QFont()
                    font.setBold(True)
                    item.setFont(font)

                tabla.setItem(fila, columna, item)
                
def btn_ver_seguimiento(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_seguimiento_acccion(fila,parent)) 
    
def ver_seguimiento_acccion(fila, parent):
    
    from controllers.Modulo_seguimiento.Modulo_seguimiento import Seguimiento

    vinculacion_id = parent.venPri.tabla_principal_tutor.item(fila, 0).text()
    nombre_estudiante = parent.venPri.tabla_principal_tutor.item(fila, 1).text()
    tutor_id = parent.tutor_id

    dato = [vinculacion_id, nombre_estudiante, tutor_id]

    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    Seguimiento(dato,parent = parent).exec_()


# ------------------------------------------------------------------
    
def llenar_tabla_usuario(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(8)
   
        for fila in range(len(dato)):

            boton_editar_usuario = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar Usuario')
            
        
            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_editar_usuario)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_usuario(boton_editar_usuario, fila, tabla, parent)
          
            tabla.setCellWidget(fila ,7,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
                
def btn_editar_usuario(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_editar_acccion(fila,parent)) 
    
def ver_editar_acccion(fila, parent):

    from controllers.Modulo_usuarios.Modulo_usuarios import Perfil

    usuario_id = parent.venPri.tabla_usuario.item(fila, 0).text()
    nombre_usuario = parent.venPri.tabla_usuario.item(fila, 1).text()

    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    Perfil(parent, 'Editar', [usuario_id, nombre_usuario]).exec_()



# ------------------------------------------------------------------
def llenar_tabla_institucion(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(6)
   
        for fila in range(len(dato)):

            boton_editar_institucion = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar Instutición')
            
            boton_eliminar_institucion = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/accion_eliminar.png',
                tooltip = 'Inabilitar Instutición')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_editar_institucion)
            layout.addWidget(boton_eliminar_institucion)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_institucion(boton_editar_institucion, fila, tabla, parent)
            btn_eliminar_institucion(boton_eliminar_institucion, fila, tabla, parent)
          
            tabla.setCellWidget(fila ,5,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
                
def btn_editar_institucion(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_editar_acccion_institucion(fila,parent)) 

def btn_eliminar_institucion(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_eliminar_acccion(fila,parent)) 
    
def ver_editar_acccion_institucion(fila, parent):
    
    from controllers.Modulo_mantenimiento.Mantenimiento_instituciones import Instituciones

    institucion_id = parent.venPri.tabla_intituciones.item(fila, 0).text()
    nombre_institucion = parent.venPri.tabla_intituciones.item(fila, 1).text()

    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()

    Instituciones(parent, 'Editar', [institucion_id, nombre_institucion]).exec_()

def ver_eliminar_acccion(fila, parent):
    
    institucion_id = parent.venPri.tabla_intituciones.item(fila, 0).text()
    nombre_institucion = parent.venPri.tabla_intituciones.item(fila, 1).text()

    mensaje = f"¿Está seguro(a) de inabilitar la institución  {nombre_institucion.upper()}? Al aceptar ya no se mostrará la institucíon en vinculacíon como opción."

    respuesta = QtWidgets.QMessageBox.question(parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    if respuesta == QtWidgets.QMessageBox.Yes:
        
        if not parent.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        parent.conec_base.getDatosProcess_condicion("CambiarEstadoInstitucion", (institucion_id,'Inactivo'))
        parent.llenado_instituciones('Activo')

        QtWidgets.QMessageBox.information(parent, "Mensaje", f"La institución  {nombre_institucion.upper()} se ha inabilitado exitosamente.")


# -----------------------------------------------------------------------
        
def llenar_tabla_proyectos(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(4)
   
        for fila in range(len(dato)):

            boton_editar_proyecto = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar Proyecto')
            
            boton_eliminar_proyecto = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/accion_eliminar.png',
                tooltip = 'Inabilitar Proyecto')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_editar_proyecto)
            layout.addWidget(boton_eliminar_proyecto)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_proyecto(boton_editar_proyecto, fila, tabla, parent)
            btn_eliminar_proyecto(boton_eliminar_proyecto, fila, tabla, parent)
          
            tabla.setCellWidget(fila , 3 ,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
                
def btn_editar_proyecto(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_editar_acccion_proyecto(fila,parent)) 

def btn_eliminar_proyecto(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_eliminar_acccion_proyecto(fila,parent)) 
    
def ver_editar_acccion_proyecto(fila, parent):
    
    from controllers.Modulo_mantenimiento.Mantenimiento_proyectos import Proyectos

    proyecto_id = parent.venPri.tabla_proyectos.item(fila, 0).text()

    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()

    Proyectos(parent, 'Editar', proyecto_id).exec_()

def ver_eliminar_acccion_proyecto(fila, parent):
    
    proyecto_id = parent.venPri.tabla_proyectos.item(fila, 0).text()
   
    mensaje = f"¿Está seguro(a) de inabilitar el proyecto? Al aceptar ya no se mostrará la institucíon en vinculacíon como opción."

    respuesta = QtWidgets.QMessageBox.question(parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    if respuesta == QtWidgets.QMessageBox.Yes:
        
        if not parent.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        parent.conec_base.getDatosProcess_condicion("CambiarEstadoProyecto", (proyecto_id,'Inactivo'))
        parent.llenado_proyectos('Activo')

        QtWidgets.QMessageBox.information(parent, "Mensaje", f"El proyecto  se ha inabilitado exitosamente.")