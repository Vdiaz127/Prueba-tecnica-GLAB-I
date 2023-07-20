from reservations.models import *

def verificar_correo(correo_id):
    existe_correo = Usuario.objects.filter(correo=correo_id).exists()
    if existe_correo: 
        return True
    else:
        return False

def usuario_admin(correo_id):
    usuario =  Usuario.objects.get(correo=correo_id)
    if usuario.rol=="usuario":
        return False
    else:
        return True