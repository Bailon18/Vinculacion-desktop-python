import os

def add_font_app(ruta, extension):
    '''extension: ttf, otf '''
    try:
        from PySide2.QtGui import QFontDatabase
        import os

        for font in os.listdir(ruta):
            if(font.endswith(extension)):
                font_set = os.path.join(ruta, font)
                QFontDatabase.addApplicationFont(font_set)
    except:
        pass

# Obteniendo la ruta del directorio actual del script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Concatenando la ruta del directorio de fuentes al directorio actual
font_directory = os.path.join(current_directory, 'source', 'fonts')

print(font_directory)

# Intenta cargar las fuentes desde el directorio calculado
try:
    add_font_app(font_directory, 'ttf')
except Exception as e:
    print(f"Error al cargar fuentes: {e}")
