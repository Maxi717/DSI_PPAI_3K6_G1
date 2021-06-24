import datetime


class Entrada:
    def __init__(self,fecha_venta=datetime.date.today(), hora_venta=datetime.datetime.time(), numero=-1, monto=-1,
                 sede=None, tarifa=None):
        self.fecha_venta = fecha_venta
        self.hora_venta = hora_venta
        self.numero = numero
        self.monto = monto
        self.sede = sede
        self.tarifa = tarifa

    def get_numero(self):
        return self.numero

    def get_sede(self):
        return self.sede

    def get_fecha_venta(self):
        return self.fecha_venta

    def get_hora_venta(self):
        return self.hora_venta

    def son_de_fecha_hora_y_sede(self, sede=None):
        """
        Recibe una sede y evalúa si es igual a la del objeto. También evalúa si es actual la entrada
        :return: True si la entrada pertenece a la sede y tiene fecha y hora actual
        """
        resultado = False
        fecha_actual = datetime.date.today()
        hora_actual = datetime.datetime.time()

        if sede == self.sede and self.fecha_venta == fecha_actual and self.hora_venta == hora_actual:
            resultado = True

        return resultado

    def new(self, fecha_venta=datetime.date.today(), hora_venta=datetime.datetime.utcnow(), numero=-1, monto=-1,
                 sede=None, tarifa=None):
        """"
        Alternativa de inicialización para no utilizar la definición con __init__
        """
        self.fecha_venta = fecha_venta
        self.hora_venta = hora_venta
        self.numero = numero
        self.monto = monto
        self.sede = sede
        self.tarifa = tarifa
