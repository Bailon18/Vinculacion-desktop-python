# para la ventana carga
from PySide2.QtWidgets import QDialog,QMessageBox
from PySide2.QtGui import QCloseEvent # cerrar venta
from PySide2.QtCore import Qt,QTimer,QDate
from PySide2 import QtCore

# crear excel, rutas y rutas, abrir 
import os, webbrowser 

# elegir ruta
from PySide2.QtWidgets import QFileDialog

# pdf
from fpdf import FPDF

# ventana carga reporte
from views.ui_ui_VenCargaReportes import Ui_VenCargaReportes

# VENTANA MUESTRA USUARIO
class FormRepoImforme(QDialog):

    def __init__(self, repdatos, tipo, periodo):
        super(FormRepoImforme, self).__init__()

        # clase principal
        self.raizReptCargar = Ui_VenCargaReportes()
        self.raizReptCargar.setupUi(self)

        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.contador=0

        self.repdatos = repdatos
        self.tipo = tipo
        self.periodo = periodo

        # controlador cierre
        self.sw_cierre = False

        # instancia de la clase pdf
        self.raiz_inicia_rep = ClaseGeneradorReportes()

        # EJECUTANDO LA BARRA DE PROGRESO
        self.timeLoad = QTimer()
        self.timeLoad.timeout.connect(self.progresoView)
        self.timeLoad.start(5)#30

    # CARGANDO BARRA
    def progresoView(self):
        self.raizReptCargar.barraCarga.setValue(self.contador)
        if(self.contador > 100):
            self.sw_cierre=True
            self.timeLoad.stop()
            self.close()

            # GENERAR REPORTES---- 
            self.raiz_inicia_rep.gen_mandar_datos(self,self.repdatos, self.tipo, self.periodo)

        self.contador += 1

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
    # CERRADO DE VENTANA
    def closeEvent(self, event):
        if(self.sw_cierre):
            event.accept()
        else:
            event.ignore()


