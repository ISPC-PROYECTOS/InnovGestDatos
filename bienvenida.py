#Bienvenida Usuario
#Importar módulos ValidarUsuario, ValidarContraseña y Registrar


print("TE DOY LA BIENVENIDA A NUESTRO SISTEMA")


salir=False

while  salir==False:
    print("MENU")
    print("1- INGRESO DE USUARIO")
    print("2- REGISTRAR USUARIO")
    print("3- SALIR")

    opcion=input("Ingrese una opción")

    if opcion == "1":
        usuario=input("INGRESAR USUARIO: ")
        print("validarUsuario(usuario)")
        contrasena=input("INGRESA CONTRASEÑA: ")
        print("validarContrasena(contraseña)")
        print("olvidoContrasena())")
    elif opcion== "2":
        print("registrar()")
    elif opcion== "3":
        print("saliendo")
        salir=True
    else:
        print("Opción incorrecta, vuelve a intentar")




    
