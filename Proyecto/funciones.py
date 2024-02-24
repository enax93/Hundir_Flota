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
