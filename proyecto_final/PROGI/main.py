import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulos_main import menu_usuarios
from inicio_sesion import iniciar_sesion
from registros_pluviales import menu_registros_pluviales
#from BDII import index


def main():
    salir = False

    while not salir:
        print('-----> MENÚ PRINCIPAL <-----')
        print('1. USUARIOS Y ACCESOS') #menu_usuarios
        print('2. INICIAR SESIÓN') #menu_stock_granel
        print('3. ANÁLISIS DE DATOS')
        print('4. SALIR')

        opcion = input("Seleccione una opción: ")
            
        if opcion == '1':
            menu_usuarios()
        elif opcion == '2':
            sesion_iniciada=iniciar_sesion()
             
            if sesion_iniciada is True:                                 
                from BDII import index
                index.menu_stock_granel()


        elif opcion == '3':
            menu_registros_pluviales()
        elif opcion == '4':
            print("Saliendo de la aplicación.")
            salir = True
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == '__main__':
    main()