

from PySide2 import QtCore, QtWidgets , QtGui
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon


def evento_menu(parent, parentRaiz, tr = 200, imagen=None):

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

    if imagen:
        imagen.setScaledContents(True) 
        if newWidth == 91:
            imagen.setMaximumWidth(newWidth)  
            imagen.setMaximumHeight(140)  
        else:
            imagen.setMaximumHeight(140) 
            imagen.setMaximumWidth(170) 
    
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

   
    for btn in [parent.venPri.btn_menu_estudiantes, parent.venPri.btn_menu_tutores, 
                parent.venPri.btn_menu_proyectos, parent.venPri.btn_menu_carreras,
                parent.venPri.btn_menu_instituciones]:
        
        if btn != boton:
            btn.setStyleSheet("")  

    # Cambiar la página actual
    parent.venPri.stacked_administracion.setCurrentIndex(index)


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

    for btn in [parent.venPri.radioEstudiante, parent.venPri.radioTutor, parent.venPri.radioreporteentrega]:
        if btn != boton:
            btn.setStyleSheet("")  


    parent.venPri.stackedWidget_5.setCurrentIndex(index)
   
def evento_tabla(parent):

    configuraciones_columnas = {
        parent.venPri.tabla_estudiantes: {0: 50, 4: 400, 5: 150},
        parent.venPri.tabla_tutores: {0: 50, 4: 300, 5: 150},
        parent.venPri.tabla_proyecto: {0: 50, 2: 140, 3: 150},
        parent.venPri.tabla_carrera: {0: 50, 2: 140, 3: 140},
        parent.venPri.tabla_institucion: {0: 50, 1: 450, 4:150},
        parent.venPri.tabla_vinculacion: {0: 50, 2:140, 3:150, 4:140, 5: 140},
        parent.venPri.tabla_seguimiento: {0: 50, 2:150, 3:170, 4:170, 5:150},
        parent.venPri.tabla_usuario: {0: 50, 1:300, 2:120, 3:120, 5:100, 6:130},
        parent.venPri.tabla_reporte_tutores: {0: 50},
        parent.venPri.tabla_reporte_estudiantes: {0: 300, 1: 150,  2:150, 3:170, 5:150},
        parent.venPri.tabla_reporte_memorandum_tutor: {0: 50, 1: 250},
        parent.venPri.tabla_reporte_ficha_tutor: {0: 50, 1: 250},
        parent.venPri.tabla_reporte_informe_tutor: {0:50, 1:300 , 2: 100, 3:100, 4:100, 5:100, 6:100, 7:100, 8:100, 9:100, 10:100, 11:100, 12:100, 13:100, 14:100}
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

def estilo(parent):
    estiloDefecto =QtWidgets.QStyleFactory.create('windowsvista')
    parent.venedit.bnt_ojoInv.setStyle(estiloDefecto)
    parent.venedit.bnt_ojoVis.setStyle(estiloDefecto)

# -------------------------------------------------------------------------------------------------------
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
        tabla.setColumnCount(6)
   
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


            botondetalle = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #91cbcf; border-radius:8px}
                            QToolButton:hover{background-color:#82b5b9}""",
                icono = u':/menu/detalle.png',
                tooltip = 'Detalle vinculacion')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(botoneditar)
            layout.addWidget(botoneliminar)
            layout.addWidget(botondetalle)

            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_vinculacion(botoneditar, fila, tabla, parent)
            btn_eliminar_vinculacion(botoneliminar, fila, tabla, parent)
            btn_detalle_vinculacion(botondetalle, fila, tabla, parent)

            tabla.setCellWidget(fila ,5,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                
                # if columna == 2: 
                #     estado_columna = str(dato[fila][columna])
                #     color_texto = QtGui.QColor('red') if estado_columna == 'Pendiente' else \
                #                 QtGui.QColor('blue') if estado_columna == 'En progreso' else \
                #                 QtGui.QColor('green')
                #     item.setForeground(QtGui.QBrush(color_texto))

                #     # Establecer negrita (bold) para los estados
                #     font = QtGui.QFont()
                #     font.setBold(True)
                #     item.setFont(font)

                tabla.setItem(fila, columna, item)


    else:
        tabla.setRowCount(0) 
          
def btn_editar_vinculacion(boton,fila,tabla,parent):
    
    """eventos  del boton editar """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: btn_editar_acciones_vinculacion(fila,parent)) 
    
def btn_eliminar_vinculacion(boton,fila,tabla,parent):
    
    """eventos  del boton eleminar """
    boton.clicked.connect(lambda: tabla.selectRow(fila))            
    boton.clicked.connect(lambda: btn_eliminar_acciones_vinculacion(fila,parent)) 
    
def btn_detalle_vinculacion(boton,fila,tabla,parent):
    
    """eventos  del boton seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))              
    boton.clicked.connect(lambda: btn_detalle_acciones_vinculacion(fila,parent)) 
    
def btn_editar_acciones_vinculacion(fila,parent):
 
    from controllers.Modulo_Vinculacion.Modulo_Vinculacion import Vinculacion

    vinculacion_id = parent.venPri.tabla_vinculacion.item(fila, 0).text()
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    
    Vinculacion(vinculacion_id, "editar", parent).exec_()

def btn_eliminar_acciones_vinculacion(fila, parent):

    vinculacion_id = parent.venPri.tabla_vinculacion.item(fila, 0).text()
    print('vinculacion_id ', vinculacion_id)

    mensaje = f"¿Está seguro(a) de eliminar la vinculación ? Esto eliminará los datos del estudiante y sus seguimientos realizados por el tutor asociados."

    respuesta = QtWidgets.QMessageBox.question(parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    if respuesta == QtWidgets.QMessageBox.Yes:
        
        if not parent.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return
        
        consulta_delete = "DELETE FROM vinculacion WHERE id = %s"
        parent.conec_base.deleteDatos(consulta_delete, (vinculacion_id,))
        parent.offset = 0
        parent.llenarTabla('ObtenerListaVinculaciones', 'vinculacion', parent.venPri.tabla_vinculacion)
        parent.actualizarInfoPaginacion('vinculacion', parent.venPri.lbl_pagina_vinculacion, True)
        parent.datos_inicializacion()
        parent.llenar_estudiantes_seguimientos_tutor()
        QtWidgets.QMessageBox.information(parent, "Mensaje", "La vinculación se ha eliminado exitosamente.")

def btn_detalle_acciones_vinculacion(fila, parent):
    

    from controllers.Modulo_Vinculacion.Modulo_vinculacion_detalle import VinculacionDetalle

    vinculacion_id = parent.venPri.tabla_vinculacion.item(fila, 0).text()

    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    VinculacionDetalle(vinculacion_id,parent = parent).exec_()

# -------------------------------------------------------------------------------------------------------
def cargar_tabla_reporte_estudiante(tabla,dato):
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(6)
   
        for fila in range(len(dato)):
           
            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                
                if columna == 5: 
                    estado_columna = str(dato[fila][columna])
                    if estado_columna == 'Pendiente':
                        color_texto = QtGui.QColor('#FFD700')
                    elif estado_columna == 'En Proceso':
                        color_texto = QtGui.QColor('#008000')
                    elif estado_columna == 'Culminado':
                        color_texto = QtGui.QColor('#FF0000')
                    else:
                        color_texto = QtGui.QColor('#000000')
                        
                    item.setForeground(QtGui.QBrush(color_texto))

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
        tabla.setColumnCount(7)
   
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
          
            tabla.setCellWidget(fila ,6,widget)

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
def llenar_tabla_estudiantes(parent, tabla, dato):
    

    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(6)
   
        for fila in range(len(dato)):

            boton_editar_estudiante = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar Estudiante')
            
            boton_eliminar_estudiantes = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/ok.png' if parent.venPri.check_estado_estudiantes.isChecked() else u':/menu/accion_eliminar.png',
                tooltip = 'Habilitar Estudiante' if parent.venPri.check_estado_estudiantes.isChecked() else 'Inabilitar Estudiante')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_editar_estudiante)
            layout.addWidget(boton_eliminar_estudiantes)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_estudiante(boton_editar_estudiante, fila, tabla, parent)
            btn_eliminar_estudiante(boton_eliminar_estudiantes, fila, tabla, parent)
          
            tabla.setCellWidget(fila ,5,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
                
def btn_editar_estudiante(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_editar_acccion_estudiante(fila,parent)) 

def btn_eliminar_estudiante(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_eliminar_accion_estudiante(fila,parent)) 
    
def ver_editar_acccion_estudiante(fila, parent):
    
    from controllers.Modulo_administracion.Estudiantes_administracion import EstudiantesAdmin
    
    estudiante_id = parent.venPri.tabla_estudiantes.item(fila, 0).text()
    
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()

    EstudiantesAdmin(parent, 'editar', estudiante_id).exec_()

def ver_eliminar_accion_estudiante(fila, parent):
    
    estudiante_id = parent.venPri.tabla_estudiantes.item(fila, 0).text()
    nombre_estudiante = parent.venPri.tabla_estudiantes.item(fila, 1).text()
    
    nuevo_estado = parent.venPri.check_estado_estudiantes.isChecked()
    
    print('estado del check1', nuevo_estado)    
    if( nuevo_estado == True ):
        nuevo_estado = True
    else:
        nuevo_estado = False
    print('estado del check2 ', nuevo_estado) 
    
    estado_texto = "HABILITAR" if nuevo_estado else "INHABILITAR"
    mensaje = f"¿Está seguro(a) de {estado_texto} al estudiante {nombre_estudiante.upper()}?"
    
    respuesta = QtWidgets.QMessageBox.question(
        parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
    )

    if respuesta == QtWidgets.QMessageBox.Yes:
        if not parent.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return

        try:
            parent.conec_base.updateDatos("UPDATE estudiantes SET estado = %s WHERE id = %s",(nuevo_estado, estudiante_id))
            QtWidgets.QMessageBox.information(parent, "Mensaje",f"El estado del estudiante {nombre_estudiante.upper()} se ha actualizado exitosamente." )
        except Exception as e:
            QtWidgets.QMessageBox.critical(parent, "Error",f"Hubo un problema al actualizar el estado del estudiante: {str(e)}" )
            return

        parent.offset = 0
        parent.venPri.check_estado_estudiantes.setChecked(not nuevo_estado)
        
        
        parent.llenarTabla(
            'listar_estudiantes' if nuevo_estado else 'listar_estudiantes_inactivos',
            'estudiantes',
            parent.venPri.tabla_estudiantes
        )
        
        parent.actualizarInfoPaginacion('estudiantes', parent.venPri.lbl_pagina_estudiantes, nuevo_estado)



# -----------------------------------------------------------------------

def llenar_tabla_tutores(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(6)
   
        for fila in range(len(dato)):

            boton_editar_tutores = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar Tutor')
            
            boton_eliminar_tutores = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/ok.png' if parent.venPri.check_estado_tutores.isChecked() else u':/menu/accion_eliminar.png',
                tooltip = 'Habilitar Tutor' if parent.venPri.check_estado_tutores.isChecked() else 'Inabilitar Tutor')
        
            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_editar_tutores)
            layout.addWidget(boton_eliminar_tutores)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_tutores(boton_editar_tutores, fila, tabla, parent)
            btn_eliminar_tutores(boton_eliminar_tutores, fila, tabla, parent)
          
            tabla.setCellWidget(fila ,5,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
                        
def btn_editar_tutores(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_editar_acccion_tutor(fila,parent)) 

def btn_eliminar_tutores(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_eliminar_acccion_tutor(fila,parent)) 
    
def ver_editar_acccion_tutor(fila, parent):
   

    from controllers.Modulo_administracion.Tutores_administracion import TutoresAdmin
    
    tutor_id = parent.venPri.tabla_tutores.item(fila, 0).text()
    
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()

    TutoresAdmin(parent, 'editar', tutor_id).exec_()

def ver_eliminar_acccion_tutor(fila, parent):
    
    tutor_id = parent.venPri.tabla_tutores.item(fila, 0).text()
    nombre_tutor = parent.venPri.tabla_tutores.item(fila, 1).text()
    
    nuevo_estado = parent.venPri.check_estado_tutores.isChecked()
    estado_texto = "HABILITAR" if nuevo_estado else "INHABILITAR"
    mensaje = f"¿Está seguro(a) de {estado_texto} al tutor {nombre_tutor.upper()}?"
    
    respuesta = QtWidgets.QMessageBox.question(
        parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
    )

    if respuesta == QtWidgets.QMessageBox.Yes:
        if not parent.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return

        try:
            parent.conec_base.updateDatos("UPDATE tutores SET estado = %s WHERE id = %s",(nuevo_estado, tutor_id))
            QtWidgets.QMessageBox.information(parent, "Mensaje",f"El estado del tutor {nombre_tutor.upper()} se ha actualizado exitosamente." )
        except Exception as e:
            QtWidgets.QMessageBox.critical(parent, "Error",f"Hubo un problema al actualizar el estado del tutor: {str(e)}" )
            return


        parent.offset = 0
        parent.venPri.check_estado_tutores.setChecked(not nuevo_estado)
        
        parent.llenarTabla(
            'listar_tutores' if nuevo_estado else 'listar_tutores_inactivos',
            'tutores',
            parent.venPri.tabla_tutores
        )
    
        parent.datos_inicializacion()
        parent.llenarTabla('listar_tutores', 'tutores', parent.venPri.tabla_reporte_tutores)
        parent.actualizarInfoPaginacion('tutores', parent.venPri.lbl_pagina_reporte02, True )
        parent.cargaDatosEventoReporte()
        parent.actualizarInfoPaginacion('tutores', parent.venPri.lbl_pagina_tutores, nuevo_estado)

# -------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
    
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
                icono = u':/menu/ok.png' if parent.venPri.check_estado_proyecto.isChecked() else u':/menu/accion_eliminar.png',
                tooltip = 'Habilitar Proyecto' if parent.venPri.check_estado_proyecto.isChecked() else 'Inabilitar Proyecto')

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
                
                if columna == 2:
                    estado_columna = str(dato[fila][columna])
                    # print('c ', estado_columna)
                    color_texto = QtGui.QColor('green') if estado_columna == '1' else \
                                QtGui.QColor('red')
                    item.setForeground(QtGui.QBrush(color_texto))

                    font = QtGui.QFont()
                    font.setBold(True)
                    item.setFont(font)
                    
                    texto = "Activo" if estado_columna == '1' else "Inactivo"
                    item.setText(texto)

                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
          
def btn_editar_proyecto(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_editar_acccion_proyecto(fila,parent)) 

def btn_eliminar_proyecto(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_eliminar_acccion_proyectos(fila,parent)) 
    
def ver_editar_acccion_proyecto(fila, parent):
    print("Ver editing0")
    
    from controllers.Modulo_administracion.Proyectos_administracion import ProyectosAdmin
    
    proyecto_id = parent.venPri.tabla_proyecto.item(fila, 0).text()
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    ProyectosAdmin(parent, 'editar', proyecto_id).exec_()
    
def ver_eliminar_acccion_proyectos(fila, parent):
    
    proyecto_id = parent.venPri.tabla_proyecto.item(fila, 0).text()
    nombre_proyecto = parent.venPri.tabla_proyecto.item(fila, 1).text()
    
    nuevo_estado = parent.venPri.check_estado_proyecto.isChecked()
    estado_texto = "HABILITAR" if nuevo_estado else "INHABILITAR"
    mensaje = f"¿Está seguro(a) de {estado_texto} el proyecto {nombre_proyecto.upper()}?"
    
    respuesta = QtWidgets.QMessageBox.question(
        parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
    )

    if respuesta == QtWidgets.QMessageBox.Yes:
        if not parent.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return

        try:
            parent.conec_base.updateDatos("UPDATE proyecto SET estado = %s WHERE id = %s",(nuevo_estado, proyecto_id))
            QtWidgets.QMessageBox.information(parent, "Mensaje",f"El estado del proyecto {nombre_proyecto.upper()} se ha actualizado exitosamente." )
        except Exception as e:
            QtWidgets.QMessageBox.critical(parent, "Error",f"Hubo un problema al actualizar el estado del proyecto: {str(e)}" )
            return

        parent.offset = 0
        parent.venPri.check_estado_proyecto.setChecked(not nuevo_estado)
        
        parent.llenarTabla(
            'listar_proyectos' if nuevo_estado else 'listar_proyectos_inactivos',
            'proyecto',
            parent.venPri.tabla_proyecto
        )
        
        parent.datos_inicializacion()
        
        parent.actualizarInfoPaginacion('proyecto', parent.venPri.lbl_pagina_proyectos, nuevo_estado)
       
       
# -------------------------------------------------------------------------------------------------------------- 
        
def llenar_tabla_carreras(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(4)
   
        for fila in range(len(dato)):

            boton_editar_carrera = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar Carrera')

            
            boton_eliminar_carrera = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/ok.png' if parent.venPri.check_estado_carrera.isChecked() else u':/menu/accion_eliminar.png',
                tooltip = 'Habilitar carrera' if parent.venPri.check_estado_carrera.isChecked() else 'Inabilitar carrera')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_editar_carrera)
            layout.addWidget(boton_eliminar_carrera)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_carrera(boton_editar_carrera, fila, tabla, parent)
            btn_eliminar_carrera(boton_eliminar_carrera, fila, tabla, parent)
          
            tabla.setCellWidget(fila , 3 ,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                
                if columna == 2:
                    estado_columna = str(dato[fila][columna])
                    # print('c ', estado_columna)
                    color_texto = QtGui.QColor('green') if estado_columna == '1' else \
                                QtGui.QColor('red')
                    item.setForeground(QtGui.QBrush(color_texto))

                    font = QtGui.QFont()
                    font.setBold(True)
                    item.setFont(font)
                    
                    texto = "Activo" if estado_columna == '1' else "Inactivo"
                    item.setText(texto)

                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
          
def btn_editar_carrera(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_editar_acccion_carrera(fila,parent)) 

def btn_eliminar_carrera(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_eliminar_acccion_carrera(fila,parent)) 
    
def ver_editar_acccion_carrera(fila, parent):
    
    from controllers.Modulo_administracion.Carreras_administracion import CarrerasAdmin
    carrera_id = parent.venPri.tabla_carrera.item(fila, 0).text()
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    CarrerasAdmin(parent, 'editar', carrera_id).exec_()
    
def ver_eliminar_acccion_carrera(fila, parent):
    
    carrera_id = parent.venPri.tabla_carrera.item(fila, 0).text()
    nombre_carrera = parent.venPri.tabla_carrera.item(fila, 1).text()
    
    nuevo_estado = parent.venPri.check_estado_carrera.isChecked()
    estado_texto = "HABILITAR" if nuevo_estado else "INHABILITAR"
    mensaje = f"¿Está seguro(a) de {estado_texto} la carrera {nombre_carrera.upper()}?"
    
    respuesta = QtWidgets.QMessageBox.question(
        parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
    )

    if respuesta == QtWidgets.QMessageBox.Yes:
        if not parent.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return

        try:
            parent.conec_base.updateDatos("UPDATE carrera SET estado = %s WHERE id = %s",(nuevo_estado, carrera_id))
            QtWidgets.QMessageBox.information(parent, "Mensaje",f"El estado de la carrera {nombre_carrera.upper()} se ha actualizado exitosamente." )
        except Exception as e:
            QtWidgets.QMessageBox.critical(parent, "Error",f"Hubo un problema al actualizar el estado de la carrera: {str(e)}" )
            return
        parent.offset = 0
        parent.venPri.check_estado_carrera.setChecked(not nuevo_estado)
        
        parent.llenarTabla(
            'listar_carreras' if nuevo_estado else 'listar_carreras_inactivas',
            'carrera',
            parent.venPri.tabla_carrera
        )
        
        parent.actualizarInfoPaginacion('carrera', parent.venPri.lbl_pagina_carrera, nuevo_estado)
        
        
        
# --------------------------------------------------------------------------------------------------------------

def llenar_tabla_institucion(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(5)
   
        for fila in range(len(dato)):

            boton_editar_institucion = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                            QToolButton:hover{background-color:#cbe1e3}""",
                icono = u':/menu/acccion_editar.png',
                tooltip = 'Editar Institucion')
            

            boton_eliminar_institucion = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                icono = u':/menu/ok.png' if parent.venPri.check_estado_insti.isChecked() else u':/menu/accion_eliminar.png',
                tooltip = 'Habilitar Institucion' if parent.venPri.check_estado_insti.isChecked() else 'Inabilitar Institucion')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(boton_editar_institucion)
            layout.addWidget(boton_eliminar_institucion)
 
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar_institucion(boton_editar_institucion, fila, tabla, parent)
            btn_eliminar_institucion(boton_eliminar_institucion, fila, tabla, parent)
          
            tabla.setCellWidget(fila , 4 ,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                
                if columna == 3:
                    estado_columna = str(dato[fila][columna])
                    # print('c ', estado_columna)
                    color_texto = QtGui.QColor('green') if estado_columna == '1' else \
                                QtGui.QColor('red')
                    item.setForeground(QtGui.QBrush(color_texto))

                    font = QtGui.QFont()
                    font.setBold(True)
                    item.setFont(font)
                    
                    texto = "Activo" if estado_columna == '1' else "Inactivo"
                    item.setText(texto)

                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
          
def btn_editar_institucion(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_editar_acccion_institucion(fila,parent)) 

def btn_eliminar_institucion(boton,fila,tabla,parent):
    
    """eventos  del boton agregar seguimiento """
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: ver_eliminar_acccion_institucion(fila,parent)) 
    
