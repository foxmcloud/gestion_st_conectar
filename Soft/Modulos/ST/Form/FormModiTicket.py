# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormModiTicket.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(742, 375)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/alta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 301, 331))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_4 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.layoutWidget1 = QtGui.QWidget(self.groupBox_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 23, 271, 111))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_10 = QtGui.QLabel(self.layoutWidget1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout.addWidget(self.label_10)
        self.Edit_Ticket = QtGui.QLineEdit(self.layoutWidget1)
        self.Edit_Ticket.setObjectName(_fromUtf8("Edit_Ticket"))
        self.horizontalLayout.addWidget(self.Edit_Ticket)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.Edit_CUIT = QtGui.QLineEdit(self.layoutWidget1)
        self.Edit_CUIT.setObjectName(_fromUtf8("Edit_CUIT"))
        self.horizontalLayout_2.addWidget(self.Edit_CUIT)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_11 = QtGui.QLabel(self.layoutWidget1)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_11.addWidget(self.label_11)
        self.Fecha_Conig = QtGui.QDateEdit(self.layoutWidget1)
        self.Fecha_Conig.setDate(QtCore.QDate(2016, 1, 19))
        self.Fecha_Conig.setCalendarPopup(True)
        self.Fecha_Conig.setTimeSpec(QtCore.Qt.LocalTime)
        self.Fecha_Conig.setObjectName(_fromUtf8("Fecha_Conig"))
        self.horizontalLayout_11.addWidget(self.Fecha_Conig)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget2 = QtGui.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 24, 271, 101))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.layoutWidget2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.Edit_N_S = QtGui.QLineEdit(self.layoutWidget2)
        self.Edit_N_S.setObjectName(_fromUtf8("Edit_N_S"))
        self.horizontalLayout_3.addWidget(self.Edit_N_S)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_6 = QtGui.QLabel(self.layoutWidget2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_9.addWidget(self.label_6)
        self.Edit_Marca = QtGui.QLineEdit(self.layoutWidget2)
        self.Edit_Marca.setObjectName(_fromUtf8("Edit_Marca"))
        self.horizontalLayout_9.addWidget(self.Edit_Marca)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_10.addWidget(self.label_5)
        self.Edit_Modelo = QtGui.QLineEdit(self.layoutWidget2)
        self.Edit_Modelo.setObjectName(_fromUtf8("Edit_Modelo"))
        self.horizontalLayout_10.addWidget(self.Edit_Modelo)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 32, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(48, 130, 231, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setBaseSize(QtCore.QSize(100, 1000))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_5.addWidget(self.groupBox)
        self.layoutWidget3 = QtGui.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(330, 10, 381, 331))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget4 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(11, 24, 341, 151))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.layoutWidget4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.Edit_AyN = QtGui.QLineEdit(self.layoutWidget4)
        self.Edit_AyN.setObjectName(_fromUtf8("Edit_AyN"))
        self.horizontalLayout_5.addWidget(self.Edit_AyN)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.layoutWidget4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.Edit_Dom = QtGui.QLineEdit(self.layoutWidget4)
        self.Edit_Dom.setObjectName(_fromUtf8("Edit_Dom"))
        self.horizontalLayout_6.addWidget(self.Edit_Dom)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_4 = QtGui.QLabel(self.layoutWidget4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.Edit_Tel = QtGui.QLineEdit(self.layoutWidget4)
        self.Edit_Tel.setObjectName(_fromUtf8("Edit_Tel"))
        self.horizontalLayout_7.addWidget(self.Edit_Tel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_9 = QtGui.QLabel(self.layoutWidget4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        self.Edit_Mail = QtGui.QLineEdit(self.layoutWidget4)
        self.Edit_Mail.setObjectName(_fromUtf8("Edit_Mail"))
        self.horizontalLayout_8.addWidget(self.Edit_Mail)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.Edit_Comentarios = QtGui.QLineEdit(self.groupBox_3)
        self.Edit_Comentarios.setObjectName(_fromUtf8("Edit_Comentarios"))
        self.verticalLayout_4.addWidget(self.Edit_Comentarios)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.btn_Editar = QtGui.QPushButton(self.layoutWidget3)
        self.btn_Editar.setObjectName(_fromUtf8("btn_Editar"))
        self.horizontalLayout_14.addWidget(self.btn_Editar)
        self.btn_Cancelar = QtGui.QPushButton(self.layoutWidget3)
        self.btn_Cancelar.setObjectName(_fromUtf8("btn_Cancelar"))
        self.horizontalLayout_14.addWidget(self.btn_Cancelar)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.Edit_Ticket, self.Edit_CUIT)
        Dialog.setTabOrder(self.Edit_CUIT, self.Fecha_Conig)
        Dialog.setTabOrder(self.Fecha_Conig, self.Edit_N_S)
        Dialog.setTabOrder(self.Edit_N_S, self.Edit_Marca)
        Dialog.setTabOrder(self.Edit_Marca, self.Edit_Modelo)
        Dialog.setTabOrder(self.Edit_Modelo, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.Edit_AyN)
        Dialog.setTabOrder(self.Edit_AyN, self.Edit_Dom)
        Dialog.setTabOrder(self.Edit_Dom, self.Edit_Tel)
        Dialog.setTabOrder(self.Edit_Tel, self.Edit_Mail)
        Dialog.setTabOrder(self.Edit_Mail, self.Edit_Comentarios)
        Dialog.setTabOrder(self.Edit_Comentarios, self.btn_Editar)
        Dialog.setTabOrder(self.btn_Editar, self.btn_Cancelar)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Modificacion de Tickets", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Datos CONIG", None))
        self.label_10.setText(_translate("Dialog", "N° de Ticket (CONIG)", None))
        self.label.setText(_translate("Dialog", "CUIL", None))
        self.label_11.setText(_translate("Dialog", "Fecha Conig", None))
        self.groupBox.setTitle(_translate("Dialog", "Datos Maquina", None))
        self.label_7.setText(_translate("Dialog", "Numero de Serie", None))
        self.label_6.setText(_translate("Dialog", "Marca", None))
        self.label_5.setText(_translate("Dialog", "Modelo", None))
        self.label_8.setText(_translate("Dialog", "Motivo", None))
        self.comboBox.setItemText(0, _translate("Dialog", "EL DISPLAY TIENE PIXELES DAÑADOS", None))
        self.comboBox.setItemText(1, _translate("Dialog", "EL EQUIPO NO ENCIENDE", None))
        self.comboBox.setItemText(2, _translate("Dialog", "TECLADO NO FUNCIONA", None))
        self.comboBox.setItemText(3, _translate("Dialog", "ERROR DE DISCO RIGIDO", None))
        self.comboBox.setItemText(4, _translate("Dialog", "LA PANTALLA NO FUNCIONA", None))
        self.comboBox.setItemText(5, _translate("Dialog", "PANTALLA ROTA", None))
        self.comboBox.setItemText(6, _translate("Dialog", "PROBLEMAS DE BATERIA", None))
        self.comboBox.setItemText(7, _translate("Dialog", "PROBLEMAS DE SOFTWARE", None))
        self.comboBox.setItemText(8, _translate("Dialog", "FALLA DE CARGADOR", None))
        self.comboBox.setItemText(9, _translate("Dialog", "CARGADOR CON DAÑOS FISICOS", None))
        self.comboBox.setItemText(10, _translate("Dialog", "NO CARGA LA BATERIA", None))
        self.comboBox.setItemText(11, _translate("Dialog", "FALLA DE ACTUALIZACIÓN DE BIOS", None))
        self.comboBox.setItemText(12, _translate("Dialog", "TECLADO ROTO", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Datos", None))
        self.label_2.setText(_translate("Dialog", "Apellidos y Nombres", None))
        self.label_3.setText(_translate("Dialog", "Domicilio", None))
        self.label_4.setText(_translate("Dialog", "Tel de contacto / Cel", None))
        self.label_9.setText(_translate("Dialog", "Mail (Opcional)", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Detalle del caso", None))
        self.btn_Editar.setText(_translate("Dialog", "Editar", None))
        self.btn_Cancelar.setText(_translate("Dialog", "Cancelar", None))

import resource_rc
