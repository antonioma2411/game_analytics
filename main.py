import csv
from librerias.videojuego import Videojuego  # Clase propia que representa un videojuego
import os


# Muestra el menú principal por pantalla
def pintarMenu():
    print("===== GAME ANALYTICS =====")
    print("1. Cargar fichero")
    print("2. Mostrar estadísticas")
    print("3. Exportar CSV transformado")
    print("4. Salir")


# Lee el CSV original y devuelve una lista de objetos Videojuego
# Si hay error, devuelve lista vacía
def cargarFichero():
    lista_juegos = []  # Se crea antes del try para que siempre exista
    try:
        with open(r'C:\Users\antonioma2411\Desktop\game_analytics\datos\videojuegos.csv', encoding="utf-8") as f:
            data = csv.reader(f)
            cabecera = next(data)  # Se salta la cabecera

            for fila in data:
                juego = Videojuego(
                    id_juego=fila[0],
                    titulo=fila[1],
                    genero=fila[2],
                    precio=float(fila[3]),          # ValueError si no es número
                    horas_jugadas=float(fila[4]),
                    valoracion=float(fila[5])
                )
                lista_juegos.append(juego)

    except FileNotFoundError:
        print("ERROR: No existe el fichero indicado.")
        return []
    except ValueError:
        print("ERROR: El precio contiene valores no válidos.")
        return []

    return lista_juegos


# Calcula una media: suma total entre cantidad de elementos
def avg(num1, lenNum):
    avg = num1 / lenNum
    return avg


# Calcula y muestra el total de juegos, horas medias y precio medio
def mostrarEstadisticas(lista_juegos):

    precioMedio = 0
    horasMedia = 0

    for juego in lista_juegos:
        precioMedio = precioMedio + juego.precio
        horasMedia = horasMedia + juego.horas_jugadas

    precioMedio = avg(precioMedio, len(lista_juegos))
    horasMedia = avg(horasMedia, len(lista_juegos))

    print("=====Estadisticas Generales=====")
    print(f"Total Juegos:          {len(lista_juegos)}")
    print(f"Horas medias:          {horasMedia:.2f}H")
    print(f"Precio medio:          {precioMedio:.2f}€")


# Escribe un nuevo CSV con los datos transformados
def exportarCSV(lista_juegos):
    try:
        with open(r'C:\Users\antonioma2411\Desktop\game_analytics\datos\videojuegos_transformado.csv', mode="w", encoding="utf-8", newline="") as f:
            escritor = csv.writer(f)

            cabecera = [
                "id", "titulo", "genero", "precio",
                "horas_jugadas", "valoracion",
                "categoria_precio", "nivel_dedicacion"
            ]
            escritor.writerow(cabecera)

            for juego in lista_juegos:
                escritor.writerow(juego.filaCSV())

    except FileNotFoundError:
        print("ERROR: No existe el fichero indicado.")
    except ValueError:
        print("ERROR: El precio contiene valores no válidos.")


# Bandera: indica si ya se cargó el fichero
ficheroCargado = False

# Bucle principal
while True:
    pintarMenu()
    opcion = input("Selecciona una opción (1-4): ").strip()

    match opcion:
        case "1":
            lista_juegos = cargarFichero()
            # Solo se marca como cargado si la lista tiene datos
            if lista_juegos:
                ficheroCargado = True
                print("Fichero cargado correctamente.")
            else:
                ficheroCargado = False

        case "2":
            if ficheroCargado:
                mostrarEstadisticas(lista_juegos)
            else:
                print("El fichero no está cargado")

        case "3":
            if ficheroCargado:
                exportarCSV(lista_juegos)
            else:
                print("El fichero no está cargado")

        case "4":
            print("Saliendo de la aplicación. ¡Hasta pronto!")
            break

        case _:
            print("Opción no válida. Por favor, introduce un número del 1 al 4.")