def ver_editar_acccion_institucion(fila, parent):
    
    from controllers.Modulo_administracion.Instituciones_administracion import InstitucionesAdmin
    institucion_id = parent.venPri.tabla_institucion.item(fila, 0).text()
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()
    InstitucionesAdmin(parent, 'editar', institucion_id).exec_()
    
def ver_eliminar_acccion_institucion(fila, parent):
    

    institucion_id = parent.venPri.tabla_institucion.item(fila, 0).text()
    nombre_institucion = parent.venPri.tabla_institucion.item(fila, 1).text()
    
    nuevo_estado = parent.venPri.check_estado_insti.isChecked()
    estado_texto = "HABILITAR" if nuevo_estado else "INHABILITAR"
    mensaje = f"¿Está seguro(a) de {estado_texto} la institución {nombre_institucion.upper()}?"
    
    respuesta = QtWidgets.QMessageBox.question(
        parent, "Mensaje", mensaje,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
    )

    if respuesta == QtWidgets.QMessageBox.Yes:
        if not parent.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(None, "Error", "No hay conexión a Internet.")
            return

        try:
            parent.conec_base.updateDatos("UPDATE institucion SET estado = %s WHERE id = %s",(nuevo_estado, institucion_id))
            QtWidgets.QMessageBox.information(parent, "Mensaje",f"El estado de la institucion {nombre_institucion.upper()} se ha actualizado exitosamente." )
        except Exception as e:
            QtWidgets.QMessageBox.critical(parent, "Error",f"Hubo un problema al actualizar el estado de la institucion: {str(e)}" )
            return

        parent.offset = 0
        parent.venPri.check_estado_insti.setChecked(not nuevo_estado)
        
        parent.llenarTabla(
            'listar_institucion' if nuevo_estado else 'listar_instituciones_inactivas',
            'institucion',
            parent.venPri.tabla_institucion
        )
        
        parent.actualizarInfoPaginacion('institucion', parent.venPri.lbl_pagina_instituto, nuevo_estado)



