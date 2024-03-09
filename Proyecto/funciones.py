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

def agregar_barcos_peques(tablero, barcos_peques):
    for tamano_barco, cantidad in barcos_peques.items():
        for i in range(cantidad):
            exito = False
            while not exito:
                exito, posiciones_barco = agregar_barco(tablero, int(tamano_barco))
                
                # Si la colocación del barco fue exitosa, puedes hacer algo con las posiciones
                if exito:
                    print(f"Barco de tamaño {tamano_barco} agregado en posiciones: {posiciones_barco}")
                else:
                    print(f"No se pudo colocar el barco de tamaño {tamano_barco}. Reintentando...")


# Diccionario con información de barcos pequeños
barcos = {
    "barcos_pos_1": 4,
    "barcos_pos_2": 3,
    "barcos_pos_3": 2,
    "barcos_pos_4": 1
    # Otras claves y valores para el jugador 1
}


def agregar_barco (tablero, tamano_barco):
    direccion = random.choice(['norte', 'sur', 'este', 'oeste'])
    posiciones_barco = []

    if direccion == 'norte':
        fila_inicio = random.randint(tamano_barco - 1, len(tablero) - 1)
        columna_inicio = random.randint(0, len(tablero[0]) - 1)
        if fila_inicio - tamano_barco + 1 >= 0:
            for i in range(fila_inicio, fila_inicio - tamano_barco, -1):
                if tablero[i][columna_inicio] != "🌊":
                    return False, []
                posiciones_barco.append((i, columna_inicio))
            for i in range(fila_inicio, fila_inicio - tamano_barco, -1):
                tablero[i][columna_inicio] = "B"
            return True, posiciones_barco

    elif direccion == 'sur':
        fila_inicio = random.randint(0, len(tablero) - tamano_barco)
        columna_inicio = random.randint(0, len(tablero[0]) - 1)
        if fila_inicio + tamano_barco <= len(tablero):
            for i in range(fila_inicio, fila_inicio + tamano_barco):
                if tablero[i][columna_inicio] != "🌊":
                    return False, []
                posiciones_barco.append((i, columna_inicio))
            for i in range(fila_inicio, fila_inicio + tamano_barco):
                tablero[i][columna_inicio] = "B"
            return True, posiciones_barco

    elif direccion == 'este':
        fila_inicio = random.randint(0, len(tablero) - 1)
        columna_inicio = random.randint(0, len(tablero[0]) - tamano_barco)
        if columna_inicio + tamano_barco <= len(tablero[0]):
            for i in range(columna_inicio, columna_inicio + tamano_barco):
                if tablero[fila_inicio][i] != "🌊":
                    return False, []
                posiciones_barco.append((fila_inicio, i))
            for i in range(columna_inicio, columna_inicio + tamano_barco):
                tablero[fila_inicio][i] = "B"
            return True, posiciones_barco

    elif direccion == 'oeste':
        fila_inicio = random.randint(0, len(tablero) - 1)
        columna_inicio = random.randint(tamano_barco - 1, len(tablero[0]) - 1)
        if columna_inicio - tamano_barco + 1 >= 0:
            for i in range(columna_inicio, columna_inicio - tamano_barco, -1):
                if tablero[fila_inicio][i] != "🌊":
                    return False, []
                posiciones_barco.append((fila_inicio, i))
            for i in range(columna_inicio, columna_inicio - tamano_barco, -1):
                tablero[fila_inicio][i] = "B"
            return True, posiciones_barco


# Crear el tablero
tablero_jug_1 = crear_tablero(10, 10)
tablero_jug_2 = crear_tablero (10,10)

# Obtener los barcos pequeños del diccionario
barcos_peques = {k.split("_")[2]: v for k, v in barcos.items() if "pos" in k}
print (barcos_peques)




