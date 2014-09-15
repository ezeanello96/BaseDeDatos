import sys
from PyQt4 import QtCore, QtGui
from Main import Main
from Ventana1 import Ventana1
from Ventana2 import Ventana2
from database import DataBase
from PyQt4.uic import *
import os
from PyQt4.QtGui import (QAbstractItemView, QApplication, QFileDialog,
                         QMainWindow, QTabWidget, QDialog)

bDia = 0
bAnio = 0
bMes = 0
bFecha = 0
bHora = 0
bTipo = 0

class Principal(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ventana = Main()
        self.ventana.setupUi(self)
        
        self.connect(self.ventana.pushButton_2, QtCore.SIGNAL('clicked()'), self.abrir_ventana_agregar)
        self.connect(self.ventana.pushButton, QtCore.SIGNAL('clicked()'), self.abrir_ventana_buscar)
        
    def abrir_ventana_agregar(self):
        self.w = Agregar()
        self.w.show()
            
    def abrir_ventana_buscar(self):
        bDia = str(self.ventana.comboDia.currentText())
        bAnio = str(self.ventana.comboAnio.currentText())
        bMes = str(self.ventana.comboMes.currentText())
        bFecha = bDia +"-"+ bMes +"-"+ bAnio
        bHora = str(self.ventana.comboHora.currentText())
        bTipo = str(self.ventana.comboBox.currentText())
        self.w = Buscar()
        self.w.show()    
 
class Agregar(QDialog):
    def __init__(self, parent=None):
         QtGui.QWidget.__init__(self, parent)
         self.ventana2 = Ventana2()
         self.ventana2.setupUi(self)
         self.connect(self.ventana2.btnGuardar, QtCore.SIGNAL('clicked()'), self.ingresar_datos)
         self.connect(self.ventana2.btnAtras, QtCore.SIGNAL('clicked()'), self.exit)
    
    def ingresar_datos(self): 
         nombre_cliente = str(self.ventana2.txtb_name.text()) 
         cant_horas = str(self.ventana2.lineEdit.text())
         dia = str(self.ventana2.comboDia.currentText())
         mes = str(self.ventana2.comboMes.currentText())
         anio = str(self.ventana2.comboAnio.currentText())
         fecha = dia +"-"+ mes +"-"+ anio
         hora = str(self.ventana2.comboHora.currentText())
         fecha_hora = str(fecha + hora)
         tipo_cancha = str(self.ventana2.comboBox.currentText())
         DataBase().agregar_turno(nombre_cliente, fecha_hora, cant_horas, tipo_cancha)
         print "Se cargaron los datos"
         DataBase().get_all
         
    def exit(self):
        self.close()

class Buscar(QDialog):
    def __init__(self, parent=None):
         QtGui.QWidget.__init__(self, parent)
         self.ventana3 = Ventana1()
         self.ventana3.setupUi(self)
         self.connect(self.ventana3.pushButton, QtCore.SIGNAL('clicked()'), self.exit)
         

    def exit(self):
         self.close()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ventana = Principal()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()