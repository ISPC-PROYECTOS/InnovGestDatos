import os
import random
import pandas as pd

def cargar_registros_pluviales():
    año = input("Ingrese el año para cargar los registros pluviales: ")
    archivo_csv = f'registroPluvial{año}.csv'

    if os.path.exists(archivo_csv):
        print(f"Archivo encontrado: {archivo_csv}")
        datos = pd.read_csv(archivo_csv)
        mes = int(input("Ingrese el mes (1-12) para mostrar los registros: "))
        
        if 1 <= mes <= 12:
            print(f"Registros pluviales para el mes {mes} del año {año}:")
            print(datos[f'Mes {mes}'])
        else:
            print("Mes inválido. Debe estar entre 1 y 12.")
    else:
        print(f"No se encontró el archivo. Generando registros aleatorios para el año {año}.")
        registros = generar_registros_aleatorios()
        guardar_en_csv(registros, año)

def generar_registros_aleatorios():
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    registros = []

    for dias in dias_por_mes:
        mes_registros = [random.randint(0, 500) for _ in range(dias)]  
        
        mes_registros += [None] * (31 - dias)  
        registros.append(mes_registros)
    
    return registros

def guardar_en_csv(registros, año):
    
    df = pd.DataFrame({f'Mes {i+1}': registros[i] for i in range(len(registros))})
    
    df.to_csv(f'registroPluvial{año}.csv', index=False)
    print(f"Registros pluviales guardados en {año}.")


cargar_registros_pluviales()
