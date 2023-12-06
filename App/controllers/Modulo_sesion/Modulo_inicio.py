
from PySide2 import QtWidgets, QtCore

# Importaciones para enviar correo
from email.mime.text import MIMEText
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from datetime import datetime


# importado desde views 
from views.ui_login import Ui_ventana_sesion

# importamos la clase de la base datos
from db.Modulo_base import BaseDatos

# importamos funcion_inicio
from controllers.Modulo_sesion.funcion_inicio import estilos_login , limpiar_login , evento_ocultar

class Login(QtWidgets.QDialog):
    
    def __init__(self):

        super(Login, self).__init__()

        self.venLogin = Ui_ventana_sesion()
        self.venLogin.setupUi(self)
        
        self.conec_base = BaseDatos()
        
        self.venLogin.line_correo.setText("paucarmontesbailon@gmail.com")
        self.venLogin.line_contrasena.setText("admin123456")
    
        # Quitar sombra - titulo de barra
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # boton para eliminar la ventana
        self.venLogin.btn_close.clicked.connect(lambda: self.close())
        
        # Estilos
        estilos_login(self)
        
        # Botones para cambiar de pagina
        self.venLogin.btn_cancelarr.clicked.connect(lambda : limpiar_login(self,0))
        self.venLogin.btn_recuperar.clicked.connect(lambda : limpiar_login(self,1))
        
        # --- tool_ojo_visi ocultamos | toll_ojo_invi mostramos por defecto ---
        self.venLogin.tol_visible.hide()
        
        self.venLogin.tol_invsible.clicked.connect(lambda: evento_ocultar(
                    self.venLogin.tol_invsible,self.venLogin.tol_visible,self.venLogin.line_contrasena,1))
        self.venLogin.tol_visible.clicked.connect(lambda: evento_ocultar(
                    self.venLogin.tol_invsible,self.venLogin.tol_visible,self.venLogin.line_contrasena,2))
        
        
        
        self.venLogin.btn_aceptar.clicked.connect(lambda: self.validarIngreso())
        self.venLogin.btn_enviar.clicked.connect(lambda : self.enviar_correo())
        
    def validarIngreso(self):

        from controllers.Modulo_utils.Modulo_venCarga import Ui_VenCarga
        self.hide()
        Ui_VenCarga(["49583837","Administrador" ,"nombre_rol_reverse","Bailon","Paucar Montes", None]).exec_()
        
        # # datos de los inputs
        # correoIngreso = self.venLogin.line_correo.text()
        # contrasenaIngreso= self.venLogin.line_contrasena.text()

       
        # rol , usuario, sede = self.conec_base.getDatosProcess("sp_consulta_inicio")
    
        # # convertimos la lista de roles a diccionario
        # self.dic_roles=dict(zip([i[0] for i in rol],[i[1] for i in rol]))
        
        #  # convertimos la lista de sedes a diccionario
        # self.dic_sedes=dict(zip([i[0] for i in sede],[i[1] for i in sede]))
        
        
        # if usuario:

        #     usuaroLista = list(usuario)
            
        #     correoExtraido = [x for x in usuaroLista if(correoIngreso in x)]
            
        #     if (correoExtraido):
                
        #         usuario = correoExtraido[0]
                
        #         # contraseña ingresa no es ingual a la contraseña base de datos
        #         if(contrasenaIngreso != usuario[4]):
                    
        #             # mensaje contrraseña incorrecta
        #             QtWidgets.QMessageBox.critical(self,"Conexión","Contraseña incorrecto!")
        #             return 
                
        #         # contraseña ingresa es ingual a la contraseña base de datos y estado es distinto a activo
        #         elif( usuario[4] == contrasenaIngreso) and int(usuario[5]) != 1:
                    
        #             QtWidgets.QMessageBox.critical(self,"Conexión","Su cuenta no se encuentra activa!")
        #             return 
                
        #         # correcta 
        #         else:
                    
        #             usuariorol = self.conec_base.getDatos_condicion("SELECT rol_id  FROM usuario_rol where usuario_dni=%s ",[usuario[0]])
                    
        #             datorol = [self.dic_roles[x[0]] for x in usuariorol]
                    
                
        #             # nombre → id
        #             dic_roles_reverse = dict(zip(self.dic_roles.values(),self.dic_roles.keys()))
                   
                    
                    
        #             if len(datorol)>1:
                        
        #                 mensaje = QtWidgets.QInputDialog()
        #                 mensaje.setStyleSheet('QComboBox {combobox-popup: 0}')
                                                                                                
        #                 itemseleccionado, ok = mensaje.getItem(self,'Roles',str(f'{" "*4}Usted cuenta con mas de un rol\n{" "*8}'
        #                                                         'Escoja rol para iniciar sesión'), datorol, 0, False)                                              
        #                 if ok and itemseleccionado:                                                                                                                    
        #                     nombre_rol = itemseleccionado
        #                 else:
        #                     return
        #             else:
        #                 nombre_rol = datorol[0]
                        

        #             nombre_usuario = usuario[1]
        #             apellido = usuario[2]
                    

        #             foto = usuario[7] if len(usuario) == 8 else 0
                    
        #             dni = usuario[0]
                    
        #             nom = nombre_usuario[0:nombre_usuario.index(" ")] if " " in nombre_usuario else nombre_usuario
                    
        #             from controllers.Modulo_utils.Modulo_venCarga import Ui_VenCarga
        #             self.hide()
        #             Ui_VenCarga([dni,nombre_rol,dic_roles_reverse[nombre_rol],nom,apellido, foto, self.dic_sedes[usuario[6]], self.dic_sedes]).exec_()
                    
        #     else:
        #         QtWidgets.QMessageBox.critical(self,"Conexión","Correo no existe!")
        # else:
        #     QtWidgets.QMessageBox.critical(self,"Conexión","La base de datos está vacío")
            
    def enviar_correo(self):
        """enviar contraseña al correo registrado"""
        # dato correo - consulta a BD

      
        correo = self.venLogin.line_email2.text()

        if correo:

            get_datos = self.conec_base.getDatos_condicion("""SELECT nombre, correo, contrasena FROM usuario
                                                                where correo= %s""",(correo))
            dato_validar = [x for x in get_datos]
            if(dato_validar):

                # obtenemos primera posicion 
                dato = [x for x in dato_validar[0]]

                # datos de fecha --- inicio
                fechactual = datetime.now()
                # 24H → AM/PM
                horaEntrada = datetime.strptime(f"{fechactual.hour}:{fechactual.minute}:{fechactual.second}", "%H:%M:%S")
                horaSalida = datetime.strftime(horaEntrada, "%I:%M:%S %p")
                # datos de fecha --- fin

                emisor = 'paucarmontesbailon@gmail.com'
                contra = 'kevinandre188'

                receptor = correo
                
                try:
                    # Configuracion del mail
                    mensaje = MIMEMultipart("alternative") # standar
                    mensaje['Subject'] = "Solicitud de recuperación de contraseña"
                    mensaje['From'] = emisor
                    mensaje['To'] = receptor


                    div_fechahora = f'{fechactual.strftime("%d/%m/%Y")} {horaSalida}'
                    div_usuarionom = dato[0]
                    div_contrasena = dato[2]
                    div_ahoactual= str(fechactual.year)

                    html = self.codigo_html_envio(div_fechahora,div_usuarionom,div_contrasena,div_ahoactual,emisor,dato[1])
                    parte_html = MIMEText(html, 'html')
                    mensaje.attach(parte_html)

                    context = ssl.create_default_context()

                    with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as server:
                        server.login(emisor, contra)
                        server.sendmail(emisor, receptor, mensaje.as_string())

                    self.venLogin.line_mensaje.setText(dato[0]+' recibió su contraseña con éxito.')
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self, 'Error', f'Recuperación de contraseña fallido, por favor\nconsultar con el soporte contactoexec@gmail.com')
            
            else:
                self.venLogin.line_mensaje.setText('Error, correo no registrado en la base de datos.')
        else:
            self.venLogin.line_mensaje.setText('Error, Campo correo vacío.')
                

    def codigo_html_envio(self,fechahora,usuarionom,contrasena,ahoactual,emisor,receptor):
        """codigo fuente de la plantilla html"""


        imagen = str("https://static.wixstatic.com/media/57c50b_10ace1329e484af3abaa7321ca5d7010~mv2.jpg/v1/fill/w_350,h_197,al_c,q_80,usm_0.66_1.00_0.01/57c50b_10ace1329e484af3abaa7321ca5d7010~mv2.webp")
                
        urlweb = "https://padmaperu.com/"

        mensajehtml = f"""
                        <html>
                            <body>
                                <div style="font-family:'Helvetica Neue',Helvetica,Roboto,Arial,sans-serif;direction:ltr"> 
                                    <img alt="" height="1" width="1" >
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F2F2F2">
                                        <tbody>
                                            <tr> 
                                                <td  bgcolor="#F2F2F2" align="center" style="padding:0 8px">  
                                                    <table width="100%" cellpadding="0" cellspacing="0" border="0"> 
                                                        <tbody>
                                                            <tr>
                                                                <td align="center" style="padding:25px 0px">
                                                                    <a><img src="{imagen}" width="150" style="display:block" border="0"></a>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table> 

                                                    <table  style="max-width:550px;border-radius:24px" width="100%" bgcolor="#FFFFFF"  cellpadding="15" cellspacing="15" border="0"> 
                                                        <tbody>
                                                            <tr>
                                                                <td style="padding-bottom:24px!important"> 
                                                                    <table width="100%" cellpadding="0"cellspacing="0" border="0">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td> 
                                                                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td>
                                                                                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td style="padding-bottom:24px"> 
                                                                                                                        <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                                                                                            <tbody>
                                                                                                                                <tr> 
                                                                                                                                    <td align="center" style="font-family:'Helvetica Neue',Roboto,Arial,sans-serif;font-size:26px; line-height:32px;color:#000000;font-weight:bold">
                                                                                                                                            Bienvenido(a) a Argos
                                                                                                                                    </td> 
                                                                                                                                </tr>
                                                                                                                                <tr> 
                                                                                                                                    <td align="center" style="font:13px/18px HelveticaNeue,Helvetica,Arial,sans-serif;color:#666;padding:8px 0 0">
                                                                                                                                    Soporte y seguridad
                                                                                                                                    </td>
                                                                                                                                </tr>
                                                                                                                            </tbody>
                                                                                                                        </table>
                                                                                                                    </td> 
                                                                                                            </tr>
                                                                                                            <tr>
                                                                                                                <td  style="background:#3A4F50;height:6px;display:block;font-size:1px">&zwnj;</td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr> 
                                                                        </tbody>
                                                                    </table>
                                                                </td> 
                                                            </tr>
                                                            <tr> 
                                                                <td style="padding-top:0!important">
                                                                    <table width="100%" cellpadding="0" cellspacing="0"border="0">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td>
                                                                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                                                        <tbody><tr>
                                                                                            <td>
                                                                                                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                                                                    <tbody>
                                                                                                        <tr>
                                                                                                            <td style="padding-bottom:32px">
                                                                                                                <a style="text-decoration:none" target="_blank"> 

                                                                                                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                                                                                        <tbody>
                                                                                                                            <tr>
                                                                                                                                <td align="left" style="font-weight:bold;padding-bottom:10px"> 
                                                                                                                                    <a style="color:#000000;font-size:19px;line-height:24px"> 
                                                                                                                                    Solicitud recuperación de contraseña</a> 

                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                            <tr> 
                                                                                                                                <td align="left" style="font-size:14px;line-height:20px;font-weight:500;color:#2d2d2d;padding-bottom:4px">
                                                                                                                                    <span>Emitido el </span> 
                                                                                                                                    <span style="font-weight:400;display:inline!important;color:#767676">{fechahora}</span> 
                                                                                                                                </td>
                                                                                                                            </tr> 
                                                                                                                            <tr> 
                                                                                                                                <td align="left" style="font-size:14px;line-height:20px;font-weight:400;color:#4b4b4b;padding-bottom:4px">    
                                                                                                                                    Hola {usuarionom} con el correo {receptor} registrado en el programa, nos complace infórmate que su contraseña se le ha enviado con éxito, recuerda mantener en secreto dicha clave:
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                            <tr> 
                                                                                                                                <td align="left" style="font-family:'Helvetica Neue',Roboto,Arial,sans-serif;color:#28979f;font-size:14px;line-height:35px;padding-bottom:4px">
                                                                                                                                {contrasena}
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                        </tbody>
                                                                                                                    </table>
                                                                                                                </a>
                                                                                                            </td>
                                                                                                        </tr>
                                                                                                    </tbody>
                                                                                                </table>
                                                                                            </td> 
                                                                                        </tr>
                                                                                    <tr> 
                                                                                <td> 
                                                                                <table width="100%" cellpadding="0" cellspacing="0" border="0"> 
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center"> 
                                                                                                <div>
                                                                                                    <a href="{urlweb}" style="background-color:#3A4F50;border:1px solid #3A4F50;border-radius:100px;color:#ffffff;display:inline-block;font-family:'Helvetica Neue',
                                                                                                        Helvetica,Arial,Liberation Sans,Roboto,Noto,sans-serif;font-size:16px;
                                                                                                        font-weight:bold;line-height:44px;text-align:center;text-decoration:none;width:100%">
                                                                                                        Visitar página oficial de ARGOS
                                                                                                    </a>
                                                                                                </div>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table> 
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table> 
                                                                    </td>
                                                                        </tr>
                                                            </tbody>
                                                        </table> 
                                                    </td>
                                                </tr> 
                                            </tbody>
                                        </table> 
                                
                                        <table style="max-width:550px" width="100%" bgcolor="#F2F2F2" cellpadding="0" cellspacing="0" border="0">
                                            <tbody>
                                                <tr>
                                                    <td style="padding:0px 4px"> 
                                                        <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                            <tbody> 
                                                                <tr>
                                                                    <td style="font-size:12px;line-height:16px;color:#2d2d2d;padding:40px 0 16px" align="left">
                                                                        El correo de soporte estará al pendiente de sus consultas de contraseña, se agradece su comprensión y que un buen día.
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table> 
                                            
                                                        <table align="center" width="100%" cellpadding="0" cellspacing="0" border="0" style="font-size:12px;color:#2d2d2d;line-height:22px;Margin:0 auto">
                                                            <tbody>
                                                                <tr>
                                                                    <td lang="en" align="center" style="padding:0 0px 0px"> © {ahoactual} ARGOS - COLOMBIA</td> 
                                                                </tr>
                                                                <tr>
                                                                    <td lang="en" align="center" style="padding:0px">{emisor}</td> 
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                </body>
                            </html>
        
        """
        return mensajehtml