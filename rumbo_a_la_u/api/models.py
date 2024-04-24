from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True, db_column='user_id')
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo_electronico = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=1,default=1)

    class Meta:
        db_table = 'USUARIOS'