def solicitar_datos():
    usuario = input('Ingresa el usuario: ').lower()
    contraseña = int(input('Ingresa la contraseña: '))
    return usuario, contraseña

def ingreso():
    usuario, contraseña = solicitar_datos()  
    intentos_restantes = 4
    if usuario == 'pepe' and contraseña == 123456789:
        
        print('Ingreso a la app.')
        pass
    elif usuario == 'pepe':
        while intentos_restantes > 1:
            intentos_restantes -= 1
            print(f'Contraseña incorrecta. Te quedan {intentos_restantes} intentos.')
            contraseña = input('Ingresa la contraseña nuevamente: ')
            if contraseña == '123456789':
                print('Ingreso a la app.')
                break
        else: 
                print('Cuenta bloqueada.')
    else:
        print('Usuario no reconocido.')