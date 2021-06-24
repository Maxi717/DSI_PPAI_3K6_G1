from fpdf import *


class ImpresorEntradas():
    def __init__(self):
        pass

    def imprimir(self, entrada):
        fecha_venta = str(entrada.fecha_venta)
        hora_venta = str(entrada.hora_venta)
        numero = str(entrada.numero)
        monto = str(entrada.monto)
        nombre_sede = str(entrada.sede.nombre)
        tarifa = str(entrada.tarifa)
        tipo_entrada = str(entrada.tarifa.tipo_entrada.nombre)
        tipo_visita = str(entrada.tarifa.tipo_visita.nombre)
        pdf = FPDF()
        pdf.set_font('Arial', '', 11)
        pdf.set_title('ENTRADA MUSEO')
        pdf.add_page()
        pdf.set_text_color(170, 170, 170)
        pdf.cell(0, h=15, txt='Fecha de venta: ' + fecha_venta, align='L')
        pdf.set_font('Arial', '', 14)
        pdf.cell(0, h=15, txt='N° Entrada: ' + numero, align='R', ln=1)
        pdf.set_font('Arial', '', 11)
        pdf.cell(0, h=-5, txt='Hora emision: ' + hora_venta, align='L', ln=1)
        pdf.set_font('Arial', '', 18)
        pdf.cell(0, h=10, txt='Precio $: ' + monto, align='R', ln=1)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, h=10, txt='Sede: ' + nombre_sede, align='C', ln=1)
        pdf.set_font('Arial', 'B', 24)
        pdf.set_text_color(255, 255, 255)
        pdf.set_fill_color(38, 40, 60)
        pdf.cell(0, h=10, txt='Entrada: ' + tipo_entrada, align='C', ln=1, fill=True)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', '', 16)
        pdf.cell(0, h=10, txt='Visita: ' + tipo_visita, align='C', ln=1)
        pdf.line(0, 80, 210, 80)
        pdf.output('entrada' + str(numero) + '.pdf', 'F')



