def olvido_contrasena():
    print("Olvido de Contraseña")
    opcion = input("¿Desea reestablecer la contraseña? (si/no): ").strip().lower()
    if opcion == "si":
        correo = input("Ingrese su correo electrónico: ").strip()
        print(f"Se ha enviado un correo a {correo}.")
    else:
        print("Gracias por su tiempo.")

if __name__ == '__main__': 
    olvido_contrasena()