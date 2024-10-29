# EVIDENCIA DE APRENDIZAJE Nº3

## Ampliaciones de Programación I  
Se han añadido las siguientes funcionalidades adicionales a la aplicación:

### Opciones de Ordenamiento
- Permitir elegir entre dos formas de ordenamiento por username:
  - Ordenar utilizando la técnica de burbuja.
  - Ordenar utilizando el método `sort()` de Python (usando la clave `username`).
- Guardar los usuarios ordenados en el archivo `usuarios.ispc` solo si se elige esta opción (no es necesario mantener el orden en el CRUD).

### Búsqueda de Usuarios
- Al buscar un usuario por username, se muestra un mensaje adicional indicando si la búsqueda fue realizada mediante búsqueda secuencial (si no se había ordenado previamente) o mediante búsqueda binaria (si se eligió ordenarlos).

### Carga de Registros Pluviales
- Especificar un año para cargar los registros pluviales.
- Si el archivo CSV correspondiente al año se encuentra disponible, se utiliza.
- Si no existe, se generan los registros pluviales de forma aleatoria utilizando Pandas, creando un DataFrame que representa los datos de lluvia para cada día del año, y se guardan en un archivo CSV (por ejemplo, registroPluvial2023.csv). La generación de registros aleatorios se realiza mediante la función generar_registros_aleatorios.
- Mostrar los registros de un mes específico elegido por el usuario.

### Gráficos de Lluvias
- Se generan gráficos con Matplotlib:
  - Gráfico de barras para mostrar las lluvias anuales.
  - Gráfico de dispersión con los meses en el eje x y los días en el eje y.
  - Gráfico circular que abarque todos los meses.

## Ampliaciones de Base de Datos II  
- Presentar la configuración y conexión a la base de datos desde el backend.
- Incorporar consultas y filtrados (CRUD y consultas complejas).