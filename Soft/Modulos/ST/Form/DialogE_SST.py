# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogE_SST.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_DE_S(object):
    def setupUi(self, DE_S):
        DE_S.setObjectName(_fromUtf8("DE_S"))
        DE_S.resize(300, 271)
        self.layoutWidget = QtGui.QWidget(DE_S)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 258, 242))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listado = QtGui.QListWidget(self.layoutWidget)
        self.listado.setObjectName(_fromUtf8("listado"))
        self.verticalLayout.addWidget(self.listado)
        self.btn_Actualizar = QtGui.QPushButton(self.layoutWidget)
        self.btn_Actualizar.setObjectName(_fromUtf8("btn_Actualizar"))
        self.verticalLayout.addWidget(self.btn_Actualizar)

        self.retranslateUi(DE_S)
        QtCore.QMetaObject.connectSlotsByName(DE_S)

    def retranslateUi(self, DE_S):
        DE_S.setWindowTitle(_translate("DE_S", "Entrega o Retiro de ST", None))
        self.label.setText(_translate("DE_S", "Seleccione numeros de serie", None))
        self.btn_Actualizar.setText(_translate("DE_S", "Actualizar", None))

