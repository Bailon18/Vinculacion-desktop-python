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

class PDF(FPDF):
    
    def __init__(self):
        super().__init__()
        # Definir la ruta absoluta del directorio de fuentes
        self.font_dir = os.path.abspath('source/fonts/')
        
        # Registrar todas las fuentes Roboto
        self.register_roboto_fonts()

    def register_roboto_fonts(self):
        self.add_font('Roboto-Light', '', os.path.join(self.font_dir, 'Roboto-Light.ttf'), uni=True)
        self.add_font('Roboto-Regular', '', os.path.join(self.font_dir, 'Roboto-Regular.ttf'), uni=True)
        self.add_font('Roboto-Bold', '', os.path.join(self.font_dir, 'Roboto-Bold.ttf'), uni=True)

    def header(self):
        self.set_font('Roboto-Bold', '', 20)  
        self.set_text_color(58, 79, 80)  
        self.cell(0, 10, 'Detalle de Vinculación', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Roboto-Regular', '', 8) 
        self.set_text_color(128) 
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Roboto-Bold', '', 16)  
        self.set_text_color(58, 79, 80)  
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def add_card(self, title, body_dict):
        self.set_fill_color(220, 220, 220)  
        self.set_text_color(58, 79, 80)  
        self.set_font('Roboto-Bold', '', 14) 
        self.cell(0, 10, title, 0, 1, 'L', fill=True)
        self.ln(6)
        
        self.set_font('Roboto-Regular', '', 12)  
        key_color = (80, 80, 80)  
        value_color = (58, 79, 80)  
        
        key_width = 45
        value_width = 140
        
        for key, value in body_dict.items():
            self.set_text_color(*key_color)
            self.cell(key_width, 2, f'{key}:', 0, 0, 'L')
            
            self.set_text_color(*value_color)
            self.multi_cell(value_width, 2, value, 0, 'L')
            
            self.ln(8)
            
    def add_student_table(self, header, data):
        self.set_fill_color(58, 79, 80)  
        self.set_text_color(255, 255, 255)  
        self.set_font('Roboto-Bold', '', 12)  
        
        # Header
        cell_width = 45
        for col in header:
            self.cell(cell_width, 10, col, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Roboto-Regular', '', 12) 
        self.set_text_color(58, 79, 80)  
        self.set_fill_color(245, 245, 245) 
        
        # Data
        fill = False
        for row in data:
            for item in row:
                self.cell(cell_width, 10, str(item), 1, 0, 'C', fill)
            self.ln()
            fill = not fill
            
    def add_logo(self, logo_path):
            self.image(logo_path, x=8, y=2, w=25)

# VENTANA MUESTRA USUARIO
class FormRepoImforme(QDialog):

    def __init__(self, vinculacion_datos, estudiantes_datos):
        super(FormRepoImforme, self).__init__()

        # clase principal
        self.raizReptCargar = Ui_VenCargaReportes()
        self.raizReptCargar.setupUi(self)

        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.contador=0

        self.vinculacion_datos = vinculacion_datos
        self.estudiantes_datos = estudiantes_datos

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
            self.raiz_inicia_rep.gen_mandar_datos(self,self.vinculacion_datos, self.estudiantes_datos)

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
       
    def gen_mandar_datos(self, parent, vinculacion_datos, estudiantes_datos):


        # fecha de generacion del informe
        fecha_data_act = QDate.currentDate().toString("dd-MM-yyyy")

   
        # nombre del archivo
        nombre_archivo = f'DetalleVinculacion_{fecha_data_act}'

        self.ruta_save = self.guardarArchivo(nombre_archivo)
        if(self.ruta_save==''):return
        
        
        # if(tipo == "estudiantes"):
        #     self.gene_reporte_estudiantes(datos)  
        # elif( tipo == "informe"):
        #     self.gene_reporte_informe(datos, periodo)
        # elif( tipo == "ficha"):
        #     self.gene_reporte_ficha(datos, periodo)
        # else:
        #     self.gene_reporte_memorandum(datos, periodo)
        
        
        self.generar_detalle_vinculacion(vinculacion_datos, estudiantes_datos)
            
            
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
        
    def generar_detalle_vinculacion(self, vinculacion_datos, estudiantes_datos):
        
        
        pdf = PDF()
        pdf.add_page()
        
        image_path = os.path.abspath('source/image/logito2.png')
        pdf.add_logo(image_path)
        
        # Información de Vinculación
        vinculacion = vinculacion_datos[0]
        vinculacion_text = {
            'Fecha de Inicio': vinculacion['fecha_inicio'],
            'Código IES': vinculacion['codigo_ies'],
            'Campo Específico': vinculacion['campo_especifico'],
            'Periodo Académico': vinculacion['periodo_academico'],
            'Institución': vinculacion['institucion_nombre']
        }
        
        pdf.add_card('Detalle de Vinculación', vinculacion_text)
        
        # Información del Tutor
        tutor_text = {
            'Nombre del Tutor': vinculacion['tutor_nombre'],
            'Cédula del Tutor': vinculacion['tutor_identificacion'],
            'Teléfono del Tutor': vinculacion['tutor_telefono'],
            'Correo del Tutor': vinculacion['tutor_correo']
        }
        
        pdf.add_card('Detalle del Tutor', tutor_text)
        
        # Información del Proyecto
        proyecto_text = {
            'Nombre del Proyecto': vinculacion['proyecto_nombre']
        }
        
        pdf.add_card('Detalle del Proyecto', proyecto_text)
        
        # Información de Estudiantes
        header = ['Cédula', 'Nombre', 'Estado', 'Horas']
        data = estudiantes_datos
        
        pdf.chapter_title('Estudiantes Vinculados')
        pdf.add_student_table(header, data)
        
        pdf.output(self.ruta_save)