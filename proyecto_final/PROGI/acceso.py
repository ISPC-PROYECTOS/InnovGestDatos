from datetime import datetime
import json

class Acceso: 
    def __init__(self, usuarioLogueado):
        self.id_acceso = None
        self.fecha_ingreso = None
        self.fecha_salida = None
        self.__usuarioLogueado = usuarioLogueado
        self.id_acceso = self.generar_id_acceso()  # Generar un ID de acceso único

    def generar_id_acceso(self):
        return datetime.now().timestamp()  # Ejemplo de ID único

    def login(self, email, contrasena):
        if self.__usuarioLogueado.get_email() == email and self.__usuarioLogueado.get_contrasena() == contrasena:
            self.fecha_ingreso = datetime.now()
            self.registrar_acceso()  # Llama al método para registrar el acceso
            return True
        else:
            return False
        
    def registrar_acceso(self):
        acceso_data = {
            "id_acceso": self.id_acceso,
            "email": self.__usuarioLogueado.get_email(),
            "fecha_ingreso": self.fecha_ingreso.isoformat()
        }
        with open('accesos.ispc', 'a') as file:
            file.write(json.dumps(acceso_data) + '\n')

    def logout(self):
        self.fecha_salida = datetime.now()
        acceso_data = {
            "id_acceso": self.id_acceso,
            "email": self.__usuarioLogueado.get_email(),
            "fecha_salida": self.fecha_salida.isoformat()
        }
        with open('accesos.ispc', 'a') as file:
            file.write(json.dumps(acceso_data) + '\n')

    def get_usuarioLogueado(self):
        return self.__usuarioLogueado

    def __str__(self):
        return(f"Identificacion de Acceso : {self.id_acceso}, Usuario: {self.get_usuarioLogueado()}, "
                f"Ingreso: {self.fecha_ingreso}, Salida: {self.fecha_salida}") 