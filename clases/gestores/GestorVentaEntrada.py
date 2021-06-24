from datetime import datetime

from ..fronteras import PantallaVentaEntrada
 
pantalla = PantallaVentaEntrada()

class GestorVentaEntrada:
    def __init__(self, logeado_empleado, tarifas, usuario):
        self.logueadoEmpleado = logeado_empleado
        self.tarifas = tarifas
        self.usuario = usuario


    def opcion_venta_entradas(self):
        self.logueadoEmpleado = self.buscar_empleado_logueado()
        sede = self.buscar_sede(self.logueadoEmpleado)
        vector_tarifas = self.buscar_tarifas_sede(sede)

        pantalla.mostrar_tarifas(vector_tarifas)

    def buscar_empleado_logueado(self):
        empleado_logueado = Sesion.get_empleado_en_sesion()
        return empleado_logueado

    def buscar_sede(self, empleado_logueado):
        sede = Empleado.obtener_sede(empleado_logueado)
        return sede

    def buscar_tarifas_sede(self, sede):
        vector_tarifas = Sede.obtener_tarifas_vigentes(sede)
        return vector_tarifas

    def tomar_tarifas_seleccionadas(self, tarifa):
        self.tarifas = tarifa
        duracion_exposiciones_vigentes = self.buscar_expociciones_vigentes()
        return duracion_exposiciones_vigentes

        pantalla.seleccionar_cantidad_entradas()

    def buscar_exposiciones_vigentes(self, tarifa):
        duracion_exposiciones_vigentes = Sede.calcular_duracion_exposiciones_vigentes(tarifa)
        return duracion_exposiciones_vigentes


    def cantidad_entradas_a_emitir(self, cantidad_entradras):
        cap_maxima = self.buscar_capacidad_sede()
        fecha_hora = self.obtener_fecha_hora_actual()
        cant_visitantes_en_sede = Entrada.buscar_visitantes_en_sede(fecha_hora)
        cant_visitantes_por_asistir = ReservaVisita.buscar_reservas_para_asistir(fecha_hora)

        resultado = self.validar_limite_visitantes(cap_maxima, cant_visitantes_en_sede, cant_visitantes_por_asistir, cantidad_entradras)
        if resultado:
            lista_total_venta = self.calcular_total_venta(cantidad_entradras)
            pantalla.mostrar_detalle_entrada(lista_total_venta, cantidad_entradras, self.tarifas)

    def buscar_capacidad_sede(self):
        capacidad_maxima = Sede.mostrar_cantidad_maxima_visitantes()
        return capacidad_maxima

    def obtener_fecha_hora_actual(self):
        fecha_hora = datetime.now()
        return fecha_hora

    def validar_limite_visitantes(self,cap_maxima,cant_visitantes_en_sede, cant_visitantes_por_asistir,cantidad_entradras):
        cant_total = cant_visitantes_por_asistir + cant_visitantes_en_sede + cantidad_entradras
        if cap_maxima >= cant_total:
            return True

        else:
            return False

    def calcular_total_venta(self, cantidad_entradas):
        tarifa = self.tarifas
        precio_total = cantidad_entradas * tarifa
        return precio_total

    def tomar_confirmacion_venta(self):
        ultimo_numero_entrada = self.buscar_ultimo_numero_entrada()


    def buscar_ultimo_numero_entrada(self):
        vector = [Entrada]
        ultimo_numero = 0
        for i in vector:
            numero = i.get_nro()
            if numero > ultimo_numero:
                ultimo_numero = numero
        return ultimo_numero

gestor = GestorVentaEntrada()
gestor.opcion_venta_entradas()
