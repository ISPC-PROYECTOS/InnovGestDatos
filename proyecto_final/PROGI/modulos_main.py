from funciones_main import agregar_usuario, modificar_usuario,eliminar_usuario, buscar_usuario, mostrar_usuarios, ordenar_usuarios_burbuja, ordenar_usuarios_sort

def menu_usuarios():
    salir = False

    while not salir:
        print('-----> MENÚ USUARIOS Y ACCESOS <-----')
        print('1. CRUD') #menu_crud
        print('2. MOSTRAR ACCESOS') #menu_accesos
        print('3. ORDENAMIENTO Y BÚSQUEDA') #ordenamiento_busqueda
        print('4. SALIR')

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menu_crud()
        elif opcion == '2':
            menu_accesos()
        elif opcion == '3':
            ordenamiento_busqueda()
        elif opcion == '4':
            salir = True
        else:
            print("Opción no válida, intente nuevamente.")

def menu_crud():
    salir = False

    while not salir:
        print('-----> MENÚ CRUD <-----')
        print('1. AGREGAR USUARIO')
        print('2. MODIFICAR USUARIO')
        print('3. ELIMINAR USUARIO')
        print('4. SALIR')

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_usuario()
            pass
        elif opcion == '2':
            modificar_usuario()
            pass
        elif opcion == '3':
            eliminar_usuario()
            pass
        elif opcion == '4':
            salir = True
        else:
            print("Opción no válida, intente nuevamente.")
    
def menu_accesos():
    salir = False

    while not salir:
        print('-----> MENÚ ACCESOS <-----')
        print('1. MOSTRAR ACCESOS')
        print('2. MOSTRAR INTENTOS FALLIDOS')
        print('3. SALIR')

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            # Mostrar accesos.ispc
            pass
        elif opcion == '2':
            # Mostrar logs.txt
            pass
        elif opcion == '3':
            salir = True
        else:
            print("Opción no válida, intente nuevamente.")

def ordenamiento_busqueda():
    salir = False

    while not salir:
        print('1. ORDENAR USUARIOS')
        print('2. BUSCAR Y MOSTRAR USUARIOS') #buscar_mostrar
        print('3. SALIR')
    
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            # Agregar función de ordenamiento
            pass
        elif opcion == '2':
            buscar_mostrar()
        elif opcion == '3':
            salir = True
        else:
            print("Opción no válida, intente nuevamente.")


def buscar_mostrar():
    salir = False

    while not salir:
        print('1. BÚSQUEDA POR DNI')
        print('2. BÚSQUEDA POR USERNAME')
        print('3. BÚSQUEDA POR EMAIL')
        print('4. MOSTRAR USUARIOS') #DOS OPCIONES
        print('5. SALIR')

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            # Búsqueda por DNI
            pass
        elif opcion == '2':
            # Búsqueda por username
            pass
        elif opcion == '3':
            # Búsqueda por email
            pass
        elif opcion == '4':
            # Mostrar todos los usuarios
            pass
        elif opcion == '5':
            salir = True
        else:
            print("Opción no válida, intente nuevamente.")