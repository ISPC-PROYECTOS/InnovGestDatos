import pickle
from usuario import Usuario

# Función para guardar usuario
def guardar_usuario(usuario):
    try:
        with open('usuarios.ispc', 'ab') as archivo:
            pickle.dump(usuario, archivo)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Función para mostrar los datos guardados
def mostrar_datos():
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            while True:
                try:
                    usuario = pickle.load(archivo)
                    if isinstance(usuario, Usuario):
                        print(f"DNI: {usuario.get_dni()}, Usuario: {usuario.get_username()}, Email: {usuario.get_email()}")
                    else:
                        print("Objeto no es una instancia de Usuario")
                except EOFError:
                    # Cuando se alcanza el final del archivo, terminamos
                    break
    except FileNotFoundError:
        print("No se ha encontrado el archivo de datos.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

# Función para cargar los datos desde un archivo binario
def cargar_datos():
    usuarios = []
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            while True:
                try:
                    usuario = pickle.load(archivo)
                    if isinstance(usuario, Usuario):
                        usuarios.append(usuario)
                    else:
                        print("Objeto no es una instancia de Usuario")
                except EOFError:
                    break
    except FileNotFoundError:
        print("El archivo 'usuarios.ispc' no existe.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
    return usuarios

# Función para guardar todos los usuarios en un archivo binario
def guardar_todos_los_usuarios(usuarios):
    try:
        with open('usuarios.ispc', 'wb') as archivo:
            for usuario in usuarios:
                if isinstance(usuario, Usuario):
                    pickle.dump(usuario, archivo)
                else:
                    print("Objeto no es una instancia de Usuario")
        print("Todos los datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Función para verificar usuarios
def verificar_usuarios():
    usuarios = []
    try:
        with open('usuarios.ispc', 'rb') as file:
            while True:
                try:
                    usuario = pickle.load(file)
                    if isinstance(usuario, Usuario):
                        usuarios.append(usuario)
                    else:
                        print("Objeto no es una instancia de Usuario")
                except EOFError:
                    break
    except FileNotFoundError:
        print("El archivo usuarios.ispc no existe.")
    return usuarios