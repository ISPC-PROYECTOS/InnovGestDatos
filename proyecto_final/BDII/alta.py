from .conexion_bd import conectar_base_datos, cerrar_conexion
from .mostrar_tablas import mostrar_categorias, mostrar_productos_granel_disponibles

def alta():
    salir = False
    while not salir:
        print('Ingresa la opción que desea dar de ALTA:')
        print('1 - PRODUCTOS')
        print('2 - PRESENTACIÓN')
        print('3 - PROVEEDOR')
        print('4 - SALIR')
        
        alternativa = int(input('Ingrese una opción: '))

        if alternativa == 1:
            mostrar_categorias()
            alta_producto()
            print('\nPRODUCTO dado de ALTA con éxito.\n')
        elif alternativa == 2:
            print("Corrobore que la presentación del producto no existe.")
            print("ID/ NOMBRE/ CANTIDAD/ TAMAÑO/ UM/ MAX/ MIN/ CATEGORÍA")
            mostrar_productos_granel_disponibles()
            alta_presentacion()
            print('\nPRESENTACIÓN dada de ALTA con éxito.\n')
        elif alternativa == 3:
            alta_proveedor()
            print('\nPROVEEDOR dado de ALTA con éxito.\n')
        elif alternativa == 4:
            print('\nSaliendo de la opción de ALTA...\n')
            salir = True
        else:
            print('\nOpción incorrecta\n')

def alta_producto():
    conn, cursor = conectar_base_datos()
    if conn:
        cursor = conn.cursor()
        try:
            descripcion = input('Ingresa la descripción del producto: ').upper()
            cantidad = int(input('Ingresa la cantidad: '))
            tamano = int(input('Ingresa el tamaño: '))
            unidad_medida = input('Ingresa la unidad de medida: ').lower()
            cantidad_max = int(input('Ingresa la cantidad máxima: '))
            cantidad_min = int(input('Ingresa la cantidad mínima: '))
            id_categoria = int(input('Ingresa el ID de la categoría: '))

            query = """
            INSERT INTO productosgranel 
            (descripcion, cantidad, tamano, unidadmedida, cantidadmax, cantidadmin, idcategoria) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (descripcion, cantidad, tamano, unidad_medida, cantidad_max, cantidad_min, id_categoria)
            cursor.execute(query, values)
            conn.commit()
        except Exception as e:
            print(f"Error al insertar el producto: {e}")

def alta_presentacion():
    conn, cursor = conectar_base_datos()
    if conn:
        cursor = conn.cursor()
        try:
            descripcion = input('Ingresa la descripción del producto: ').upper()
            cantidad = int(input('Ingresa la cantidad: '))
            tamano = int(input('Ingresa el tamaño: '))
            unidad_medida = input('Ingresa la unidad de medida: ').lower()
            cantidad_max = int(input('Ingresa la cantidad máxima: '))
            cantidad_min = int(input('Ingresa la cantidad mínima: '))
            id_producto_granel = int(input('Ingresa el ID del producto a granel: '))

            query = """
            INSERT INTO presentaciones 
            (descripcion, cantidad, tamano, unidadmedida, cantidadmax, cantidadmin, idproductogranel) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (descripcion, cantidad, tamano, unidad_medida, cantidad_max, cantidad_min, id_producto_granel)
            cursor.execute(query, values)
            conn.commit()
        except Exception as e:
            print(f"Error al insertar la presentación: {e}")

def alta_proveedor():
    conn, cursor = conectar_base_datos()
    if conn:
        cursor = conn.cursor()
        try:
            CUIT = input('Ingresa el CUIT(XX-XXXXXXXX-XX): ')
            proveedor = input('Ingresa el nombre del proveedor: ').upper()
            direccion = input('Ingresa la dirección: ').lower()
            telefono = input('Ingresa el número de teléfono: ')
            email = input('Ingresa el email: ').lower()
            tiempo_de_entrega = int(input('Ingresa en número de días el tiempo de entrega (ej: 7): '))

            query = """
            INSERT INTO proveedores 
            (CUIT, proveedor, direccion, telefono, email, tiempodeentrega) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (CUIT, proveedor, direccion, telefono, email, tiempo_de_entrega)
            cursor.execute(query, values)
            conn.commit()
        except Exception as e:
            print(f"Error al insertar el proveedor: {e}")