from PySide2 import QtWidgets

# importaciones de modulo funcion general
from controllers.Modulo_utils.Funcion_validaciones import *
from controllers.Modulo_principal.funcion_general import *


def configuracionVentanaAdmin(parent):

    # Quitar fondo, transparencia
    parent.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    parent.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
    parent.venAdmi.btn_closeadmi.clicked.connect(lambda: parent.parent.raizOpacidad.close())
    parent.venAdmi.btn_closeadmi.clicked.connect(lambda: parent.close())


    # Evento para obtener el rol elegido
    parent.venAdmi.admi.clicked.connect(lambda: eventorol(parent, parent.venAdmi))
    parent.venAdmi.user.clicked.connect(lambda: eventorol(parent, parent.venAdmi))


    # Evento para mostrar y ocultar contraseña
    parent.venAdmi.bnt_ojoVis.hide()
    parent.venAdmi.bnt_ojoInv.show()

    # --- toolbutton ---
    parent.venAdmi.bnt_ojoInv.clicked.connect(lambda: evento_ocultar(parent.venAdmi.bnt_ojoInv,
                                                    parent.venAdmi.bnt_ojoVis, parent.venAdmi.line_contrasena, 1))
    parent.venAdmi.bnt_ojoVis.clicked.connect(lambda: evento_ocultar(parent.venAdmi.bnt_ojoInv,
                                                    parent.venAdmi.bnt_ojoVis, parent.venAdmi.line_contrasena, 2))

    # Validacion de campos 
    val_numerIngreso(parent, parent.venAdmi.line_dni)
    val_cadenaIngreso(parent, parent.venAdmi.line_nombre)
    val_cadenaIngreso(parent, parent.venAdmi.line_apeP)
   