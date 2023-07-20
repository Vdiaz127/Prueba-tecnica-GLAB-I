from django.contrib.auth.backends import BaseBackend
from .models import Usuario_Admin


class BackendDeAutenticacion(BaseBackend):
    def authenticate(self, request, correo_id=None, contraseña=None):
        try:
            usuario = Usuario_Admin.objects.get(correo=correo_id)#(correo__correo=correo)
            if usuario.check_password(contraseña):
                return usuario
        except Usuario_Admin.DoesNotExist:
            return None

    def get_user(self, correo_id):
        try:
            return Usuario_Admin.objects.get(correo=correo_id)
        except Usuario_Admin.DoesNotExist:
            return None