from funciones_main import agregar_usuario, modificar_usuario, eliminar_usuario, buscar_usuario, mostrar_usuarios

class CrudUsuario:
    def __init__(self):
        pass

    def crear_usuario(self, dni, username, email, contrasena):
        agregar_usuario(dni, username, contrasena, email)

    def actualizar_usuario(self, dni, nuevo_username=None, nuevo_email=None, nueva_contrasena=None):
        modificar_usuario(dni, nuevo_username, nueva_contrasena, nuevo_email)

    def eliminar_usuario(self, dni):
        eliminar_usuario(dni)

    def buscar_usuario(self, dni):
        return buscar_usuario(dni)

    def mostrar_usuarios(self):
        mostrar_usuarios()