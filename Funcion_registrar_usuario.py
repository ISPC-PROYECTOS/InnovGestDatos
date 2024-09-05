
import re

def validar_clave(clave):
    if len(clave) < 8:
        return False, "La clave debe tener al menos 8 caracteres."

    minúscula = re.search(r"[a-z]", clave) is not None
    mayúscula = re.search(r"[A-Z]", clave) is not None
    número = re.search(r"\d", clave) is not None
    caracter_especial = re.search(r"[^\w\s]", clave) is not None  
    
    condiciones_cumplidas = sum([minúscula, mayúscula, número, caracter_especial])


    if condiciones_cumplidas >= 2:
        return True, "La clave es válida."
    else:
        return False, "La clave debe cumplir al menos 2 de las siguientes condiciones: minúscula, mayúscula, número, caracter especial."
# Diccionario que arme mari?
usuarios = {}


def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    
    while True:
        dni = input("Ingrese su dni: ")
        if dni in usuarios:
            print("El dni ya se encuentra registrado.")
        else:
            break
    
    correo = input("Ingrese su correo electrónico: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
    
    while True:
        nombre_usuario = input("Ingrese su nombre de usuario (6-12 caracteres): ")
        if not (6 <= len(nombre_usuario) <= 12):
            print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
        elif any(usuario["nombreUsuario"] == nombre_usuario for usuario in usuarios.values()):
            print("El nombre de usuario ya está registrado. Intente con otro.")
        else:
            break
    while True:
        clave = input("Ingrese su clave: ")
        valida, mensaje = validar_clave(clave)
        if valida:
            break
        else:
            print(mensaje)
    
    
    usuarios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "fecha_nacimiento": fecha_nacimiento,
        "nombreUsuario": nombre_usuario,
        "clave": clave
    }
    
    print("Usuario registrado con éxito.")


registrar_usuario()


print("Usuarios registrados:")
for dni, info in usuarios.items():
    print(f"DNI: {dni}, Nombre: {info['nombre']}, Nombre de Usuario: {info['nombreUsuario']}")
    
