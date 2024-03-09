# DEFINICION DE LIBRERIAS
from librerias import *

# DEFINICION DE FUNCIONES
from funciones import *

# DEFINICION DE CLASES
from clases import *

# DEFINICION DE VARIABLES
from variables import *

def main():
    while True:

        print("1. Reglas del juego \n")
        print("2. Iniciar el juego \n")
        print("3. Salir \n")
        limpiar_pantalla ()

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            reglas()

        elif opcion == "2":
            iniciar_juego()

        elif opcion == "3":
            salir()

        else:
            print("La opción seleccionada no existe. Presione Enter para continuar.")
            input()
            limpiar_pantalla()

if __name__ == "__main__":
    limpiar_pantalla()
    main()

main ()