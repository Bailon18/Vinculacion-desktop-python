
from PySide2 import QtWidgets , QtCore , QtGui
#from prueba import Tranferencia
from views.ui_ventana_principal import Ui_principal
from views.ui_usuario_admi import Ui_Admi
from views.ui_usuario_perfil import Ui_Perfil
from views.ui_admiedit import Ui_AdmiEdit

import re, os
from PIL import Image

# importaciones de modulo funcion general

from controllers.Modulo_principal.funcion_general import *

# importaciones de modulo utils 
from controllers.Modulo_utils.config.configVenPrincipal import configuracionVentana
from controllers.Modulo_utils.config.configVenAdmin import configuracionVentanaAdmin
from controllers.Modulo_utils.config.configVenPerfil import configuracionVentanaPerfil
from controllers.Modulo_utils.config.configVenEditUsuario import configuracionVentanaEdit


from controllers.Modulo_computador.Modulo_computador import Computador
from controllers.Modulo_computador.Modulo_transferencia import Tranferencia

# importamos la clase de la base datos
from db.Modulo_base import BaseDatos


class Principal(QtWidgets.QMainWindow):

    def __init__(self, *args , parent=None):
        
        super(Principal, self).__init__(parent)
        self.venPri = Ui_principal()
        self.venPri.setupUi(self)
        
        self.conec_base = BaseDatos()
        
        
        # # Datos de inicio 
        # self.dni = args[0]
        # self.nombreUsuario = args[3]
        # self.nombreRol = args[1]
        # self.foto = args[6]
        # self.apellido = args[4]
        # self.ide_rol = args[2]
        # self.sedes = args[7]
        
        # self.venPri.lbl_tituloSede.setText(str(args[5]).upper())
        
        
        # configuracionVentana(self)
        
        
        # self.configuracion()
        # self.controlSalida = True
        
        # self.cargaCompu(5)
        # self.cargar_usuario()
        
        # Boton abrir ventana para agregar un usuario nuevo
        # self.venPri.btn_agregarusu.clicked.connect(lambda: self.abrirUsuario())
        # self.venPri.btn_nuevoComputador.clicked.connect(lambda: self.abrirComputador())
        # self.venPri.btn_transferencia.clicked.connect(lambda: self.abrirTransferencia())

        
        # self.venPri.cbox_perfil.activated.connect(lambda: self.evento_perfil())
        self.venPri.btn_cerrar.clicked.connect(lambda: self.cerrar_sesion())
        
        # self.venPri.line_busqueda_usuario.textChanged.connect(lambda texto: self.busqueda_usuarios()
        #                                                       if(texto != '') else self.cargar_usuario)
        # self.venPri.line_busquedaCompu.textChanged.connect(lambda texto: self.busqueda_computadora()
        #                                                    if(texto != '') else self.cargaCompu(self.venPri.cbox_rango.currentText()))
        
        # self.venPri.cbox_rango.currentTextChanged.connect(lambda rango: self.evento_rango(rango))
        
        # # btn recargar llenado
        # self.venPri.btn_recargarcomput.clicked.connect(lambda: self.cargaCompu(self.venPri.cbox_rango.currentText()))

        evento_menu(self, self.venPri, tr=0)
        evento_hora(self)
        evento_tabla(self)
        self.venPri.boton_deslizable.clicked.connect(lambda: evento_menu(self, self.venPri))
        

        #self.venPri.btn_home.clicked.connect(lambda: self.funcionbotonmenu())
        self.venPri.btn_afiliacion.clicked.connect(lambda: evento_pagina(self, 0, self.venPri.btn_afiliacion))
        self.venPri.btn_reporte.clicked.connect(lambda: evento_pagina(self, 2, self.venPri.btn_reporte))
        self.venPri.btn_usuario.clicked.connect(lambda: evento_pagina(self, 1, self.venPri.btn_usuario))



    def closeEvent(self, event):
        '''
        Metodo para cerrar la aplicacion con una condición 
        '''
        
        if self.controlSalida:
            if(QtWidgets.QMessageBox.question(self, "Mensaje", "¿Desea cerrar la aplicacíon?.", 
                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No ) == QtWidgets.QMessageBox.Yes):
                event.accept()
            else:
                event.ignore()
            
    def cerrar_sesion(self):
        '''
        Metodo que tiene por funcion cerrar sesion  tambien apartir de una condicion
        '''
        from controllers.Modulo_sesion.Modulo_inicio import Login
        
        self.controlSalida = False
        if(QtWidgets.QMessageBox.question(self, "Mensaje", "¿Desea cerrar la Sesión?.", 
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No ) == QtWidgets.QMessageBox.Yes):
            
           self.close()
           self.logincito = Login()
           self.logincito.show()
           
        else:
            self.controlSalida = True










    def evento_rango(self, rango):
        
        consulta = self.conec_base.getDatos_condicion("""SELECT id, DATE_FORMAT( fecha_registro, "%%d-%%m-%%Y"), serial, 
                                                                placa, modelo_id, marca,compania_id, ticket 
                                                            FROM computador 
                                                            WHERE sede_id = %s Order by id DESC 
                                                            LIMIT %s; """, (self.sede_actual, int(rango)))

        if consulta:
            computadoras = [list(x) for x in consulta]
            cargatablaComputador(self, self.venPri.tabla_principal, computadoras)
    
    def cargaCompu(self, rango):
        
        computadoras = self.conec_base.getDatosProcess_condicion('sp_listaComputador', [self.sede_actual,'%d-%m-%Y', rango])
        computadoras = [list(x) for x in computadoras[0]]
        
        if computadoras:
            cargatablaComputador(self, self.venPri.tabla_principal, computadoras)
        else:  
            self.venPri.tabla_principal.setRowCount(0)

    def busqueda_computadora(self):
        opcion = self.venPri.cbox_filtrarCompu.currentIndex()
        textoBusqueda = self.venPri.line_busquedaCompu.text().strip()
        computadoras = self.conec_base.getDatosProcess_condicion('sp_filtrarComputadora',[self.sede_actual, '%d-%m-%Y', opcion, '%'+textoBusqueda+'%'])
        computadoras = [list(x) for x in computadoras[0]]
        if computadoras:
            cargatablaComputador(self, self.venPri.tabla_principal, computadoras)
            
    def cargar_usuario(self):
        
        '''
        Metodo que tiene por funcion obtener usuarios total de la base de datos
        y respectivamente  envia la lista de usuarios a la funcion algoritmo_usuarios()
        '''
        
        usuarios = self.conec_base.getDatos("""
        SELECT u.dni, u.nombre, u.apellidos, u.sede_id,
		u.correo, r.descripcion cargo, if(u.estado = 1, "Activo", "Bloqueado") Estado
        FROM usuario_rol ur 
        inner join rol r on ur.rol_id = r.id
        inner join usuario u on ur.usuario_dni = u.dni
        """)
        
        self.algoritmo_usuarios(usuarios)
    
    def busqueda_usuarios(self):

        usuario = self.venPri.line_busqueda_usuario.text()
        print('usuario ', usuario)
        usuarios = self.conec_base.getDatos_condicion("""
                                                       
                SELECT u.dni, u.nombre, u.apellidos, u.sede_id,
                u.correo, r.descripcion cargo, if(u.estado = 1, "Activo", "Bloqueado") Estado
                FROM usuario_rol ur 
                inner join rol r on ur.rol_id = r.id
                inner join usuario u on ur.usuario_dni = u.dni

                and concat_ws(u.nombre,' ', u.apellidos) LIKE %s
                
                """, ('%'+usuario+'%'))

        if(usuarios):
            self.algoritmo_usuarios(usuarios)

    def algoritmo_usuarios(self, usuarios):
        '''
        Metodo que tiene por funcion juntar los roles del usuario apartir ('-')
        y respectivamente envia los datos para llenar la tabla de usuarios
        :param list suarios: lista de usuarios 
        '''
        if usuarios:
            lista = [list(x) for x in usuarios]
            lista_princi = []
            for lis in lista:
                try:
                    dnis = [dni[0] for dni in lista_princi]
                    if(lis[0] in dnis):
                        index = dnis.index(lis[0])
                        lista_princi[index][5] = lis[5]+" - " + \
                            (lista_princi[index][5]).title()
                        continue
                except:
                    pass
                lista_princi.append(lis)
            cargausuarioicon(self, self.venPri.tabla_usuario, lista_princi)    
        
    def abrirUsuario(self):
        '''
        Metodo que tiene por funcion abrir formulario de llenado para un nuevo usuario
        '''
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        UsuarioAdmi(self).exec_()
        
    def abrirComputador(self):
        '''
        Metodo que tiene por funcion abrir formulario de llenado para un nuevo Computador
        '''
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        Computador([], 1, self).exec_()
            
    def abrirTransferencia(self):
        
        self.raizOpacidad.resize(self.width(), self.height())
        self.raizOpacidad.show()
        Tranferencia(self.sede_actual, self).exec_()
            
        
        
    def evento_perfil(self):
     
        if self.venPri.cbox_perfil.currentIndex() == 0:
            self.raizOpacidad.resize(self.width(), self.height())
            self.raizOpacidad.show()
            UsuarioPerfil(self).exec_()
        else:
            self.cerrar_sesion()
        
    def configuracion(self):
        '''
        configuracion basicas para cargar datos y condiciones de menu
        '''
        
        apellido = self.apellido[0:self.apellido.index(' ')] if(' ' in self.apellido) else self.apellido
        self.venPri.lbl_usuario.setText(self.nombreUsuario +' '+ apellido)
        self.venPri.lbl_rol.setText(self.nombreRol)
        
        
        # Desactivamos el boton reporte si no son administradora y soporte
        if self.nombreRol != 'Admin':
            self.venPri.btn_usuario.hide()

        # Limpiamos la foto y agregamos la actualizada
        self.venPri.lbl_foto.clear()
        
        if self.foto != 0:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(self.foto, 'png')
            self.venPri.lbl_foto.setPixmap(pixmap)
            
            
        modelos , compania , sede_actual = self.conec_base.getDatosProcess_condicion('sp_cargarComputador', [self.dni]) 
        
        self.sede_actual = sede_actual[0][0]
        
        # Cargamos los modelos , companias convertimos a diccionario
        self.modelos=dict(zip([i[0] for i in modelos],[i[1] for i in modelos]))
        self.compania=dict(zip([i[0] for i in compania],[i[1] for i in compania]))
        