# --------------------------------------------------------------------------------------------------------------
def llenar_tabla_tutores_reportes(parent, tabla, dato):
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(6)
   
        for fila in range(len(dato)):

            botonEntrega = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #91cbcf; border-radius:8px}
                            QToolButton:hover{background-color:#82b5b9}""",
                icono = u':/menu/agregar_entrega.png',
                tooltip = 'Agregar Entrega')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(botonEntrega)

            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_entrega(botonEntrega, fila, tabla, parent)
            tabla.setCellWidget(fila ,5,widget)
            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)


    else:
        tabla.setRowCount(0) 
          
def btn_entrega(boton,fila,tabla,parent):
  
    boton.clicked.connect(lambda: tabla.selectRow(fila))          
    boton.clicked.connect(lambda: btn_entrega_acciones(fila,parent)) 
    
def btn_entrega_acciones(fila, parent):
    
    from controllers.Modulo_entrega.Modulo_entrega import Entrega
    
    idTutor = parent.venPri.tabla_reporte_tutores.item(fila, 0).text()
    tutor = parent.venPri.tabla_reporte_tutores.item(fila, 1).text()
    
    nombre_completo = " ".join(tutor.split()[:3])
    
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()

    Entrega(parent, 'informe', [idTutor, nombre_completo] ).exec_()
  
    
