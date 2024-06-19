
from PySide2 import QtCore, QtWidgets , QtGui
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon


def evento_tabla(parent):
    
    configuraciones_columnas = {
        parent.vinculacion.tabla_estudiante_seleccionado: {5: 120}
    }

    for tabla in configuraciones_columnas:
        header = tabla.horizontalHeader()
        header.setVisible(True)       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        for columna, ancho in configuraciones_columnas[tabla].items():
            tabla.setColumnWidth(columna, ancho)
        for i in range(1, tabla.columnCount()):
            if i not in configuraciones_columnas[tabla]:
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)