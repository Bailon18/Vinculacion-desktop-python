from db.conexion import Conexion
from db.logger_base import logger

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    def __enter__(self):

        self.__conn = Conexion.obtenerConexion()
        self.__conn.ping(True)
        self.__cursor = self.__conn.cursor()
        return self.__cursor


    def __exit__(self, exception_type, exception_value, exception_traceback):

        if exception_value:
            self.__conn.rollback()  
        else:
            self.__conn.commit() 

        self.__cursor.close()    
        Conexion.liberarConexion(self.__conn)
        

                    
 
             
    
    