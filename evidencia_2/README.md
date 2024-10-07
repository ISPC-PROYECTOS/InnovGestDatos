#EVIDENCIA DE APRENDIZAJE Nº2

# Proyecto de Gestión de Usuarios

Este proyecto implementa una aplicación en Python utilizando los conceptos de Programación Orientada a Objetos (POO) y el manejo de archivos.

Es una aplicación de gestión de usuarios que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los usuarios,

así como iniciar sesión. Utiliza archivos para almacenar los datos de los usuarios y los registros de acceso.

## Estructura de Archivos

El proyecto está compuesto por los siguientes archivos:

- **main.py**: Archivo principal que ejecuta la aplicación.
- **acceso.py**: Maneja el registro de accesos de los usuarios.
- **crud.py**: Contiene las funciones CRUD para la gestión de usuarios.
- **funciones_main.py**: Define las funciones para agregar, modificar, eliminar, buscar y mostrar usuarios.
- **inicio_sesion.py**: Maneja el proceso de inicio de sesión de los usuarios.
- **manipulacion_archivos.py**: Contiene funciones para manipular archivos y guardar los datos de los usuarios.
- **modulos_main.py**: Define los menús que se muestran al usuario.
- **usuario.py**: Define la clase Usuario con los atributos y métodos necesarios.
- **validaciones.py**: Contiene funciones para validar la entrada de datos del usuario.
- 
## ¿Cómo Ejecutar el Programa?

1. Clonar el repositorio o descargar los archivos del proyecto.
2. Abrir una terminal y buscar la carpeta donde se encuentran los archivos.
3. Ejecutar el archivo `main.py`

## ## ¿Cuales son los pasos para Probar el Programa?

Las opciones que se encontramos en el programa al momento de ejecutarlo son:

1. **Acceder al Menú Principal**:
   - Al iniciar, está el menú principal donde se encuentran 3 opciones que incluyen CRUD ,iniciar sesión o salir

2. Al elegir la opción CRUD , se accede a las siguientes opciones:

2.a **Agregar un Usuario**:
   - Selecciona la opción correspondiente para acceder al menú CRUD.
   - Escoge "AGREGAR USUARIO" e ingresa la información requerida:
     - DNI: Un número de identificación de 7 u 8 dígitos.
     - Nombre de usuario: Solo letras, en minúsculas.
     - Correo electrónico: Debe incluir '@' y '.com'.
     - Contraseña: Mínimo 8 caracteres, que contenga letras y números.
   - Confirma que el usuario se haya agregado exitosamente.

2.b**Modificar un Usuario**:
   - Desde el menú CRUD, selecciona "MODIFICAR USUARIO".
   - Ingresa el DNI del usuario que deseas modificar.
   - Proporciona la nueva información (nombre de usuario, correo electrónico, contraseña).
   - Aparece un mensaje que confirma que la modificación fue exitosa.
     
2.c**Eliminar un Usuario**:
   - En el menú CRUD, selecciona "ELIMINAR USUARIO".
   - Ingresa el DNI del usuario que deseas eliminar.
   - Si la eliminación fue correcta se recibe un mensaje que confirma que el usuario ha sido eliminado correctamente.

2.d**Buscar un Usuario**:
   - Selecciona "BUSCAR USUARIO" en el menú CRUD.
   - Ingresa el DNI del usuario que deseas buscar.
   - Una vez realizada la busqueda el programa muestra la información del usuario.
     
2.e**Mostrar un Usuario**:
   - Selecciona "MOSTRAR USUARIO" en el menú CRUD.
   - Se despliega el listado de usuarios ingresados.

2.f**Volver al menu principal**:
   -Regresa al menu inicial.

     
3 **Iniciar Sesión**:
   - Regresa al menú principal y selecciona "INICIAR SESIÓN".
   - Ingresa el correo electrónico y la contraseña del usuario que agregaste.
   - Verifica que el inicio de sesión sea exitoso.

8. **Cerrar el Programa**:
   - Selecciona la opción "SALIR" del menú principal para cerrar el programa.

## Resultados Esperados
- Deberías poder agregar, modificar, buscar y eliminar usuarios sin problemas.
- Al iniciar sesión, deberías recibir un mensaje de "Inicio de sesión exitoso" si las credenciales son correctas.
- Cualquier error en los datos ingresados debería ser manejado adecuadamente, informándote sobre qué dato es incorrecto.

##Requisitos adicionales
Aparte de la instalación de Python, no se requiere ningún otro software adicional. Puedes descargar Python desde su página oficial.

