from Forms.MenuPrincipalST import *
from Login import *
import sys
import os
import Modulos.ST.Cargar_Movimientos
import Modulos.ST.Escribir
import Modulos.ST.escribircolegios
import Modulos.ST.entradaysalida
from Modulos.ST.Altas import *
from Modulos.ST.exportarcsv import *
from Modulos.ST.modificar_Dire import *
from PyQt4 import QtSql
import Modulos.ST.Escribir
import Modulos.ST.Escribir_Parque
from reportlab.lib.pagesizes import legal,A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


class MenuPrincipal(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.IniciarBase()
        self.usuario = ""
        login = FormLogin()
        login.exec_()
        if not login.Logeado:
            sys.exit()
        self.usuario = os.id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.btn_Alta, QtCore.SIGNAL('clicked()'), self.generar_Alta)
        #QtCore.QObject.connect(self.ui.btn_Modificar, QtCore.SIGNAL('clicked()'), self.modificar_ticket)
        QtCore.QObject.connect(self.ui.rb_ad, QtCore.SIGNAL('clicked()'), self.Completar_lista_alumnos)
        QtCore.QObject.connect(self.ui.rb_pq, QtCore.SIGNAL('clicked()'), self.Completar_lista_parque)
        QtCore.QObject.connect(self.ui.btn_Cambiar_Estado, QtCore.SIGNAL('clicked()'), self.cambiarestado_ticket)
        QtCore.QObject.connect(self.ui.btn_BorrarRegistro, QtCore.SIGNAL('clicked()'), self.eliminar_registro)
        QtCore.QObject.connect(self.ui.btn_Lista_Cerrados, QtCore.SIGNAL('clicked()'), self.listar_cerrados)
        QtCore.QObject.connect(self.ui.actionCargar_Datos_Directivo, QtCore.SIGNAL('triggered()'), self.modificar_dire)
        QtCore.QObject.connect(self.ui.actionAbrir_carpeta_de_tickets, QtCore.SIGNAL('triggered()'), self.abrir_carpeta)
        QtCore.QObject.connect(self.ui.actionRetira_Servicio_Tecnico, QtCore.SIGNAL('triggered()'), self.retira_st)
        QtCore.QObject.connect(self.ui.actionEntrega_Servicio_Tecnico, QtCore.SIGNAL('triggered()'), self.entrega_st)
        QtCore.QObject.connect(self.ui.actionTabla_Excel, QtCore.SIGNAL('triggered()'),lambda:self.exportar_tabla('sta'))
        QtCore.QObject.connect(self.ui.actionTabla_ST_Parque_Escolar, QtCore.SIGNAL('triggered()'),lambda:self.exportar_tabla('parst'))
        QtCore.QObject.connect(self.ui.actionTabla_Alumnos, QtCore.SIGNAL('triggered()'),lambda:self.exportar_tabla('ad'))
        QtCore.QObject.connect(self.ui.actionTabla_Parque, QtCore.SIGNAL('triggered()'),lambda:self.exportar_tabla('par'))
        QtCore.QObject.connect(self.ui.actionRenovar_ticket_a, QtCore.SIGNAL('triggered()'), self.rehacer_ticket)
        QtCore.QObject.connect(self.ui.actionRenovar_Ticket_p, QtCore.SIGNAL('triggered()'), self.rehacer_ticket_parque)
        QtCore.QObject.connect(self.ui.actionGenerar_Etiquetas, QtCore.SIGNAL('triggered()'), self.hacer_etiquetas)
        QtCore.QObject.connect(self.ui.btn_agregarComentario, QtCore.SIGNAL('clicked()'), self.agregarcomentario)

        #QtCore.QObject.connect(self.ui.Edit_AyN,QtCore.SIGNAL())

        self.filter_proxy_model = QtGui.QSortFilterProxyModel()
        self.Completar_lista_alumnos()


        self.cursor.execute("SELECT COUNT(*) FROM DIRECTIVO WHERE ID = 1")
        a = self.cursor.fetchone()
        if a[0] == 0 :
            self.modificar_dire()

    def agregarcomentario(self):
        if self.fila_diferente_seleccionada() != None:
            self.ticket = str(self.filter_proxy_model.data(self.filter_proxy_model.index(self.fila_diferente_seleccionada(), 0)))
        else:
            return

        self.message = QtGui.QMessageBox.question(self, 'Agregando Comentario',
                                                      "¿Quiere Agregar un comentario al ticket " + str(
                                                          self.ticket) + "  ?",
                                                      QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if self.message == QtGui.QMessageBox.Yes:
            Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.ticket, self.usuario, ('>' + self.ui.edt_comentario.text()))
            self.ui.edt_comentario.clear()
            Modulos.ST.Cargar_Movimientos.mostrar_Movimiento(self.ticket)
            QtGui.QMessageBox.about('¡Se agrego con exito!')

    def exportar_tabla(self,tipo):
        exportarExcel(self.cursor,tipo)

    def abrir_carpeta(self):
        if getattr(sys, 'frozen', False):
            # frozen
            dir_ = os.path.dirname(sys.executable)
            os.startfile(dir_ + "/Tickets")
        else:
            # unfrozen
            dir_ = os.path.dirname(os.path.realpath(__file__))
            print(dir_ + "/Tickets")
            os.startfile(dir_ + "/Tickets")
            #s = (os.path.dirname(__file__) + "/Tickets")

    def retira_st(self):
        retira = Modulos.ST.entradaysalida.Form_ES(self.usuario, self.cursor, self.con, "Retira")
        retira.exec()
        if self.alumno:
            self.ui.rb_ad.setChecked(True)
            self.Completar_lista_alumnos()
        if self.parque:
            self.ui.rb_pq.setChecked(True)
            self.Completar_lista_parque()

    def entrega_st(self):
        entrega = Modulos.ST.entradaysalida.Form_ES(self.usuario, self.cursor, self.con, "Entrega")
        entrega.exec()
        if self.alumno:
            self.ui.rb_ad.setChecked(True)
            self.Completar_lista_alumnos()
        if self.parque:
            self.ui.rb_pq.setChecked(True)
            self.Completar_lista_parque()

    def closeEvent(self, *args, **kwargs):
        self.con.close()
        self.db.close()

    def modificar_dire(self):
        modi = FormModiDir(self.usuario,self.con,self.cursor)
        modi.exec_()
        self.ui.rb_ad.setChecked(True)
        self.Completar_lista_alumnos()

    def fila_diferente_seleccionada(self):
        try:
            indexes = self.model_sele.selectedIndexes()
            for index in indexes:
                text = u"(%i,%i)" % (index.row(), index.column())
            self.ticket = self.filter_proxy_model.data(self.filter_proxy_model.index(index.row(), 0))
            self.cursor = self.con.cursor()
            self.cursor.execute("SELECT ST.COMENTARIOS FROM ST WHERE N_TICKET = '" + str(self.ticket) + "'")
            self.comentarios = self.cursor.fetchone()
            if self.comentarios == "":
                self.ui.plainTextEdit.setPlainText("")
            else:
                s = ''
                s = Modulos.ST.Cargar_Movimientos.mostrar_Movimiento(self.ticket)
                self.ui.plainTextEdit.setPlainText((self.comentarios[0]+ '\n' +s ))
            return index.row()
        except UnboundLocalError:
            QtGui.QMessageBox.about(self, "Ninguna Fila seleccionada",
                                    "Por favor seleccione una fila")

    def setear_Usuario(self, usuario):
        self.usuario = usuario

    def obtener_Usuario(self):
        return self.usuario

    def CerrarBase(self):
        self.con.close()

    def IniciarBase(self): ##DEFINO BD
        self.con = sqlite3.connect("bbdd.dat") ##Sino existe la creo...
        self.cursor = self.con.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ALU_MAQ(
        CUIL INTEGER NOT NULL,
        A_N TEXT NOT NULL,
        DOMICILIO TEXT NULL,
        TEL TEXT NULL,
        MAIL TEXT NULL,
        N_S TEXT NOT NULL,
        MARCA TEXT NOT NULL,
        MODELO TEXT NOT NULL,
        PRIMARY KEY(CUIL,N_S))""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS REFERENTES(
        ID_ATEI INTEGER PRIMARY KEY NOT NULL,
        A_N_ATEI TEXT NOT NULL,
        USUARIO TEXT NOT NULL,
        PASS TEXT NOT NULL)""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ST(
        N_TICKET INTEGER PRIMARY KEY NOT NULL,
        N_S_FK INTEGER NOT NULL,
        ID_ATEI_FK NOT NULL,
        MOTIVO TEXT NOT NULL,
        ESTADO TEXT NOT NULL,
        FECHA_CARGA DATE NOT NULL,
        FECHA_CONIG DATE,
        COMENTARIOS TEXT,
        FOREIGN KEY(N_S_FK) REFERENCES ALU_MAQ(N_S),
        FOREIGN KEY(ID_ATEI_FK) REFERENCES REFERENTES(ID_ATEI))""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS MOVIMIENTOS(
        ID_MOV INTEGER PRIMARY KEY NOT NULL,
        N_TICKET_FK INTEGER,
        ID_ATEI_FK INTEGER,
        DETALLE TEXT NOT NULL,
        FECHA DATE NOT NULL,
        HORA TEXT NOT NULL,
        FOREIGN KEY(ID_ATEI_FK) REFERENCES REFERENTES(ID_ATEI))""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS DIRECTIVO(
        ID INTEGER PRIMARY KEY NOT NULL,
        CUIL INTEGER NOT NULL,
        A_N TEXT NOT NULL,
        DOMICILIO TEXT NULL,
        TEL TEXT NULL,
        MAIL TEXT NULL)""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS PARQUE_ESCOLAR(
        N_S TEXT NOT NULL,
        MARCA TEXT NOT NULL,
        MODELO TEXT NOT NULL,
        CONDICION TEXT NOT NULL,
        ID_DIRECTIVO_FK INTEGER,
        PRIMARY KEY(N_S),
        FOREIGN KEY(ID_DIRECTIVO_FK) REFERENCES DIRECTIVO(ID))""")

        self.con.commit()
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE') ##Driver para utilizar la bd de SQLITE3
        self.db.setDatabaseName("bbdd.dat") ##Seteo la base de datos
        self.db.open() ##La abro para trabajar con el entorno de PyQt

    def Completar_lista_parque(self): ##Completa grilla de parque
        self.model = QtSql.QSqlQueryModel()
        self.model.setQuery(
            'SELECT ST.N_TICKET AS "N° TICKET",REFERENTES.A_N_ATEI AS "ATEI",ST.MOTIVO,ST.ESTADO,ST.FECHA_CONIG,PARQUE_ESCOLAR.* FROM ST INNER JOIN PARQUE_ESCOLAR ON PARQUE_ESCOLAR.N_S = ST.N_S_FK AND ST.ESTADO != "Caso Cerrado" LEFT JOIN REFERENTES ON ST.ID_ATEI_FK = REFERENTES.ID_ATEI')
        self.ui.comboBox.clear()


        self.ui.comboBox.addItems([self.model.headerData(x,QtCore.Qt.Horizontal) for x in range(self.model.columnCount())]) ##Llena el combobox con el nombre de las columnas

        self.filter_proxy_model.setSourceModel(self.model)
        self.ui.Edit_Filtro.textChanged.connect(self.on_lineEdit_textChanged)
        self.ui.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)
        self.model_sele = QtGui.QItemSelectionModel(self.filter_proxy_model)
        self.ui.tableWidget.setModel(self.filter_proxy_model)
        self.ui.tableWidget.setSelectionModel(self.model_sele)


        self.con.commit()
        self.ticket = str(self.filter_proxy_model.data(self.filter_proxy_model.index(0, 0)))
        self.ui.btn_Alta.setEnabled(True)
        #self.ui.btn_Modificar.setEnabled(True)
        self.ui.btn_BorrarRegistro.setEnabled(True)
        self.ui.btn_Cambiar_Estado.setEnabled(True)
        self.ui.btn_Lista_Cerrados.setText("Listado de casos cerrados")
        self.model_sele.selectionChanged.connect(self.fila_diferente_seleccionada)
        QtCore.QObject.connect(self.ui.btn_Lista_Cerrados, QtCore.SIGNAL('clicked()'), self.listar_cerrados)
        self.ui.plainTextEdit.setPlainText("")
        self.parque = True
        self.alumno = False

    def Completar_lista_alumnos(self):
        self.model = QtSql.QSqlQueryModel() ##QUERY
        self.model.setQuery(
            'SELECT ST.N_TICKET AS "N° TICKET",REFERENTES.A_N_ATEI AS "ATEI",ST.MOTIVO,ST.ESTADO,ST.FECHA_CONIG,ALU_MAQ.* FROM ST INNER JOIN ALU_MAQ ON ALU_MAQ.N_S = ST.N_S_FK AND ST.ESTADO != "Caso Cerrado" LEFT JOIN REFERENTES ON ST.ID_ATEI_FK = REFERENTES.ID_ATEI ')

        self.ui.comboBox.clear()

        self.ui.comboBox.addItems([self.model.headerData(x,QtCore.Qt.Horizontal) for x in range(self.model.columnCount())]) ##Llena el combobox con el nombre de las columnas

       #Filtro edit
        self.filter_proxy_model.setSourceModel(self.model)
        self.ui.Edit_Filtro.textChanged.connect(self.on_lineEdit_textChanged)
        self.ui.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)

       #/Filtro Edit



        #Modelo Seleccion Tabla
        self.model_sele = QtGui.QItemSelectionModel(self.filter_proxy_model)
        self.ui.tableWidget.setModel(self.filter_proxy_model)
        self.ui.tableWidget.setSelectionModel(self.model_sele)
        #/Modelo Seleccion Tabla


        self.ticket = str(self.filter_proxy_model.data(self.filter_proxy_model.index(0, 0)))
        #Habilito Botones
        self.ui.btn_Alta.setEnabled(True)
        self.ui.btn_BorrarRegistro.setEnabled(True)
        self.ui.btn_Cambiar_Estado.setEnabled(True)
        #/Habilito Botones
        self.ui.btn_Lista_Cerrados.setText("Listado de casos cerrados")

        self.model_sele.selectionChanged.connect(self.fila_diferente_seleccionada) #Fila Seleccionada
        #Conecto el boton listar cerrados con la funcion listar cerrados
        QtCore.QObject.connect(self.ui.btn_Lista_Cerrados, QtCore.SIGNAL('clicked()'), self.listar_cerrados)
        #activo el radio button Alumnos / Docentes
        self.ui.rb_ad.setChecked(True)
        #Dejo vacio el campo de texto comentarios
        self.ui.plainTextEdit.setPlainText("")
        #Bandera para saber que el radio button parque no fue seleccionado
        self.parque = False
        #Bandera para saber que el radio button alumno fue seleccionado
        self.alumno = True

    @QtCore.pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        search = QtCore.QRegExp(    text,
                                    QtCore.Qt.CaseInsensitive,
                                    QtCore.QRegExp.RegExp
                                    )
        self.filter_proxy_model.setFilterRegExp(search)

    @QtCore.pyqtSlot(int)
    def on_comboBox_currentIndexChanged(self):
        self.filter_proxy_model.setFilterKeyColumn(self.ui.comboBox.currentIndex())

    def listar_cerrados(self):
        self.cursor = self.con.cursor()
        self.model = QtSql.QSqlQueryModel()
        self.model.setQuery(
            'SELECT ST.N_TICKET AS "N° TICKET",ST.N_S_FK AS "NUMERO DE SERIE",ST.MOTIVO,ST.ESTADO,ST.FECHA_CONIG  FROM ST WHERE ST.ESTADO = "Caso Cerrado"')

        self.ui.comboBox.clear()
        self.ui.comboBox.addItems([self.model.headerData(x,QtCore.Qt.Horizontal) for x in range(self.model.columnCount())]) ##Llena el combobox con el nombre de las columnas
        self.filter_proxy_model.setSourceModel(self.model)
        self.ui.Edit_Filtro.textChanged.connect(self.on_lineEdit_textChanged)
        self.ui.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)

        self.model_sele = QtGui.QItemSelectionModel(self.filter_proxy_model)
        self.ui.tableWidget.setModel(self.filter_proxy_model)
        self.ui.tableWidget.setSelectionModel(self.model_sele)
        self.con.commit()
        self.ticket = str(self.filter_proxy_model.data(self.filter_proxy_model.index(0, 0)))
        self.model_sele.selectionChanged.connect(self.fila_diferente_seleccionada) #Fila Seleccionada
        self.ui.btn_Lista_Cerrados.setText("Listar Casos no resueltos")
        self.ui.btn_Alta.setEnabled(False)
        #self.ui.btn_Modificar.setEnabled(False)


        self.ui.btn_BorrarRegistro.setEnabled(False)
        self.ui.btn_Cambiar_Estado.setEnabled(False)
        QtCore.QObject.connect(self.ui.btn_Lista_Cerrados, QtCore.SIGNAL('clicked()'), self.Completar_lista_alumnos)

    def generar_Alta(self):
        alta = FormAlta(self.usuario,self.con,self.cursor)
        alta.exec_()
        self.Completar_lista_alumnos()

    def cambiarestado_ticket(self):
        if self.fila_diferente_seleccionada() != None:
            self.ticket = str(self.filter_proxy_model.data(self.filter_proxy_model.index(self.fila_diferente_seleccionada(), 0)))
            self.estadoDB = self.filter_proxy_model.data(self.filter_proxy_model.index(self.fila_diferente_seleccionada(), 3))
            self.estadonuevo = self.cambiar_estado(self.estadoDB)
        else:
            return

        if self.estadonuevo != "Caso Cerrado":
            self.message = QtGui.QMessageBox.question(self, 'Cambiando estado',
                                                      "¿Quiere cambiar el estado del ticket " + str(
                                                          self.ticket) + " a " + self.estadonuevo + " ?",
                                                      QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if self.message == QtGui.QMessageBox.Yes:
                self.cursor.execute(
                    'UPDATE ST SET ESTADO = "' + self.estadonuevo + '" WHERE N_TICKET = ' + str(self.ticket) + ' ')
                self.con.commit()
                Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.ticket, self.usuario, 'Cambio de estado a: ' + self.estadonuevo)
                if self.alumno:
                    self.ui.rb_ad.setChecked(True)
                    self.Completar_lista_alumnos()
                if self.parque:
                    self.ui.rb_pq.setChecked(True)
                    self.Completar_lista_parque()
        else:
            self.message = QtGui.QMessageBox.question(self, 'Cerrando Caso', "¿El ticket  " + str(
                self.ticket) + " Fue solucionado correctamente? ", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if self.message == QtGui.QMessageBox.Yes:
                self.cursor.execute(
                    'UPDATE ST SET ESTADO = "' + self.estadonuevo + '" WHERE N_TICKET = ' + str(self.ticket) + ' ')
                self.con.commit()
                Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.ticket, self.usuario, 'Cambio de estado a: ' + self.estadonuevo)
                if self.alumno:
                    self.ui.rb_ad.setChecked(True)
                    self.Completar_lista_alumnos()
                if self.parque:
                    self.ui.rb_pq.setChecked(True)
                    self.Completar_lista_parque()
            if self.message == QtGui.QMessageBox.No:
                self.cursor.execute(
                    'UPDATE ST SET ESTADO = "' + "Equipo Recibido a la espera de ST" + '" WHERE N_TICKET = ' + str(
                        self.ticket) + ' ')
                self.con.commit()
                self.estadonuevo = "Equipo Recibido a la espera de ST , NO SOLUCIONADO"
                Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.ticket, self.usuario, 'Cambio de estado a: ' + self.estadonuevo)

                if self.alumno:
                    self.ui.rb_ad.setChecked(True)
                    self.Completar_lista_alumnos()
                if self.parque:
                    self.ui.rb_pq.setChecked(True)
                    self.Completar_lista_parque()


        self.ui.Edit_Filtro.setText("")

    def cambiar_estado(self, state):
        estados = (
            "Alta de Ticket", "Equipo retirado a la espera de ST", "Equipo Recibido a la espera de ST", "Equipo Retirado por ST",
            "Equipo devuelto por ST", "Caso Cerrado")
        y = 0
        for x in estados:
            if x == state:
                z = y + 1
            y += 1

        return estados[z]

    def eliminar_registro(self):
        if self.fila_diferente_seleccionada() != None:
            self.ticket = self.filter_proxy_model.data(
                self.filter_proxy_model.index(self.fila_diferente_seleccionada(), 0))
        else:
            return
        text, result = QtGui.QInputDialog.getText(self, "Baja de Ticket", "Detalle la razon de la baja del Ticket")
        if result:
            self.cursor.execute("DELETE FROM ST WHERE N_TICKET = '" + str(self.ticket) + "'")
            self.con.commit()
            Modulos.ST.Cargar_Movimientos.cargar_Movimiento(self.ticket, self.usuario,
                                                         "Baja del Ticket, Razon: " + text)
            self.Completar_lista_alumnos()

    def rehacer_ticket(self):
        if self.fila_diferente_seleccionada() != None:
            self.ticket = self.filter_proxy_model.data(
                self.filter_proxy_model.index(self.fila_diferente_seleccionada(), 0))
        else:
            return

        #####Datos colegio##########
        self.cursor.execute('SELECT CUE,CIUDAD,COLEGIO FROM DIRECTIVO')
        datos = self.cursor.fetchone()

        self.datos_colegio = {
            'colegio' : datos[2],
            'cue' : datos[0],
            'ciudad' : datos[1]
        }

        ###Datos ticket###
        self.cursor.execute('SELECT ST.N_TICKET AS "N° TICKET",REFERENTES.A_N_ATEI AS "ATEI",ST.MOTIVO,ST.ESTADO,ST.FECHA_CONIG,ST.COMENTARIOS,ALU_MAQ.* FROM ST INNER JOIN ALU_MAQ ON ALU_MAQ.N_S = ST.N_S_FK AND ST.ESTADO != "Caso Cerrado" LEFT JOIN REFERENTES ON ST.ID_ATEI_FK = REFERENTES.ID_ATEI WHERE ST.N_TICKET = "' + str(self.ticket) + '"')
        resultado = self.cursor.fetchone()

        ##Rehaciendo ticket
        try:
            pdfmetrics.registerFont(TTFont('Liberation-Sans', 'LiberationSans-Regular.ttf'))
            pdfmetrics.registerFont(TTFont('LiberationSans-I', 'LiberationSans-Italic.ttf'))
            pdfmetrics.registerFont(TTFont('LiberationSans-BI', 'LiberationSans-BoldItalic.ttf'))
            pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'LiberationSans-Bold.ttf'))

            linea = str(resultado[7])
            nombre = linea[:-1]
            directorio = "Tickets\Ticket " +str(self.ticket) + " - " + nombre + ".pdf"
            print(directorio)
            c = canvas.Canvas(directorio,
                        pagesize=legal)
            c.alignment = "TA_JUSTIFY"
            width, height = legal
            Modulos.ST.Escribir.escribir_Texto(c, str(self.ticket), str(resultado[6]), resultado[7], resultado[8], resultado[9], resultado[11], resultado[12], resultado[13], resultado[4], resultado[2], resultado[5], resultado[10],self.datos_colegio)
            c.save()
            QtGui.QMessageBox.about(self, "Renovacion de ticket", "Ticket renovado correctamente")
        except PermissionError:
            QtGui.QMessageBox.warning(self, "Renovacion de ticket", "No se pudo renovar el ticket , no tenga abierto el archivo a renovar")
            return
        except TypeError:
            QtGui.QMessageBox.warning(self, "Renovacion de ticket", "La fila seleccionada no corresponde a una maquina del parque escolar")
            return

    def rehacer_ticket_parque(self):
        if self.fila_diferente_seleccionada() != None:
            self.ticket = self.filter_proxy_model.data(
                self.filter_proxy_model.index(self.fila_diferente_seleccionada(), 0))
        else:
            return

        #####Datos colegio##########
        self.cursor.execute('SELECT CUE,CIUDAD,COLEGIO,CUIL,A_N,DOMICILIO,TEL,MAIL FROM DIRECTIVO')
        datos = self.cursor.fetchone()

        self.datos_colegio = {
            'cue' : datos[0],
            'ciudad' : datos[1],
            'colegio' : datos[2],
            'cuil' : datos[3],
            'a_n' : datos[4],
            'domi': datos[5],
            'tel' : datos[6],
            'mail' : datos[7],
        }

        ###Datos ticket###
        self.cursor.execute('SELECT ST.N_TICKET AS "N° TICKET",REFERENTES.A_N_ATEI AS "ATEI",ST.MOTIVO,ST.ESTADO,ST.FECHA_CONIG,ST.COMENTARIOS,PARQUE_ESCOLAR.* FROM ST INNER JOIN PARQUE_ESCOLAR ON PARQUE_ESCOLAR.N_S = ST.N_S_FK AND ST.ESTADO != "Caso Cerrado" LEFT JOIN REFERENTES ON ST.ID_ATEI_FK = REFERENTES.ID_ATEI WHERE ST.N_TICKET = "' + str(self.ticket) + '"')

        resultado = self.cursor.fetchone()

        ##Rehaciendo ticket
        try:
            pdfmetrics.registerFont(TTFont('Liberation-Sans', 'LiberationSans-Regular.ttf'))
            pdfmetrics.registerFont(TTFont('LiberationSans-I', 'LiberationSans-Italic.ttf'))
            pdfmetrics.registerFont(TTFont('LiberationSans-BI', 'LiberationSans-BoldItalic.ttf'))
            pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'LiberationSans-Bold.ttf'))
            c = canvas.Canvas(
                        "Tickets\Ticket " +str(self.ticket) + " - " + self.datos_colegio['a_n'] + ".pdf",
                        pagesize=legal)
            c.alignment = "TA_JUSTIFY"
            width, height = legal
            Modulos.ST.Escribir_Parque.escribir_Texto(c, str(self.ticket), str(self.datos_colegio['cuil']), self.datos_colegio['a_n'], self.datos_colegio['domi'], self.datos_colegio['tel'], resultado[6], resultado[7], resultado[8], resultado[4], resultado[2], resultado[5], self.datos_colegio['mail'], self.datos_colegio)
            c.save()
            QtGui.QMessageBox.about(self, "Renovacion de ticket", "Ticket renovado correctamente")
        except PermissionError:
            QtGui.QMessageBox.warning(self, "Renovacion de ticket", "No se pudo renovar el ticket, no abra el archivo")
            return
        except TypeError:
            QtGui.QMessageBox.warning(self, "Renovacion de ticket", "La fila seleccionada no corresponde a una maquina de un alumno")
            return

    def hacer_etiquetas(self):
        #####Datos colegio##########
        self.cursor.execute('SELECT CUE,CIUDAD,COLEGIO FROM DIRECTIVO')
        datos = self.cursor.fetchone()

        self.datos_colegio = {
            'colegio' : datos[2],
            'cue' : datos[0],
            'ciudad' : datos[1]
        }
        #### Datos colegio finish###

        Modulos.ST.escribircolegios.escribir_Texto(self.datos_colegio)
        QtGui.QMessageBox.about(self, "Etiquetas para colegios", "Se crearon correctamente las etiquetas")

