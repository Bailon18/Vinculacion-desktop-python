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

    def header(self):
        self.set_font('Arial', 'B', 20)
        self.set_text_color(58, 79, 80)
        self.cell(0, 10, 'Detalle de Vinculación', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(58, 79, 80)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def add_card(self, title, body_dict):
        self.set_fill_color(220, 220, 220)
        self.set_text_color(58, 79, 80)
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L', fill=True)
        self.ln(6)
        
        self.set_font('Arial', '', 12)
        key_color = (80, 80, 80)
        value_color = (58, 79, 80)
        
        key_width = 45
        value_width = 140
        
        for key, value in body_dict.items():
            self.set_text_color(*key_color)
            self.cell(key_width, 2, f'{key}:', 0, 0, 'L')
            
            self.set_text_color(*value_color)
            self.multi_cell(value_width, 4, value, 0, 'L')
            
            self.ln(8)
      
    
    def add_student_table(self, header, data):
        self.set_fill_color(58, 79, 80)
        self.set_text_color(255, 255, 255)
        self.set_font('Arial', 'B', 12)


        col_widths = [0] * len(header)
        

        for i, col in enumerate(header):
            col_widths[i] = max(col_widths[i], self.get_string_width(col) + 4)

        # Update column widths with data widths
        for row in data:
            for i, item in enumerate(row):
                col_widths[i] = max(col_widths[i], self.get_string_width(str(item)) + 4) 

    
        total_width = self.w - 2 * self.l_margin

        scaling_factor = total_width / sum(col_widths)

        col_widths = [width * scaling_factor for width in col_widths]

        for i, col in enumerate(header):
            self.cell(col_widths[i], 10, col, 1, 0, 'C', True)
        self.ln()

        self.set_font('Arial', '', 12)
        self.set_text_color(58, 79, 80)
        self.set_fill_color(245, 245, 245)
        
        # Print the data
        fill = False
        for row in data:
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, str(item), 1, 0, 'C', fill)
            self.ln()
            fill = not fill
            
    def add_logo(self, logo_path):
        self.image(logo_path, x=8, y=2, w=25)




