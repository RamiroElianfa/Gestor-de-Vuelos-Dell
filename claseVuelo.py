class Vuelo:
    def __init__(self, codigo, aerolinea, avion, ubicacion_real, ruta, estado, origen, destino):
        self.__codigo = codigo
        self.__avion = avion
        self.__aerolinea = aerolinea
        self.__asientos_ocupados = 0
        self.__ubicacion_real = ubicacion_real
        self.__ruta = ruta
        self.__estado = estado
        self.__origen = origen
        self.__destino = destino

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    @property
    def avion(self):
        return self.__avion
    @avion.setter
    def avion(self, nuevo_avion):
        self.__avion = nuevo_avion

    @property
    def aerolinea(self):
        return self.__aerolinea
    @aerolinea.setter
    def aerolinea(self, nueva_aerolinea):
        self.__aerolinea = nueva_aerolinea

    @property
    def asientos_ocupados(self):
        return self.__asientos_ocupados
    @asientos_ocupados.setter
    def asientos_ocupados(self, nuevos_asientos_ocupados):
        self.__asientos_ocupados = nuevos_asientos_ocupados

    @property
    def ubicacion_real(self):
        return self.__ubicacion_real
    @ubicacion_real.setter
    def ubicacion_real(self, nueva_ubicacion_real):
        self.__ubicacion_real = nueva_ubicacion_real

    @property
    def ruta(self):
        return self.__ruta
    @ruta.setter
    def ruta(self, nueva_ruta):
        self.__ruta = nueva_ruta

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    @property
    def origen(self):
        return self.__origen
    @origen.setter
    def origen(self, nuevo_origen):
        self.__origen = nuevo_origen

    @property
    def destino(self):
        return self.__destino
    @destino.setter
    def destino(self, nuevo_destino):
        self.__destino = nuevo_destino