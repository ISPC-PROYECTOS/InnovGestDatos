class Usuario:
    def __init__(self, dni, username, email, contrasena):
        self.__dni = dni
        self.__username = username
        self.__email = email
        self.__contrasena = contrasena

    def get_dni(self):
        return self.__dni
    
    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def get_contrasena(self):
        return self.__contrasena

    def mostrar_datos(self):
        return f"DNI: {self.__dni}, Usuario: {self.__username}, Email: {self.__email}"