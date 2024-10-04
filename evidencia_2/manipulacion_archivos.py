import pickle  
from datetime import datetime  

# Función para guardar los datos en un archivo binario  
def guardar_datos(usuario, contrasena):
    if not usuario or not contrasena:
        print("Usuario y contraseña no pueden estar vacíos.")
        return

    datos = {
        'usuario': usuario,
        'contrasena': contrasena,
        'fecha_hora': datetime.now()
    }

    try:
        with open('datos_usuario.bin', 'ab') as archivo:
            pickle.dump(datos, archivo)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")  
# Función para mostrar los datos guardados  
def mostrar_datos():  
    try:  
        with open('datos_usuario.bin', 'rb') as archivo:  
            while True:  
                try:  
                    # Leer un objeto del archivo  
                    datos = pickle.load(archivo)  
                    print(f"Usuario: {datos['usuario']}, Contraseña: {datos['contrasena']}, Fecha y Hora: {datos['fecha_hora']}")  
                except EOFError:  
                    # Cuando se alcanza el final del archivo, terminamos  
                    break  
    except FileNotFoundError:  
        print("No se ha encontrado el archivo de datos.")  

# Solicitar el usuario y la contraseña  
if __name__ == "__main__":
    usuario = input("Ingresa tu usuario: ")
    contrasena = input("Ingresa tu contraseña: ")

# Llamar a la función para guardar los datos  
guardar_datos(usuario, contrasena)  

print("Datos guardados exitosamente.") 
mostrar_datos()


    
  