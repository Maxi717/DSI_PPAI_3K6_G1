from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class PantallaVentaEntrada:
    def __init__(self):
        window = Tk()
        window.geometry("600x400")
        window.resizable(False, False)
        window.config(background='#1f2f3f')
        window.title('Pantalla Venta de Entradas')
        main_tittle = Label(text="Venta de Entradas")
        main_tittle.pack()


        tarifa_seleccionada_label = Label(text="Tarifa: ")
        tarifa_seleccionada_label.place(x=22, y=70)

        #cant_entradas = ttk.Combobox(window, width=17, state='readonly')
        #cant_entradas.place(x=22, y=190)
        combo_tarifa = ttk.Combobox(window, width=58, state='readonly')
        combo_tarifa.place(x=22, y=95)
        opciones_tarifas = ["TIPO ENTRADA 1, $100 + TIPO VISITA 1, $100 + CON GUIA, $100", "TIPO ENTRADA 2, $100  + TIPO VISITA 2, $100 + CON GUIA, $100",
         "TIPO ENTRADA 3, $100 + TIPO VISITA 3, $100 + SIN GUIA, $100", "TIPO ENTRADA 4, $100 + TIPO VISITA 4, $100 + SIN GUIA, $100"]
        combo_tarifa['values'] = opciones_tarifas
        
        #opciones_tarifas = self.mostrar_tarifas_vigentes()
        #combo_tarifa['values'] = opciones_tarifas
        combo_tarifa.set("-")
        Button(window, text="Obtener", command=self.obtener_tarifa).place(x=400, y=93)

        '''
        tipo_entradas_label = Label(text="Tipo Entrada: ")
        tipo_entradas_label.place(x=22, y=130)
        combo_tipo_entradas = ttk.Combobox(window, width=20, state='readonly')
        #combo_tipo_entradas.place(x=)
        tipo_visitas_label = Label(text="Tipo Visita: ")
        tipo_visitas_label.place(x=300, y=130)
        combo_tipo_visitas = ttk.Combobox(window, width=20, state='readonly')
        combo_tipo_visitas.place(x=22, y=160)
       '''
       #CANTIDAD DE ENTRADAS
        cant_entradas_label = Label(text="Cantidad de entradas: ")
        cant_entradas_label.place(x=22, y=150)
        cant_entradas = IntVar()
        #tarifa_seleccionada = StringVar()


        cant_entradas_entry = Entry(textvariable=cant_entradas, width="20")
        tarifa_seleccionada_entry = Entry(textvariable=combo_tarifa, width="40")
        #entradas_entry = Entry(textvariable=entradas, width="40")

        cant_entradas_entry.place(x=22, y=175)
        #tarifa_seleccionada_entry.place(x=22, y=300)
        #entradas_entry.place(x=22, y=160)

        submit_btn = Button(window, text="Confirmar Venta", command=self.send_data(), width="40", height="2")
        submit_btn.place(x=22, y=300)

        lista = [()]


        #mostrar_detalle_entradas(lista)

        window.mainloop()

    def mostrar_tarifas_vigentes(self, vector_tarifa):
        pass

    def send_data(self):
        pass

    def obtener_tarifa(args):
        pass

    def mostrar_detalle_entradas(lista):
        total_filas = len(lista)
        total_columnas = len(lista)
        for i in range(total_filas):
            for j in range(total_columnas):
                e = Entry(width=20, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, lista[i][j])
        detalle_entradas = Toplevel()
        PantallaVentaEntrada.ventana += 1
        detalle_entradas.mainloop()










def mainloop(self):
    self.root.mainloop()

if __name__ == '__main__':
    pantalla_venta_entradas = PantallaVentaEntrada()
    pantalla_venta_entradas.mainloop()

  #  def __init__(self, cant_entradas, combo_tarifas, entradas, tarifa_seleccionada):
   #     self.cant_entradas=cant_entradas
    #    self.combo_tarifas=combo_tarifas
     #   self.entradas=entradas
      #  self.tarifa_seleccionada=tarifa_seleccionada
