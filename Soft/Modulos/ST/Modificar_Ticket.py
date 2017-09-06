import sys

import Modulos.ST.Cargar_Movimientos
from Modulos.ST.Form.FormModiTicket import *
from Modulos.ST.Form.FormModiTicketParque import *
from PyQt4.QtCore import QDate


class FormModiTicket(QtGui.QDialog):
    def __init__(self,usuario,con,cursor,ticket,tipo, parent=None):
        QtGui.QWidget.__init__(self, parent)
        if tipo:
            self.uidm = Ui_Dialog()
        else:
            self.uidm = Ui_Dialog_Parque()
        self.uidm.setupUi(self)
        self.usuario = usuario
        self.con = con
        self.cursor = cursor
        self.tipo = tipo
        self.cargarDatos(ticket)
        QtCore.QObject.connect(self.uidm.btn_Editar, QtCore.SIGNAL('clicked()'), self.modificar)
        QtCore.QObject.connect(self.uidm.btn_Cancelar, QtCore.SIGNAL('clicked()'), self.cerrar)

    def cerrar(self):
        self.close()

    def cargarDatos(self,ticket):
        if self.tipo:
            self.cursor.execute("SELECT * FROM ALU_MAQ INNER JOIN ST ON ALU_MAQ.N_S = ST.N_S_FK AND ST.N_TICKET = '" + ticket + "' ")
            if self.cursor.fetchone() != None:
                self.cursor.execute("SELECT * FROM ALU_MAQ INNER JOIN ST ON ALU_MAQ.N_S = ST.N_S_FK AND ST.N_TICKET = '" + ticket + "' ")
                x = self.cursor.fetchone()
                self.ticket_viejo = str(x[8])
                self.cuil_viejo = str(x[0])
                self.uidm.Edit_Ticket.setText(str(x[8]))
                self.uidm.Edit_CUIT.setText(str(x[0]))
                self.uidm.Edit_AyN.setText(x[1])
                self.uidm.Edit_Dom.setText(x[2])
                self.uidm.Edit_Tel.setText(x[3])
                self.uidm.Edit_Mail.setText(x[4])
                self.uidm.Edit_N_S.setText(x[5])
                self.uidm.Edit_Marca.setText(x[6])
                self.uidm.Edit_Modelo.setText(x[7])
                self.uidm.Edit_Comentarios.setText(x[15])
                self.uidm.comboBox.setCurrentIndex(self.uidm.comboBox.findText(x[11].strip()))
                ### Obtener fecha y guardarla en el campo de fecha CONIG.
                año,mes,dia = (int(x[13][6:]),int(x[13][3:5]),int(x[13][0:2]))
                fecha_conig = QDate(año,mes,dia)
                self.uidm.Fecha_Conig.setDate(fecha_conig)
        else:
            self.cursor.execute("SELECT * FROM PARQUE_ESCOLAR INNER JOIN ST ON PARQUE_ESCOLAR.N_S = ST.N_S_FK AND ST.N_TICKET = '" + ticket + "' ")
            if self.cursor.fetchone() != None:
                self.cursor.execute("SELECT * FROM PARQUE_ESCOLAR INNER JOIN ST ON PARQUE_ESCOLAR.N_S = ST.N_S_FK AND ST.N_TICKET = '" + ticket + "' ")
                x = self.cursor.fetchone()
                self.ticket_viejo = str(x[5])
                self.n_s_viejo = str(x[0])
                self.uidm.Edit_Ticket.setText(str(x[5]))
                self.uidm.Edit_N_S.setText(str(x[0]))
                self.uidm.Edit_Marca.setText(str(x[1]))
                self.uidm.Edit_Modelo.setText(x[2])
                self.uidm.comboBox.setCurrentIndex(self.uidm.comboBox.findText(x[8].strip()))
                self.uidm.cmb_condicion.setCurrentIndex(self.uidm.cmb_condicion.findText(x[3]))
                self.uidm.Edit_Comentarios.setText(x[12])
                ### Obtener fecha y guardarla en el campo de fecha CONIG.
                año,mes,dia = (int(x[11][6:]),int(x[11][3:5]),int(x[11][0:2]))
                fecha_conig = QDate(año,mes,dia)
                self.uidm.Fecha_Conig.setDate(fecha_conig)

    def modificar(self):
        if self.tipo: ## Si el ticket es de alumno o docente modificar siguientes tablas...
            self.datos_modificar_alum_doc = (self.uidm.Edit_CUIT.text(),
                self.uidm.Edit_AyN.text(), self.uidm.Edit_Dom.text(),
                self.uidm.Edit_Tel.text(), self.uidm.Edit_Mail.text(),self.uidm.Edit_Marca.text(),
                self.uidm.Edit_Modelo.text(),self.uidm.Edit_N_S.text()
            )
            self.datos_modificar_st = ( self.uidm.Edit_Ticket.text(),self.uidm.Edit_N_S.text(),
                                        self.uidm.comboBox.currentText(),self.uidm.Fecha_Conig.text(),
                                        self.uidm.Edit_Comentarios.text())

            self.cursor.execute('UPDATE ALU_MAQ SET CUIL = ?, A_N = ?,DOMICILIO = ?,TEL = ? ,MAIL = ?,MARCA = ?,MODELO = ?,N_S = ? WHERE CUIL = '+self.cuil_viejo,
                                    self.datos_modificar_alum_doc)
            self.cursor.execute('UPDATE ST SET N_TICKET = ?, N_S_FK = ?,MOTIVO = ? ,FECHA_CONIG = ?,COMENTARIOS = ? WHERE N_TICKET = '+self.ticket_viejo,self.datos_modificar_st)
            self.con.commit()
            Modulos.ST.Cargar_Movimientos.actualizar_Ticket_Movimiento(self.uidm.Edit_Ticket.text(),self.ticket_viejo)
            Modulos.ST.Cargar_Movimientos.cargar_Movimiento(int(self.uidm.Edit_Ticket.text()), self.usuario, 'Modifico Ticket Alumno / Docente')

            self.close()
        else:
            self.datos_modificar_equipo_parque = (self.uidm.Edit_N_S.text(),
                self.uidm.Edit_Marca.text(), self.uidm.Edit_Modelo.text(),
                self.uidm.cmb_condicion.currentText()
            )
            self.datos_modificar_st = ( self.uidm.Edit_Ticket.text(),self.uidm.Edit_N_S.text(),
                                        self.uidm.comboBox.currentText(),self.uidm.Fecha_Conig.text(),
                                        self.uidm.Edit_Comentarios.text())

            self.cursor.execute('UPDATE PARQUE_ESCOLAR SET N_S = ?, MARCA = ?,MODELO = ?,CONDICION = ? WHERE N_S = '+self.n_s_viejo,
                                    self.datos_modificar_equipo_parque)
            self.con.commit()
            self.cursor.execute('UPDATE ST SET N_TICKET = ?, N_S_FK = ?,MOTIVO = ? ,FECHA_CONIG = ?,COMENTARIOS = ? WHERE N_TICKET = '+self.ticket_viejo,self.datos_modificar_st)
            self.con.commit()
            Modulos.ST.Cargar_Movimientos.actualizar_Ticket_Movimiento(self.uidm.Edit_Ticket.text(),self.ticket_viejo)
            Modulos.ST.Cargar_Movimientos.cargar_Movimiento(int(self.uidm.Edit_Ticket.text()), self.usuario, 'Modifico Ticket Parque')
            self.close()
