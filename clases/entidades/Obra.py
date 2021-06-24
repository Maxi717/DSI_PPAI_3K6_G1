import datetime

class Obra:
    def init(self, alto, ancho, codigo_sensor, descripcion, duracion_extendida, duracion_resumida,
                 fecha_primer_ingreso, nombre_obra, peso, valuacion, fecha_creacion=datetime.date.today()):
        self.alto = alto
        self.ancho = ancho
        self.codigo_sensor = codigo_sensor
        self.descripcion = descripcion
        self.duracion_extendida = duracion_extendida
        self.duracion_resumida = duracion_resumida
        self.fecha_creacion = fecha_creacion
        self.fecha_primer_ingreso = fecha_primer_ingreso
        self.nombre_obra = nombre_obra
        self.peso = peso
        self.valuacion = valuacion

    def get_duracion_resumida(self):
        return self.duracionResumida