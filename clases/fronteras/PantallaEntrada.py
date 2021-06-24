import tkinter

class PantallaEntrada():
    def act_cant_visitantes(self, cant_max, cant_actual):
        cant_maxima_visitantes = 'CAPACIDAD MAXIMA: ' + str(cant_max)
        cant_actual_visitantes = 'VISITANTES ACTUALES: ' + str(cant_actual)
        self.pantalla = tkinter.Tk()
        self.pantalla.geometry("990x300")
        self.pantalla.resizable(0,0)
        self.pantalla.config(background='#1f2f3f')
        self.pantalla.title('Pantalla Entrada')
        self.current_max_label = tkinter.Label(text="", font=('ComicSans', 44), fg='#ffffff', bg='#449a66',pady=10,padx=10)
        self.current_max_label.place(x=140, y=160)
        self.current_act_label = tkinter.Label(text="", font=('ComicSans', 44), fg='#ffffff', bg='#72a922',pady=10,padx=10)
        self.current_act_label.place(x=100, y=50)
        self.current_max_label.configure(text= cant_maxima_visitantes)
        self.current_act_label.configure(text=cant_actual_visitantes)
        self.pantalla.mainloop()

    def visitantes(self,cant_maxima_visitantes, cant_actual_visitantes):
        return cant_maxima_visitantes, cant_actual_visitantes