def cargar_tabla_reporte_informes(tabla, dato, periodo, parent):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(15)
   
        for fila in range(len(dato)):
            

            boton_editar = crearbotoneslista(
                stilo=u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                        QToolButton:hover{background-color:#cbe1e3}""",
                icono=u':/menu/ok.png',
                tooltip='Editar')


            # Crear un layout horizontal y añadir los botones
            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1, 1, 1, 1)
            layout.setSpacing(3)
            layout.addWidget(boton_editar)

            # Crear un widget y establecer el layout horizontal
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_editar(boton_editar, fila, tabla, periodo, parent)
            
            # Añadir el widget con los botones a la última columna de la tabla
            tabla.setCellWidget(fila, 14, widget)

            # Añadir los datos a las primeras cuatro columnas
            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                
                if dato[fila][columna] == 'SI':
                    item.setForeground(QtGui.QBrush(QtGui.QColor('green')))
                elif dato[fila][columna] == 'NO':
                    item.setForeground(QtGui.QBrush(QtGui.QColor('red')))
                
                tabla.setItem(fila, columna, item)
                
    else:
        tabla.setRowCount(0)


def btn_editar(btn, fila, tabla , periodo, parent):

    btn.clicked.connect(lambda: tabla.selectRow(fila))          
    btn.clicked.connect(lambda: btn_editar_accion(fila,periodo, parent, tabla)) 
    
    
    
