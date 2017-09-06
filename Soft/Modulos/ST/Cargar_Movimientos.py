#!/usr/bin/env python
# -*- coding: utf-8 -*-
##Se escribe el texto correspondiente al ticket##
from datetime import date
import time
import sqlite3

def cargar_Movimiento(ticket,usuario,movimiento):
    today = date.today()
    fecha = (today.strftime("%d"),today.strftime("%m"),today.strftime("%Y"))
    hora = time.strftime("%X")
    datos = (None,str(ticket),str(usuario),movimiento,(fecha[0] +'/'+fecha[1]+'/'+fecha[2]),hora)
    con = sqlite3.connect("bbdd.dat")
    cursor = con.cursor()
    cursor.execute("INSERT INTO MOVIMIENTOS (ID_MOV,N_TICKET_FK,ID_ATEI_FK,DETALLE,FECHA,HORA) VALUES (?,?,?,?,?,?)",
                    datos)
    con.commit()

def mostrar_Movimiento(ticket):
    con = sqlite3.connect("bbdd.dat")
    cursor = con.cursor()
    l = ""
    for row in cursor.execute("SELECT MOVIMIENTOS.DETALLE,MOVIMIENTOS.FECHA,REFERENTES.A_N_ATEI  FROM MOVIMIENTOS LEFT JOIN REFERENTES ON REFERENTES.ID_ATEI = MOVIMIENTOS .ID_ATEI_FK WHERE MOVIMIENTOS.N_TICKET_FK = '"+str(ticket)+"'"):
        s = (' - '.join(map(str,row))) + "\n"
        l += s
    return l

def actualizar_Ticket_Movimiento(n_ticket,n_ticket_viejo):
    con = sqlite3.connect("bbdd.dat")
    cursor = con.cursor()
    cursor.execute("UPDATE MOVIMIENTOS SET N_TICKET_FK = ? WHERE N_TICKET_FK = "+n_ticket_viejo,(n_ticket,))
    con.commit()

if __name__ == '__main__':
    print(mostrar_Movimiento(1001))
