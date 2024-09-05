""" sumar: Suma de dos número reales (float), recibe dos números y
devuelve la suma de los mismos
b. restar: Resta de dos número reales (float), recibe dos números y
devuelve la resta del primer número menos el segundo
c. dividir: División de dos números reales (float), recibe dos números
y devuelve el resultado de dividir el primer número por el segundo.
i. Nota: Aquí considerar en la división el caso de división por
cero y hacer un manejo de excepción.
d. multiplicar: Multiplicación de dos números reales (float), recibe
dos números y devuelve el resultado de multiplicarlos entre sí.
e. sumar_n: Suma de n número reales (float), recibe una cantidad
variable de números y devuelve la suma de los mismos
f. promedio_n: Promedio de n número reales (float), recibe una
cantidad variable de números y devuelve el valor promedio de los
mismos
g. Nota:
i. todas las funciones deberán retornar un número flotante con
dos números decimales.
ii. se deberán hacer los controles (manejo de errores y
aserciones) que se consideren necesarios y hagan robusto a la
aplicación
""" #para no repetir codigo ver de poner una funcion operaciones  
    #
def control_numeros(numero1,numero2):
    assert isinstance(numero1, (int, float)), "El primer argumento debe ser un número"
    assert isinstance(numero2, (int, float)), "El segundo argumento debe ser un número"
    
def sumar(numero1,numero2):
    try:
        control_numeros(numero1,numero2)
        resultado = round((numero1 + numero2), 2)
        return resultado
    except Exception as error:
        print(f"Error al sumar los números: {error}")
        return None
def restar(numero1,numero2):
    try:
        resultado = round((numero1 - numero2), 2)
        return resultado
    except Exception as error:
        print(f"Error al restar los números: {error}")
        return None
def multiplicar(numero1,numero2):
    try:
        resultado = round((numero1 * numero2), 2)
        return resultado
    except Exception as error:
        print(f"Error al multiplicar los números: {error}")
        return None
def dividir(numero1,numero2):
    try:
        assert numero2 != 0 , "El segundo argumento argumento debe diferente a cero"
        resultado = round((numero1 / numero2), 2)
        return resultado
    except Exception as error:
        print(f"Error al dividir los números: {error}")
        return None
def promedio(*numeros):
    try: 
        assert all(isinstance(numero, float) for numero in numeros),"Todos los argumentos deben ser números flotantes"

        resultado = round(sum(numeros) / len(numeros), 2)
        return resultado
    except Exception as error:
        print(f"Error al calcular el promedio: {error}")
        return None
 #prueba si funciona

"""if __name__ == "__main__":
    
    print("Suma:", sumar(3.50, 2.73))
    print("Resta:", restar(3.55, 2.78))
    print("División:", dividir(3.52, 2.74))
    print("Multiplicación:", multiplicar(3.53, 2.79))
    print("Promedio de n números:", promedio(9.50, 8.25, 3.80))"""

    