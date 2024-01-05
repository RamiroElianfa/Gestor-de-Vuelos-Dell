from claseAerolinea import Aerolinea
from claseAvion import Avion
from claseVuelo import Vuelo

aerolineas = {}
contador = 0  

while True:
    opcion = int(input("""Bienvenido al Gestor de reservas de vuelos           
    Seleccione la opción que desea realizar

    1. Administrar aerolineas
    2. Administrar aviones
    3. Administrar vuelos
    0. Salir
    """)) 

    if opcion == 0: 
        break

    elif opcion == 1:

        while True:

            opcion2 = int(input("""Seleccione la opción que desea realizar
            1. Registrar Aerolinea
            2. Ver todas las Aerolineas
            0. Salir"""))

            if opcion2 == 0:
                break

            if opcion2 == 1:

                nombre_aerolinea = input("Nombre de la Aerolinea: ")
                iata_aerolinea = input("IATA de la aerolinea: ")
                aerolinea = Aerolinea(nombre_aerolinea, iata_aerolinea)
                
                contador += 1
                aerolineas[contador] = aerolinea

            if opcion2 == 2:
                #Traer los valores del diccionario e inmprimirlos en orden alfabetico
                pass


    elif opcion == 2:

        while True:
        
            opcion2 = int(input("""Seleccione la opción que desea realizar
            1. Registrar Avion
            0. Salir"""))

            if opcion2 == 0:
                break

            if opcion2 == 1:

                fabricante = input("Fabricante: ")
                modelo = input("Modelo: ")
                matricula = input("Matricula: ")
                capacidad_max = int(input("Capacidad Maxima: "))

                aerolineas_valores = list(aerolineas.values())
                
                for clave, valor in aerolineas:
                    print("{0} - {1}".format(clave, valor.aero_nombre))

                eleccion_aero = int(input("Elige la aerolinea dueña: "))
                if eleccion_aero in range(1, len(aerolineas_valores) + 1):

                    aerolinea_elegida = aerolineas[eleccion_aero]

                    avion = Avion(aerolinea_elegida, fabricante, modelo, matricula, capacidad_max)

                else:                   
                    print("No se logró registrar el avión exitosamente.")

    elif opcion == 3:

        while True:

            opcion2 = int(input("""Seleccione la opción que desea realizar
            1. Registrar Vuelo
            0. Salir"""))

            if opcion2 == 0:
                break

            if opcion2 == 1:

                aerolineas_valores = list(aerolineas.values())
                
                for clave, valor in aerolineas:
                    print("{0} - {1}".format(clave, valor.aero_nombre))

                eleccion_aero = int(input("Elige la aerolinea dueña: "))

                #Este if else lo podria hacer la misma clase Aerolinea
                if not eleccion_aero.aviones:
                    print("La aerolinea elegida no tiene aviones con los cuales volar.")

                else:
                    eleccion_aero.imprimir_aviones_con_indice()

                eleccion_avion = int(input("Elige el avion a volar: "))

                #Creo que aca deberia haber un while
                if eleccion_aero.verificar_eleccion_avion(eleccion_avion) == True:
                    avion_elegido = eleccion_aero.aviones[eleccion_avion]

                else:
                    print("El numero de avion no esta definido.")

                codigo = input("Codigo: ")
                ubicacion_real = input("Ubicación actual del avión: ")
                ruta = input("Ruta: ")
                estado = input("Estado: ")
                origen = input("Origen: ")
                destino = input("Destino: ")

                #Instanciar el objeto vuelo








            
