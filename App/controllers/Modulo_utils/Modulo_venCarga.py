# funciones PySide2
from PySide2 import QtCore
from PySide2.QtWidgets import QDialog,QGraphicsDropShadowEffect
from PySide2.QtCore import Qt,QTimer

# diseño principal
from views.ui_ventanaCarga import Ui_VentanaCarga 

# ventana que se abrira
from controllers.Modulo_principal.Modulo_general import Principal

from PySide2.QtGui import QColor


def createSombra(cantidad=1, radio=28, ejex=0, ejey=0, colores=[0,0,0,80]):
    
    lista_sombras = []
    for i in range(cantidad):
        efecto_sombra = QGraphicsDropShadowEffect()
        efecto_sombra.setBlurRadius(radio)
        efecto_sombra.setXOffset(ejex)
        efecto_sombra.setYOffset(ejey)
        # color (r,g,b,a) tomar en cuenta que en a→255 es el valor maximo de opacidad
        cr, cg, cb, ca = colores
        efecto_sombra.setColor(QColor(cr, cg, cb, ca));

        lista_sombras.append(efecto_sombra)

    if(cantidad==1):
        return lista_sombras[0]

    else:
        return lista_sombras

def setSombra(objeto, efecto_sombra):
    objeto.setGraphicsEffect(efecto_sombra)



class Ui_VenCarga(QDialog):

    def __init__(self, lista_data):
        super(Ui_VenCarga, self).__init__()

        self.raizCarga = Ui_VentanaCarga()
        self.raizCarga.setupUi(self)

        # MODIFICAR PRIORIDAD DE VENTANA
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.lista_data = lista_data


        self.contador=0

        # QUITAR FONDO, TRANSAPARENCIA
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.configuraciones_widgets()


        # CAMBIAR TEXTO EN PLENA CARGA
        self.raizCarga.labTitu.setText(f'{self.lista_data[3]} {self.lista_data[4]}')
        # EJECUTANDO LA BARRA DE PROGRESO
        self.timeLoad = QTimer()
        self.timeLoad.timeout.connect(self.progresoView)
        self.timeLoad.start(20)#30

    def configuraciones_widgets(self):

        self.l1, self.l2 = createSombra(2)
        setSombra(self.raizCarga.frameLoad,self.l1)     
        setSombra(self.raizCarga.frameLoad,self.l2)     

    # CARGANDO BARRA
    def progresoView(self):

        self.raizCarga.progreLoad.setValue(self.contador)
        if(self.contador > 100):
            self.timeLoad.stop()

            self.close()

            dni, nombre_rol,nombre_rol_reverse,nom,apellido, foto = self.lista_data
            
            self.main = Principal(dni, nombre_rol,nombre_rol_reverse,nom,apellido, foto)
            self.main.showMaximized()
            #self.main.show()

        self.contador += 1

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass