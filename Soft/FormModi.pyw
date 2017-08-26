# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormModi.ui'
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

class Ui_DialogModi(object):
    def setupUi(self, DialogModi):
        DialogModi.setObjectName(_fromUtf8("DialogModi"))
        DialogModi.resize(387, 302)
        self.groupBox = QtGui.QGroupBox(DialogModi)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 361, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 341, 221))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.Edit_AyN = QtGui.QLineEdit(self.layoutWidget)
        self.Edit_AyN.setObjectName(_fromUtf8("Edit_AyN"))
        self.horizontalLayout_8.addWidget(self.Edit_AyN)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_7.addWidget(self.label_3)
        self.Edit_Dom = QtGui.QLineEdit(self.layoutWidget)
        self.Edit_Dom.setObjectName(_fromUtf8("Edit_Dom"))
        self.horizontalLayout_7.addWidget(self.Edit_Dom)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.Edit_Tel = QtGui.QLineEdit(self.layoutWidget)
        self.Edit_Tel.setObjectName(_fromUtf8("Edit_Tel"))
        self.horizontalLayout_6.addWidget(self.Edit_Tel)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.Edit_Marca = QtGui.QLineEdit(self.layoutWidget)
        self.Edit_Marca.setObjectName(_fromUtf8("Edit_Marca"))
        self.horizontalLayout_5.addWidget(self.Edit_Marca)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.Edit_Modelo = QtGui.QLineEdit(self.layoutWidget)
        self.Edit_Modelo.setObjectName(_fromUtf8("Edit_Modelo"))
        self.horizontalLayout_4.addWidget(self.Edit_Modelo)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout.addWidget(self.label_9)
        self.Edit_Mail = QtGui.QLineEdit(self.layoutWidget)
        self.Edit_Mail.setObjectName(_fromUtf8("Edit_Mail"))
        self.horizontalLayout.addWidget(self.Edit_Mail)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.btn_Modificar = QtGui.QPushButton(self.layoutWidget)
        self.btn_Modificar.setObjectName(_fromUtf8("btn_Modificar"))
        self.horizontalLayout_11.addWidget(self.btn_Modificar)
        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.retranslateUi(DialogModi)
        QtCore.QMetaObject.connectSlotsByName(DialogModi)

    def retranslateUi(self, DialogModi):
        DialogModi.setWindowTitle(_translate("DialogModi", "Modificacion de registro", None))
        self.groupBox.setTitle(_translate("DialogModi", "Datos Alumno / Docente", None))
        self.label_2.setText(_translate("DialogModi", "Apellidos y Nombres", None))
        self.label_3.setText(_translate("DialogModi", "Domicilio", None))
        self.label_4.setText(_translate("DialogModi", "Tel de contacto / Cel", None))
        self.label_6.setText(_translate("DialogModi", "Marca", None))
        self.label_5.setText(_translate("DialogModi", "Modelo", None))
        self.label_9.setText(_translate("DialogModi", "Mail (Opcional)", None))
        self.btn_Modificar.setText(_translate("DialogModi", "Modificar", None))