def atacar(tablero_oponente, fila_ataque=None, columna_ataque=None, turno_jugador=True):
    while True:
        try:
            if turno_jugador:
                if fila_ataque is None:
                    fila_ataque = int(input("Ingresa la fila para el ataque (0-9): "))
                if columna_ataque is None:
                    columna_ataque = int(input("Ingresa la columna para el ataque (0-9): "))
            else:
                if fila_ataque is None:
                    fila_ataque = random.randint(0, len(tablero_oponente) - 1)
                if columna_ataque is None:
                    columna_ataque = random.randint(0, len(tablero_oponente[0]) - 1)
            
            # Validar las coordenadas
            if fila_ataque < 0 or fila_ataque >= len(tablero_oponente) or columna_ataque < 0 or columna_ataque >= len(tablero_oponente[0]):
                print("Coordenadas fuera de los límites del tablero. Intenta nuevamente.")
                fila_ataque = None
                columna_ataque = None
                continue  # Reinicia el bucle si las coordenadas son inválidas

            coordenadas_atacadas = (fila_ataque, columna_ataque)

            if tablero_oponente[fila_ataque][columna_ataque] == "X" or tablero_oponente[fila_ataque][columna_ataque] == "O":
                print("Ya has atacado estas coordenadas. Intenta nuevamente.")
                  # Reinicia el bucle si ya se atacaron esas coordenadas
                fila_ataque = None
                columna_ataque = None
                continue
            # Verificar si el ataque impacta en un barco del oponente
            if tablero_oponente[fila_ataque][columna_ataque] == "B":
                tablero_oponente[fila_ataque][columna_ataque] = 'X'  # Marcar como impactado en el tablero del oponente
                mensaje = "¡Impacto!"
                
            else:
                tablero_oponente[fila_ataque][columna_ataque] = 'O'  # Marcar como agua en el tablero del oponente
                mensaje = "Agua"

            print(mensaje)

            return True, coordenadas_atacadas, mensaje

        except ValueError:
            print("Por favor, ingresa un número válido.")



def hundidos (tablero):
    contador = 0
    for fila in tablero:
        for casilla in fila:
            if casilla == "X":
                contador += 1
    return contador

def imprimir_tablero(tablero, ocultar_barcos=False, mostrar_ataques=False):
    
    for fila_index, fila in enumerate(tablero):
        fila_mostrar = []
        for columna_index, casilla in enumerate(fila):
            if ocultar_barcos and casilla == "B":
                fila_mostrar.append(" 🌊 ")
            elif mostrar_ataques and casilla in ["X", "O"]:
                fila_mostrar.append(f" {casilla} ")
            else:
                fila_mostrar.append(" 🌊 ")  # Símbolo de mar

        # Imprimir el número de fila, la fila con sus elementos y el marco lateral
        print(f"{fila_index} |{'|'.join(map(str, fila_mostrar))}|")



def ataque_maquina(tablero_oponente):
    # Generar coordenadas aleatorias
    fila_ataque = random.randint(0, len(tablero_oponente) - 1)
    columna_ataque = random.randint(0, len(tablero_oponente[0]) - 1)

    # Atacar utilizando la función existente
    mensaje, _, _ = atacar(tablero_oponente, fila_ataque, columna_ataque)
    print(f"fila de ataque  {fila_ataque} \n columna de ataque {columna_ataque}")
    print (mensaje)
    time.sleep(3)

def iniciar_juego():
    barcos_hundidos_humano = 0
    barcos_hundidos_maquina = 0
    
    print ("Barcos del Jugador Humano \n")
    agregar_barcos_peques(tablero_jug_1, barcos_peques)
    print(tablero_jug_1)
    time.sleep(3)
    limpiar_pantalla ()
    
    print ("Barcos del Jugador Maquina \n")
    agregar_barcos_peques(tablero_jug_2, barcos_peques)
    print (tablero_jug_2)
    time.sleep(10)
    limpiar_pantalla ()
    

    turno = random.choice(["humano", "maquina"])

    while barcos_hundidos_humano < 10 and barcos_hundidos_maquina < 10:
        os.system("cls" if os.name == "nt" else "clear")

        if turno == "humano":
            print("\nTablero del Jugador Humano:")
            imprimir_tablero(tablero_jug_2, ocultar_barcos=True, mostrar_ataques=True)

            print("\nTurno del Jugador Humano:")
            atacar(tablero_jug_2, turno_jugador=True)
            #imprimir_tablero(tablero_jug_2, ocultar_barcos=True)

            barcos_hundidos_maquina = hundidos(tablero_jug_2)
            print(f"Barcos hundidos del jugador máquina: {barcos_hundidos_maquina}")
            time.sleep (2)

            if barcos_hundidos_maquina == 10:
                print("¡El Jugador Humano ha ganado!")
                break

            turno = "maquina"

        elif turno == "maquina":
            print("\nTablero del Jugador Máquina:")
            imprimir_tablero(tablero_jug_1, ocultar_barcos=True)

            print("\nTurno del Jugador Máquina:")
            ataque_maquina(tablero_jug_1)
            imprimir_tablero(tablero_jug_1, ocultar_barcos=True, mostrar_ataques=True)

            barcos_hundidos_humano = hundidos(tablero_jug_1)
            print(f"Barcos hundidos del Jugador Máquina: {barcos_hundidos_humano}")
            time.sleep (2)

            if barcos_hundidos_humano == 10:
                print("¡El Jugador Máquina ha ganado!")
                break

            turno = "humano"
            time.sleep(1)

        continuar_jugando = input("Presiona ENTER para seguir jugando o escribe 'salir' para rendirte: ")
        if continuar_jugando.lower() == "salir":
            salir()

