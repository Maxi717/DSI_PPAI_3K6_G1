from datetime import date, datetime
from .DetalleExposicion import *

class exposicion:

    def __init__(self, fecha_fin, fecha_inicio, hora_apertura, hora_cierre, nombre, empleado, detalle_exposicion, fecha_fin_replanificada = -1, fecha_inicio_replanificada = -1):
        self.fecha_fin = fecha_fin
        self.fecha_fin_replanificada = fecha_fin_replanificada
        self.fecha_inicio = fecha_inicio
        self.fecha_inicio_replanificada = fecha_inicio_replanificada
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
        self.nombre = nombre
        self.emplead = empleado
        self.detalle_exposicion = [detalle_exposicion]

    def es_vigente(self):
        fecha_actual = datetime.now().date()

        if self.fecha_fin_replanificada == -1:
            if self.fecha_fin <= fecha_actual:
                return False
            else:
                return True
        else:
            if self.fecha_fin_replanificada <= fecha_actual:
                return False
            else:
                return True

    def calcular_duracion_obras_expuestas(self):
        duracion = 0
        
        for i in self.detalle_exposicion:
            duracion += i.buscarDuracionObras()
        
        return duracion