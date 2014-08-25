# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Proyecto3.ui'
#
# Created: Mon Aug 11 11:20:19 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(484, 466)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 461))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.dateEdit = QtGui.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.verticalLayout.addWidget(self.dateEdit)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.timeEdit = QtGui.QTimeEdit(self.verticalLayoutWidget)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.verticalLayout.addWidget(self.timeEdit)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox)
        self.btnGuardar = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnGuardar.setObjectName(_fromUtf8("btnGuardar"))
        self.verticalLayout.addWidget(self.btnGuardar)
        self.btnAtras = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnAtras.setObjectName(_fromUtf8("btnAtras"))
        self.verticalLayout.addWidget(self.btnAtras)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Ingrese el dia:", None))
        self.label_3.setText(_translate("Dialog", "Ingrese la hora:", None))
        self.label_4.setText(_translate("Dialog", "Ingrese la cantidad de horas:", None))
        self.label_5.setText(_translate("Dialog", "Ingrese el tipo de cancha:", None))
        self.comboBox.setItemText(0, _translate("Dialog", "Futbol", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Tenis", None))
        self.comboBox.setItemText(2, _translate("Dialog", "Basquet", None))
        self.btnGuardar.setText(_translate("Dialog", "Guardar cambios", None))
        self.btnAtras.setText(_translate("Dialog", "Atras", None))