def btn_editar_accion(fila, periodo, parent, tabla):
    
    from controllers.Modulo_entrega.Modulo_entrega_edicion import EntregaEdicion
    
    
    tutor_id = tabla.item(fila, 0).text()
    tutor = tabla.item(fila, 1).text()
    periodo_seleccionado = periodo
    
    
    parent.raizOpacidad.resize(parent.width(), parent.height())
    parent.raizOpacidad.show()

    EntregaEdicion(parent, [tutor_id, tutor, periodo_seleccionado] ).exec_()



def cargar_tabla_reporte_ficha_memorandum(tabla, dato, periodo, parent, tipo):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(5)  # Ajusta el número de columnas según sea necesario
        
        for fila in range(len(dato)):
            
            # Crear botones "Sí" y "No"
            boton_si = crearbotoneslista(
                stilo=u"""QToolButton{background-color: #DEF5F8; border-radius:8px}
                        QToolButton:hover{background-color:#cbe1e3}""",
                icono=u':/menu/ok.png',
                tooltip='Entregó')

            boton_no = crearbotoneslista(
                stilo=u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                        QToolButton:hover{background-color:#ebdada}""",
                icono=u':/menu/no.png',
                tooltip='No entrega')

            # Crear un layout horizontal y añadir los botones
            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1, 1, 1, 1)
            layout.setSpacing(3)
            layout.addWidget(boton_si)
            layout.addWidget(boton_no)

            # Crear un widget y establecer el layout horizontal
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_si(boton_si, fila, tabla, periodo, parent, tipo)
            btn_no(boton_no, fila, tabla, periodo, parent, tipo)
            
            # Añadir el widget con los botones a la última columna de la tabla
            tabla.setCellWidget(fila, 4, widget)

            # Añadir los datos a las primeras cuatro columnas
            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)

    else:
        tabla.setRowCount(0)

