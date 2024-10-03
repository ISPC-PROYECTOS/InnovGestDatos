class Usuario:
    def __init__(self, id_usuario, username, email):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__email = email

    def get_id_usuario(self):
        return self.__id_usuario
    
    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def mostrar_datos(self):
        return f"identificador unico de Susuario: {self.__id_usuario}, Nombre de usuario: {self.__username}, email: {self.__email}"


    