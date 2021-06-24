from datetime import date
from datetime import time

class Sesion:
    def __int__(self, fecha_fin, fecha_inicio, hora_fin, hora_inicio):
        self.fecha_fin = date.today()
        self.fecha_inicio = date.today()
        self.hora_fin = time.now()
        self.hora_inicio = time.now()

    def conocer_usuario(self):
        pass

    def get_empleado_en_sesion(self):
        pass