def btn_si(btn, fila, tabla , periodo, parent, tipo):

    btn.clicked.connect(lambda: tabla.selectRow(fila))          
    btn.clicked.connect(lambda: btn_si_accion(fila,periodo, parent, tipo, tabla)) 
    
def btn_no(btn, fila, tabla , periodo, parent, tipo):

    btn.clicked.connect(lambda: tabla.selectRow(fila))          
    btn.clicked.connect(lambda: btn_no_accion(fila,periodo, parent, tipo, tabla)) 
    
def btn_si_accion(fila, periodo, parent, tipo, tabla):
    
    tutor_id = tabla.item(fila, 0).text()
    tutor = tabla.item(fila, 1).text()


    periodo_seleccionado = periodo
    

    
    mensaje_confirmacion = f"¿Está seguro(a) de actualizar la entrega de {tipo} para el tutor {tutor.upper()}?"
    mensaje_exito = f"Se agregó exitosamente la entrega de {tipo} para el tutor {tutor.upper()}"
    
    # Verificar si ya existe una entrega para el tutor en el mismo periodo
    consulta_existencia = f"SELECT COUNT(*) FROM {tipo} WHERE tutor_id = %s AND periodo_academico = %s"
    existencia = parent.conec_base.getDatos_condicion(consulta_existencia, (tutor_id, periodo_seleccionado))
    
    if existencia[0][0] > 0:
        QtWidgets.QMessageBox.warning(parent, "Mensaje", f"El tutor {tutor.upper()} ya tiene una entrega de {tipo} registrada para este periodo.")
        return
    
    # Confirmación antes de realizar la inserción
    respuesta = QtWidgets.QMessageBox.question(
        parent, "Confirmación", mensaje_confirmacion,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
    )
    
    if respuesta == QtWidgets.QMessageBox.Yes:
        if tipo == 'fichas':
            parent.conec_base.updateDatos("INSERT INTO fichas (is_ficha, periodo_academico, tutor_id) VALUES (%s, %s, %s)",
                                          (True, periodo_seleccionado, tutor_id))
            QtWidgets.QMessageBox.information(parent, "Mensaje", mensaje_exito)
                
        elif tipo == 'memorandum':
            parent.conec_base.updateDatos("INSERT INTO memorandum (is_memorandum, periodo_academico, tutor_id) VALUES (%s, %s, %s)",
                                          (True, periodo_seleccionado, tutor_id))
            QtWidgets.QMessageBox.information(parent, "Mensaje", mensaje_exito)
            
    parent.cargaDatosEventoReporte()


