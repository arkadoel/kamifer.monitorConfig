import sys
import os

if sys.version.__contains__('2.'):
    print('Python 2.x, no se puede ejecutar, se necesita python3')
elif sys.version.__contains__('3.'):
    print('Python 3.x, correcto')
    from PyQt5 import QtGui, QtCore
    #from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from Constantes import Const
    import IconoSistema
    from Logica import Logica


class Ventana(QWidget):
    def __init__(self, parent=None):
        super(Ventana, self).__init__(parent)

        self.monitores = Logica().detectar_monitores()
        self.setWindowIcon(QIcon(Const.ICONO))
        print(self.monitores)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Monitor Config')
        self.initGui()
        self.show()

    def initGui(self):
        self.gridFondo = QGridLayout()
        fila = 0

        brillos = Logica().get_actual_brightness()

        for monitor in self.monitores:
            if(brillos.__contains__(monitor)):
                lbl = QLabel(monitor, self)
                self.gridFondo.addWidget(lbl, fila, 0)

                brilloActual =  int(float(brillos[monitor]) * 100)
                print(brilloActual)

                sld = QSlider(QtCore.Qt.Horizontal)
                sld.setObjectName(str(fila))
                sld.setMaximum(100)
                sld.setMinimum(1)
                sld.setFocusPolicy(QtCore.Qt.NoFocus)
                sld.setGeometry(30, 40, 100, 30)
                sld.setValue(brilloActual)
                sld.valueChanged.connect( lambda value, monitor=str(monitor): self.changeValue(value, monitor))
                self.gridFondo.addWidget(sld, fila, 1)
                fila = fila + 1

        self.setLayout(self.gridFondo)

    def changeValue(self, value, monitor ):
        brillo = value/100
        print(brillo)
        comando = 'xrandr --output ' + monitor  + ' --brightness ' + str( brillo)
        print(comando)
        os.system(comando)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Logica().detectar_monitores()
    Logica().get_actual_brightness()
    IconoSistema.IconoSistema(app)
    win = Ventana()
    app.exec_()