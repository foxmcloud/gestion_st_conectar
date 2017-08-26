#!/usr/bin/env python
# -*- coding: utf-8 -*-
##Se escribe el texto correspondiente al ticket##

def escribir_Texto(c, ticket, cuil, A_N, Domi, tel, n_s, marca, modelo, fecha, motivo, detalle, mail,datos_colegio):
    c.line(0, 750, 614, 750)
    c.line(484,1000,484,520)
    c.line(230,1000,230,750)
    c.line(0,920,484,920)
    c.line(310,1000,310,920)
    c.line(0,1000,614,1000)
    c.line(0,520,612,520)
    c.line(0,1000,0,520)
    c.line(612,1000,612,520)
    #c.line(484,840,612,840)


    """LINEAS
    c.line(0,450,612,450)
    c.drawString(160,495,"CUE:")
    
    c.drawString(10,470,"COLEGIO:")
    c.drawString(10,495,"CIUDAD:")
    
    FINISH LINEAS COLEGIO"""
    c.drawString(510,730,"N° de Ticket")



    c.drawString(10,900,"Datos de Alumno o Docente")
    c.line(8,897,163,897)

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
    #Ticket Alumno
    c.drawString(510,980,"N° de Ticket")

    c.drawString(520,880,"N° Serie")

    c.drawString(525,850,"Motivo")

    c.drawString(500,825,"Fecha de Ticket")

    c.drawString(525,800,"Detalle")

    #/TicketAlumno

    c.drawString(520,615,"N° Serie")
    c.drawString(525,588,"Motivo")
    c.drawString(525,565,"Detalle")
    

    c.setFont('LiberationSans-BI',11)
    ##Datos Alumno / Docente
    c.drawString(10,865,cuil)
    c.drawString(10,835,A_N[0:29])
    c.drawString(10,805,Domi[0:37])
    c.drawString(10,775,tel)
    ## Datos Maquina
    c_c = len(detalle)
    if c_c <= 35 :
        c.drawString(245,860,detalle[0:30])
    else:
        c.drawString(245,860,detalle[0:30])
        c.drawString(245,840,detalle[30:60])

    c.setFont('LiberationSans-BI',8)
    #Detalle Ticket Maquina
    c.drawString(490,555,detalle[0:30])
    c.drawString(490,545,detalle[30:60])
    c.drawString(490,535,detalle[60:90])
    c.drawString(490,525,detalle[90:120])
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
    c.setFont('LiberationSans-BI',8)
    c.drawCentredString(550,840,motivo[0].upper() + motivo[1:].lower())  ## Ticket para alumno motivo
    c.drawString(50,760,mail)
    c.drawString(530,815,fecha)
    c.setFont('LiberationSans-BI',11)
    ##Fecha de ticket

    c.drawString(110,925,fecha)

    #Motivo
    c.setFont('LiberationSans-BI',9)
    c.drawString(290,900,motivo)
    c.setFont('LiberationSans-BI',11)
    #Firmas
    c.drawString(340,730,"Retira equipo reparada")
    c.drawString(180,730,"Recibo equipo para ST")
    c.drawString(5,730,"Retira equipo a la espera de ST")


    #Primeras lineas
    c.line(25,700,130,700)  #700
    c.line(190,700,295,700)
    c.line(345,700,450,700)

    #Segundas Lineas
    c.line(25,660,130,660) #660
    c.line(190,660,295,660)
    c.line(345,660,450,660)

    #Terceras Lineas
    c.line(25,620,130,620)
    c.line(190,620,295,620)
    c.line(345,620,450,620)

    #Cuartas Lineas
    c.line(25,580,130,580)
    c.line(345,580,450,580)

    #Firma
    c.drawString(60,690,"Firma")
    c.drawString(225,690,"Firma")
    c.drawString(385,690,"Firma")

    #Aclaracion
    c.drawString(50,650,"Aclaración")
    c.drawString(215,650,"Aclaración")
    c.drawString(375,650,"Aclaración")

    #DNI
    c.drawString(65,610,"DNI")
    c.drawString(230,610,"Fecha")
    c.drawString(390,610,"DNI")

    #Fecha
    c.drawString(60,570,"Fecha")
    c.drawString(385,570,"Fecha")

    #N° de Orden de Entrega y de Retiro

    c.drawString(25,530,"N° de Orden de Retiro: ____________")

    c.drawString(235,530,"N° de Orden de Entrega: ____________")
    #Parte del ticket para la maquina

    c.drawCentredString(545,603,n_s)
    c.setFont('LiberationSans-BI',8)
    c.drawCentredString(550,578,motivo[0].upper() + motivo[1:].lower())


    c.setFont('LiberationSans-BI',10)
    colegio = datos_colegio['colegio']
    c.drawString(520,695,datos_colegio['cue'])
    c.drawString(520,685,datos_colegio['ciudad'])
    c.drawString(500,675,colegio[0:19])
    c.drawString(500,665,colegio[19:39])
    c.drawString(500,655,colegio[39:59])
    c.drawString(500,645,colegio[59:79])

    c.drawString(520,945,datos_colegio['cue'])
    c.drawString(520,935,datos_colegio['ciudad'])
    c.drawString(500,925,colegio[0:19])
    c.drawString(500,915,colegio[19:39])
    c.drawString(500,905,colegio[39:59])
    c.drawString(500,895,colegio[59:79])

    c.drawString(10,965,datos_colegio['cue']+ ' - ' +datos_colegio['ciudad'])
    c.drawString(10,955,colegio[0:45])
    c.drawString(10,945,colegio[45:70])



    ##Datos Colegio
    #c.setFont('LiberationSans-BI',16)
    #colegio = datos_colegio['colegio']
    #c.drawString(200,495,datos_colegio['cue'])
    #c.drawString(70,495,datos_colegio['ciudad'])
    #c.setFont('LiberationSans-BI',18)
    #c.drawString(75,470,colegio[0:60])

    c.setFont('LiberationSans-BI',22)
    c.drawString(500,710,ticket)    ##Numero de Ticket para la maquina
    c.drawString(500,960,ticket)    ##Numero de Ticket para el alumno/docente
    c.drawString(90,980,ticket)     ##Para el referente


    c.setFont('LiberationSans-Bold', 11)

if __name__ == '__main__':
    from reportlab.lib.pagesizes import legal
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    datos_colegio = {
        'colegio' : " Centro Polivalente de Arte de Ushuaia - Prof. Inés María Bustelo",
        'cue' : "940026000",
        'ciudad' : "Rio Grande"
    }
    pdfmetrics.registerFont(TTFont('Liberation-Sans', 'LiberationSans-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-I', 'LiberationSans-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-BI', 'LiberationSans-BoldItalic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'LiberationSans-Bold.ttf'))
    c = canvas.Canvas("ticket.pdf", pagesize=legal)
    c.alignment = "TA_JUSTIFY"
    width, height = legal
    escribir_Texto(c, "10000", "233790912299", "Troncoso gustavo", "Pref.Naval 870 1P dto2", "15503176", "SZSE10IS4321432432", "NOBLEX", "NT1015E", "10/04/2016", "No carga la bateria", "blabalbalbalablablablablablabalbalbalbalbalbalbalbalbalbalbala","fdsafdsa@gmail.com",datos_colegio)
    c.save()    
