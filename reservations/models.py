from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, clave, **extra_fields):
        usuario = self.model(
            correo=correo,
            **extra_fields
        )
        usuario.set_password(clave)
        usuario.save(using=self._db)
        return usuario
    
class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(primary_key=True)
    rol = models.CharField(max_length=20, default="usuario")
    tipo_documento = models.CharField(max_length=20)
    numero_documento = models.CharField(max_length=20)
    class Meta:
        db_table = 'Usuario'

class Usuario_Admin(AbstractBaseUser):
    correo = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "correo"
    class Meta:
        db_table = 'Usuario Administrador'
    objects = UsuarioManager() 

class Reservacion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_reservacion = models.DateField()
    tipo_reserva = models.CharField(max_length=20)
    cantidad_personas = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    reservado = models.BooleanField(default=False)

    class Meta:
        db_table = 'Reservacion'