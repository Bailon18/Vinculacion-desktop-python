
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/ RESTRICCION DE INGRESO /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator,QIntValidator
from PySide2.QtCore import QDate # para fechas

def val_nombre_apellido(parent, objeto):
    valNombreApellido = QRegExpValidator(parent)
    valNombreApellido.setRegExp(QRegExp("^[a-zA-ZÀ-ÿ ]+$"))  # Permitir letras y espacios y acentos
    objeto.setValidator(valNombreApellido) 


def val_identifiacion(parent, objeto):
    valCadenaNum = QRegExpValidator(parent)
    valCadenaNum.setRegExp(QRegExp("^\d{9}-\d{1}$"))
    objeto.setValidator(valCadenaNum)  # Aplicar el validador al QLineEdit
    
def mascara_identificacion(objeto):
    """Máscara de ingreso"""
    objeto.setInputMask("999999999\-9")

def val_periodo_academico(parent, objeto):
    # Validador para el formato P1-2023 o P2-2023
    valPeriodoAcademico = QRegExpValidator(parent)
    valPeriodoAcademico.setRegExp(QRegExp("^P[1-2]-\d{4}$"))
    objeto.setValidator(valPeriodoAcademico)  # Aplicar el validador al QLineEdit

def mascara_periodo_academico(objeto):
    """Máscara de ingreso"""
    objeto.setInputMask("P9-9999")
    

def val_codigo_campoespecifico(parent, objeto):
    # Validador para el formato 1-6A
    valcampoespecifico = QRegExpValidator(parent)
    valcampoespecifico.setRegExp(QRegExp("^[1-9]-[1-9][A-Z]$"))
    objeto.setValidator(valcampoespecifico) 

def mascara_campoespecifico(objeto):
    """Máscara de ingreso"""
    objeto.setInputMask("9-9A")  # Esto limita la entrada al formato específico 1-6A


def val_codigo_ies(parent, objeto):
    # Validador para el formato de 4 dígitos del 1 al 9
    valCodigoIES = QRegExpValidator(parent)
    valCodigoIES.setRegExp(QRegExp("^[1-9]{4}$"))
    objeto.setValidator(valCodigoIES) 

def mascara_codigo_ies(objeto):
    """Máscara de ingreso"""
    objeto.setInputMask("9999") 
    

import re

import re

def validar_correo_electronico(correo):
    
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    patron_compilado = re.compile(patron_correo)
    
    if patron_compilado.match(correo):
        return True
    else:
        return False




    
