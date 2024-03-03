import pandas as pd
import numpy as np
import random

barcos = {
    "barco_1_eslora" : 4,
    "barco_2_eslora" : 3,
    "barco_3_eslora" : 2,
    "barco_4_eslora" : 1,
}

## Esta funcion de crear tablero sobra lo indico como variables ##
#def crear_tablero(filas, columnas):
 #   return np.full((filas, columnas), "", dtype=str)

# Inicio los tableros como variables porque me parece mas sencillos para llamarlos luego

tablero_jug_1 = np.full((10, 10), " ", dtype=str)
tablero_jug_2 = np.full ((10,10), " ", dtype= str)



def agregar_barco(tablero, tamano_barco): # esta es la variable principal
    direccion = random.choice(['norte', 'sur', 'este', 'oeste'])
    if direccion == 'norte':
        fila_inicio = random.randint(tamano_barco - 1, len(tablero) - 1)
        columna_inicio = random.randint(0, len(tablero[0]) - 1)
        if fila_inicio - tamano_barco + 1 >= 0:
            for i in range(fila_inicio, fila_inicio - tamano_barco, -1):
                if tablero[i][columna_inicio] != " ":
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
for tamano_barco in tamanos_barcos:
    
    resultado = agregar_barco(tablero_jug_1, tamano_barco)
    resultado2 = agregar_barco (tablero_jug_2, tamano_barco)


    
        


print (tablero_jug_1)
print (tablero_jug_2)

"""
AQUi TERMINA LA FUNCION COLOCAR BARCOS RANDOM 
                Y
AQUI EMPIEZA LA FUNCION DE ATAQUE que son varias

"""


def atacar(tablero_oponente):
    while True:
        fila_ataque = int(input("Ingresa la fila para el ataque (0-9): "))
        columna_ataque = int(input("Ingresa la columna para el ataque (0-9): "))
        
        # Validar las coordenadas
        if fila_ataque < 0 or fila_ataque >= len(tablero_oponente) or columna_ataque < 0 or columna_ataque >= len(tablero_oponente[0]):
            print("Coordenadas fuera de los límites del tablero. Intenta nuevamente.")
            continue  # Reinicia el bucle si las coordenadas son inválidas

        coordenadas_atacadas = (fila_ataque, columna_ataque)

        if tablero_oponente[fila_ataque][columna_ataque] == "X" or tablero_oponente[fila_ataque][columna_ataque] == "O":
            print("Ya has atacado estas coordenadas. Intenta nuevamente.")
            continue  # Reinicia el bucle si ya se atacaron esas coordenadas

        # Verificar si el ataque impacta en un barco del oponente
        if tablero_oponente[fila_ataque][columna_ataque] == "B":
            tablero_oponente[fila_ataque][columna_ataque] = 'X'  # Marcar como impactado en el tablero del oponente
            mensaje = "¡Impacto!"
            exito = True
        else:
            tablero_oponente[fila_ataque][columna_ataque] = 'O'  # Marcar como agua en el tablero del oponente
            mensaje = "Agua"
            exito = True

        return mensaje, exito, coordenadas_atacadas




def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))


def juego():
    vidas_humano = 10
    vidas_maquina = 10

    while vidas_humano > 0 and vidas_maquina > 0:
        print("Turno del Jugador Humano:")
        mensaje, exito, coordenadas = atacar(tablero_jug_2)
        print(mensaje)

        if exito:
            vidas_maquina -= 1

        print(f"Vidas restantes del Jugador Máquina: {vidas_maquina}")

        if vidas_maquina == 0:
            print("¡El Jugador Humano ha ganado!")
            break

        print("\nTurno del Jugador Máquina:")
        mensaje, exito, coordenadas = atacar(tablero_jug_1)
        print(mensaje)

        if exito:
            vidas_humano -= 1

        print(f"Vidas restantes del Jugador Humano: {vidas_humano}")

        if vidas_humano == 0:
            print("¡El Jugador Máquina ha ganado!")

# Llamada a la función juego
juego()
