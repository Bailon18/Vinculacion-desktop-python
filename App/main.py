
# ------ Importacion Modulo error ------
from controllers.Modulo_sesion.funcion_inicio import suppress_qt_warnings , add_font_app
import sys

# ------ Importacion PySide2 ------
from PySide2 import QtWidgets
from PySide2 import QtCore
# ------ Importacion Modulo Login ------
from controllers.Modulo_sesion.Modulo_inicio import Login


# aqui se ejecuta todo el programa
if __name__ == "__main__":
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    # --- Traduccion a español ---
    traductor = QtCore.QTranslator(app)
    lugar = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    traductor.load("qtbase_%s" % lugar, path)
    app.installTranslator(traductor)

    try:
        add_font_app(r'source\fonts', 'ttf')
    except Exception as e:
        print(f"Error al cargar fuentes: {e}")

    
    ventana_ses = Login()
    ventana_ses.show()
    sys.exit(app.exec_())
   
