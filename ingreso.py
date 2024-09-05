# Si ingresa correctamente dejar un mensaje de ingreso a la aplicación y (si
# vemos archivos de texto) guardar en un archivo llamado “ingresos.txt” el
# nombre de usuario y la fecha de ingreso.

# Si el nombreUsuario es correcto y la clave no, la aplicación deberá ir
# avisando de los intentos fallidos y recordando que al cuarto intento se
# bloquea el acceso a dicho usuario, además * (si vemos archivos de texto)
# de dejar registro (log.txt) en un archivo de texto.

def solicitar_datos():
    usuario = input('Ingresa el usuario: ')
    contraseña = input('Ingresa la contraseña: ')
    return usuario, contraseña

def ingreso():
    usuario, contraseña = solicitar_datos()  
    intentos_restantes = 4
    if usuario == 'pepe' and contraseña == 123456789:
        print('Ingreso a la app.')
    elif usuario == 'pepe':
        while intentos_restantes > 1:
            intentos_restantes -= 1
            print(f'Contraseña incorrecta. Te quedan {intentos_restantes} intentos.')
            contraseña = input('Ingresa la contraseña nuevamente: ')
            if contraseña == '123456789':
                print('Ingreso a la app.')
        else: 
            print('Cuenta bloqueada.')
    else:
        print('Usuario no reconocido.')

if __name__ == '__main__':
    ingreso()