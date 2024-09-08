#Bienvenida Usuario

from ingreso import ingreso
from Funcion_registrar_usuario import registrar_usuario

salir=False

print("TE DOY LA BIENVENIDA A NUESTRO SISTEMA")

while  salir==False:
    print("MENU")
    print("1- INGRESO DE USUARIO")
    print("2- REGISTRAR USUARIO")
    print("3- SALIR")

    opcion=input("Ingrese una opción: ")

    if opcion == "1":
        ingreso()
    elif opcion== "2":
        registrar_usuario()
    elif opcion== "3":
        
        print("SALIENDO")
        salir=True
    else:
        print("Opción incorrecta, vuelve a intentar")




    
