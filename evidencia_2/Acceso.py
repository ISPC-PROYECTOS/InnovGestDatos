# Acceso.py
from usuario import Usuario
from datetime import datetime

class Acceso: 
    def __init__(self, usuarioLogueado):
        self.id_acceso = None
        self.fecha_ingreso = None
        self.fecha_salida = None
        self.__usuarioLogueado = usuarioLogueado

    def login(self, email, contrasena):
        print(f"Email ingresado: {email}")
        print(f"Email del usuario: {self.__usuarioLogueado.get_email()}")
        print(f"Contraseña ingresada: {contrasena}")
        print(f"Contraseña del usuario: {self.__usuarioLogueado.get_contrasena()}")
        
        if self.__usuarioLogueado.get_email() == email and self.__usuarioLogueado.get_contrasena() == contrasena:
            self.fecha_ingreso = datetime.now()
            return True
        else:
            return False
        
    def logout(self):
        self.fecha_salida = datetime.now()

    def get_usuarioLogueado(self):
        return self.__usuarioLogueado

    def __str__(self):
        return (f"Identificacion de Acceso : {self.id_acceso}, Usuario: {self.get_usuarioLogueado()}, "
                f"Ingreso: {self.fecha_ingreso}, Salida: {self.fecha_salida}")

# Prueba
usuario1 = Usuario("3465878", "jesivaldi", "jesivaldi@gmail.com", "contraseña")

acceso = Acceso(usuario1)

email = input("Ingrese su email: ")
contrasena = input("Ingrese su contraseña: ")

if acceso.login(email, contrasena):
    print("Inicio de sesión exitoso")
else:
    print("Email o contraseña incorrectos")
