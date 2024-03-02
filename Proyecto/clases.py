from librerias import *

# CREAMOS LA CLASE TABLERO
class TableroFlota():

    # Función de inicialización. Entradas: jugador, barcos (nº y tamaño) y dimensión del tablero.
    def __init__(self, jugador, barcos, dimension=10):
        self.jugador = jugador
        self.dimension = dimension
        self.barcos = barcos

    # Función para colocar los barcos al principio del juego.
    def colocar_barcos(self):
        for barco in self.barcos: # Recorremos el diccionario de barcos
            while True:
                x = random.randint(0, self.dimension - 1)
                y = random.randint(0, self.dimension - 1)
                orientacion = random.choice(['h', 'v'])
                
                if self.posicion_valida(x, y, orientacion, barco.longitud):
                    if orientacion == 'h':
                        for i in range(barco.longitud):
                            self.tablero[y][x + i] = 1
                    elif orientacion == 'v':
                        for i in range(barco.longitud):
                            self.tablero[y + i][x] = 1
                    break

    def posicion_valida(self, x, y, orientacion, longitud):
        if orientacion == 'h' and x + longitud > self.dimension:
            return False
        elif orientacion == 'v' and y + longitud > self.dimension:
            return False
        
        for i in range(longitud):
            if orientacion == 'h':
                if self.tablero[y][x + i] == 1:
                    return False
            elif orientacion == 'v':
                if self.tablero[y + i][x] == 1:
                    return False
        
        return True
    
    def imprimir_tablero(self):
        print("Tablero de", self.jugador)
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.tablero[i][j] == 1:
                    print("O", end=" ")
                else:
                    print("~", end=" ")
            print(" ", i)
