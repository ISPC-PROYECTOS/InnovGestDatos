#Captcha
#Captcha
import random

from aritmetica import sumar, restar, multiplicar, dividir, promedio, suma_numeros

def generate_captcha():
    numero1 = round(random.uniform(1, 10),2)
    numero2 = round(random.uniform(1, 10),2)
    operacion = random.choice (["+", "-","*" , "/", "prom","suma"]) #elige una operacion de la lista al azar

      
    if operacion == "+":
        resultado = sumar(numero1, numero2)
    elif operacion == "-":
        resultado = restar (numero1, numero2)
    elif operacion == "*":
        resultado = multiplicar(numero1, numero2)
    elif operacion == "prom":
        resultado = promedio(numero1, numero2)
    else:
        resultado = dividir(numero1, numero2)

    captcha_text = f"{numero1} {operacion} {numero2}"
    
        
    return captcha_text, resultado

def comprobar_captcha():
    captcha_text, resultado = generate_captcha()
    print(f"Resuelve esta operación si eres humano: {captcha_text}")

    respuesta = float(input("Ingrese el resultado del captcha: "))

    if respuesta == resultado:
        print("Captcha correcto")
    else:
        print("Captcha incorrecto")
"""    
if __name__ == "__main__":
    
    captcha, resultado = generate_captcha()
    print(f"El captcha es: {captcha}")
    print(f"El resultado es: {resultado}") #esto no se deberia mostrar, solo lo dejo para ver el resultado.
    
    respuesta = float(input("Ingrese el resultado del captcha: "))
    
    if respuesta == resultado:
        print("Captcha correcto")
    else:
        print("Captcha incorrecto")
        
        print(f"Por favor realiza esta operacion para comprobar que sos humano: {numero1} {operacion} {numero2}") """

