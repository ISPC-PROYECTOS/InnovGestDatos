# Bienvenida al sistema
import sys
import os

# Agregar el directorio raíz del proyecto a sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from evidencia_1.modulos.ingreso import ingreso
from evidencia_1.modulos.registrar_usuario import registrar_usuario

def menu():
    print("TE DOY LA BIENVENIDA A NUESTRO SISTEMA")
    salir = False

    while not salir:
        print("MENU")
        print("1- INGRESO DE USUARIO")
        print("2- REGISTRAR USUARIO")
        print("3- SALIR")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ingreso()  
            break
        elif opcion == "2":
            registrar_usuario()  
            break
        elif opcion == "3":
            print("SALIENDO")
            salir = True  
        else:
            print("Opción incorrecta, vuelve a intentar")  

if __name__ == '__main__':
    menu()