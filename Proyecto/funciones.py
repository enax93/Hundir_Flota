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


#funcion para atacar 

def atacar(tablero_oponente, fila, columna, coordenadas_atacadas):
    # Validar las coordenadas
    if fila < 0 or fila >= len(tablero_oponente) or columna < 0 or columna >= len(tablero_oponente[0]):
        return "Coordenadas fuera de los límites del tablero", False
    
    # Verificar si las coordenadas ya han sido atacadas previamente
    if (fila, columna) in coordenadas_atacadas:
        return "Ya has atacado estas coordenadas", False
    
    # Verificar si el ataque impacta en un barco del oponente
    if tablero_oponente[fila][columna] == 1:  # 1 representa un barco en el tablero del oponente
        tablero_oponente[fila][columna] = 'X'  # Marcar como impactado en el tablero del oponente
        coordenadas_atacadas.add((fila, columna))  # Agregar coordenadas a las atacadas
        return "¡Impacto!", True
    else:
        tablero_oponente[fila][columna] = 'O'  # Marcar como agua en el tablero del oponente
        coordenadas_atacadas.add((fila, columna))  # Agregar coordenadas a las atacadas
        return "Agua", True
    

# funcion para recibir ataque 

def recibir_ataque(tablero_jugador, fila, columna, coordenadas_atacadas):
    # Validar las coordenadas
    if fila < 0 or fila >= len(tablero_jugador) or columna < 0 or columna >= len(tablero_jugador[0]):
        return "Coordenadas fuera de los límites del tablero", False
    
    # Verificar si las coordenadas ya han sido atacadas previamente
    if (fila, columna) in coordenadas_atacadas:
        return "Ya has recibido un ataque en estas coordenadas", False
    
    # Verificar si el ataque impacta en un barco del jugador
    if tablero_jugador[fila][columna] == 1:  # 1 representa un barco en el tablero del jugador
        tablero_jugador[fila][columna] = 'X'  # Marcar como impactado en el tablero del jugador
        coordenadas_atacadas.add((fila, columna))  # Agregar coordenadas a las atacadas
        return "¡Impacto!", True
    else:
        tablero_jugador[fila][columna] = 'O'  # Marcar como agua en el tablero del jugador
        coordenadas_atacadas.add((fila, columna))  # Agregar coordenadas a las atacadas
        return "Agua", True