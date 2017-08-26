####Funcion para escribir pdf de etiquetas colegios####

def escribir_Texto(datos_colegio):
    from reportlab.lib.pagesizes import legal
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    pdfmetrics.registerFont(TTFont('Liberation-Sans', 'LiberationSans-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-I', 'LiberationSans-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-BI', 'LiberationSans-BoldItalic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'LiberationSans-Bold.ttf'))
    c = canvas.Canvas("Tickets/Etiqueta Colegios.pdf", pagesize=legal)
    c.alignment = "TA_JUSTIFY"
    width, height = legal

    y = 1000

    for i in range(1,21):
        c.setFont('Liberation-Sans', 11)
        c.line(0,y,612,y)
        c.drawString(170,y-20,"CUE:")
        c.drawString(15,y-40,"COLEGIO:")
        c.drawString(15,y-20,"CIUDAD:")
        c.line(0,y-100,612,y-100)
        ##Datos Colegio
        c.setFont('LiberationSans-BI',16)
        colegio = datos_colegio['colegio']
        c.drawString(200,y-20,datos_colegio['cue'])
        c.drawString(70,y-20,datos_colegio['ciudad'])
        c.setFont('LiberationSans-BI',18)
        c.drawString(75,y-40,colegio[0:60])
        y = y - 50

    c.save()


if __name__ == '__main__':
    datos_colegio = {
        'colegio' : ' Centro Polivalente de Arte de Ushuaia - Prof. Inés María Bustelo',
        'cue' : '940026000',
        'ciudad' : 'Rio Grande',
    }
    escribir_Texto(datos_colegio)