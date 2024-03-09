from librerias import *
from clases import *
from variables import *


def reglas():
    print("Reglas del Juego 'Hundir la Flota'\n")

    print("1. Objetivo del Juego:")
    print("   - El objetivo principal del juego es hundir todos los barcos del oponente antes de que este hunda los tuyos.\n")

    print("2. Tablero de Juego:")
    print("   - Cada jugador tiene un tablero cuadriculado donde se colocan sus barcos. Este tablero está dividido en filas y columnas de 10x10 celdas.\n")

    print("3. Colocación de Barcos:")
    print("   - Cada jugador tiene una flota de barcos de diferentes longitudes (barcos de 4, 3, 2 y 1 celdas).")
    print("   - Antes de empezar, se colocan los barcos de cada jugador de forma aleatoria.\n")

    print("4. Turnos de Ataque:")
    print("   - El juego se juega por turnos, iniciando por el jugador. En cada turno, un jugador realiza un ataque lanzando un misil a una coordenada del tablero.")
    print("   - Si el misil impacta en una celda ocupada por un barco, se considera un '¡Impacto!' y se marca en el tablero del oponente con una 'X'. Si el misil cae al agua, se marca con una 'O'.\n")

    print("5. Hundir Barcos:")
    print("   - Un barco se considera hundido cuando todas sus celdas han sido impactadas. El jugador es informado cuando un oponente haya hundido uno de sus barcos.\n")

    print("6. Final del Juego:")
    print("   - El juego continúa hasta que todos los barcos de un jugador hayan sido hundidos.")
    print("   - El jugador que hunda todos los barcos del oponente primero, gana la partida.\n")

    print("7. Repetir o Rendirse:")
    print("   - Después de cada turno, el jugador puede optar por seguir jugando o rendirse.")
    print("   - Para seguir jugando, simplemente presiona 'Enter' para pasar al siguiente turno.")
    print("   - Para rendirse, escribe 'salir' cuando se le solicite y se dará por terminada la partida.\n")

    print("8. Disfruta y dejános tus comentarios para una siguiente versión:")

    opcion = input("Presiona Enter para iniciar el juego o escribe 'salir' para terminarlo: ")
    if opcion.lower() == "salir":
        salir()
    limpiar_pantalla()
    iniciar_juego()


def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def salir():
    print("Hasta luego")
    sys.exit()

def crear_tablero(filas, columnas):
    return np.full((filas, columnas), "🌊", dtype=str)

def colocar_barcos(tablero, barcos):
    for tamano_barco in barcos.values():
        agregar_barco(tablero, tamano_barco)


def agregar_barco(tablero, tamano_barco):
    direccion = random.choice(['norte', 'sur', 'este', 'oeste'])

    if direccion == 'norte':
        fila_inicio = random.randint(tamano_barco - 1, len(tablero) - 1)
        columna_inicio = random.randint(0, len(tablero[0]) - 1)

        if fila_inicio - tamano_barco + 1 >= 0 and all(tablero[i][columna_inicio] == "🌊" for i in range(fila_inicio, fila_inicio - tamano_barco, -1)):
            for i in range(fila_inicio, fila_inicio - tamano_barco, -1):
                tablero[i][columna_inicio] = "B"
            return True

    elif direccion == 'sur':
        fila_inicio = random.randint(0, len(tablero) - tamano_barco)
        columna_inicio = random.randint(0, len(tablero[0]) - 1)

        if fila_inicio + tamano_barco <= len(tablero) and all(tablero[i][columna_inicio] == "🌊" for i in range(fila_inicio, fila_inicio + tamano_barco)):
            for i in range(fila_inicio, fila_inicio + tamano_barco):
                tablero[i][columna_inicio] = "B"
            return True

    elif direccion == 'este':
        fila_inicio = random.randint(0, len(tablero) - 1)
        columna_inicio = random.randint(0, len(tablero[0]) - tamano_barco)

        if columna_inicio + tamano_barco <= len(tablero[0]) and all(tablero[fila_inicio][i] == "🌊" for i in range(columna_inicio, columna_inicio + tamano_barco)):
            for i in range(columna_inicio, columna_inicio + tamano_barco):
                tablero[fila_inicio][i] = "B"
            return True

    elif direccion == 'oeste':
        fila_inicio = random.randint(0, len(tablero) - 1)
        columna_inicio = random.randint(tamano_barco - 1, len(tablero[0]) - 1)

        if columna_inicio - tamano_barco + 1 >= 0 and all(tablero[fila_inicio][i] == "🌊" for i in range(columna_inicio, columna_inicio - tamano_barco, -1)):
            for i in range(columna_inicio, columna_inicio - tamano_barco, -1):
                tablero[fila_inicio][i] = "B"
            return True

    return False


def atacar(tablero_oponente, coordenadas_atacadas=None, turno_jugador=True):
    while True:
        try:
            if turno_jugador:
                fila_ataque = int(input(f"Ingresa la fila para el ataque (0-9): "))
                columna_ataque = int(input("Ingresa la columna para el ataque (0-9): "))

            else:
                fila_ataque = random.randint(0, len(tablero_oponente) - 1)
                columna_ataque = random.randint(0, len(tablero_oponente[0]) - 1)

            coordenadas_atacadas_actual = (fila_ataque, columna_ataque)

            if coordenadas_atacadas and coordenadas_atacadas_actual in coordenadas_atacadas:
                print("Ya has atacado estas coordenadas. Intenta nuevamente.")
                continue

            if tablero_oponente[fila_ataque][columna_ataque] == "B":
                tablero_oponente[fila_ataque][columna_ataque] = 'X'
                mensaje = "¡Impacto!"
            else:
                tablero_oponente[fila_ataque][columna_ataque] = 'O'
                mensaje = "Agua"

            print(mensaje)

            return True, coordenadas_atacadas_actual, mensaje

        except ValueError:
            print("Por favor, ingresa un número válido para las coordenadas.")
        except IndexError:
            print("Coordenadas fuera de los límites del tablero.")


