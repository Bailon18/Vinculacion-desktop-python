
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/ RESTRICCION DE INGRESO /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator,QIntValidator
from PySide2.QtCore import QDate # para fechas


def val_numEnteroIngreso(parent,objeto):  # numero de historia || enteros
    """solo datos numericos enteros ej [1-9] 1411426 (para numeros de historia)"""
    valCadenaNumEnt = QRegExpValidator(parent)
    valCadenaNumEnt.setRegExp(QRegExp('[1-9]+[0-9]+$'))

    objeto.setValidator(valCadenaNumEnt)

def val_numerIngreso(parent,objeto): # numero dni
    """solo datos numericos ej: 00240152 (para dni) 00042743724"""
    valCadenaNum = QRegExpValidator(parent)
    valCadenaNum.setRegExp(QRegExp('[0-9]+$'))

    objeto.setValidator(valCadenaNum)


def val_cadenaIngreso(parent,objeto): # cadena
    """solo datos cadena en caja para nombres jua pera"""
    valCadenaSpac = QRegExpValidator(parent)
    valCadenaSpac.setRegExp(QRegExp('[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$'))
    
    objeto.setValidator(valCadenaSpac)




