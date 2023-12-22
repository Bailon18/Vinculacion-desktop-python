
from PySide2 import QtCore, QtWidgets , QtGui


def evento_tabla(parent):

    parent.seguimiento_tutor.tabla_listado_seguimiento.horizontalHeader().setVisible(True)

    index = [0, 3] 
    tamano = [70, 160]  

    for ind, tam in zip(index, tamano):
        parent.seguimiento_tutor.tabla_listado_seguimiento.setColumnWidth(ind, tam)

    parent.seguimiento_tutor.tabla_listado_seguimiento.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    for ind in index:
        parent.seguimiento_tutor.tabla_listado_seguimiento.horizontalHeader().setSectionResizeMode(ind, QtWidgets.QHeaderView.Fixed)
