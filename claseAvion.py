import claseAerolinea

class Avion:
    def __init__(self, aerolinea, fabricante, modelo, matricula, capacidad_max):
        self.__aerolinea = aerolinea
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__matricula = matricula
        self.__capacidad_max = capacidad_max
        self.__cantidad_vuelos = 0
        self.__combustible = False

    @property
    def aerolinea(self):
        return self.__aerolinea
    @aerolinea.setter
    def aerolinea(self,nueva_aerolinea):
        self.__aerolinea = nueva_aerolinea

    @property
    def fabricante(self):
        return self.__fabricante
    @fabricante.setter
    def fabricante(self,nuevo_fabricante):
        self.__fabricante = nuevo_fabricante

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self,nuevo_modelo):
        self.__modelo = nuevo_modelo

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,nueva_matricula):
        self.__matricula = nueva_matricula

    @property
    def capacidad_max(self):
        return self.__capacidad_max
    @capacidad_max.setter
    def capacidad_max(self,nueva_capacidad_max):
        self.__capacidad_max = nueva_capacidad_max

    @property
    def cantidad_vuelos(self):
        return self.__cantidad_vuelos
    @cantidad_vuelos.setter
    def cantidad_vuelos(self,nueva_cantidad_vuelos):
        self.__cantidad_vuelos = nueva_cantidad_vuelos

    @property
    def combustible(self):
        return self.__combustible
    @combustible.setter
    def combustible(self,nueva_combustible):
        self.__combustible = nueva_combustible
    