def hundidos(tablero, barcos):
    total_longitud_barcos = sum(barcos.values())
    contador = 0

    for fila in tablero:
        for casilla in fila:
            if casilla == "X":
                contador += 1

    return contador == total_longitud_barcos


def imprimir_tablero(tablero, ocultar_barcos=False, mostrar_ataques=False):
    for fila_index, fila in enumerate(tablero):
        fila_mostrar = []
        for columna_index, casilla in enumerate(fila):
            if ocultar_barcos and casilla == "B":
                fila_mostrar.append(" 🌊 ")
            elif mostrar_ataques and casilla in ["X", "O"]:
                fila_mostrar.append(f" {casilla} ")
            else:
                fila_mostrar.append(" 🌊 ")

        print(f"{fila_index} |{'|'.join(map(str, fila_mostrar))}|")


def ataque_maquina(tablero_oponente, coordenadas_atacadas_maquina):
    while True:
        fila_ataque = random.randint(0, len(tablero_oponente) - 1)
        columna_ataque = random.randint(0, len(tablero_oponente[0]) - 1)

        if (fila_ataque, columna_ataque) in coordenadas_atacadas_maquina:
            continue

        if tablero_oponente[fila_ataque][columna_ataque] == "B":
            tablero_oponente[fila_ataque][columna_ataque] = 'X'
            mensaje = "¡Impacto!"
            coordenadas_atacadas_actual = (fila_ataque, columna_ataque)
            print(f"Fila de ataque: {fila_ataque}\nColumna de ataque: {columna_ataque}")
            print("Coordenadas atacadas actualmente:", [coordenadas_atacadas_actual])
            time.sleep(3)
        else:
            mensaje = "Agua"
            coordenadas_atacadas_actual = (fila_ataque, columna_ataque)
            print(f"Fila de ataque: {fila_ataque}\nColumna de ataque: {columna_ataque}")
            print("Coordenadas atacadas actualmente:", [coordenadas_atacadas_actual])
            break

    return True, coordenadas_atacadas_actual, mensaje


def iniciar_juego():
    
        tablero_jug_1 = crear_tablero(10,10)
        tablero_jug_2 = crear_tablero(10,10)

        colocar_barcos(tablero_jug_1, barcos)
        colocar_barcos(tablero_jug_2, barcos)

        barcos_hundidos_humano = 0
        barcos_hundidos_maquina = 0
        turno = "humano"
        coordenadas_atacadas_humano = []
        coordenadas_atacadas_maquina = []

        while not hundidos(tablero_jug_1, barcos) and not hundidos(tablero_jug_2, barcos):
            
            while True:
                limpiar_pantalla()

                if turno == "humano":
                    print("\nTablero del Jugador Humano:")
                    imprimir_tablero(tablero_jug_2, ocultar_barcos=True, mostrar_ataques=True)

                    print("\nTurno del Jugador Humano:")
                    _, coordenadas_atacadas_actual, mensaje = atacar(tablero_jug_2, coordenadas_atacadas_humano, turno_jugador=True)
                    coordenadas_atacadas_humano.append(coordenadas_atacadas_actual)

                    if mensaje == "¡Impacto!":
                        print(f"Impacto en {coordenadas_atacadas_actual}")
                        barcos_hundidos_maquina += 1
                        if barcos_hundidos_maquina == len(barcos):
                            print("Barco hundido del jugador máquina.")
                            time.sleep(2)
                        continue

                    if barcos_hundidos_maquina == len(barcos):
                        print("¡El Jugador Humano ha ganado!")
                        print()

                        print("Tablero del jugador")
                        print()
                        print(tablero_jug_1)

                        break

                    turno = "maquina"

                elif turno == "maquina":
                    '''print("\nTablero del Jugador Máquina:")
                    imprimir_tablero(tablero_jug_1, ocultar_barcos=True)'''

                    print("\nTurno del Jugador Máquina:")
                    _, coordenadas_atacadas_actual, mensaje = ataque_maquina(tablero_jug_1, coordenadas_atacadas_maquina)
                    coordenadas_atacadas_maquina.append(coordenadas_atacadas_actual)

                    imprimir_tablero(tablero_jug_1, ocultar_barcos=True, mostrar_ataques=True)

                    if mensaje == "¡Impacto!":
                        print(f"Impacto en {coordenadas_atacadas_actual}")
                        barcos_hundidos_humano += 1
                        if barcos_hundidos_humano == len(barcos):
                            print("Barco hundido del Jugador Humano.")
                            time.sleep(2)
                        continue
                    if barcos_hundidos_humano == len(barcos):
                        print("¡El Jugador Máquina ha ganado!")
                        print()

                        print("Tablero del jugador")
                        print()
                        print(tablero_jug_1)

                        break

                    turno = "humano"
                    time.sleep(1)
    
                continuar_jugando = input("Presiona ENTER para seguir jugando o escribe 'salir' para rendirte: ")
                if continuar_jugando.lower() == "salir":
                    salir()



