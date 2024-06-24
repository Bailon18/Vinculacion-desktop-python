from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 20)
        self.set_text_color(58, 79, 80)  
        self.cell(0, 10, 'Detalle de Vinculación', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
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
            self.multi_cell(value_width, 2, value, 0, 'L')
            
            self.ln(8)

    def add_student_table(self, header, data):
        self.set_fill_color(58, 79, 80)  
        self.set_text_color(255, 255, 255)  
        self.set_font('Arial', 'B', 12)
        
        # Header
        cell_width = 45
        for col in header:
            self.cell(cell_width, 10, col, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Arial', '', 12)
        self.set_text_color(58, 79, 80)  
        self.set_fill_color(245, 245, 245) 
        
        # Data
        fill = False
        for row in data:
            for item in row:
                self.cell(cell_width, 10, str(item), 1, 0, 'C', fill)
            self.ln()
            fill = not fill

def generar_pdf(vinculacion_datos, estudiantes_datos, filename):
    pdf = PDF()
    pdf.add_page()
    
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
    
    pdf.output(filename)
    print(f"PDF guardado como {filename}")

# Datos hipotéticos para la vinculación
vinculacion_datos = [{
    'fecha_inicio': '2023-01-15',
    'codigo_ies': 'ABC123',
    'campo_especifico': 'Ingeniería de Sistemas',
    'periodo_academico': '2023A',
    'institucion_nombre': 'Universidad XYZ',
    'tutor_nombre': 'Juan Pérez',
    'tutor_identificacion': '1234567890',
    'tutor_telefono': '0999999999',
    'tutor_correo': 'juan.perez@example.com',
    'proyecto_nombre': 'Proyecto de Innovación'
}]

# Datos hipotéticos para los estudiantes
estudiantes_datos = [
    ['9876543210', 'Carlos García', 'Pendiente', 20],
    ['8765432109', 'Ana Martínez', 'En Proceso', 40],
    ['7654321098', 'Luis Rodríguez', 'Culminado', 60]
]

filename = 'Detalle_Vinculacion_Moderno.pdf'
generar_pdf(vinculacion_datos, estudiantes_datos, filename)
