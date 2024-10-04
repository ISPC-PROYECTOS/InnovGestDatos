#from manejo_archivos import cargar_usuarios
from Acceso1 import Acceso1

def iniciar_sesion():
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")

    usuarios = cargar_usuarios() #usar 
    for usuario in usuarios:
        if usuario.get_email() == email:
            acceso = Acceso1(usuario)
            if acceso.login(email, contrasena):
                print("Inicio de sesión exitoso")
                return acceso
        
            else:
                print("Contraseña incorrecta")
                return None
    print("Usuario no encontrado")
    return None

# Ejemplo de uso
if __name__ == "__main__":
    acceso = iniciar_sesion()
    if acceso:
        print("Sesión iniciada con éxito")
    else:
        print("Error al iniciar sesión")
        
"""# manejo_archivos.py, es para probar, dps usar el de marie y consu
import json
from Usuario import Usuario

def guardar_usuario(usuario):
    with open('usuarios.txt', 'a') as file:
        file.write(json.dumps(usuario.__dict__) + '\n')

def cargar_usuarios():
    usuarios = []
    with open('usuarios.txt', 'r') as file:
        for line in file:
            data = json.loads(line.strip())
            usuario = Usuario(data['_Usuario__id_usuario'], data['_Usuario__username'], data['_Usuario__email'], data['_Usuario__contrasena'])
            usuarios.append(usuario)
    return usuarios"""