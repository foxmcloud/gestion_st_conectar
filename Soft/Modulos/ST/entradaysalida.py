import Modulos.ST.Cargar_Movimientos
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.Qt import *

from Modulos.ST.Form import DialogE_SST


class Form_ES(QtGui.QDialog):
    def __init__(self,usuario,cursor,con,estado,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = DialogE_SST.Ui_DE_S()
        self.ui.setupUi(self)
        self.con = con
        self.cursor = cursor
        self.usuario = usuario
        self.estado = estado

        QtCore.QObject.connect(self.ui.btn_Actualizar, QtCore.SIGNAL('clicked()'), self.actualizar)

        if self.estado == "Retira":
            self.cursor.execute("SELECT N_S_FK FROM ST WHERE ESTADO = '"+"Equipo Recibido a la espera de ST""'")
        elif self.estado == "Entrega":
            self.cursor.execute("SELECT N_S_FK FROM ST WHERE ESTADO = '"+"Equipo Retirado por ST""'")


        for i in cursor.fetchall():
            item = QListWidgetItem(i[0])
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.listado.addItem(item)

    def actualizar(self):
        itemsTextList = []
        for i in range(self.ui.listado.count()):
            if self.ui.listado.item(i).checkState() == Qt.Checked:
                self.ui.listado.item(i).text()
                itemsTextList.append(str(self.ui.listado.item(i).text()))
        result = QtGui.QMessageBox.question(self,"Confirmando",
                                                "¿Actualizar los casos seleccionados a Retirado por ST?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            for i in itemsTextList:
                if self.estado == "Retira":
                    self.cursor.execute('UPDATE ST SET ESTADO = "'+'Equipo Retirado por ST' +'" WHERE N_S_FK = "' + str(i) + '" ')
                    self.con.commit()
                    self.cursor.execute('SELECT N_TICKET FROM ST WHERE N_S_FK = "'+str(i)+'"')
                    self.ticket = self.cursor.fetchall()
                    Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.ticket[0][0], self.usuario, 'Cambio de estado: a Equipo Retirado por ST')
                if self.estado == "Entrega":
                    self.cursor.execute('UPDATE ST SET ESTADO = "'+'Equipo devuelto por ST' +'" WHERE N_S_FK = "' + str(i) + '" ')
                    self.con.commit()
                    self.cursor.execute('SELECT N_TICKET FROM ST WHERE N_S_FK = "'+str(i)+'"')
                    self.ticket = self.cursor.fetchall()
                    Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.ticket[0][0], self.usuario, 'Cambio de estado a: Equipo devuelto por ST')


            self.close()










if __name__ == "__main__":
    import sqlite3
    import sys
    con = sqlite3.connect("bbdd.dat")
    cursor = con.cursor()
    app = QtGui.QApplication(sys.argv)
    form = Form_ES()
    form.show()
    sys.exit(app.exec_())

    
        
        
