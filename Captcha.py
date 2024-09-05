#Captcha
import random

from aritmetica import sumar, restar, multiplicar, dividir, promedio

def generate_captcha():
    numero1 = round(random.uniform(1, 10),2)
    numero2 = round(random.uniform(1, 10),2)
    operacion = random.choice(["+", "-","*" , "/", "prom"]) #elige una operacion de la lista al azar

    print(f"Por favor realiza esta operacion para comprobar que sos humano: {numero1} {operacion} {numero2}")   
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
if __name__ == "__main__":
    
    captcha, resultado = generate_captcha()
    print(f"El captcha es: {captcha}")
    print(f"El resultado es: {resultado}") #esto no se deberia mostrar, solo lo dejo para ver el resultado.
    
    respuesta = float(input("Ingrese el resultado del captcha: "))
    
    if respuesta == resultado:
        print("Captcha correcto")
    else:
        print("Captcha incorrecto")

