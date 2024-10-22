from conexion_bd import cursor

def mostrar_productos_fraccionados_disponibles():
    query = "SELECT idProductoFracc, descripcion, cantidad, tamano, unidadMedida, cantidadMax, cantidadMin, idProductoGranel FROM stockagranel.presentaciones"
    cursor.execute(query)
    productos = cursor.fetchall()
    if productos:
        for producto in productos:
            print(producto)
    else:
        print("No hay productos en la base de datos.")

def mostrar_productos_granel_disponibles():
    query = "SELECT idProductoGranel, descripcion, cantidad, tamano, unidadMedida, cantidadMax, cantidadMin, idCategoria FROM productosgranel"
    cursor.execute(query)
    productos = cursor.fetchall()
    if productos:
        for producto in productos:
            print(producto)
    else:
        print("No hay productos en la base de datos.")

def mostrar_categorias():
    query = "SELECT idCategoria, categoria FROM categorias"
    cursor.execute(query)
    categorias = cursor.fetchall()
    if categorias:
        print("ID/CATEGORIA: ")
        for categoria in categorias:
            print(categoria)
    else:
        print("No hay categorias en la base de datos.")

def mostrar_proveedores():
    query = "SELECT CUIT, proveedor, direccion, telefono, email, tiempoDeEntrega FROM proveedores"
    cursor.execute(query)
    proveedores = cursor.fetchall()
    if proveedores:
        for proveedor in proveedores:
            print(proveedor)
    else:
        print("No hay proveedores en la base de datos.")