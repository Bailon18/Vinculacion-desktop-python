
from PySide2 import QtWidgets
from os import environ

def evento_ocultar(tol_inv,tol_vis,line,dato): # cambiar
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

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

def add_font_app(ruta, extension):
    '''extension: ttf, otf '''
    try:
        from PySide2.QtGui import QFontDatabase
        import os

        for font in os.listdir(ruta):
            if(font.endswith(extension)):
                font_set = os.path.join(ruta, font)
                QFontDatabase.addApplicationFont(font_set)
    except:
        pass

def limpiar_login(parent,index):

    parent.venLogin.stackedWidget.setCurrentIndex(index)
    parent.venLogin.line_correo.setText('')
    parent.venLogin.line_contrasena.setText('')
    parent.venLogin.line_email2.setText('')

def estilos_login(parent):
    
    estiloDefecto = QtWidgets.QStyleFactory.create('windowsvista')
    parent.venLogin.btn_aceptar.setStyle(estiloDefecto)
    parent.venLogin.btn_recuperar.setStyle(estiloDefecto)
    parent.venLogin.btn_close.setStyle(estiloDefecto)
    parent.venLogin.tol_invsible.setStyle(estiloDefecto)
    parent.venLogin.tol_visible.setStyle(estiloDefecto)
    

