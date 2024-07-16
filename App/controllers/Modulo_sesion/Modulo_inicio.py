
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMessageBox

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
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return

        correoIngreso = self.venLogin.line_correo.text()
        contrasenaIngreso = self.venLogin.line_contrasena.text()
        
        print('correoIngreso', correoIngreso)
        print('contrasenaIngreso', contrasenaIngreso)

        # Buscar en la tabla de usuarios
        resultado_usuario = self.conec_base.getDatos_condicion(
            '''
            SELECT u.user_id, u.nombre, r.role_name AS role_nombre, u.estado
            FROM usuarios u
            JOIN roles r ON u.role_id = r.role_id
            WHERE u.correo_electronico = %s AND u.contrasena = %s
            ''',
            (correoIngreso, contrasenaIngreso)
        )

        if resultado_usuario:
            datos_usuario = resultado_usuario[0]
            estado_usuario = datos_usuario[3]
            
            if estado_usuario == 'Activo':
                from controllers.Modulo_utils.Modulo_venCarga import Ui_VenCarga
                self.hide()
                Ui_VenCarga(
                    [datos_usuario[0],
                    f"{datos_usuario[1]}", 
                    datos_usuario[2]] 
                ).exec_()
            else:
                QMessageBox.warning(self, "Usuario Inactivo", f"Sr {datos_usuario[1]}, su cuenta está inactiva. Comuníquese con el administrador.")
            return

        # Buscar en la tabla de tutores
        resultado_tutor = self.conec_base.getDatos_condicion(
            '''
            SELECT id, nombres, 'Tutor' AS role_nombre, estado
            FROM tutores
            WHERE correo = %s AND contrasena = %s
            ''',
            (correoIngreso, contrasenaIngreso)
        )


        if resultado_tutor:
          
            datos_tutor = resultado_tutor[0]
            estado_usuario = datos_tutor[3]

            if estado_usuario != 0 :
                from controllers.Modulo_utils.Modulo_venCarga import Ui_VenCarga
            
                self.hide()
                Ui_VenCarga(
                    [datos_tutor[0], 
                    f"{datos_tutor[1]}",  
                    datos_tutor[2]]  
                ).exec_()
            else:
                QMessageBox.warning(self, "Tutor Inactivo", f"Sr {datos_tutor[1]}, su cuenta está inactiva. Comuníquese con el administrador.")
       
    
        else:
            QMessageBox.critical(self, "Error de Inicio de Sesión", "El correo electrónico o la contraseña son incorrectos.")


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
    
    def enviar_correo(self):
        if not self.conec_base.verificarConexionInternet():
            QtWidgets.QMessageBox.critical(self, "Error", "No hay conexión a Internet.")
            return
    
        correo = self.venLogin.line_email2.text()

        if correo:
            # Buscar en la tabla de usuarios
            get_datos_usuario = self.conec_base.getDatos_condicion(
                """SELECT nombre, correo_electronico, contrasena, estado 
                FROM usuarios 
                WHERE correo_electronico = %s""",
                (correo,)
            )
            
            # Buscar en la tabla de tutores
            get_datos_tutor = self.conec_base.getDatos_condicion(
                """SELECT nombres AS nombre, correo, contrasena, estado 
                FROM tutores 
                WHERE correo = %s""",
                (correo,)
            )

            # Unir resultados
            get_datos = get_datos_usuario if get_datos_usuario else get_datos_tutor
            dato_validar = [x for x in get_datos]

            if dato_validar:
                dato = [x for x in dato_validar[0]]

                if (get_datos_usuario and dato[3] == 'Activo') or (get_datos_tutor and dato[3] == 1):  # Verificar estado
                    fechactual = datetime.now()
                    horaEntrada = datetime.strptime(f"{fechactual.hour}:{fechactual.minute}:{fechactual.second}", "%H:%M:%S")
                    horaSalida = datetime.strftime(horaEntrada, "%I:%M:%S %p")

                    emisor = 'pedro29pablo062000@gmail.com'
                    contra = 'dnhummctzntwjujz'
                    receptor = correo
                    
                    try:
                        # Configuracion del mail
                        mensaje = MIMEMultipart("alternative")  # standar
                        mensaje['Subject'] = "Solicitud de recuperación de contraseña"
                        mensaje['From'] = emisor
                        mensaje['To'] = receptor

                        div_fechahora = f'{fechactual.strftime("%d/%m/%Y")} {horaSalida}'
                        div_usuarionom = dato[0]
                        div_contrasena = dato[2]
                        div_ahoactual = str(fechactual.year)

                        html = self.codigo_html_envio(div_fechahora, div_usuarionom, div_contrasena, div_ahoactual, emisor, dato[1])
                        parte_html = MIMEText(html, 'html')
                        mensaje.attach(parte_html)

                        context = ssl.create_default_context()

                        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                            server.login(emisor, contra)
                            server.sendmail(emisor, receptor, mensaje.as_string())

                        self.venLogin.line_mensaje.setText(dato[0] + ' recibió su contraseña con éxito.')
                    except Exception as e:
                        QtWidgets.QMessageBox.critical(self, 'Error', 'Recuperación de contraseña fallida, por favor\nconsultar con el soporte')
                else:
                    self.venLogin.line_mensaje.setText(f'Sr {dato[0]}, su cuenta está inactiva. Comuníquese con el administrador.')
            else:
                self.venLogin.line_mensaje.setText('Error, correo no registrado en la base de datos.')
        else:
            self.venLogin.line_mensaje.setText('Error, Campo correo vacío.')

                

    def codigo_html_envio(self,fechahora,usuarionom,contrasena,ahoactual,emisor,receptor):
        """codigo fuente de la plantilla html"""


        imagen = str("https://univercimas.com/wp-content/uploads/2021/05/Logo-de-la-Universidad-Estatal-del-Sur-de-Manabi-UNESUM.jpg")
                
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
                                                                                                                                            Bienvenido(a) a UNESUM
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
                                                                                                        Visitar página oficial de UNESUM
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
                                                                    <td lang="en" align="center" style="padding:0 0px 0px"> © {ahoactual} UNESUM - ECUADOR</td> 
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