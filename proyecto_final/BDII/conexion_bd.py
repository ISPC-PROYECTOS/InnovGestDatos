"""import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = ""
BD = "stockagranel"

conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=BD
)

cursor = conn.cursor()

def cerrarConexion():
    cursor.close()
    conn.close()"""
import mysql.connector
from mysql.connector import Error

HOST = "localhost"
USER = "root"
PASSWORD = "tu_contraseña"
BD = "stockagranel"

try:
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=BD
    )
    if conn.is_connected():
        print("Conexión a la base de datos exitosa.")
        cursor = conn.cursor()
except Error as e:
    print(f"Error al conectar a la base de datos: {e}")
    print("Por favor, configure los datos de conexión y pruebe nuevamente.")

def cerrarConexion():
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexión a la base de datos cerrada.")
