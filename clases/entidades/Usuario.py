import datetime


class Usuario:
    def __int__(self, caducidad=datetime.datetime.now(), contra="", nombre="", empleado=None):
        self.caducidad = caducidad
        self.contrasena = contra
        self.nombre = nombre
        self.empleado = empleado

    def conocer_empleado(self):
        pass

    def obtener_empleado(self):
        return self.empleado
