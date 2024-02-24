import sys
import os
import random
import numpy as np

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


while True:
    
    print("1. Reglas del juego \n")
    print("2. Iniciar el juego \n")
    print("3. Salir \n")

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