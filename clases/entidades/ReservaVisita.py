from _datetime import *

class ReservaVisita:
    def __init__(self, cantidad_alumnos=-1, cantidad_alumnos_confirmada=-1,
                 duracion_estimada=-1, fecha_hora_creacion=datetime.now().strftime('%Y-%m-%d %H:%M'),
                 fecha_hora_reserva=datetime.now().strftime('%Y-%m-%d %H:%M'), hora_fin_real= datetime.now().strftime('%H:%M'),
                 hora_inicio_real= datetime.now().strftime('%H:%M'), numero_reserva=-1, sede=""):
        # con o sin segundos? %H:%M:%S
        self.cantidad_alumnos = cantidad_alumnos
        self.cantidad_alumnos_confirmada = cantidad_alumnos_confirmada
        self.duracion_estimada = duracion_estimada
        self.fecha_hora_creacion = fecha_hora_creacion
        self.fecha_hora_reserva = fecha_hora_reserva
        self.hora_fin_real = hora_fin_real
        self.hora_inicio_real = hora_inicio_real
        self.numero_reserva = numero_reserva
        self.sede = sede

    def son_para_fecha_hora_y_sede(self,fecha_y_hora, sede):
        if self.fecha_hora_reserva == fecha_y_hora and self.sede == sede:
            return True
        else:
            return False

def crear_cambio_estado(self):
    pass

def obtener_alumnos_en_reserva(self):
    pass
