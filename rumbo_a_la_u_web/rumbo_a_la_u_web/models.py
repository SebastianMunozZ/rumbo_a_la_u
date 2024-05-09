from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuarios(models.Model):
    user_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)

    class Meta:
        db_table = 'USUARIOS'
