#!/usr/bin/env python
# -*- coding: utf-8 -*-
##Se escribe el texto correspondiente al ticket##

def escribir_Texto(c, ticket, cuil, A_N, Domi, tel, n_s, marca, modelo, fecha, motivo, detalle, mail,datos_colegio):
    c.line(0, 750, 484, 750)
    c.line(484,1000,484,710)
    c.line(230,1000,230,750)
    c.line(0,920,484,920)
    c.line(310,1000,310,920)
    c.line(0,1000,614,1000)
    c.line(0,710,614,710)
    c.line(0,1000,0,670)
    c.line(612,1000,612,670)
    #c.line(484,840,612,840)

    """
    ##LINEAS COLEGIO
    c.line(0,640,612,640)
    c.drawString(510,685,"CUE:")
    c.drawString(125,685,"COLEGIO:")
    c.drawString(10,685,"CIUDAD:")
    """
    ##FINISH LINEAS COLEGIO




    c.drawString(10,900,"Datos de Directivo")
    c.line(8,897,120,897)

    c.drawString(10,880,"CUIL: ")
    c.drawString(10,850,"Apellidos y Nombres: ")
    c.drawString(10,820,"Domicilio: ")
    c.drawString(10,790,"Tel / Cel: ")
    c.drawString(10,760,"Email: ")


    c.drawString(10,985,"N° de Ticket: ")

    c.drawString(10,925,"Fecha de Ticket: ")

    c.drawString(245,900,"Motivo:  ")
    c.drawString(245,880,"Detalle: ")

    c.drawString(245,820,"¿Solucionado?: ")
    c.drawString(340,820,"SI")
    c.drawString(360,820,"NO")

    c.line(245,800,460,800)
    c.line(245,780,460,780)
    c.line(245,760,460,760)

    c.drawString(245,980,"Datos de ")
    c.drawString(245,960,"Maquina")

    c.drawString(320,980,"N° Serie: ")
    c.drawString(320,960,"Marca: ")
    c.drawString(320,940,"Modelo: ")

    c.drawString(510,980,"N° de Ticket")

    c.drawString(520,880,"N° Serie")

    c.drawString(525,850,"Motivo")

    c.drawString(500,825,"Fecha de Ticket")

    c.drawString(525,800,"Detalle")

    c.setFont('LiberationSans-BI',11)
    ##Datos Alumno / Docente
    c.drawString(10,865,cuil)
    c.drawString(10,835,A_N[0:29])
    c.drawString(10,805,Domi)
    c.drawString(10,775,tel)
    ## Datos Maquina
    c_c = len(detalle)
    if c_c <= 35 :
        c.drawString(245,860,detalle[0:30])
    else:
        c.drawString(245,860,detalle[0:30])
        c.drawString(245,840,detalle[30:60])

    c.setFont('LiberationSans-BI',8)
    #Detalle Ticket Alumno
    c.drawString(490,790,detalle[0:30])
    c.drawString(490,780,detalle[30:60])
    c.drawString(490,770,detalle[60:90])
    c.drawString(490,760,detalle[90:120])


    c.setFont('LiberationSans-BI',11)
    c.drawString(370,980,n_s)
    c.drawString(370,960,marca)
    c.drawString(370,940,modelo[0:15])
    ##Ticket Alumno
    c.drawCentredString(545,865,n_s)
    c.setFont('LiberationSans-BI',7)
    c.drawString(50,760,mail)
    c.drawCentredString(550,840,motivo[0].upper() + motivo[1:].lower())  ## Ticket para alumno motivo
    c.drawString(530,815,fecha)
    c.setFont('LiberationSans-BI',11)
    ##Fecha de ticket

    c.drawString(110,925,fecha)

    #Motivo
    c.setFont('LiberationSans-BI',9)
    c.drawString(290,900,motivo)
    c.setFont('LiberationSans-BI',11)

    """
    ##Datos Colegio


    c.drawString(540,685,datos_colegio['cue'])
    c.drawString(60,685,datos_colegio['ciudad'])
    c.drawString(185,685,colegio[0:60])
    """
    colegio = datos_colegio['colegio']
    #N° de Orden de Entrega y de Retiro
    c.setFont('LiberationSans-BI',10)
    c.drawString(520,945,datos_colegio['cue'])
    c.drawString(520,935,datos_colegio['ciudad'])
    c.drawString(500,925,colegio[0:19])
    c.drawString(500,915,colegio[19:39])
    c.drawString(500,905,colegio[39:59])
    c.drawString(500,895,colegio[59:79])

    c.drawString(10,965,datos_colegio['cue']+ ' - ' +datos_colegio['ciudad'])
    c.drawString(10,955,colegio[0:45])
    c.drawString(10,945,colegio[45:70])

    c.drawString(25,730,"N° de Orden de Retiro: ____________")

    c.drawString(235,730,"N° de Orden de Entrega: ____________")
    
    c.setFont('LiberationSans-BI',22)
    c.drawString(500,960,ticket)    ##Numero de Ticket para la maquina
    c.drawString(90,980,ticket)     ##Para el referente


    c.setFont('LiberationSans-Bold', 11)

if __name__ == '__main__':
    from reportlab.lib.pagesizes import legal
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    pdfmetrics.registerFont(TTFont('Liberation-Sans', 'LiberationSans-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-I', 'LiberationSans-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-BI', 'LiberationSans-BoldItalic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'LiberationSans-Bold.ttf'))
    datos_colegio = {
        'colegio' : " Centro Polivalente de Arte de Ushuaia - Prof. Inés María Bustelo",
        'cue' : "940026000",
        'ciudad' : "Rio Grande"
    }
    c = canvas.Canvas("ticket.pdf", pagesize=legal)
    c.alignment = "TA_JUSTIFY"
    width, height = legal
    escribir_Texto(c, "10000", "233790912299", "Troncoso gustavo", "Pref.Naval 870 1P dto2", "15503176", "AA545435345", "NOBLEX", "NT1015E", "10/04/2016", "No carga la bateria", "NO CARGA LA BATERIA POR FAVOR MANDAR UNA NUEVA","asdsadsa",datos_colegio)
    c.save()    
