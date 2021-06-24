from .TipoVisita import *
from .TipoEntrada import *
from datetime import *

class tarifa:
    def __init__(self, fecha_fin_vigencia, fecha_inicio_vigencia, monto, monto_adicional_guia, tipo_entrada, tipo_visita):
        self.fecha_fin_vigencia = fecha_fin_vigencia
        self.fecha_inicio_vigencia = fecha_inicio_vigencia
        self.monto = monto
        self.monto_adicional_guia = monto_adicional_guia
        self.tipo_entrada = tipo_entrada
        self.tipo_visita = tipo_visita

    def conocer_tipo_visita(self):
        return self.tipo_visita.mostrar_nombre()

    def conocer_tipo_entrada(self):
        return self.tipo_entrada.mostar_nombre()

    def mostrar_montos_vigentes(self):
        if self.fecha_fin_vigencia >= datetime.now().date():
            return [self.monto, self.conocer_tipo_entrada(), self.conocer_tipo_visita()]
        else:
            return []