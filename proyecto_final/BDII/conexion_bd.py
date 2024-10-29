import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = "vicki1996"
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
    conn.close()