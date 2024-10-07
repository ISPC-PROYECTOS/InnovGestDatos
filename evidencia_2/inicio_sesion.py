from manipulacion_archivos import verificar_usuarios
from acceso import Acceso

def iniciar_sesion():
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")

    try:
        usuarios = verificar_usuarios()
        
        for usuario in usuarios:
            if usuario.get_email() == email:
                acceso = Acceso(usuario)
                if acceso.login(email, contrasena):
                    print("Inicio de sesión exitoso")
                    return acceso
                else:
                    print("Contraseña incorrecta")
                    return None
        print("Usuario no encontrado")
        return None
    except Exception as e:
        print(f"Error durante el inicio de sesión: {e}")
        return None