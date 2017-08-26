from datetime import date

import Modulos.ST.Cargar_Movimientos
import Modulos.ST.Escribir
from reportlab.lib.pagesizes import legal
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from Modulos.ST.Form.FormAlta import *

import Modulos.ST.Escribir_Parque


class FormAlta(QtGui.QDialog):
    def __init__(self,usuario,con,cursor,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uid = Ui_Dialog() ##Cargo el formulario Clase en FormAlta.py
        self.uid.setupUi(self)
        self.con = con
        self.cursor = cursor
        self.usuario = usuario
        self.uid.Fecha_Conig.setMaximumDate(QtCore.QDate.currentDate()) ##Fecha maxima el dia de hoy
        self.uid.Fecha_Conig_2.setMaximumDate(QtCore.QDate.currentDate()) ##Fecha maxima el dia de hoy
        self.uid.Fecha_Conig.setDate(QtCore.QDate.currentDate())
        self.uid.Fecha_Conig_2.setDate(QtCore.QDate.currentDate())
        self.uid.btn_Editar.setEnabled(False) ##Deshabilita boton Editar de la solapa alumno /docente
        self.uid.btn_Limpiar.setEnabled(False) ##Deshabilita boton Limpiar de la solapa alumno /docente
        self.uid.btn_Editar_par.setEnabled(False) ##Deshabilita boton Editar de la solapa Parque Escolar
        self.uid.btn_Limpiar_par.setEnabled(False) ##Deshabilita boton Limpiar de la solapa Parque Escolar
        self.buscar_datos_directivo() ##Busco datos de directivo
        QtCore.QObject.connect(self.uid.btn_Generar, QtCore.SIGNAL('clicked()'), self.imprimir_Ticket) ##Conecto señales
        QtCore.QObject.connect(self.uid.btn_buscar, QtCore.SIGNAL('clicked()'), self.buscar_datos)
        QtCore.QObject.connect(self.uid.btn_Buscar_par, QtCore.SIGNAL('clicked()'), self.buscar_datos_par)
        QtCore.QObject.connect(self.uid.btn_Generar_2, QtCore.SIGNAL('clicked()'), self.imprimir_Ticket_Parque)
        QtCore.QObject.connect(self.uid.btn_Limpiar, QtCore.SIGNAL('clicked()'), self.limpiar_datos)
        QtCore.QObject.connect(self.uid.btn_Limpiar_par, QtCore.SIGNAL('clicked()'), self.limpiar_datos_par)
        self.editar = False
        self.editar_parque = False
        self.busco_parque = False
        self.busco = False

    def limpiar_datos(self):
        self.uid.Edit_Ticket.setText("")
        self.uid.Edit_CUIT.setText("")
        self.uid.Edit_Comentarios.setText("")
        self.uid.Edit_AyN.setText("")
        self.uid.Edit_Dom.setText("")
        self.uid.Edit_Tel.setText("")
        self.uid.Edit_Mail.setText("")
        self.uid.Edit_N_S.setText("")
        self.uid.Edit_Marca.setText("")
        self.uid.Edit_Modelo.setText("")
        self.uid.Edit_N_S.setEnabled(True)
        self.uid.Edit_CUIT.setEnabled(True)
        self.uid.Edit_AyN.setEnabled(True)
        self.uid.Edit_Dom.setEnabled(True)
        self.uid.Edit_Tel.setEnabled(True)
        self.uid.Edit_Mail.setEnabled(True)
        self.uid.Edit_Marca.setEnabled(True)
        self.uid.Edit_Modelo.setEnabled(True)
        self.busco = False
        self.editar = False
        self.uid.btn_Editar.setEnabled(False)
        self.uid.btn_Limpiar.setEnabled(False)

    def limpiar_datos_par(self):
        self.uid.Edit_Ticket_2.setText("")
        self.uid.Edit_Comentarios_2.setText("")
        self.uid.Edit_N_S_2.setText("")
        self.uid.Edit_Marca_2.setText("")
        self.uid.Edit_Modelo_2.setText("")
        self.uid.Edit_N_S_2.setEnabled(True)
        self.uid.Edit_Marca_2.setEnabled(True)
        self.uid.Edit_Modelo_2.setEnabled(True)
        self.uid.cmb_condicion.setEnabled(True)
        self.busco_parque = False
        self.editar_parque = False
        self.uid.btn_Editar_par.setEnabled(False)
        self.uid.btn_Limpiar_par.setEnabled(False)

    def modo_edicion(self):
        self.editar = True
        self.cuil_viejo = self.uid.Edit_CUIT.text()
        self.uid.Edit_N_S.setEnabled(True)
        self.uid.Edit_CUIT.setEnabled(True)
        self.uid.Edit_AyN.setEnabled(True)
        self.uid.Edit_Dom.setEnabled(True)
        self.uid.Edit_Tel.setEnabled(True)
        self.uid.Edit_Mail.setEnabled(True)
        self.uid.Edit_Marca.setEnabled(True)
        self.uid.Edit_Modelo.setEnabled(True)

    def modo_edicion_par(self):
        self.editar_parque = True
        self.ns_viejo = self.uid.Edit_N_S_2.text()
        self.uid.cmb_condicion.setEnabled(True)
        self.uid.Edit_N_S_2.setEnabled(True)
        self.uid.Edit_Marca_2.setEnabled(True)
        self.uid.Edit_Modelo_2.setEnabled(True)

    def buscar_datos_directivo(self):
        self.cursor.execute('SELECT * FROM DIRECTIVO')
        if self.cursor.fetchone() != None:
            self.cursor.execute('SELECT * FROM DIRECTIVO')
            datos = self.cursor.fetchone()
            self.uid.Edit_CUIT_2.setText(str(datos[1]))
            self.uid.Edit_AyN_2.setText(datos[2])
            self.uid.Edit_Dom_2.setText(datos[3])
            self.uid.Edit_Tel_2.setText(datos[4])
            self.uid.Edit_Mail_2.setText(datos[5])
            self.uid.Edit_CUIT_2.setEnabled(False)
            self.uid.Edit_AyN_2.setEnabled(False)
            self.uid.Edit_Dom_2.setEnabled(False)
            self.uid.Edit_Tel_2.setEnabled(False)
            self.uid.Edit_Mail_2.setEnabled(False)
        else:
            self.uid.tab_2.setEnabled(False)

    def buscar_datos(self):

        self.cursor.execute("SELECT * FROM ALU_MAQ WHERE CUIL = '" + self.uid.Edit_CUIT.text() + "' ")
        if self.cursor.fetchone() != None:
            self.cursor.execute("SELECT * FROM ALU_MAQ WHERE CUIL = '" + self.uid.Edit_CUIT.text() + "' ")
            x = self.cursor.fetchone()
            self.uid.Edit_AyN.setText(x[1])
            self.uid.Edit_Dom.setText(x[2])
            self.uid.Edit_Tel.setText(x[3])
            self.uid.Edit_Mail.setText(x[4])
            self.uid.Edit_N_S.setText(x[5])
            self.uid.Edit_Marca.setText(x[6])
            self.uid.Edit_Modelo.setText(x[7])
            self.uid.Edit_N_S.setEnabled(False)
            self.uid.Edit_CUIT.setEnabled(False)
            self.uid.Edit_AyN.setEnabled(False)
            self.uid.Edit_Dom.setEnabled(False)
            self.uid.Edit_Tel.setEnabled(False)
            self.uid.Edit_Mail.setEnabled(False)
            self.uid.Edit_Marca.setEnabled(False)
            self.uid.Edit_Modelo.setEnabled(False)
            self.busco = True
            self.uid.btn_Editar.setEnabled(True)
            self.uid.btn_Limpiar.setEnabled(True)
            QtCore.QObject.connect(self.uid.btn_Editar, QtCore.SIGNAL('clicked()'), self.modo_edicion)
        else:
            QtGui.QMessageBox.about(self, "CUIL no existe",
                                    "El CUIL ingresado no existe en el sistema, por favor complete manualmente")

    def buscar_datos_par(self):
        self.cursor.execute("SELECT * FROM PARQUE_ESCOLAR WHERE N_S = '" + self.uid.Edit_N_S_2.text() + "' ")
        if self.cursor.fetchone() != None:
            self.cursor.execute("SELECT * FROM PARQUE_ESCOLAR WHERE N_S = '" + self.uid.Edit_N_S_2.text() + "' ")
            x = self.cursor.fetchone()
            self.uid.Edit_Marca_2.setText(x[1])
            self.uid.Edit_Modelo_2.setText(x[2])
            if x[3] == "PRESTAMO":
                self.uid.cmb_condicion.setCurrentIndex(0)
            if x[3] == "USO ESCOLAR":
                self.uid.cmb_condicion.setCurrentIndex(1)
            if x[3] == "PARA REASIGNAR":
                self.uid.cmb_condicion.setCurrentIndex(2)

            self.uid.cmb_condicion.setEnabled(False)
            self.uid.Edit_N_S_2.setEnabled(False)
            self.uid.Edit_Marca_2.setEnabled(False)
            self.uid.Edit_Modelo_2.setEnabled(False)
            self.busco_parque = True
            self.uid.btn_Editar_par.setEnabled(True)
            self.uid.btn_Limpiar_par.setEnabled(True)
            QtCore.QObject.connect(self.uid.btn_Editar_par, QtCore.SIGNAL('clicked()'), self.modo_edicion_par)
        else:
            QtGui.QMessageBox.about(self, "No existe equipo",
                                    "El numero de serie ingresado no existe en el sistema, por favor complete manualmente")

    def validacion_ticket_parque(self):
        if self.uid.Edit_Ticket_2.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de Ticket")
            self.uid.Edit_Ticket_2.setFocus()
            return
        if self.uid.Edit_CUIT_2.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de CUIL")
            self.uid.Edit_CUIT_2.setFocus()
            return
        if self.uid.Edit_N_S_2.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de serie")
            self.uid.Edit_N_S_2.setFocus()
            return

        if self.uid.Edit_AyN_2.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Apellidos y Nombres")
            self.uid.Edit_AyN_2.setFocus()
            return

        if self.uid.Edit_Tel_2.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Telefono de contacto")
            self.uid.Edit_Tel_2.setFocus()
            return

        if (not self.uid.Edit_Ticket_2.text().isdigit()):
            QtGui.QMessageBox.about(self, "Dato texto en campo Ticket", "Numero de Ticket Mal Ingresado")
            self.uid.Edit_Ticket_2.setFocus()
            return
        if (not self.uid.Edit_CUIT_2.text().isdigit()):
            QtGui.QMessageBox.about(self, "Dato texto en campo CUIL",
                                    "Acuerdese que el CUIL no lleva letras , y escribalo de forma numerica sin los guiones")
            self.uid.Edit_CUIT_2.setFocus()
            return
        self.cursor.execute("SELECT * FROM PARQUE_ESCOLAR WHERE N_S = '" + self.uid.Edit_N_S_2.text() + "' ")
        if self.cursor.fetchone() != None:
            QtGui.QMessageBox.about(self, "NUMERO DE SERIE YA INGRESADO",
                                    "El numero de serie ingresado ya fue asociado al sistema")
            self.uid.Edit_N_S_2.setFocus()
        else:
            self.cursor.execute("SELECT * FROM ALU_MAQ WHERE N_S = '" + self.uid.Edit_N_S_2.text() + "' ")
            if self.cursor.fetchone() != None:
                QtGui.QMessageBox.about(self, "NUMERO DE SERIE YA INGRESADO",
                                    "El numero de serie ingresado ya fue asociado al sistema")
                self.uid.Edit_N_S_2.setFocus()
            else:
                self.cursor.execute("SELECT * FROM ST WHERE N_TICKET= '" + self.uid.Edit_Ticket_2.text() + "' ")
                if self.cursor.fetchone() != None:
                    QtGui.QMessageBox.about(self, "N° Ticket", "El N° Ticket ingresado ya fue asociado al sistema")
                    self.uid.Edit_Ticket_2.setFocus()
                else:
                    return True

    def validacion_parque_edit(self):
        if self.uid.Edit_Ticket_2.text() == "":
                QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de Ticket")
                self.uid.Edit_Ticket_2.setFocus()
                return
        if self.uid.Edit_CUIT_2.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de CUIL")
            self.uid.Edit_CUIT_2.setFocus()
            return
        if self.uid.Edit_N_S_2.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de serie")
            self.uid.Edit_N_S_2.setFocus()
            return

        if self.uid.Edit_AyN_2.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Apellidos y Nombres")
            self.uid.Edit_AyN_2.setFocus()
            return

        if self.uid.Edit_Tel_2.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Telefono de contacto")
            self.uid.Edit_Tel_2.setFocus()
            return

        if (not self.uid.Edit_Ticket_2.text().isdigit()):
            QtGui.QMessageBox.about(self, "Dato texto en campo Ticket", "Numero de Ticket Mal Ingresado")
            self.uid.Edit_Ticket_2.setFocus()
            return
        if (not self.uid.Edit_CUIT_2.text().isdigit()):
            QtGui.QMessageBox.about(self, "Dato texto en campo CUIL",
                                    "Acuerdese que el CUIL no lleva letras , y escribalo de forma numerica sin los guiones")
            self.uid.Edit_CUIT_2.setFocus()
            return

        self.cursor.execute("SELECT * FROM ST WHERE N_TICKET= '" + self.uid.Edit_Ticket_2.text() + "' ")
        if self.cursor.fetchone() != None:
            QtGui.QMessageBox.about(self, "N° Ticket", "El N° Ticket ingresado ya fue asociado al sistema")
            self.uid.Edit_Ticket_2.setFocus()
        else:
            self.cursor.execute(
                "SELECT * FROM ST WHERE N_S_FK = '" + str(self.ns_viejo) + "' AND ESTADO != 'Caso Cerrado'")
            if self.cursor.fetchone() != None:
                QtGui.QMessageBox.about(self, "Ticket asociado existente",
                                        "El Equipo ingresado ya tiene un ticket asignado y no fue terminado")
                return
            else:
                self.cursor.execute(
                "SELECT * FROM ST WHERE N_S_FK = '" + self.uid.Edit_N_S_2.text() + "' AND ESTADO != 'Caso Cerrado'")
                if self.cursor.fetchone() != None:
                    QtGui.QMessageBox.about(self, "Ticket asociado existente",
                                        "El Equipo ingresado ya tiene un ticket asignado y no fue terminado")
                    return
                else:
                    return True

    def imprimir_Ticket_Parque(self):
        if not self.busco_parque:
            if self.validacion_ticket_parque():
                pdfmetrics.registerFont(TTFont('Liberation-Sans', 'LiberationSans-Regular.ttf'))
                pdfmetrics.registerFont(TTFont('LiberationSans-I', 'LiberationSans-Italic.ttf'))
                pdfmetrics.registerFont(TTFont('LiberationSans-BI', 'LiberationSans-BoldItalic.ttf'))
                pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'LiberationSans-Bold.ttf'))

                self.id_atei = self.usuario
                self.estado = "Alta de Ticket"
                self.today = date.today()
                self.fecha = (self.today.strftime("%d"), self.today.strftime("%m"), self.today.strftime("%Y"))
                if (not self.uid.Edit_Ticket_2.text().isdigit()):
                    QtGui.QMessageBox.about(self, "Dato texto en campo Ticket", "Numero de Ticket Mal Ingresado")
                    self.uid.Edit_Ticket_2.setFocus()
                    return
                self.datos = (self.uid.Edit_N_S_2.text(), self.uid.Edit_Marca_2.text(), self.uid.Edit_Modelo_2.text(),
                                          self.uid.cmb_condicion.currentText(), 1)
                self.datos_ticket = (
                    self.uid.Edit_Ticket_2.text(), self.uid.Edit_N_S_2.text(), self.id_atei,
                    self.uid.comboBox_2.currentText(),
                    self.estado, (self.fecha[0] + '/' + self.fecha[1] + '/' + self.fecha[2]), self.uid.Fecha_Conig_2.text(),
                    self.uid.Edit_Comentarios_2.text())
                self.cursor.execute(
                    "INSERT INTO PARQUE_ESCOLAR (N_S,MARCA,MODELO,CONDICION,ID_DIRECTIVO_FK) VALUES (?,?,?,?,?)",
                    self.datos)
                self.con.commit()
                self.cursor.execute(
                    "INSERT INTO ST (N_TICKET,N_S_FK,ID_ATEI_FK,MOTIVO,ESTADO,FECHA_CARGA,FECHA_CONIG,COMENTARIOS) VALUES (?,?,?,?,?,?,?,?)",
                    self.datos_ticket)
                self.con.commit()

                self.cursor.execute('SELECT CUE,CIUDAD,COLEGIO FROM DIRECTIVO')
                datos = self.cursor.fetchone()

                self.datos_colegio = {
                    'colegio' : datos[2],
                    'cue' : datos[0],
                    'ciudad' : datos[1]
                }
                c = canvas.Canvas(
                    "Tickets\Ticket " + self.uid.Edit_Ticket_2.text() + " - " + self.uid.Edit_AyN_2.text() + ".pdf",
                                pagesize=legal)
                c.alignment = "TA_JUSTIFY"
                width, height = legal
                Modulos.ST.Escribir_Parque.escribir_Texto(c, self.uid.Edit_Ticket_2.text(), self.uid.Edit_CUIT_2.text(),
                                                          self.uid.Edit_AyN_2.text(), self.uid.Edit_Dom_2.text(),
                                                          self.uid.Edit_Tel_2.text(), self.uid.Edit_N_S_2.text(),
                                                          self.uid.Edit_Marca_2.text(), self.uid.Edit_Modelo_2.text(),
                                                          self.uid.Fecha_Conig_2.text(), self.uid.comboBox_2.currentText(),
                                                          self.uid.Edit_Comentarios_2.text(), self.uid.Edit_Mail_2.text(),self.datos_colegio)
                Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.uid.Edit_Ticket_2.text(), self.usuario,
                                                                         'Alta de Ticket ' + self.uid.Edit_Ticket_2.text())
                c.save()
                self.close()
                QtGui.QMessageBox.about(self, "Registro guardado", "Registro Guardado satisfactoriamente")
        else:
             if self.validacion_parque_edit():
                pdfmetrics.registerFont(TTFont('Liberation-Sans', 'LiberationSans-Regular.ttf'))
                pdfmetrics.registerFont(TTFont('LiberationSans-I', 'LiberationSans-Italic.ttf'))
                pdfmetrics.registerFont(TTFont('LiberationSans-BI', 'LiberationSans-BoldItalic.ttf'))
                pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'LiberationSans-Bold.ttf'))
                self.id_atei = self.usuario
                self.cursor.execute(
                   "SELECT * FROM ST WHERE N_S_FK = '" + self.uid.Edit_N_S_2.text() + "' AND ESTADO != 'Caso Cerrado'")
                self.con.commit()

                self.estado = "Alta de Ticket"
                self.today = date.today()
                self.fecha = (self.today.strftime("%d"), self.today.strftime("%m"), self.today.strftime("%Y"))
                self.datos_ticket = (
                    self.uid.Edit_Ticket_2.text(), self.uid.Edit_N_S_2.text(), self.id_atei,
                    self.uid.comboBox_2.currentText(),
                    self.estado, (self.fecha[0] + '/' + self.fecha[1] + '/' + self.fecha[2]), self.uid.Fecha_Conig_2.text(),
                    self.uid.Edit_Comentarios_2.text())

                if self.editar:
                    self.cursor.execute('UPDATE PARQUE_ESCOLAR SET N_S = "' + str(self.uid.Edit_N_S_2.text()) + '", MARCA = "'+str(self.uid.Edit_Marca_2.text()) +'", MODELO = "'+str(self.uid.Edit_Modelo_2.text())+'", CONDICION = "'+str(self.uid.cmb_condicion.currentText()) +'"  WHERE N_S = ' + str(self.ns_viejo) + ' ')
                    self.con.commit()
                self.cursor.execute(
                    "INSERT INTO ST (N_TICKET,N_S_FK,ID_ATEI_FK,MOTIVO,ESTADO,FECHA_CARGA,FECHA_CONIG,COMENTARIOS) VALUES (?,?,?,?,?,?,?,?)",
                    self.datos_ticket)
                self.con.commit()

                self.cursor.execute('SELECT CUE,CIUDAD,COLEGIO FROM DIRECTIVO')
                datos = self.cursor.fetchone()
                """
                self.datos_colegio = {
                    'colegio' : datos[2],
                    'cue' : datos[0],
                    'ciudad' : datos[1]
                }
                """
                self.datos_colegio = {}
                c = canvas.Canvas(
                    "Tickets\Ticket " + self.uid.Edit_Ticket_2.text() + " - " + self.uid.Edit_AyN_2.text() + ".pdf",
                                pagesize=legal)
                c.alignment = "TA_JUSTIFY"
                width, height = legal
                Modulos.ST.Escribir_Parque.escribir_Texto(c, self.uid.Edit_Ticket_2.text(), self.uid.Edit_CUIT_2.text(),
                                                          self.uid.Edit_AyN_2.text(), self.uid.Edit_Dom_2.text(),
                                                          self.uid.Edit_Tel_2.text(), self.uid.Edit_N_S_2.text(),
                                                          self.uid.Edit_Marca_2.text(), self.uid.Edit_Modelo_2.text(),
                                                          self.uid.Fecha_Conig_2.text(), self.uid.comboBox_2.currentText(),
                                                          self.uid.Edit_Comentarios_2.text(), self.uid.Edit_Mail_2.text(),self.datos_colegio)
                Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.uid.Edit_Ticket_2.text(), self.usuario,
                                                                         'Alta de Ticket ' + self.uid.Edit_Ticket_2.text())
                c.save()
                self.close()
                QtGui.QMessageBox.about(self, "Registro guardado", "Registro Guardado satisfactoriamente")

    def validacion_ticket_alumno(self):
        if self.uid.Edit_Ticket.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de Ticket")
            self.uid.Edit_Ticket.setFocus()
            return
        if self.uid.Edit_CUIT.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de CUIL")
            self.uid.Edit_CUIT.setFocus()
            return
        if self.uid.Edit_N_S.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de serie")
            self.uid.Edit_N_S.setFocus()
            return

        if self.uid.Edit_AyN.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Apellidos y Nombres")
            self.uid.Edit_AyN.setFocus()
            return

        if self.uid.Edit_Tel.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Telefono de contacto")
            self.uid.Edit_Tel.setFocus()
            return

        if (not self.uid.Edit_Ticket.text().isdigit()):
            QtGui.QMessageBox.about(self, "Dato texto en campo Ticket", "Numero de Ticket Mal Ingresado")
            self.uid.Edit_Ticket.setFocus()
            return
        if (not self.uid.Edit_CUIT.text().isdigit()):
            QtGui.QMessageBox.about(self, "Dato texto en campo CUIL",
                                    "Acuerdese que el CUIL no lleva letras , y escribalo de forma numerica sin los guiones")
            self.uid.Edit_CUIT.setFocus()
            return
        self.cursor.execute("SELECT * FROM ALU_MAQ WHERE CUIL = '" + self.uid.Edit_CUIT.text() + "' ")
        if self.cursor.fetchone() != None:
            QtGui.QMessageBox.about(self, "CUIL YA INGRESADO", "El cuil ingresado ya fue asociado al sistema")
            self.uid.Edit_CUIT.setFocus()
        else:
            self.cursor.execute("SELECT * FROM ALU_MAQ WHERE N_S = '" + self.uid.Edit_N_S.text() + "' ")
            if self.cursor.fetchone() != None:
                QtGui.QMessageBox.about(self, "NUMERO DE SERIE YA INGRESADO",
                                        "El numero de serie ingresado ya fue asociado al sistema")
                self.uid.Edit_N_S.setFocus()
            else:
                self.cursor.execute("SELECT * FROM PARQUE_ESCOLAR WHERE N_S = '" + self.uid.Edit_N_S_2.text() + "' ")
                if self.cursor.fetchone() != None:
                    QtGui.QMessageBox.about(self, "NUMERO DE SERIE YA INGRESADO",
                                            "El numero de serie ingresado ya fue asociado al sistema")
                    self.uid.Edit_N_S_2.setFocus()
                else:
                    self.cursor.execute("SELECT * FROM ST WHERE N_TICKET= '" + self.uid.Edit_Ticket.text() + "' ")
                    if self.cursor.fetchone() != None:
                        QtGui.QMessageBox.about(self, "N° Ticket", "El N° Ticket ingresado ya fue asociado al sistema")
                        self.uid.Edit_Ticket.setFocus()
                    else:
                        return True

    def validacion_alu_edit(self):
        if self.uid.Edit_Ticket.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de Ticket")
            self.uid.Edit_Ticket.setFocus()
            return
        if self.uid.Edit_CUIT.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de CUIL")
            self.uid.Edit_CUIT.setFocus()
            return
        if self.uid.Edit_N_S.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Numero de serie")
            self.uid.Edit_N_S.setFocus()
            return

        if self.uid.Edit_AyN.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Apellidos y Nombres")
            self.uid.Edit_AyN.setFocus()
            return

        if self.uid.Edit_Tel.text() == "":
            QtGui.QMessageBox.about(self, "Campo Vacio", "Ingrese Telefono de contacto")
            self.uid.Edit_Tel.setFocus()
            return

        if (not self.uid.Edit_Ticket.text().isdigit()):
            QtGui.QMessageBox.about(self, "Dato texto en campo Ticket", "Numero de Ticket Mal Ingresado")
            self.uid.Edit_Ticket.setFocus()
            return
        if (not self.uid.Edit_CUIT.text().isdigit()):
            QtGui.QMessageBox.about(self, "Dato texto en campo CUIL",
                                    "Acuerdese que el CUIL no lleva letras , y escribalo de forma numerica sin los guiones")
            self.uid.Edit_CUIT.setFocus()
            return

        self.cursor.execute("SELECT * FROM ST WHERE N_TICKET= '" + self.uid.Edit_Ticket.text() + "' ")
        if self.cursor.fetchone() != None:
            QtGui.QMessageBox.about(self, "N° Ticket", "El N° Ticket ingresado ya fue asociado al sistema")
            self.uid.Edit_Ticket.setFocus()
        else:
            self.cursor.execute(
                "SELECT * FROM ST WHERE N_S_FK = '" + str(self.uid.Edit_N_S.text()) + "' AND ESTADO != 'Caso Cerrado'")
            if self.cursor.fetchone() != None:
                QtGui.QMessageBox.about(self, "Ticket asociado existente",
                                        "El Equipo ingresado ya tiene un ticket asignado y no fue terminado")
                return
            else:
                return True

    def imprimir_Ticket(self):
        pdfmetrics.registerFont(TTFont('Liberation-Sans', 'LiberationSans-Regular.ttf'))
        pdfmetrics.registerFont(TTFont('LiberationSans-I', 'LiberationSans-Italic.ttf'))
        pdfmetrics.registerFont(TTFont('LiberationSans-BI', 'LiberationSans-BoldItalic.ttf'))
        pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'LiberationSans-Bold.ttf'))

        if not self.busco:
            if self.validacion_ticket_alumno():
                self.id_atei = self.usuario
                self.estado = "Alta de Ticket"
                self.today = date.today()
                self.fecha = (self.today.strftime("%d"), self.today.strftime("%m"), self.today.strftime("%Y"))
                self.datos = (self.uid.Edit_CUIT.text(), self.uid.Edit_AyN.text(), self.uid.Edit_Dom.text(),
                              self.uid.Edit_Tel.text(), self.uid.Edit_Mail.text(), self.uid.Edit_N_S.text(),
                              self.uid.Edit_Marca.text(), self.uid.Edit_Modelo.text())
                self.datos_ticket = (self.uid.Edit_Ticket.text(), self.uid.Edit_N_S.text(), self.id_atei,
                                     self.uid.comboBox.currentText(), self.estado,
                                     (self.fecha[0] + '/' + self.fecha[1] + '/' + self.fecha[2]),
                                     self.uid.Fecha_Conig.text(), self.uid.Edit_Comentarios.text())
                self.cursor.execute(
                    "INSERT INTO ALU_MAQ (CUIL,A_N,DOMICILIO,TEL,MAIL,N_S,MARCA,MODELO) VALUES (?,?,?,?,?,?,?,?)",
                    self.datos)
                self.con.commit()
                self.cursor.execute(
                    "INSERT INTO ST (N_TICKET,N_S_FK,ID_ATEI_FK,MOTIVO,ESTADO,FECHA_CARGA,FECHA_CONIG,COMENTARIOS) VALUES (?,?,?,?,?,?,?,?)",
                    self.datos_ticket)
                self.con.commit()

                self.cursor.execute('SELECT CUE,CIUDAD,COLEGIO FROM DIRECTIVO')
                datos = self.cursor.fetchone()

                self.datos_colegio = {
                    'colegio' : datos[2],
                    'cue' : datos[0],
                    'ciudad' : datos[1]
                }

                c = canvas.Canvas(
                    "Tickets\Ticket " + self.uid.Edit_Ticket.text() + " - " + self.uid.Edit_AyN.text() + ".pdf",
                    pagesize=legal)
                c.alignment = "TA_JUSTIFY"
                width, height = legal
                Modulos.ST.Escribir.escribir_Texto(c, self.uid.Edit_Ticket.text(), self.uid.Edit_CUIT.text(),
                                                   self.uid.Edit_AyN.text(), self.uid.Edit_Dom.text(),
                                                   self.uid.Edit_Tel.text(), self.uid.Edit_N_S.text(),
                                                   self.uid.Edit_Marca.text(), self.uid.Edit_Modelo.text(),
                                                   self.uid.Fecha_Conig.text(), self.uid.comboBox.currentText(),
                                                   self.uid.Edit_Comentarios.text(), self.uid.Edit_Mail.text(),self.datos_colegio)
                Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.uid.Edit_Ticket.text(), self.usuario,
                                                             'Alta de Ticket ' + self.uid.Edit_Ticket.text())
                c.save()
                self.close()
                QtGui.QMessageBox.about(self, "Registro guardado", "Registro Guardado satisfactoriamente")
        else:
            if self.validacion_alu_edit():
                self.id_atei = self.usuario
                self.cursor.execute(
                    "SELECT * FROM ST WHERE N_S_FK = '" + self.uid.Edit_N_S.text() + "' AND ESTADO != 'Caso Cerrado'")


                self.estado = "Alta de Ticket"
                self.today = date.today()
                self.fecha = (self.today.strftime("%d"), self.today.strftime("%m"), self.today.strftime("%Y"))
                self.datos_ticket = (
                    self.uid.Edit_Ticket.text(), self.uid.Edit_N_S.text(), self.id_atei,
                    self.uid.comboBox.currentText(),
                    self.estado, (self.fecha[0] + '/' + self.fecha[1] + '/' + self.fecha[2]),
                    self.uid.Fecha_Conig.text(),
                    self.uid.Edit_Comentarios.text())

                if self.editar:
                    self.cursor.execute('UPDATE ALU_MAQ SET CUIL = "' + str(self.uid.Edit_CUIT.text()) + '", A_N = "'+str(self.uid.Edit_AyN.text()) +'", DOMICILIO = "'+str(self.uid.Edit_Dom.text())+'", TEL = "'+str(self.uid.Edit_Tel.text())+'", MAIL = "'+str(self.uid.Edit_Mail.text())+'", N_S = "'+str(self.uid.Edit_N_S.text())+'",MARCA = "'+str(self.uid.Edit_Marca.text())+'",MODELO = "'+str(self.uid.Edit_Modelo.text())+'" WHERE CUIL = ' + str(self.cuil_viejo) + ' ')
                    self.con.commit()
                self.cursor.execute(
                    "INSERT INTO ST (N_TICKET,N_S_FK,ID_ATEI_FK,MOTIVO,ESTADO,FECHA_CARGA,FECHA_CONIG,COMENTARIOS) VALUES (?,?,?,?,?,?,?,?)",
                    self.datos_ticket)
                self.con.commit()

                self.cursor.execute('SELECT CUE,CIUDAD,COLEGIO FROM DIRECTIVO')
                datos = self.cursor.fetchone()

                self.datos_colegio = {
                    'colegio' : datos[2],
                    'cue' : datos[0],
                    'ciudad' : datos[1]
                }


                c = canvas.Canvas(
                    "Tickets\Ticket " + self.uid.Edit_Ticket.text() + " - " + self.uid.Edit_AyN.text() + ".pdf",
                    pagesize=legal)
                c.alignment = "TA_JUSTIFY"
                width, height = legal
                Modulos.ST.Escribir.escribir_Texto(c, self.uid.Edit_Ticket.text(), self.uid.Edit_CUIT.text(),
                                                   self.uid.Edit_AyN.text(), self.uid.Edit_Dom.text(),
                                                   self.uid.Edit_Tel.text(), self.uid.Edit_N_S.text(),
                                                   self.uid.Edit_Marca.text(), self.uid.Edit_Modelo.text(),
                                                   self.uid.Fecha_Conig.text(), self.uid.comboBox.currentText(),
                                                   self.uid.Edit_Comentarios.text(), self.uid.Edit_Mail.text(),self.datos_colegio)
                Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.uid.Edit_Ticket.text(), self.usuario,
                                                             'Alta de Ticket ' + self.uid.Edit_Ticket.text())
                c.save()
                self.close()
                QtGui.QMessageBox.about(self, "Registro guardado", "Registro Guardado satisfactoriamente")
