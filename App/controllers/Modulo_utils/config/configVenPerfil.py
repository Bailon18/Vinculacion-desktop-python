from PySide2 import QtWidgets

# importaciones de modulo funcion general
from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_principal.funcion_general import *


def configuracionVentanaPerfil(parent):
    

    # Quitar fondo, transparencia
    parent.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    parent.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                        QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
    parent.venPerfil.btn_closeperfil.clicked.connect(
        lambda: parent.parent.raizOpacidad.close())
    
    parent.venPerfil.btn_closeperfil.clicked.connect(lambda: parent.close())

    # --- tool_ojo_visi ocultamos | toll_ojo_invi mostramos por defecto ---
    parent.venPerfil.bnt_ojoVis.hide()
    parent.venPerfil.bnt_ojoInv.show()

    # --- toolbutton ---
    parent.venPerfil.bnt_ojoInv.clicked.connect(lambda: evento_ocultar(parent.venPerfil.bnt_ojoInv,
                                                                        parent.venPerfil.bnt_ojoVis, parent.venPerfil.line_contrasena, 1))
    parent.venPerfil.bnt_ojoVis.clicked.connect(lambda: evento_ocultar(parent.venPerfil.bnt_ojoInv,
                                                                        parent.venPerfil.bnt_ojoVis, parent.venPerfil.line_contrasena, 2))

    # Validar campos
    val_cadenaIngreso(parent, parent.venPerfil.line_nombre)
    val_cadenaIngreso(parent, parent.venPerfil.line_apeP)

   