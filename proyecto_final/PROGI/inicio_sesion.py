from manipulacion_archivos import verificar_usuarios
from acceso import Acceso
from manipulacion_archivos import registrar_fallo

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
                    return True
                else:
                    print("Contraseña incorrecta")
                    registrar_fallo(f"Intento fallido: Contraseña incorrecta para el usuario {email}")
                    return False
        print("Usuario no encontrado")
        registrar_fallo(f"Intento fallido: Usuario no encontrado con el email {email}")
        return False
    except Exception as e:
        print(f"Error durante el inicio de sesión: {e}")
        registrar_fallo(f"Error durante el inicio de sesión: {e}")
        return False