import sys

import Modulos.ST.Cargar_Movimientos
from Modulos.ST.Form.FormModiDir import *
from Modulos.ST.obtenercolegios import obtenercolegio


class FormModiDir(QtGui.QDialog):
    def __init__(self,usuario,con,cursor, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uidm = Ui_DialogModi()
        self.uidm.setupUi(self)
        self.usuario = usuario
        self.con = con
        self.cursor = cursor
        self.cargarDatos()
        QtCore.QObject.connect(self.uidm.btn_Modificar, QtCore.SIGNAL('clicked()'), self.modificar)

    def closeEvent(self, QCloseEvent):
        self.cursor.execute("SELECT COUNT(*) FROM DIRECTIVO WHERE ID = 1")
        a = self.cursor.fetchone()
        if a[0] == 0 :
            sys.exit()

    def cargarDatos(self):
        self.cursor.execute('SELECT * FROM DIRECTIVO')
        if self.cursor.fetchone() != None:
            self.cursor.execute('SELECT * FROM DIRECTIVO')
            datos = self.cursor.fetchone()
            self.uidm.Edit_CUIL.setText(str(datos[1]))
            self.uidm.Edit_AyN.setText(datos[2])
            self.uidm.Edit_Dom.setText(datos[3])
            self.uidm.Edit_Tel.setText(datos[4])
            self.uidm.Edit_Mail.setText(datos[5])
            self.uidm.btn_Modificar.setText('Modificar')

    def modificar(self):

        colegio, ciudad = obtenercolegio(self.uidm.cmb_CUE.currentText())

        self.datos_modificar = (
            self.uidm.Edit_CUIL.text(), self.uidm.Edit_AyN.text(), self.uidm.Edit_Dom.text(), self.uidm.Edit_Tel.text(),
            self.uidm.Edit_Mail.text(),self.uidm.cmb_CUE.currentText(),colegio,ciudad)



        self.cursor.execute('SELECT * FROM DIRECTIVO')
        if self.cursor.fetchone() != None:
            self.cursor.execute('UPDATE DIRECTIVO SET CUIL = ?, A_N = ?,DOMICILIO = ?,TEL = ? ,MAIL = ?,CUE = ?,COLEGIO = ?,CIUDAD = ? ',
                                self.datos_modificar)
            self.con.commit()
            Modulos.ST.Cargar_Movimientos.cargar_Movimiento(None, self.usuario, 'Modifico Director')
        else:
            self.cursor.execute("INSERT INTO DIRECTIVO (CUIL,A_N,DOMICILIO,TEL,MAIL,CUE,COLEGIO,CIUDAD) VALUES (?,?,?,?,?,?,?,?)",
                                self.datos_modificar)
            self.con.commit()
            Modulos.ST.Cargar_Movimientos.cargar_Movimiento(None, self.usuario, 'Inserto Director')
        self.close()
