
from PySide2.QtCore import (QPoint, QEasingCurve, QParallelAnimationGroup, QPropertyAnimation, 
                            QAbstractAnimation)

from PySide2 import QtGui , QtWidgets

class Clase_EfectoSlider:
    
    def __init__(self, miStack, dicobjet, transicion=1):
        
        self.miStack = miStack

        # control de transicion /*/*/*/*/*/*/
        'indica si hay alguna transcicion ejecutandose'
        self.ctrl_animacion = False

        self.dicobjet = dicobjet # {index : btn_objeto}
        self.transicion = transicion # 1v 2h


        self.bloqueado = True
    
    def establecer_bloqueo(self, booleano):
        self.bloqueado = booleano

    def establecer_index(self, index):
        self.bloeuqarBotones(index)
        self.miStack.setCurrentIndex(index)

    def transicion_stacked(self, index_final, indexSiguientes = []):
        """ Animacion de cambio del StackedWidget """

        # obtener index actual /*/*/*/*/*/*/
        index_inicio = self.miStack.currentIndex()

        # condicionamiento /*/*/*/*/*/*/
        if(self.ctrl_animacion)or(index_final==index_inicio):
            return

        # control de transicion (activo) /*/*/*/*/*/*/
        self.ctrl_animacion = True

        self.bloeuqarBotones(index_final)

        # index /*/*/*/*/*/*/
        self.index_inicio = index_inicio
        self.index_final = index_final

        # tamaño de widget para transciciones /*/*/*/*/*/*/
        ancho_stk = self.miStack.width()
        alto_stk = self.miStack.height()

        # efecto de avance y retroceso /*/*/*/*/*/*/
        if(self.index_inicio in indexSiguientes):
            if(self.transicion==1):
                offsetx = 0; offsety = -alto_stk
            else:
                offsetx = ancho_stk; offsety = 0

        else:
            if(self.transicion==1):
                offsetx = 0; offsety = alto_stk
            else:
                offsetx = -ancho_stk; offsety = 0

        # configuraciones /*/*/*/*/*/*/
        velocidad_tansicion = 500
        efecto_transicion = QEasingCurve.OutExpo # OutCubic | InOutQuint | OutExpo
        self.miStack.widget(self.index_final).resize(ancho_stk, alto_stk)

        
        # posicionamiento del widget /*/*/*/*/*/*/
        self.punto_actual = self.miStack.widget(self.index_inicio).pos()
        self.punto_final = self.miStack.widget(self.index_final).pos()

        # mostrar el siguiente widged en la transicion /*/*/*/*/*/*/
        self.miStack.widget(self.index_final).show()

        # obtener punto de referencia /*/*/*/*/*/*/
        offset = QPoint(offsetx, offsety)

        # animacion de transcicion de widgets /*/*/*/*/*/*/
        animacion_stack = QParallelAnimationGroup(self.miStack, finished=self.realizarAnimacion)

        animacion_inicio = QPropertyAnimation(
            self.miStack.widget(self.index_inicio),b"pos",
            duration=velocidad_tansicion, easingCurve=efecto_transicion,
            startValue=self.punto_actual,
            endValue=self.punto_final - offset)

        animacion_final = QPropertyAnimation(
            self.miStack.widget(self.index_final),b"pos",
            duration=velocidad_tansicion, easingCurve=efecto_transicion,
            startValue=self.punto_actual + offset,
            endValue=self.punto_final)

        animacion_stack.addAnimation(animacion_inicio)
        animacion_stack.addAnimation(animacion_final)

        # iniciar efecto /*/*/*/*/*/*/
        animacion_stack.start(QAbstractAnimation.DeleteWhenStopped)

    def realizarAnimacion(self):
        self.miStack.setCurrentIndex(self.index_final) # asignar index
        self.miStack.widget(self.index_inicio).hide()
        self.miStack.widget(self.index_inicio).move(self.punto_actual)

        # control de transicion (desactivado) /*/*/*/*/*/*/
        self.ctrl_animacion = False


    def bloeuqarBotones(self, index_establecer):

        if(self.bloqueado):
            for btns in self.dicobjet.values():
                btns.setEnabled(True)

            self.dicobjet[index_establecer].setEnabled(False)


# CLASE DE OPACIDAD
class Clase_Opacidad(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Clase_Opacidad, self).__init__(parent)

    # evento de QPainter
    def paintEvent(self, event):
        
        qp = QtGui.QPainter()
        qp.begin(self)
        # color (r,g,b,a) tomar en cuenta que en a→255 es el valor maximo de opacidad
        qp.setBrush(QtGui.QColor(0, 0, 0, 120))
        # poner el efecto al tamaño que se le aplico a esta clase
        # nota: -1 y +1 es para quitar los bordes negros (normalemente iria 0)
        qp.drawRect(-1, -1, self.size().width()+1, self.size().height()+1)
        qp.end()
