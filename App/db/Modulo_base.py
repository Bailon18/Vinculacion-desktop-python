
from db.conexion import Conexion
from db.logger_base import logger
from db.cursor_del_pool import CursorDelPool
import requests


class BaseDatos:


    @classmethod
    def verificarConexionInternet(cls):
        try:
            response = requests.get("http://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    @classmethod
    def getDatos(cls,consulta):
        with CursorDelPool() as cursor:    
            cursor.execute(consulta)
            registros = cursor.fetchall()
            return registros
       
    @classmethod
    def getDatos_condicion(cls,consulta,dato):
        with CursorDelPool() as cursor:    
            cursor.execute(consulta, dato)
            registros = cursor.fetchall()
            return registros

    @classmethod
    def getDatosProcess(cls,consulta):
        with CursorDelPool() as cursor:
            cursor.callproc(consulta)
            results = [cursor.fetchall()]
            
            while cursor.nextset():
                results.append(cursor.fetchall())
            
            results = results[0:-1]
            return results  

    @classmethod
    def getDatosProcess_condicion(cls,consulta,dato):
        with CursorDelPool() as cursor:    
            cursor.callproc(consulta, dato)
            results = [cursor.fetchall()]
            
            while cursor.nextset():
                results.append(cursor.fetchall())
            
            results = results[0:-1]
            return results

    @classmethod
    def setDatos(cls, consulta,dato):
        with CursorDelPool() as cursor:
            cursor.execute(consulta, dato)
            
    @classmethod
    def setDatosProcess(cls, nomprocess, dato):
        with CursorDelPool() as cursor:
            cursor.callproc(nomprocess, dato)

    @classmethod
    def setDatosListFor(cls, consulta,dato):
        with CursorDelPool() as cursor:
            cursor.executemany(consulta,dato)
                  
    @classmethod
    def updateDatos(cls, consulta,datos):
        with CursorDelPool() as cursor:
            cursor.execute(consulta, datos)
             
    @classmethod
    def deleteDatos(cls, consulta,dato):
        with CursorDelPool() as cursor:
            cursor.execute(consulta, dato)
            
            

 