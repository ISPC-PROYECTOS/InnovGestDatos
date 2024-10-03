def solicitar_usuario():
    usuario = input('Ingresa el usuario: ').lower()
    return usuario

def solicitar_contraseña():
    contraseña = input('Ingresa la contraseña: ')
    return contraseña

def ingreso():
    intentos_restantes = 4
    
    usuario = solicitar_usuario()
    if usuario != 'pepe':
        print('Usuario no reconocido.')
        return
    
    while intentos_restantes > 0:
        contraseña = solicitar_contraseña()
        
        if contraseña == '123456789':
            print('Ingreso al sistema.')
            return
        else:
            intentos_restantes -= 1
            print(f'Contraseña incorrecta. Te quedan {intentos_restantes} intentos.')
    
    print('Cuenta bloqueada.')

if __name__ == '__main__':
    ingreso()