from librerias import *

def reglas():
    print("Estas son las reglas")

def iniciar_juego():
    print("Aqui veremos el juego")

def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def salir():
    print("Hasta luego")
    sys.exit()

'''
Función agregar barco: para el tablero de turno (jugador o máquina), coloca un barco, de eslora tamano_barco, aleatoriamente.
'''

barcos = {
    "barco_1_eslora" : 4,
    "barco_2_eslora" : 3,
    "barco_3_eslora" : 2,
    "barco_4_eslora" : 1,
}



def crear_tablero(filas, columnas):
    return np.full((filas, columnas), "🌊", dtype=str)

def colocar_barcos(tablero, barcos):
    for tamano_barco in barcos.values():
        agregar_barco(tablero, tamano_barco)


def agregar_barco(tablero, tamano_barco): # esta es la variable principal
    direccion = random.choice(['norte', 'sur', 'este', 'oeste'])
    if direccion == 'norte':
        fila_inicio = random.randint(tamano_barco - 1, len(tablero) - 1)
        columna_inicio = random.randint(0, len(tablero[0]) - 1)
        if fila_inicio - tamano_barco + 1 >= 0:
            for i in range(fila_inicio, fila_inicio - tamano_barco, -1):
                if tablero[i][columna_inicio] != "🌊":
                    return False
            for i in range(fila_inicio, fila_inicio - tamano_barco, -1):
                tablero[i][columna_inicio] = "B"
            return True
        
    elif direccion == 'sur':
        fila_inicio = random.randint(0, len(tablero) - tamano_barco)
        columna_inicio = random.randint(0, len(tablero[0]) - 1)
        if fila_inicio + tamano_barco <= len(tablero):
            for i in range(fila_inicio, fila_inicio + tamano_barco):
                if tablero[i][columna_inicio] != " ":
                    return False
            for i in range(fila_inicio, fila_inicio + tamano_barco):
                tablero[i][columna_inicio] = "B"
            return True
        
    elif direccion == 'este':
        fila_inicio = random.randint(0, len(tablero) - 1)
        columna_inicio = random.randint(0, len(tablero[0]) - tamano_barco)
        if columna_inicio + tamano_barco <= len(tablero[0]):
            for i in range(columna_inicio, columna_inicio + tamano_barco):
                if tablero[fila_inicio][i] != " ":
                    return False
            for i in range(columna_inicio, columna_inicio + tamano_barco):
                tablero[fila_inicio][i] = "B"
            return True
        
    elif direccion == 'oeste':
        fila_inicio = random.randint(0, len(tablero) - 1)
        columna_inicio = random.randint(tamano_barco - 1, len(tablero[0]) - 1)
        if columna_inicio - tamano_barco + 1 >= 0:
            for i in range(columna_inicio, columna_inicio - tamano_barco, -1):
                if tablero[fila_inicio][i] != " ":
                    return False
            for i in range(columna_inicio, columna_inicio - tamano_barco, -1):
                tablero[fila_inicio][i] = "B"
            return True

tamanos_barcos = list (barcos.values()) # creamos una lista con los valores o eslora de los barcos


#llamamos a la funcion agregar_barco(matriz_espacios, tamanos_barcos) metiendo los parametros del diccionario
tablero_jug_1 = crear_tablero(10, 10)
tablero_jug_2 = crear_tablero(10, 10)

colocar_barcos(tablero_jug_1, barcos)
colocar_barcos(tablero_jug_2, barcos)



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

def juego():
    barcos_hundidos_humano = 0
    barcos_hundidos_maquina = 0
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

juego()
