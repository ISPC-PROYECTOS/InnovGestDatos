from modulos_main import menu_pricipal, menu_crud
from funciones_main import agregar_usuario, modificar_usuario,eliminar_usuario, buscar_usuario, mostrar_usuarios,
ordenar_usuarios_burbuja, ordenar_usuarios_sort
from inicio_sesion import iniciar_sesion

def main():
    salir = False

    while not salir:
        menu_pricipal()
        opcion_1 = int(input('Ingrese la opción elegida: '))
        if opcion_1 == 1:
            while not salir:
                menu_crud()
                opcion_2 = int(input('Ingrese la opción: '))
                if opcion_2 == 1:
                    agregar_usuario()
                elif opcion_2 == 2:
                    modificar_usuario()
                elif opcion_2 == 3:
                    eliminar_usuario()
                elif opcion_2 == 4:
                    buscar_usuario()
                elif opcion_2 == 5:
                    mostrar_usuarios()
                elif opcion_2 == 6:
                    ordenar_usuarios_burbuja()
                elif opcion_2 == 7:
                    ordenar_usuarios_sort()
                elif opcion_2 == 8:
                    break
                else:
                    print('Opción incorrecta, volvé a ingresarla.')
        elif opcion_1 == 2:
            iniciar_sesion()
        elif opcion_1 == 3:
            print("Saliendo de la aplicación.")
            salir = True
        else:
            print('Opción incorrecta, volvé a ingresarla.')

if __name__ == '__main__':
    main()
