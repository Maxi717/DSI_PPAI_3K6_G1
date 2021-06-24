from Tarifa import *
from Exposicion import *

class Sede:
    def __init__(self, exposiciones=[],tarifas=[], cant_maxima_visitantes=-1, cant_max_por_guia=-1, nombre=""):
        self.cant_maxima_visitantes = cant_maxima_visitantes
        self.cant_max_por_guia = cant_max_por_guia
        self.nombre = nombre
        self.tarifas = tarifas
        self.exposiciones = exposiciones

    def get_cantidad_maxima_visitntes(self):
        return self.cant_maxima_visitantes

    def obtenerTarifasVigentes(self):
        tarifas_vigentes =[]
        for tarifa in self.tarifas:
            if tarifa.mostrar_montos_vigentes() != []:
                tarifas_vigentes.append(tarifa.mostrar_montos_vigentes())
        return tarifas_vigentes

    def calcular_duracion_exposiciones_vigentes(self):
        duracion_expo_vigentes = 0
        for expo in self.exposiciones:
            if expo.es_vigente() == True:
                duracion_expo_vigentes += expo.calcular_duracion_obras_expuestas()
        return duracion_expo_vigentes


    def mostrar_cantidad_maxima_visitantes(self):
        return self.cant_maxima_visitantes


def buscar_exposiciones(self):
    pass

def conocer_exposicion(self):
    pass

def buscar_duracion_exposiciones(self):
    pass




