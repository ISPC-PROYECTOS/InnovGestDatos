
#------------------------------------prueba raice------------------------
import mysql.connector
from mysql.connector import Error

HOST = "localhost"
USER = "root"
PASSWORD = "su_contraseña"
BD = "stockagranel"

class ErrorConexion(Exception):
    pass

def conectar_base_datos():
    try:
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=BD
        )
        if conn.is_connected():
            print("Conexión a la base de datos exitosa.")
            return conn
    except Error as e:
        raise ErrorConexion(f"Error al conectar a la base de datos: {e}")

def cerrar_conexion(conn):
    if conn.is_connected():
        conn.cursor().close()
        conn.close()
        print("Conexión a la base de datos cerrada.")

