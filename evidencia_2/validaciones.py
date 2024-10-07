import re

def validar_dni(dni):
    if dni.isdigit() and (len(dni) == 8 or len(dni) == 7):
        return True
    return False

def validar_usuario(usuario):
    usuario = usuario.lower()
    if usuario.isalpha():
        return usuario
    return False
        
def validar_email(correo):
    correo = correo.lower()
    if '@' in correo and '.com' in correo:
        return correo
    return False
    
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    if not re.search(r"[a-z]", contrasena):
        return False
    if not re.search(r"[0-9]", contrasena):
        return False
    return True