import os
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generar_registros_aleatorios():
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    registros = []

    for dias in dias_por_mes:
        mes_registros = [random.randint(0, 500) for _ in range(dias)]
        mes_registros += [0] * (31 - dias)
        registros.append(mes_registros)

    return registros


def cargar_registros_pluviales():
    año = input("Ingrese el año para cargar los registros pluviales: ")
    carpeta = 'registros_pluviales'

    archivo_csv = os.path.join(carpeta, f'registroPluvial{año}.csv')

    if os.path.exists(archivo_csv):
        print(f"Archivo encontrado: {archivo_csv}")
        datos = pd.read_csv(archivo_csv)
    else:
        print(f"No se encontró el archivo. Generando registros aleatorios para el año {año}.")
        registros = generar_registros_aleatorios()
        guardar_en_csv(registros, año, carpeta)
        datos = pd.DataFrame({f'Mes {i+1}': registros[i] for i in range(len(registros))})
    
    return datos, año

def guardar_en_csv(registros, año, carpeta):
    df = pd.DataFrame({f'Mes {i+1}': registros[i] for i in range(len(registros))})
    archivo_csv = os.path.join(carpeta, f'registroPluvial{año}.csv')
    df.to_csv(archivo_csv, index=False)
    print(f"Registros pluviales guardados en {archivo_csv}.")

def generar_grafico_barras(registros, mes, año):
    dias = list(range(1, len(registros) + 1))
    lluvias = registros

    plt.figure(figsize=(10, 6))
    plt.bar(dias, lluvias, color='skyblue')
    plt.title(f'Lluvias del mes {mes} en el año {año}')
    plt.xlabel('Días')
    plt.ylabel('Lluvias (mm)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def generar_grafico_dispersion(registros, mes, año):
    dias = list(range(1, len(registros) + 1))
    lluvias = registros

    plt.figure(figsize=(10, 6))
    plt.scatter(dias, lluvias, color='orange')
    plt.title(f'Dispersión de lluvias del mes {mes} en el año {año}')
    plt.xlabel('Días')
    plt.ylabel('Lluvias (mm)')
    plt.xticks(np.arange(1, len(dias) + 1, 1), rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

def generar_grafico_circular(datos, año):
    lluvias_totales_por_mes = [datos[f'Mes {i+1}'].sum() for i in range(12)]
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    plt.figure(figsize=(10, 10))
    plt.pie(lluvias_totales_por_mes, labels=meses, autopct='%1.1f%%', startangle=140, 
            colors=plt.cm.Paired(np.arange(len(lluvias_totales_por_mes))))
    plt.title(f'Porcentaje de lluvias por mes en el año {año}')
    plt.axis('equal')  
    plt.tight_layout()
    plt.show()

def menu_registros_pluviales():
    datos, año = cargar_registros_pluviales()
    salir = False
    while not salir:
        print("\n---> MENÚ RESGISTROS PLUVIALES <---")
        print("1. Mostrar registros de lluvias por mes")
        print("2. Gráfico de barras de lluvias por mes")
        print("3. Gráfico de dispersión de lluvias por mes")
        print("4. Gráfico circular de lluvias anuales")
        print("5. Salir")

        opcion = input("Ingrese la opción que desea ejecutar: ")

        if opcion == "1":
            mes = int(input("Ingrese el mes (1-12) para mostrar los registros: "))
            if 1 <= mes <= 12:
                registros_mes = datos[f'Mes {mes}'].dropna().tolist()
                print(f"Registros pluviales para el mes {mes} del año {año}:")
                print(registros_mes)
            else:
                print("Mes inválido. Debe estar entre 1 y 12.")

        elif opcion == "2":
            mes = int(input("Ingrese el mes (1-12) para generar el gráfico de barras: "))
            if 1 <= mes <= 12:
                registros_mes = datos[f'Mes {mes}'].dropna().tolist()
                generar_grafico_barras(registros_mes, mes, año)
            else:
                print("Mes inválido. Debe estar entre 1 y 12.")

        elif opcion == "3":
            mes = int(input("Ingrese el mes (1-12) para generar el gráfico de dispersión: "))
            if 1 <= mes <= 12:
                registros_mes = datos[f'Mes {mes}'].dropna().tolist()
                generar_grafico_dispersion(registros_mes, mes, año)
            else:
                print("Mes inválido. Debe estar entre 1 y 12.")

        elif opcion == "4":
            generar_grafico_circular(datos, año)

        elif opcion == "5":
            print("Saliendo de registros pluviales.")
            salir = True

        else:
            print("Opción no válida. Intente de nuevo.")