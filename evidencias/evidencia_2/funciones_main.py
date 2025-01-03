from manipulacion_archivos import guardar_usuario, guardar_todos_los_usuarios,cargar_datos
from validaciones import validar_email, validar_dni, validar_usuario, validar_contrasena
from usuario import Usuario

def agregar_usuario():
    dni = input('Ingrese el DNI del usuario: ')
    while not validar_dni(dni):
        print('El dato ingresado es incorrecto, debe contener 7 u 8 números, intentelo de nuevo: ')
        dni = input('Ingrese el DNI del usuario: ')
    
    username = input("Ingrese el nombre del usuario: ").lower()
    while not validar_usuario(username):
        print('El dato ingresado es incorrecto, debe contener sólo letras, intentelo nuevamente: ')
        username = input('Ingrese el nombre del usuario: ').lower()
    
    email = input('Ingrese el email: ').lower()
    while not validar_email(email):
        print('El dato ingresado es incorrecto, intentelo nuevamente: ')
        email = input('Ingrese el email: ').lower()
    
    contrasena = input("Ingrese la contraseña, mínimo 8 caracteres, minúsculas y números: ").lower()
    while not validar_contrasena(contrasena):
        print('La contraseña no cumple con los requisitos, intentelo nuevamente: ')
        contrasena = input('Ingrese la contraseña: ').lower()
    
    # Crear una instancia de Usuario
    nuevo_usuario = Usuario(dni, username, email, contrasena)
    
    # Guardar la instancia de Usuario
    guardar_usuario(nuevo_usuario)
    
    print("Usuario agregado exitosamente.")

def modificar_usuario():
    usuarios = cargar_datos()
    if not usuarios:
        print("No hay usuarios para modificar.")
        return
    
    usuario_a_modificar = input("Ingrese el DNI del usuario a modificar: ")
    for usuario in usuarios:
        if usuario.get_dni() == usuario_a_modificar:
            nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ")
            nuevo_email = input("Ingrese el nuevo email: ")
            nueva_contrasena = input("Ingrese la nueva contraseña: ")
            
            if not validar_usuario(nuevo_usuario):
                print('Usuario no válido.')
                return
            if not validar_email(nuevo_email):
                print("Email no válido.")
                return
            if not validar_contrasena(nueva_contrasena):
                print("Contraseña no válida.")
                return
            
            usuario.set_username(nuevo_usuario)
            usuario.set_email(nuevo_email)
            usuario.set_contrasena(nueva_contrasena)
            
            guardar_todos_los_usuarios(usuarios)
            print("Usuario modificado exitosamente.")
            return
    
    print("Usuario no encontrado.")

def eliminar_usuario():
    usuarios = cargar_datos()
    if not usuarios:
        print("No hay usuarios para eliminar.")
        return

    usuario_a_eliminar = input("Ingrese el DNI del usuario a eliminar: ")
    usuarios_actualizados = [usuario for usuario in usuarios if usuario.get_dni() != usuario_a_eliminar]

    if len(usuarios) == len(usuarios_actualizados):
        print("Usuario no encontrado.")
    else:
        guardar_todos_los_usuarios(usuarios_actualizados)
        print("Usuario eliminado exitosamente.")

def buscar_usuario():
    print("Función para buscar usuario")
    usuarios = cargar_datos()
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    usuario_a_buscar = input("Ingrese el DNI del usuario a buscar: ")
    for usuario in usuarios:
        if usuario.get_dni() == usuario_a_buscar:
            print(f"Usuario encontrado: {usuario.mostrar_datos()}")
            return
    print("Usuario no encontrado.")

def mostrar_usuarios():
    usuarios = cargar_datos()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(f"DNI: {usuario.get_dni()}, Usuario: {usuario.get_username()}, Email: {usuario.get_email()}\n")