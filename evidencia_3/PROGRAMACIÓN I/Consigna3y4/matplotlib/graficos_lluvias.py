import matplotlib.pyplot as plt
import numpy as np

# Datos gráfico lluvias anuales
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
lluvias = [70, 50, 80, 120, 90, 60, 30, 20, 100, 110, 95, 85]  # Datos ficticios de lluvias en mm

# Gráfico barras lluvias anuales
plt.figure(figsize=(10, 6))
plt.bar(meses, lluvias, color='skyblue')
plt.title('Lluvias Anuales')
plt.xlabel('Meses')
plt.ylabel('Lluvias (mm)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Datos gráfico dispersión
dias = np.array([np.random.randint(1, 32) for _ in range(12)])  # Días aleatorios
meses_num = np.arange(1, 13)  # Números de meses de 1 a 12

# Gráfico dispersión
plt.figure(figsize=(10, 6))
plt.scatter(meses_num, dias, color='orange')
plt.title('Días Aleatorios por Mes')
plt.xlabel('Mes (1-12)')
plt.ylabel('Día (1-31)')
plt.xticks(meses_num, meses, rotation=45)
plt.yticks(np.arange(1, 32, 1))
plt.grid()
plt.tight_layout()
plt.show()

# Gráfico circular meses
lluvias_total = sum(lluvias)

# Gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(lluvias, labels=meses, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(np.arange(len(lluvias))))
plt.title('Lluvias por Mes')
plt.axis('equal')  # Para que el gráfico sea un círculo
plt.show()