# VENTANA MUESTRA USUARIO
class FormRepoImforme(QDialog):

    def __init__(self, vinculacion_datos = [], datos = [], modo = '', periodo = ''):
        super(FormRepoImforme, self).__init__()

        # clase principal
        self.raizReptCargar = Ui_VenCargaReportes()
        self.raizReptCargar.setupUi(self)

        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.contador=0

        self.vinculacion_datos = vinculacion_datos
        self.datos = datos
        self.modo = modo
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
            self.raiz_inicia_rep.gen_mandar_datos(self.vinculacion_datos, self.datos, self.modo, self.periodo)

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
       
    def gen_mandar_datos(self, vinculacion_datos, datos, modo, periodo):

        fecha_data_act = QDate.currentDate().toString("dd-MM-yyyy")
        
        print('modo ', modo)

        nombre_archivo = ''
        if(modo == "vinculacion"):
            nombre_archivo = f'DetalleVinculacion_{fecha_data_act}'
        elif( modo == "estudiantes"):
            nombre_archivo = f'Reporte_Vinculacion_estudiantes_{fecha_data_act}'
        elif( modo == "informe"):
            nombre_archivo = f'Reporte_tutores_informe_{fecha_data_act}'
        elif( modo == "ficha"):
            nombre_archivo = f'Reporte_tutores_fichas_{fecha_data_act}'
        else:
            nombre_archivo = f'Reporte_tutores_memorandum_{fecha_data_act}'
        
        self.ruta_save = self.guardarArchivo(nombre_archivo)
        if(self.ruta_save==''):return
        
        if(modo == "vinculacion"):
            self.generar_detalle_vinculacion(vinculacion_datos, datos)
        elif( modo == "estudiantes"):
            self.gene_reporte_estudiantes(datos[0])
        elif( modo == "informe"):
            self.gene_reporte_informe(datos, periodo)
        elif( modo == "ficha"):
            self.gene_reporte_ficha(datos, periodo)
        else:
            self.gene_reporte_memorandum(datos, periodo)
 
    
        webbrowser.open(self.ruta_save, new=2)
         
         
    def gene_reporte_estudiantes(self,data):
 

        page_width = 300  
        page_height = 538 

        # Cabeceras de las columnas
        headers = ["Per. Acad.", "Estado", "Cod. Es", "Tipo ID Est.", "ID Estudiante",
                "Nombre Estudiante", "Nombre Institución", "Tipo Institución",
                "Cod. Carrera", "Fec. Inicio", "Fec. Fin", "Horas", "Campo Esp.",
                "ID Tutor", "Nombre Tutor"]


        col_widths = [len(header) * 4 for header in headers] 

        for row in data:
            for i, item in enumerate(row):
                if i < len(col_widths): 
                    col_widths[i] = max(col_widths[i], len(str(item)) * 4) 


        total_table_width = sum(col_widths)

    
        if total_table_width > page_width:
            page_width = total_table_width + 20  

        pdf = FPDF(orientation='L', unit='mm', format=(page_height, page_width))
        pdf.add_page()

        # Configurar fuente y tamaño
        pdf.set_font("Arial", size=12)

        # Títulos
        pdf.cell(page_width, 10, txt="UNIVERSIDAD ESTATAL DEL SUR DE MANABÍ", ln=True, align='C')
        pdf.cell(page_width, 8, txt="Facultad de Ciencias Técnicas", ln=True, align='C')
        pdf.cell(page_width, 8, txt="Carrera de Tecnologías de la Información", ln=True, align='C')
        pdf.cell(page_width, 8, txt="Reporte de Vinculación Estudiante", ln=True, align='C')
        pdf.cell(page_width, 10, txt="", ln=True, align='C')

      
        logo_width = 30  
        title_width = pdf.get_string_width("Reporte de Vinculación Estudiante")  
        left_logo_x = (page_width - (title_width + 40) - logo_width) / 2 
        right_logo_x = left_logo_x + (title_width + 60)  

        # Agregar imágenes
        image_path = os.path.abspath('source/image/logito.png')
        image_path2 = os.path.abspath('source/image/logito2.png')
        pdf.image(image_path, x=left_logo_x, y=8, w=logo_width, h=30)
        pdf.image(image_path2, x=right_logo_x, y=8, w=logo_width, h=30)

        # Cabecera de la tabla
        pdf.set_fill_color(63, 87, 88)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", size=10)

        for i, header in enumerate(headers):
            pdf.cell(col_widths[i], 10, header, 1, 0, 'C', fill=True)
        pdf.ln()

        # Datos de la tabla
        pdf.set_fill_color(255, 255, 255)
        pdf.set_text_color(0, 0, 0)
        for row in data:
            for i, item in enumerate(row):
                if i < len(col_widths):  # Verificar si el índice está dentro de los límites de col_widths
                    pdf.cell(col_widths[i], 10, str(item), 1, 0, 'C')
            pdf.ln()

        pdf.ln(6)

        # Líneas finales centradas
        pdf.set_font("Arial", size=10)
        pdf.cell(page_width / 2, 10, "Elaborado por:", 0, 0, 'C')
        pdf.cell(page_width / 2, 10, "Aprobado por:", 0, 1, 'C')

        pdf.ln(8)

        pdf.cell(page_width / 2, 10, "___________________________________", 0, 0, 'C')
        pdf.cell(page_width / 2, 10, "___________________________________", 0, 1, 'C')

        pdf.cell(page_width / 2, 4, "Ing. Edwin Antonio Mero Lino, Mg.", 0, 0, 'C')
        pdf.cell(page_width / 2, 4, "Ing. Holger Delegado Lucas, PhD.", 0, 1, 'C')
        # Guardar el PDF con el nombre especificado
        pdf.output(self.ruta_save)
        

    def gene_reporte_informe(self, dato, periodo):
        
        pdf = FPDF(orientation='L')
        pdf.add_page()

        # Agregar imágenes
        image_path = os.path.abspath('source/image/logito.png')
        image_path2 = os.path.abspath('source/image/logito2.png')
        pdf.image(image_path, x=60, y=8, w=25, h=25)
        pdf.image(image_path2, x=200, y=8, w=25, h=25)

        pdf.set_font("Arial", size=12)

        pdf.cell(270, 10, txt="UNIVERSIDAD ESTATAL DEL SUR DE MANABÍ", ln=True, align='C')
        pdf.cell(270, 8, txt="Facultad de Ciencias Técnicas", ln=True, align='C')
        pdf.cell(270, 8, txt="Carrera de Tecnologias de la información", ln=True, align='C')
        pdf.cell(270, 8, txt="Informe Directores y Tutores de vinculacion con la sociedad", ln=True, align='C')
        pdf.cell(270, 10, txt="Periodo Academico "+ str(periodo), ln=True, align='C')
        pdf.cell(270, 20, txt="", ln=True, align='C')


        pdf.set_fill_color(63, 87, 88) 
        pdf.set_text_color(255, 255, 255) 
        pdf.set_font("Arial", size=10, style='B') 

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

        pdf.set_fill_color(255, 255, 255)  
        pdf.set_text_color(0, 0, 0) 
        pdf.set_font("Arial", size=10)

        # Datos de la tabla
        for row in dato:
            pdf.cell(70, 10, str(row[0]), 1, 0, 'L')
            for item in row[1:8]:
                if item == "NO":
                    pdf.set_text_color(255, 0, 0)  
                elif item == "SI":
                    pdf.set_text_color(0, 128, 0)  
                pdf.cell(15, 10, str(item), 1, 0, 'C') 
                pdf.set_text_color(0, 0, 0)  
            for item in row[8:]:
                if item == "NO":
                    pdf.set_text_color(255, 0, 0) 
                elif item == "SI":
                    pdf.set_text_color(0, 128, 0) 
                pdf.cell(20, 10, str(item), 1, 0, 'C')
                pdf.set_text_color(0, 0, 0)  
            pdf.ln()

        pdf.ln(10)


        # Pie de página
        pdf.set_font("Arial", size=10)
        pdf.cell(180, 10, "Elaborado por:", 0, 0, 'C')
        pdf.cell(10, 10, "Aprobado por:", 0, 1, 'C')
        
        pdf.ln(8)

        pdf.cell(180, 10, "___________________________________", 0, 0, 'C')
        pdf.cell(10, 10, "___________________________________", 0, 1, 'C')


        pdf.set_font("Arial", size=10)
        pdf.cell(180, 4, "Ing. Edwin Antonio Mero Lino, Mg.", 0, 0, 'C')
        pdf.cell(10, 4, "Ing. Holger Delegado Lucas, PhD.", 0, 1, 'C')


        pdf.set_font("Arial", size=10, style='B')
        pdf.cell(180, 4, "Responsable de vinculación carrera de TI", 0, 0, 'C')
        pdf.cell(10, 4, "Coordinador carrera de TI", 0, 1, 'C')


        pdf.output(self.ruta_save)


    def gene_reporte_ficha(self, dato, periodo):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        pdf.set_font("Arial", size=12)

        # Agregar imágenes
        image_path = os.path.abspath('source/image/logito.png')
        image_path2 = os.path.abspath('source/image/logito2.png')
        pdf.image(image_path, x=32, y=8, w=25, h=25)
        pdf.image(image_path2, x=165, y=8, w=25, h=25)

        pdf.cell(200, 10, txt="UNIVERSIDAD ESTATAL DEL SUR DE MANABÍ", ln=True, align='C')
        pdf.cell(200, 8, txt="Facultad de Ciencias Técnicas", ln=True, align='C')
        pdf.cell(200, 8, txt="Carrera de Tecnologias de la información", ln=True, align='C')
        pdf.cell(200, 8, txt="Ficha de inscripciónes de vinculacion con la sociedad", ln=True, align='C')
        pdf.cell(200, 10, txt="Periodo Academico " + str(periodo), ln=True, align='C')
        pdf.cell(200, 20, txt="", ln=True, align='C')

        # Ancho de la página (A4) en mm menos los márgenes
        page_width = pdf.w - 2 * pdf.l_margin
        col_width_tutor = page_width * 0.7  
        col_width_si_no = page_width * 0.15  

        # Configurar color de fondo para la cabecera de la tabla
        pdf.set_fill_color(63, 87, 88)  
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", size=10, style='B') 

        # Cabecera de la tabla
        pdf.cell(col_width_tutor, 10, "Tutor", 1, 0, 'C', fill=True)
        pdf.cell(col_width_si_no, 10, "SI", 1, 0, 'C', fill=True)
        pdf.cell(col_width_si_no, 10, "NO", 1, 1, 'C', fill=True)

        pdf.set_fill_color(255, 255, 255)  
        pdf.set_text_color(0, 0, 0)  
        pdf.set_font("Arial", size=10)

        # Datos de la tabla
        for row in dato:
            pdf.cell(col_width_tutor, 10, str(row[0]), 1, 0, 'L')  
            for item in row[1:3]: 
                if item == "SI":
                    pdf.set_text_color(0, 128, 0) 
                elif item == "NO":
                    pdf.set_text_color(255, 0, 0)
                pdf.cell(col_width_si_no, 10, str(item), 1, 0, 'C')
                pdf.set_text_color(0, 0, 0)  
            pdf.ln()

        pdf.ln(10)

        # Pie de página
        pdf.set_font("Arial", size=10)
        pdf.cell(100, 10, "Elaborado por:", 0, 0, 'C')
        pdf.cell(100, 10, "Aprobado por:", 0, 1, 'C')

        pdf.ln(8)

        pdf.cell(100, 10, "___________________________________", 0, 0, 'C')
        pdf.cell(100, 10, "___________________________________", 0, 1, 'C')

        pdf.set_font("Arial", size=10)
        pdf.cell(100, 4, "Ing. Edwin Antonio Mero Lino, Mg.", 0, 0, 'C')
        pdf.cell(100, 4, "Ing. Holger Delegado Lucas, PhD.", 0, 1, 'C')


        pdf.set_font("Arial", size=10, style='B')
        pdf.cell(100, 4, "Responsable de vinculación carrera de TI", 0, 0, 'C')
        pdf.cell(100, 4, "Coordinador carrera de TI", 0, 1, 'C')

        pdf.output(self.ruta_save)

    def gene_reporte_memorandum(self, dato, periodo):
        
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Agregar imágenes
        image_path = os.path.abspath('source/image/logito.png')
        image_path2 = os.path.abspath('source/image/logito2.png')
        pdf.image(image_path, x=32, y=8, w=25, h=25)
        pdf.image(image_path2, x=160, y=8, w=25, h=25)

        pdf.cell(200, 10, txt="UNIVERSIDAD ESTATAL DEL SUR DE MANABÍ", ln=True, align='C')
        pdf.cell(200, 8, txt="Facultad de Ciencias Técnicas", ln=True, align='C')
        pdf.cell(200, 8, txt="Carrera de Tecnologias de la información", ln=True, align='C')
        pdf.cell(200, 8, txt="Memorandum de monitoreo", ln=True, align='C')
        pdf.cell(200, 8, txt="Periodo Academico " + str(periodo), ln=True, align='C')
        pdf.cell(200, 8, txt="", ln=True, align='C')

        # Ancho de la página (A4) en mm menos los márgenes
        page_width = pdf.w - 2 * pdf.l_margin
        col_width_tutor = page_width * 0.7  # 70% para la columna de tutor
        col_width_si_no = page_width * 0.15  # 15% para cada columna de SI y NO

        # Configurar color de fondo para la cabecera de la tabla
        pdf.set_fill_color(63, 87, 88)  # Color #3f5758 en RGB
        pdf.set_text_color(255, 255, 255)  # Color de texto blanco
        pdf.set_font("Arial", size=10, style='B')  # Fuente en negrita

        # Cabecera de la tabla
        pdf.cell(col_width_tutor, 10, "Tutor", 1, 0, 'C', fill=True)
        pdf.cell(col_width_si_no, 10, "SI", 1, 0, 'C', fill=True)
        pdf.cell(col_width_si_no, 10, "NO", 1, 1, 'C', fill=True)

        pdf.set_fill_color(255, 255, 255)  # Restaurar color de fondo blanco para el contenido
        pdf.set_text_color(0, 0, 0)  # Restaurar color de texto negro
        pdf.set_font("Arial", size=10)

        # Datos de la tabla
        for row in dato:
            pdf.cell(col_width_tutor, 10, str(row[0]), 1, 0, 'L')  # Columna Tutor
            for item in row[1:3]:  # Columnas SI y NO
                if item == "SI":
                    pdf.set_text_color(0, 128, 0)  # Verde para SI
                elif item == "NO":
                    pdf.set_text_color(255, 0, 0)  # Rojo para NO
                pdf.cell(col_width_si_no, 10, str(item), 1, 0, 'C')
                pdf.set_text_color(0, 0, 0)  # Restaurar color de texto negro después de cada celda
            pdf.ln()

        pdf.ln(10)

        # Pie de página
        pdf.set_font("Arial", size=10)
        pdf.cell(95, 10, "Elaborado por:", 0, 0, 'C')
        pdf.cell(95, 10, "Aprobado por:", 0, 1, 'C')
        
        pdf.ln(8)

        pdf.cell(95, 10, "___________________________________", 0, 0, 'C')
        pdf.cell(95, 10, "___________________________________", 0, 1, 'C')
        
        # Nombres en negrita
        
        pdf.cell(95, 4, "Ing. Edwin Antonio Mero Lino, Mg.", 0, 0, 'C')
        pdf.cell(95, 4, "Ing. Holger Delegado Lucas, PhD.", 0, 1, 'C')

        # Títulos en estilo normal
        pdf.set_font("Arial", size=10, style='B')
        pdf.cell(95, 4, "Responsable de vinculación carrera de TI", 0, 0, 'C')
        pdf.cell(95, 4, "Coordinador carrera de TI", 0, 1, 'C')

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
        

        proyecto_nombre = vinculacion['proyecto_nombre']
        if len(proyecto_nombre) > 50:  # Adjust length threshold as needed
            proyecto_nombre = proyecto_nombre[:50] + '\n' + proyecto_nombre[50:]
        proyecto_text = {
            'Nombre del Proyecto': proyecto_nombre
        }
        
        pdf.add_card('Detalle del Proyecto', proyecto_text)
        
        # Información de Estudiantes
        header = ['Cédula', 'Nombre', 'Estado', 'Horas']
        data = estudiantes_datos
        
        pdf.chapter_title('Estudiantes Vinculados')
        pdf.add_student_table(header, data)
        
        pdf.output(self.ruta_save)









