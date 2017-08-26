# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
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

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(346, 226)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/user.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        self.btn_Login = QtGui.QPushButton(Login)
        self.btn_Login.setGeometry(QtCore.QRect(130, 170, 91, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Login.setIcon(icon1)
        self.btn_Login.setObjectName(_fromUtf8("btn_Login"))
        self.layoutWidget = QtGui.QWidget(Login)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 271, 101))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_usuario = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_usuario.setObjectName(_fromUtf8("lineEdit_usuario"))
        self.horizontalLayout.addWidget(self.lineEdit_usuario)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_pass = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_pass.setObjectName(_fromUtf8("lineEdit_pass"))
        self.horizontalLayout_2.addWidget(self.lineEdit_pass)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_aviso = QtGui.QLabel(Login)
        self.label_aviso.setGeometry(QtCore.QRect(40, 140, 271, 16))
        self.label_aviso.setText(_fromUtf8(""))
        self.label_aviso.setObjectName(_fromUtf8("label_aviso"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Ingresando", None))
        self.btn_Login.setText(_translate("Login", "Ingresar", None))
        self.label.setText(_translate("Login", "Usuario", None))
        self.label_2.setText(_translate("Login", "Contraseña", None))

import resource_rc