class ClaseGeneradorReportes():

    def __init__(self):

        raiz = os.getcwd()

        self.ruta_icon = raiz+r"/sources/icon_ex/logo.jpg"
        
        self.ruta_save = '' # se define al generar enlace
       

    def guardarArchivo(self, nombre_guardado):

        ruta= QFileDialog.getSaveFileName(None, 'Seleccionar archivo',nombre_guardado,'Texto (*.pdf)')
        return ruta[0]
       
    def gen_mandar_datos(self, parent, datos, tipo, periodo):


        # fecha de generacion del informe
        fecha_data_act = QDate.currentDate().toString("dd-MM-yyyy")

   
        # nombre del archivo
        nombre_archivo = f'Reporte_{tipo}_{fecha_data_act}'

        self.ruta_save = self.guardarArchivo(nombre_archivo)
        if(self.ruta_save==''):return
        
        
        if(tipo == "estudiantes"):
            self.gene_reporte_estudiantes(datos)  
        elif( tipo == "informe"):
            self.gene_reporte_informe(datos, periodo)
        elif( tipo == "ficha"):
            self.gene_reporte_ficha(datos, periodo)
        else:
            self.gene_reporte_memorandum(datos, periodo)
            
            
        webbrowser.open(self.ruta_save, new=2)
            



    def gene_reporte_estudiantes(self, dato):

        font_path = os.path.abspath('source/fonts/Roboto-Light.ttf')


        pdf = FPDF(orientation='L', unit='mm', format=(300, 538)) 
        pdf.add_page()

        pdf.add_font('Roboto', '', font_path, uni=True)

        pdf.set_font("Roboto", size=12)

        # Agregar imagen
        image_path = os.path.abspath('source/image/logito2.png')
        pdf.image(image_path, x=6, y=5, w=20, h=20)

        # Título
        pdf.cell(470, 10, txt="CARRERA DE TECNOLOGIAS DE INFORMACION", ln=True, align='C')
        pdf.cell(470, 10, txt="Reporte de Vinculación Estudiante", ln=True, align='C')
        pdf.cell(470, 10, txt="Periodo Académico " + str(dato[0][1]), ln=True, align='C')
        pdf.cell(470, 10, txt="", ln=True, align='C')

        pdf.set_fill_color(221, 235, 247) 
        pdf.set_font("Roboto", size=10, style='')

        # Cabecera de la tabla

        pdf.cell(19, 10, "Per. Acad.", 1, 0, 'C', fill=True)
        pdf.cell(19, 10, "Estado", 1, 0, 'C', fill=True)
        pdf.cell(19, 10, "Cod. Es", 1, 0, 'C', fill=True)
        pdf.cell(35, 10, "Tipo ID Est.", 1, 0, 'C', fill=True)
        pdf.cell(26, 10, "ID Estudiante", 1, 0, 'C', fill=True)
        pdf.cell(70, 10, "Nombre Estudiante", 1, 0, 'C', fill=True)
        pdf.cell(70, 10, "Nombre Institución", 1, 0, 'C', fill=True)
        pdf.cell(26, 10, "Tipo Institución", 1, 0, 'C', fill=True) #
        pdf.cell(30, 10, "Cod. Carrera", 1, 0, 'C', fill=True) #
        pdf.cell(21, 10, "Fec. Inicio", 1, 0, 'C', fill=True) #
        pdf.cell(21, 10, "Fec. Fin", 1, 0, 'C', fill=True) #
        pdf.cell(12, 10, "Horas", 1, 0, 'C', fill=True) #
        pdf.cell(20, 10, "Campo Esp.", 1, 0, 'C', fill=True) #
        pdf.cell(35, 10, "ID Tutor", 1, 0, 'C', fill=True) 
        pdf.cell(95, 10, "Nombre Tutor", 1, 1, 'C', fill=True)

        pdf.set_font("Roboto", size=10)
        # Datos de la tabla
        for row in dato:
            pdf.cell(19, 10, str(row[1]), 1, 0, 'C')  # Per. Acad.
            pdf.cell(19, 10, str(row[2]), 1, 0, 'C')  # Estado
            pdf.cell(19, 10, str(row[3]), 1, 0, 'C')  # Cod. Es
            pdf.cell(35, 10, str(row[4]), 1, 0, 'C')  # Tipo ID Est.
            pdf.cell(26, 10, str(row[5]), 1, 0, 'C')  # ID Estudiante
            pdf.cell(70, 10, str(row[6]), 1, 0, 'C')  # Nombre Estudiante
            pdf.cell(70, 10, str(row[7]), 1, 0, 'C')  # Nombre Institución
            pdf.cell(26, 10, str(row[8]), 1, 0, 'C')  # Tipo Institución
            pdf.cell(30, 10, str(row[9]), 1, 0, 'C')  # Cod Carrera
            pdf.cell(21, 10, str(row[10]), 1, 0, 'C')  # Fec. Inicio
            pdf.cell(21, 10, str(row[11]), 1, 0, 'C')  # Fec. Fin
            pdf.cell(12, 10, str(row[12]), 1, 0, 'C')  # Horas
            pdf.cell(20, 10, str(row[13]), 1, 0, 'C')  # Campo Esp.
            pdf.cell(35, 10, str(row[14]), 1, 0, 'C')  # ID Tutor
            pdf.cell(95, 10, str(row[15]), 1, 1, 'C')  # Nombre Tutor
                

        # save the pdf with name .pdf 
        pdf.output(self.ruta_save)
        
    def gene_reporte_informe(self, dato, periodo):

        font_path = os.path.abspath('source/fonts/Roboto-Light.ttf')


        pdf = FPDF(orientation='L')
        pdf.add_page()

        # Agregar fuente Roboto
        pdf.add_font('Roboto', '', font_path, uni=True)

        pdf.set_font("Roboto", size=12)

        pdf.set_font("Roboto", size=12)

        # Agregar imagen
        image_path = os.path.abspath('source/image/logito2.png')
        pdf.image(image_path, x=6, y=5, w=20,h=20)

        # Título
        pdf.cell(270, 10, txt="CARRERA DE TECNOLOGIAS DE INFORMACION", ln=True, align='C')
        pdf.cell(270, 10, txt="Informe Directores y Tutores de vinculacion con la sociedad", ln=True, align='C')
        pdf.cell(270, 10, txt="Periodo Academico "+ str(periodo), ln=True, align='C')
        pdf.cell(270, 10, txt="", ln=True, align='C')

        pdf.set_fill_color(221, 235, 247)  # Color de fondo #ddebf7
        pdf.set_font("Roboto", size=10, style='')
        pdf.cell(70, 10, "Tutor", 1, 0, 'C', fill=True)
        pdf.cell(15, 10, "Enero", 1, 0, 'C', fill=True)
        pdf.cell(15, 10, "Febrero", 1, 0, 'C', fill=True)
        pdf.cell(15, 10, "Marzo", 1, 0, 'C', fill=True)
        pdf.cell(15, 10, "Abril", 1, 0, 'C', fill=True)
        pdf.cell(15, 10, "Mayo", 1, 0, 'C', fill=True)
        pdf.cell(15, 10, "Junio", 1, 0, 'C', fill=True)
        pdf.cell(15, 10, "Julio", 1, 0, 'C', fill=True)
        pdf.cell(20, 10, "Agosto", 1, 0, 'C', fill=True)
        pdf.cell(20, 10, "Setiembre", 1, 0, 'C', fill=True) 
        pdf.cell(20, 10, "Octubre", 1, 0, 'C', fill=True) 
        pdf.cell(20, 10, "Noviembre", 1, 0, 'C', fill=True) 
        pdf.cell(20, 10, "Diciembre", 1, 1, 'C', fill=True) 

        pdf.set_font("Roboto", size=10)
        for row in dato:
            pdf.cell(70, 10, str(row[0]), 1, 0, 'L')
            for item in row[1:8]:
                pdf.cell(15, 10, str(item), 1, 0, 'C') 
            for item in row[8:]:
                pdf.cell(20, 10, str(item), 1, 0, 'C')
            pdf.ln()
        
        
        pdf.output(self.ruta_save)

    def gene_reporte_ficha(self, dato, periodo):
        font_path = os.path.abspath('source/fonts/Roboto-Light.ttf')

        pdf = FPDF(orientation='P')
        pdf.add_page()

        pdf.add_font('Roboto', '', font_path, uni=True)

        pdf.set_font("Roboto", size=12)

        # Agregar imagen
        image_path = os.path.abspath('source/image/logito2.png')
        pdf.image(image_path, x=6, y=5, w=20,h=20)

        # Título
        pdf.cell(200, 10, txt="CARRERA DE TECNOLOGIAS DE INFORMACION", ln=True, align='C')
        pdf.cell(200, 10, txt="Ficha de inscripciónes de vinculacion con la sociedad", ln=True, align='C')
        pdf.cell(200, 10, txt="Periodo Academico "+str(periodo), ln=True, align='C')
        pdf.cell(200, 10, txt="", ln=True, align='C')

        pdf.set_fill_color(221, 235, 247) 
        pdf.set_font("Roboto", size=10, style='')
        pdf.cell(100, 10, "Tutor", 1, 0, 'C', fill=True)
        pdf.cell(45, 10, "SI", 1, 0, 'C', fill=True)
        pdf.cell(45, 10, "NO", 1, 1, 'C', fill=True)

        pdf.set_font("Roboto", size=10)
        for row in dato:
            pdf.cell(100, 10, str(row[0]), 1, 0, 'L')
            for item in row[1:]:
                pdf.cell(45, 10, str(item), 1, 0, 'C') 
            pdf.ln()
        
        pdf.output(self.ruta_save)
        
    def gene_reporte_memorandum(self, dato, periodo):


        font_path = os.path.abspath('source/fonts/Roboto-Light.ttf')

        pdf = FPDF(orientation='P')
        pdf.add_page()


        pdf.add_font('Roboto', '', font_path, uni=True)

        pdf.set_font("Roboto", size=12)

        image_path = os.path.abspath('source/image/logito2.png')
        pdf.image(image_path, x=6, y=5, w=20,h=20)

        pdf.cell(200, 10, txt="CARRERA DE TECNOLOGIAS DE INFORMACION", ln=True, align='C')
        pdf.cell(200, 10, txt="Memorandum de monitoreo", ln=True, align='C')
        pdf.cell(200, 10, txt="Periodo Academico "+ str(periodo), ln=True, align='C')
        pdf.cell(200, 10, txt="", ln=True, align='C')

        pdf.set_fill_color(221, 235, 247) 
        pdf.set_font("Roboto", size=10, style='')
        pdf.cell(100, 10, "Tutor", 1, 0, 'C', fill=True)
        pdf.cell(45, 10, "SI", 1, 0, 'C', fill=True)
        pdf.cell(45, 10, "NO", 1, 1, 'C', fill=True)

        pdf.set_font("Roboto", size=10)
        for row in dato:
            pdf.cell(100, 10, str(row[0]), 1, 0, 'L')
            for item in row[1:]:
                pdf.cell(45, 10, str(item), 1, 0, 'C') 
            pdf.ln()

        pdf.output(self.ruta_save)