from modulos_main import menu_pricipal, menu_crud

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
                    print("Agregar usuario")
                    # Implementar función para agregar usuario
                elif opcion_2 == 2:
                    print("Modificar usuario")
                    # Implementar función para modificar usuario
                elif opcion_2 == 3:
                    print("Eliminar usuario")
                    # Implementar función para eliminar usuario
                elif opcion_2 == 4:
                    print("Buscar usuario")
                    # Implementar función para buscar usuario
                elif opcion_2 == 5:
                    print("Mostrar usuarios")
                    # Implementar función para mostrar usuarios
                elif opcion_2 == 6:
                    break
                else:
                    print('Opción incorrecta, volvé a ingresarla.')
        elif opcion_1 == 2:
            print("Iniciar sesión")
            # Implementar función para iniciar sesión
        elif opcion_1 == 3:
            print("Saliendo de la aplicación.")
            salir = True
        else:
            print('Opción incorrecta, volvé a ingresarla.')

if __name__ == '__main__':
    main()