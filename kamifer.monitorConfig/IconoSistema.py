from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QMenu, QPushButton, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout)
from PyQt5.QtCore import *
from Constantes import Const

class IconoSistema:

    def __init__(self, parent=None):
        self.iniciar(parent=parent)

    def iniciar(self, parent):
        self.icon = QIcon(Const.ICONO)
        self.tray = QSystemTrayIcon(parent=parent)
        self.tray.setIcon(self.icon)
        self.iconoSalir = QIcon.fromTheme("exit")

        self.agregarMenu()

        self.tray.show()

    def agregarMenu(self):
        menu = QMenu()
        #ultimaAlertaAction = menu.addAction(self.icon, 'Ver &Ultima alerta')
        #verAlertasAction = menu.addAction(self.iconoLista, "&Ver Alertas")
        menu.addSeparator()
        exitAction = menu.addAction(self.iconoSalir, "&Salir")

        exitAction.triggered.connect(QCoreApplication.instance().quit)
        #verAlertasAction.triggered.connect(lambda: self.verVentanaAlertas())
        #ultimaAlertaAction.triggered.connect(lambda: self.verUltimaAlerta())

        self.tray.activated.connect(self.onTrayIconActivated)

        self.tray.setVisible(True)

        self.tray.setContextMenu(menu)
        #self.showMessage('Aplicacion iniciada')
        Const.SYSTRAY = self

    def onTrayIconActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            # ignorar
            pass
        elif reason == QSystemTrayIcon.DoubleClick:
            #self.verVentanaAlertas()
            pass