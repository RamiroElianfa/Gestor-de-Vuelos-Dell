class Aerolinea:

    aerolineas = []
    def __init__(self, aero_nombre, iata):
        
        self.__aero_nombre      =   aero_nombre
        self.__iata             =   iata
        self.__cant_aviones     =   0
        self.__aviones          =   []
        self.__vuelos           =   []
        self.__rutas            =   []
        
        print("Se ha agegado una nueva aerolinea:", aero_nombre)

    @property
    def aero_nombre(self):
        return self.__aero_nombre
    @aero_nombre.setter
    def aero_nombre(self,nuevo_nombre):
        self.__aero_nombre= nuevo_nombre

    @property
    def iata(self):
        return self.__iata
    @iata.setter
    def iata(self,nuevo_iata):
        self.__iata= nuevo_iata

    @property
    def cant_aviones(self):
        return self.__cant_aviones
    @cant_aviones.setter
    def cant_aviones(self, lista):
        nueva_cantidad = len(lista)
        self.__cant_aviones = nueva_cantidad

    @property
    def aviones(self):
        return self.__aviones
    @aviones.setter
    def aviones(self, nueva_lista):
        self.__aviones = nueva_lista

    def imprimir_aviones_con_indice(self):
        for indice, avion in enumerate(self.__aviones, 1):
            print(f"{indice}, Matrícula: {avion.matricula} - {avion.fabricante} {avion.modelo}")

    def verificar_eleccion_avion(self, eleccion):
        if eleccion in range(1, len(self.aviones) + 1):
            return True
        else:
            return False


    def agregar_avion(self, avion):
        aviones_actuales = self.aviones
        aviones_actuales.append(avion)
        self.aviones(aviones_actuales)
        self.cant_aviones(aviones_actuales)

    @property
    def vuelos(self):
        return self.__vuelos
    @vuelos.setter
    def vuelos(self, nueva_lista):
        self.__vuelos = nueva_lista

    def agregar_vuelo(self, vuelo):
        vuelos_actuales = self.vuelos
        vuelos_actuales.append(vuelo)
        self.vuelos(vuelos_actuales)

    @property
    def rutas(self):
        return self.__rutas
    @rutas.setter
    def rutas(self, nueva_lista):
        self.__rutas = nueva_lista

    def agregar_ruta(self, ruta):
        rutas_actuales = self.rutas
        rutas_actuales.append(ruta)
        self.vuelos(rutas_actuales)

    def __str__(self):
        return f'{self.aero_nombre}\nIATA {self.iata}\nFlota actual {self.cant_aviones}'


print("Prueba para Github")