import datetime


class Empleado:
    def __int__(self, apellido="", codigo_validacion=0, cuit="", dni=0, domicilio="",
                fecha_ingreso=datetime.datetime.now(),fecha_nacimiento=datetime.datetime.now(), correo="",
                nombre="", sexo="", telefono=0, sede=None ):
        self.apellido = apellido
        self.codigo_validacion = codigo_validacion
        self.cuit = cuit
        self.dni = dni
        self.domicilio = domicilio
        self.fecha_ingreso = fecha_ingreso
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.nombre = nombre
        self.sexo = sexo
        self.telefono = telefono
        self.sede_donde_trabaja = sede

    def get_nombre(self):
        return self.nombre

    def obtener_sede(self):
        return self.sede_donde_trabaja
