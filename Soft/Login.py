from Forms.Login import *
import sqlite3
import os

class FormLogin(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.con = sqlite3.connect("bbdd.dat")
        self.cursor = self.con.cursor()
        QtCore.QObject.connect(self.ui.btn_Login, QtCore.SIGNAL('clicked()'), self.logear)
        self.Logeado = False

    def closeEvent(self, event):
        if not self.Logeado:
            result = QtGui.QMessageBox.question(self,
                                                "Confirmando",
                                                "¿Estas seguro que deseas salir?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            event.ignore()

            if result == QtGui.QMessageBox.Yes:
                self.con.close()
                event.accept()
                quit()

    def logear(self):
        usuario = (self.ui.lineEdit_usuario.text()).upper()
        contra = self.ui.lineEdit_pass.text().upper()
        self.cursor.execute("SELECT * FROM REFERENTES WHERE USUARIO= '" + usuario + "' AND PASS= '" + contra + "'")
        if self.cursor.fetchone() != None:
            self.cursor.execute("SELECT * FROM REFERENTES WHERE USUARIO= '" + usuario + "' AND PASS= '" + contra + "'")
            self.id = self.cursor.fetchone()
            self.Logeado = True
            os.id = self.id[0]
            #MenuPrincipal.setear_Usuario(MenuPrincipal, self.id[0])
            self.close()
        else:
            self.ui.label_aviso.setText("Usuario y/o Constraseña Incorrecta")
