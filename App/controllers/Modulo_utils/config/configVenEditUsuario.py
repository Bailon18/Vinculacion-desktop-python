
from PySide2 import QtWidgets

# importaciones de modulo funcion general
from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_principal.funcion_general import *


def configuracionVentanaEdit(parent):

    # Quitar fondo, transparencia
    parent.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    parent.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                        QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
    parent.venedit.btn_closeedit.clicked.connect(
        lambda: parent.parent.raizOpacidad.close())
    parent.venedit.btn_closeedit.clicked.connect(lambda: parent.close())
    
    
    # darle estilo windows a los botones de mostrar - ocultar contraseña
    estilo(parent)

    # Evento para mostrar y ocultar contraseña
    parent.venedit.bnt_ojoVis.hide()
    parent.venedit.bnt_ojoInv.show()

    # --- toolbutton ---
    parent.venedit.bnt_ojoInv.clicked.connect(lambda: evento_ocultar(parent.venedit.bnt_ojoInv,
                                                    parent.venedit.bnt_ojoVis, parent.venedit.line_contrasena, 1))
    parent.venedit.bnt_ojoVis.clicked.connect(lambda: evento_ocultar(parent.venedit.bnt_ojoInv,
                                                    parent.venedit.bnt_ojoVis, parent.venedit.line_contrasena, 2))


    parent.venedit.admi.clicked.connect(lambda: eventorol(parent, parent.venedit))  # 1
    parent.venedit.user.clicked.connect(lambda: eventorol(parent, parent.venedit))  # 2


    val_numerIngreso(parent, parent.venedit.line_dni)
    val_cadenaIngreso(parent, parent.venedit.line_nombre)
    val_cadenaIngreso(parent, parent.venedit.line_apeP)
