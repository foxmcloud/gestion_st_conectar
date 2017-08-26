import sys
from PyQt4.QtGui import *
import csv


def exportarExcel(cursor,tipo):
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.AnyFile)
    dlg.setAcceptMode(QFileDialog.AcceptSave)
    if tipo == 'sta':
        ruta = dlg.getSaveFileName(dlg,'Guardar Archivo', 'c:\\','Tabla CSV (*.csv)')
        if ruta != '':
            with open(ruta, 'w',newline='') as f:
                writer = csv.writer(f,delimiter=';')
                writer.writerow(['N°Ticket', 'ATEI','Motivo','ESTADO','FECHA DEL CONIG','CUIL','ALUMNO','DOMICILIO','CEL','MAIL','NUMERO DE SERIE','MARCA','MODELO'])
                writer.writerows([row for row in cursor.execute('SELECT ST.N_TICKET AS "N° TICKET",REFERENTES.A_N_ATEI AS "ATEI",ST.MOTIVO,ST.ESTADO,ST.FECHA_CONIG,ALU_MAQ.* FROM ST INNER JOIN ALU_MAQ ON ALU_MAQ.N_S = ST.N_S_FK LEFT JOIN REFERENTES ON ST.ID_ATEI_FK = REFERENTES.ID_ATEI ')])
    if tipo == 'ad':
        ruta = dlg.getSaveFileName(dlg,'Guardar Archivo', 'c:\\','Tabla CSV (*.csv)')
        if ruta != '':
            with open(ruta, 'w',newline='') as f:
                writer = csv.writer(f,delimiter=';')
                writer.writerow(['CUIL', 'A_N','DOMICILIO','TEL','MAIL','N_S','MARCA','MODELO'])
                writer.writerows([row for row in cursor.execute('SELECT * FROM ALU_MAQ')])
    if tipo == 'par':
        ruta = dlg.getSaveFileName(dlg,'Guardar Archivo', 'c:\\','Tabla CSV (*.csv)')
        if ruta != '':
            with open(ruta, 'w',newline='') as f:
                writer = csv.writer(f,delimiter=';')
                writer.writerow(['N_S', 'MARCA','MODELO','CONDICION','ID_DIRECTIVO_FK'])
                writer.writerows([row for row in cursor.execute('SELECT * FROM PARQUE_ESCOLAR')])
    if tipo == 'parst':
        ruta = dlg.getSaveFileName(dlg,'Guardar Archivo', 'c:\\','Tabla CSV (*.csv)')
        if ruta != '':
            with open(ruta, 'w',newline='') as f:
                writer = csv.writer(f,delimiter=';')
                writer.writerow(['N°Ticket', 'ATEI','Motivo','ESTADO','FECHA DEL CONIG','N_S','MARCA','MODELO','CONDICION','ID_DIRECTIVO_FK'])
                writer.writerows([row for row in cursor.execute('SELECT ST.N_TICKET AS "N° TICKET",REFERENTES.A_N_ATEI AS "ATEI",ST.MOTIVO,ST.ESTADO,ST.FECHA_CONIG,PARQUE_ESCOLAR.* FROM ST INNER JOIN PARQUE_ESCOLAR ON PARQUE_ESCOLAR.N_S = ST.N_S_FK LEFT JOIN REFERENTES ON ST.ID_ATEI_FK = REFERENTES.ID_ATEI')])





if __name__ == '__main__':
    app = QApplication(sys.argv)
    exportarExcel()
    sys.exit(app.exec_())