# Agregar usuario nuevo
class UsuarioAdmi(QtWidgets.QDialog):
    def __init__(self, parent=None):
        
        super(UsuarioAdmi, self).__init__()
        self.venAdmi = Ui_Admi()
        self.venAdmi.setupUi(self)

        # conexion con la bd
        self.control_admi = BaseDatos()
        
        self.parent = parent
        
        # Lista para agregar la seleccion de roles para el usuario
        self.listaseleccion = []
        
        # convertimos la lista de sedes que tiene la ventana principal a un diccinario
        self.sedes_dic = dict(zip(parent.sedes.values(),parent.sedes.keys()))
        
        # configuracion basica de la ventana
        configuracionVentanaAdmin(self)

        # Boton guardar usuario registrado 
        self.venAdmi.btn_guardar.clicked.connect(lambda: self.guardarDatosUsuario())

        
    def keyPressEvent(self, event):
        ''' 
        Metodo que detecta el boton espace y lo desabilita 
        '''
        if event.key() == QtCore.Qt.Key_Escape:
            pass
        
    def keyPressEvent(self, qKeyEvent):
        '''
        Metodo que configura para movernos de un input a otro atravez del boton enter
        '''
        if qKeyEvent.modifiers() & QtCore.Qt.AltModifier:
            qKeyEvent.ignore()
        elif qKeyEvent.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.focusNextChild()
            self.window().setAttribute(QtCore.Qt.WA_KeyboardFocusChange)
        else:
            super().keyPressEvent(qKeyEvent)
        
    def guardarDatosUsuario(self):
        '''
        Metodo que obtiene los datos del usuario , valida los campos ingresados
        y respectivamente guarda en la base de datos
        '''
        
        # Obtenemos datos del usuario 
        dni = self.venAdmi.line_dni.text()
        nombre = self.venAdmi.line_nombre.text().strip().title()
        apellidos = self.venAdmi.line_apeP.text().strip().title()
        genero = "M" if self.venAdmi.cbox_genero.currentIndex() == 1 else "F"
        fecha = self.venAdmi.date_naci.text()
        sede_id = self.sedes_dic[self.venAdmi.cbox_sedes.currentText()] if self.venAdmi.cbox_sedes.currentText() != 'Seleccionar' else 0
        estado = self.venAdmi.cbox_estado.currentIndex()
        correo = self.venAdmi.line_correo.text().strip()
        contrasena = self.venAdmi.line_contrasena.text().strip()

        # metodo para  validar el correo
        validar_correo = bool(re.findall(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', correo))

        # Dominios que el correo ingresado debe tener
        base_correo = ["@gmail.com", "@hotmail.com", "@outlook.com", "@summa-sci.com"]


        try:
            cadena_correo = correo[0:correo.index("@")]
        except:
            cadena_correo = ''

        if(correo.lstrip(cadena_correo) in base_correo):
            sw_correo_val = True
        else:
            sw_correo_val = False

        # procedimiento almacenado que retorna datos de tabla usuario , roles
        consulta_usuario , consulta_roles = self.control_admi.getDatosProcess("sp_consultausuarioAdmi")

        # convertimos los roles en un diccionario
        roles = dict(zip([ide[0] for ide in consulta_roles],[nom[1] for nom in consulta_roles]))

        # separamos el dni y correo en listas distintas
        if consulta_usuario:
            lista_dni = [x[0] for x in consulta_usuario]
            lista_correo = [x[2] for x in consulta_usuario]
            

        errores = []

        if (nombre == ''):
            errores.append("    *Dato nombre")

        if(apellidos == ''):
            errores.append("    *Dato apellidos")
            
        if len(dni) < 8:
            errores.append("    *Dato dni ")
        
        elif int(dni) in lista_dni:
            errores.append("    *Dato dni ya existe en el sistema.")
            
        if (validar_correo) == False or (sw_correo_val == False) or len(correo) == 0:
            errores.append("    *Correo no autorizado consultar con el ceo.")

        elif correo in lista_correo:
            errores.append("    *Correo ya existe en el sistema.")

        if len(contrasena) < 8:
            errores.append("    *Dato contraseña minino 8 digitos.")

        if len(self.listaseleccion) == 0:
            errores.append("    *Cargo obligatorio.")
        
        if sede_id == 0:
            errores.append("    *Sede obligatorio.")

        if self.venAdmi.cbox_genero.currentIndex() == 0:
            errores.append("    *Sexo obligatorio.")
            
      
        if not errores:
            rolesnom = ""
            
            for i in self.listaseleccion:
                rolesnom += " - "+roles[i].upper()+" - "

            if (QtWidgets.QMessageBox.question(self, "Usuario", "¿Estas segura(o) darle el rol "+rolesnom+" Al usuario?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes):

                # convertimos la foto a binario
                foto = "source\\image\\businessman.png"
                with open(foto, "rb") as f:
                    foto_base = f.read()

                # insertamos los datos a la tabla usuario
                self.control_admi.setDatos("""
                                            INSERT INTO usuario(dni, nombre, apellidos, fecha_nacimiento,correo,
                                            contrasena ,sexo, estado, foto , sede_id)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                            (dni, nombre, apellidos, fecha, correo, contrasena, genero , estado, foto_base, sede_id))

                # insertamos los datos a la tabla roles-usuario
                lista = []
                [lista.append([dni, x]) for x in self.listaseleccion]
                
                # insertamos en la tabla usuario_rol 
                self.control_admi.setDatosListFor("""INSERT INTO usuario_rol(usuario_dni, rol_id)VALUES(%s,%s)""", lista)

                QtWidgets.QMessageBox.information(self, 'Usuario', 'Usuario se agrego correctamente')

                # actualizamos la tabla usuario llamando al metodo donde recarga los datos actualizados
                self.parent.cargar_usuario()
                self.parent.raizOpacidad.close()
                self.close()
                
            else:
                return

        else:
            QtWidgets.QMessageBox.critical(
                self, 'Usuario', 'Error, revise los datos:\n'+"\n".join(errores))
 
# Perfil
class UsuarioPerfil(QtWidgets.QDialog):
    def __init__(self, parent):
        super(UsuarioPerfil, self).__init__()
        self.venPerfil = Ui_Perfil()
        self.venPerfil.setupUi(self)
        self.control_perfil = BaseDatos()
        self.parent = parent

        configuracionVentanaPerfil(self)

        self.ruta_imagen = None
        self.foto_base = None
        self.lista_usuario = []
        self.Llenado_datos()

        self.venPerfil.btn_foto.clicked.connect(self.cambiar_foto)
        self.venPerfil.btn_guardar.clicked.connect(self.guardar_datos)


    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.modifiers() & QtCore.Qt.AltModifier:
            qKeyEvent.ignore()
        elif qKeyEvent.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.focusNextChild()
            self.window().setAttribute(QtCore.Qt.WA_KeyboardFocusChange)
        else:
            super().keyPressEvent(qKeyEvent)

    def Llenado_datos(self):
        '''
        Metodo que tiene por funcion obtener datos del usuario logeado y respectivamente
        rellenar los datos en los campos correspondientes.
        
        '''
 
        # --- Datos obtenidos de la tabla usuario ---
        usuario, roles = self.control_perfil.getDatosProcess_condicion("sp_cargaperfil", [self.parent.dni])
        #USUARIO ((12345678, 'Manuel', 'Anonimo', '2000-02-01', 'manuel@gmail.com', 'admin1234', 1, None),)
        
        roles = [x[0] for x in roles]
        roles = " - ".join(roles)

        datoLogin = [x for x in usuario]
        self.lista_usuario = [x for x in datoLogin[0]]
        
        self.venPerfil.line_dni.setText(str(self.lista_usuario[0]))  # dni
        self.venPerfil.line_nombre.setText(str(self.lista_usuario[1]))
        self.venPerfil.line_apeP.setText(str(self.lista_usuario[2]))
        self.venPerfil.date_naci.setDate(QtCore.QDate.fromString(self.lista_usuario[3], "yyyy-MM-dd"))
        self.venPerfil.line_correo.setText(str(self.lista_usuario[4]))
        self.venPerfil.line_contrasena.setText(str(self.lista_usuario[5]))
        self.venPerfil.cbox_genero.setCurrentIndex(int(self.lista_usuario[6]))

        self.venPerfil.line_cargo.setText(str(roles))

        self.venPerfil.lbl_perfil.clear()
        if self.lista_usuario[7]:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(self.lista_usuario[7], 'png')
            self.venPerfil.lbl_perfil.setPixmap(pixmap)
            self.foto_base = self.lista_usuario[7]


    def cambiar_foto(self):
        """Metodo para editar la foto de tu perfil"""
        self.ruta_imagen = QtWidgets.QFileDialog.getOpenFileName(self, "Seleccionar imagen", " ", "Archivos de imagen (*.png *.jpg)")[0]

        if self.ruta_imagen:
            # Adaptar imagen
            self.foto_perfil = QtGui.QPixmap(self.ruta_imagen)

            # Mostrar imagen
            self.venPerfil.lbl_perfil.setPixmap(self.foto_perfil)

    def guardar_datos(self):
        """Metodo para actualizar datos"""

        dni = self.venPerfil.line_dni.text()  # _-_-_-_-_-

        nombre = self.venPerfil.line_nombre.text().strip().title()
        apellidoP = self.venPerfil.line_apeP.text().strip().title()
        
        fecha = self.venPerfil.date_naci.date().toString("yyyy-MM-dd")
        genero = "M" if self.venPerfil.cbox_genero.currentIndex() == 1 else "F"
        contrasena = self.venPerfil.line_contrasena.text().strip()

        controlador = []

        if nombre == '':
            controlador.append('   *Dato nombre')

        if apellidoP == '':
            controlador.append('   *Dato Apellidos')

        if len(contrasena) <= 8:
            controlador.append('   *Dato contraseña minimo 8 digitos')

        if self.venPerfil.cbox_genero.currentIndex() == 0:
            controlador.append("   *Sexo obligatorio.")

        if not controlador:
            
            # si selecciono imagen
            if self.ruta_imagen:
         
                # abrir - ajustar imagen
                foo = Image.open(self.ruta_imagen)
                mg = foo.resize((500, 350))

                # convertimos la imagen a png
                mg.save('source/assets/imageCover.png')
          
                # obtenemos la ruta raiz de la imagen
                self.ruta_imagen = os.getcwd()+"/source/assets/imageCover.png"
             
                # convertimos en byte de la imagen
                with open(self.ruta_imagen, "rb") as f:
             
                    self.foto_base = f.read()

            
            datos = (nombre, apellidoP, fecha, contrasena,genero, self.foto_base, dni)
            get_datos_base = self.control_perfil.getDatosProcess_condicion("sp_upadatePerfil", datos)[0]
            datoLogin = [x[0] for x in get_datos_base]

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(datoLogin[0], 'png')
            self.parent.venPri.lbl_foto.setPixmap(pixmap)

            self.parent.cargar_usuario()

            nom = nombre[0:nombre.index(' ')] if(' ' in nombre) else nombre
            ape = apellidoP[0:apellidoP.index(' ')] if(' ' in apellidoP) else apellidoP

            self.parent.venPri.lbl_usuario.setText(str(nom+" "+ape))

            QtWidgets.QMessageBox.information(self, 'Usuario', 'Datos fueron actualizados correctamente.')

        else:
            QtWidgets.QMessageBox.critical(
                self, 'Usuario', 'Datos no fueron actualizados revise datos\n' + "\n".join(controlador))


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
        
# Editar usuario
class UsuarioEdit(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UsuarioEdit, self).__init__()
        self.venedit = Ui_AdmiEdit()
        self.venedit.setupUi(self)
        
        self.parent = parent
        
        configuracionVentanaEdit(self)
        
        self.control_editusu = BaseDatos()
        
        
        self.listaseleccion = []
        
        
        self.cargarusuario()
        self.venedit.btn_guardar.clicked.connect(lambda: self.actualizar_usuario())



    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.modifiers() & QtCore.Qt.AltModifier:
            qKeyEvent.ignore()
        elif qKeyEvent.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.focusNextChild()
            self.window().setAttribute(QtCore.Qt.WA_KeyboardFocusChange)
        else:
            super().keyPressEvent(qKeyEvent)


    def cargarusuario(self):

       
        usuario, roles = self.control_editusu.getDatosProcess_condicion("sp_cargausuarioEdit", [self.parent.dniseleccionado, ])
        # Usuario  ((22222222, 'Manuel Raul', 'Perez Luna', '2000-01-01', 'manuel65@gmail.com', 'manuel1234567', 'M', '1'),)

        usuario = [x for x in usuario[0]]
        roles = [x[0] for x in roles]

        # los id roles de la consulta lo guardamos en lista seleccion
        self.listaseleccion = roles

        nom = ""
        for i in usuario[1]:
            if i == " ":
                break
            nom += i

        self.venedit.lbl_nombretitulo.setText(str(nom+" "+usuario[2]))
        self.venedit.lbl_dnititulo.setText(str(usuario[0]))

        self.venedit.line_dni.setText(str(usuario[0]))
        self.usuario_dni = usuario[0]
        self.venedit.line_nombre.setText(str(usuario[1]))
        self.venedit.line_apeP.setText(str(usuario[2]))

        self.venedit.date_naci.setDate(QtCore.QDate.fromString(usuario[3], "yyyy-MM-dd"))
        self.venedit.line_correo.setText(str(usuario[4]))
        self.venedit.line_contrasena.setText(str(usuario[5]))
        
        rol_id = 1 if usuario[6] == 'M' else 2
        self.venedit.cbox_genero.setCurrentIndex(rol_id)

        self.venedit.cbox_estado.setCurrentIndex(int(usuario[7]))

        for i in roles:
            if i == 3:
                self.venedit.admi.setChecked(True)
            if i == 4:
                self.venedit.user.setChecked(True)
        
   
    def actualizar_usuario(self):
        """
        Metodo que tiene por finalidad  actualizar 
        """
   
        estado = self.venedit.cbox_estado.currentIndex()
        correo = self.venedit.line_correo.text().strip()
        
        errores = []  

        if len(self.listaseleccion) == 0:
            errores.append("    *Cargo obligatorio.")

        if not errores:

            if (QtWidgets.QMessageBox.question(self, "Usuario", """¿Estas segura(o) actualizar datos del usuario?.""",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes):


                datos =  (estado , correo, self.parent.dniseleccionado)

                self.control_editusu.getDatosProcess_condicion("sp_upadateUsuario", datos)

               
                self.control_editusu.deleteDatos(
                    """DELETE FROM usuario_rol WHERE usuario_dni=%s""", (self.parent.dniseleccionado))

                for i in self.listaseleccion:
                    self.control_editusu.setDatos("""INSERT INTO usuario_rol(usuario_dni,rol_id)values(%s,%s)""",(self.parent.dniseleccionado, i))

                QtWidgets.QMessageBox.information(self, 'Usuario', 'Dato usuario se atualizo correctamente')

                #if self.parent.dni == self.usuario_dni:
                #    self.parent.venPri.lbl_psicologa.setText(
                #        str(nombre+" "+apellidoP))

                # actualizar *- pacientes/inicio/perfilsuperior

                # cargamos tabla usuario
                self.parent.cargar_usuario()

                # tabla principal
                #self.parent.rango_mostrar()

                # tabla inicio
                #consulta = consulta_pac_psi()
                #dato_inicio = self.control_editusu.getDatos_condicion(
                #    consulta+"""ORDER BY p.pas_numhistoria DESC LIMIT %s""", (12))
                #cargar_tabla(self.parent.venPri.tabla_inicio, dato_inicio)

                self.parent.raizOpacidad.close()
                self.close()

            else:
                return

        else:
            QtWidgets.QMessageBox.critical(
                self, 'Usuario', 'Dato no actualizado, revise datos\n'+"\n".join(errores))
                