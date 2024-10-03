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

def suma_numeros(*numeros):
    try:
        assert all(isinstance(numero, (int, float)) for numero in numeros),\
       "Todos los argumentos deben ser números enteros o flotantes"
        
        resultado = sum(numeros)
        return resultado
    except Exception as error:
        print(f"Error al calcular la suma de n numeros: {error}")
        return None
 #prueba si funciona

if __name__ == "__main__":
    print("Suma:", sumar(3.50, 2.73))
    print("Resta:", restar(3.55, 2.78))
    print("División:", dividir(3.52, 2.74))
    print("Multiplicación:", multiplicar(3.53, 2.79))
    print("Promedio de n números:", promedio(9.50, 8.25, 3.80))
    print("suma de n números:", suma_numeros(9.00, 8.00, 3.80))
    