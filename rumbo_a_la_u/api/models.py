from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)
    tipo_usuario = models.CharField(default=1,max_length=1)