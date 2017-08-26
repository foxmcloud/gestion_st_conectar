
#!/usr/bin/env python
# -*- coding: utf-8 -*-
###Informe Casos ST ###

def escribir_casos(c):
    c.line(614,1000,614,920)
    c.line(0,920,614,920)
    c.line(0,1000,614,1000)
    c.line(0,1000,0,920)
    c.setFont('LiberationSans-BI',20)
    c.drawString(15,960,"Informe de Casos de ST")
    c.drawString(484,960,"Fecha")
    c.setFont('LiberationSans-Bold', 10)
    c.drawString(10,900,"N° Ticket")
    c.drawString(70,900,"N° Serie")
    c.drawString(160,900,"Apellidos y Nombres")
    c.drawString(290,900,"Estado")
    c.drawString(330,900,"Razon ST")
    c.drawString(510,900,"Fecha de Carga")
    
    c.setFont('LiberationSans-Bold', 8)
    c.drawString(10,890,"1000")
    c.drawString(70,890,"SZSE10IS392193921")
    c.drawString(160,890,"Troncoso Planes Gustavo Ezeq")
    c.drawString(305,890,"4")
    c.drawString(330,890,"El display tiene los pixeles dañados")
    c.drawString(510,890,"02/05/2016")


    c.drawString(10,80,"Cantidad total de casos: ")
    c.drawString(100,80,"1")
    
    c.drawString(10,60,'Referencias:')
    c.drawString(10,50,'1 = Alta de Ticket')
    c.drawString(200,50,'2 = Equipo retirado a la espera de ST')
    c.drawString(450,50,'3 = Equipo Recibido a la espera de ST')
    c.drawString(10,40,'4 = Equipo Retirado por ST')
    c.drawString(200,40,'5 = Equipo devuelto por ST')
    c.drawString(450,40,'6 = Caso Cerrado')
    




if __name__ == '__main__':
    from reportlab.lib.pagesizes import legal
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    pdfmetrics.registerFont(TTFont('Liberation-Sans', 'LiberationSans-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-I', 'LiberationSans-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-BI', 'LiberationSans-BoldItalic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'LiberationSans-Bold.ttf'))
    c = canvas.Canvas("informe.pdf", pagesize=legal)
    c.alignment = "TA_JUSTIFY"
    width, height = legal
    escribir_casos(c)
    c.save()    
