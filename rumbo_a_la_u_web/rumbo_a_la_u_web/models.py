from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuarios(models.Model):
    user_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=255, default ="1")

    class Meta:
        db_table = 'USUARIOS'

class Alumno(models.Model):
    user = models.OneToOneField(Usuarios, primary_key=True, on_delete=models.CASCADE)
    ano_de_ingreso = models.CharField(max_length=255, default='2024')
    nivel_de_educacion = models.CharField(max_length=255, default='Media Completa')
    comuna_id = models.CharField(max_length=255, default='1')

    class Meta:
        db_table = 'ESTUDIANTES'

class Profesor(models.Model):
    usuario = models.OneToOneField(Usuarios, on_delete=models.CASCADE)
    asignatura = models.CharField(max_length=255)
    # Tus campos específicos de Profesor aquí

    class Meta:
        db_table = 'PROFESORES'