def btn_no_accion(fila, periodo, parent, tipo, tabla):
    
    tutor_id = tabla.item(fila, 0).text()
    tutor = tabla.item(fila, 1).text()
    periodo_seleccionado = periodo
    estado_si = tabla.item(fila, 2).text()
    estado_no = tabla.item(fila, 3).text()
    
    estado = True if estado_no != '' else False
    
    print('estado ', estado)
    
    if( estado == True):
        QtWidgets.QMessageBox.warning(parent, "Mensaje", f"No se puede eliminar porque aun no tiene asignacion")
        return
    
    mensaje_confirmacion = f"¿Está seguro(a) de eliminar  la entrega de {tipo} para el tutor {tutor.upper()}?"


    respuesta = QtWidgets.QMessageBox.question(
        parent, "Confirmación", mensaje_confirmacion,
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
    )
    
    if respuesta == QtWidgets.QMessageBox.Yes:
        if tipo == 'fichas':
            parent.conec_base.updateDatos("DELETE FROM fichas WHERE periodo_academico = %s and tutor_id = %s",
                                          (periodo_seleccionado, tutor_id))
            QtWidgets.QMessageBox.information(parent, "Mensaje", mensaje_confirmacion)
                
        elif tipo == 'memorandum':
            parent.conec_base.updateDatos("DELETE FROM memorandum WHERE periodo_academico = %s and tutor_id = %s",
                                          (periodo_seleccionado, tutor_id))
            QtWidgets.QMessageBox.information(parent, "Mensaje", mensaje_confirmacion)
            
    parent.cargaDatosEventoReporte()
            

                
                
                
                
                
                
            # else:
            #     parent.conec_base.updateDatos("INSERT into fichas(is_ficha, periodo_academico, tutor_id) VALUES(%s, %s)",(estado_entrega, periodo_seleccionado, tutor_id))
            #     QtWidgets.QMessageBox.information(parent, "Mensaje",f"Se agrego exitosamente la entrega de ficha del tutor {tutor.upper()}" )
    

    
