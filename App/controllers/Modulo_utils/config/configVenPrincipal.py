from PySide2 import QtWidgets

# importaciones de modulo funcion general
from controllers.Modulo_principal.funcion_general import *
from ..funcion_efecto import *

def configuracionVentana(parent):

    # Evento Opacidad -----------------------
    parent.raizOpacidad = Clase_Opacidad(parent)
    parent.raizOpacidad.close()


    # Evento de menu
    evento_menu(parent, parent.venPri, tr=0)
    parent.venPri.boton_deslizable.clicked.connect(lambda : evento_menu(parent, parent.venPri))

    # Evento de hora
    evento_hora(parent)
    
    evento_tabla(parent)

    # Evento  Menu
    sliderStack_bar = Clase_EfectoSlider(parent.venPri.stackedWidget,
                                            {0: parent.venPri.btn_almacen,
                                            2: parent.venPri.btn_reporte, 1: parent.venPri.btn_usuario}, 1)

    sliderStack_bar.establecer_index(0)
    parent.venPri.btn_almacen.clicked.connect(lambda: sliderStack_bar.transicion_stacked(0, [1, 2]))
    parent.venPri.btn_reporte.clicked.connect(lambda: sliderStack_bar.transicion_stacked(2, [1]))
    parent.venPri.btn_usuario.clicked.connect(lambda: sliderStack_bar.transicion_stacked(1, []))


   