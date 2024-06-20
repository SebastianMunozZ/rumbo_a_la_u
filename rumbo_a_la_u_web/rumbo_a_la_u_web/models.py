
from django.db import models


class Usuarios(models.Model):
    user_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=255, default="1")

    class Meta:
        db_table = 'USUARIOS'


class Alumno(models.Model):
    user = models.OneToOneField(
        Usuarios, primary_key=True, on_delete=models.CASCADE)
    ano_de_ingreso = models.CharField(max_length=255, default='2024')
    nivel_de_educacion = models.CharField(
        max_length=255, default='Media Completa')
    comuna_id = models.CharField(max_length=255, default='1')

    class Meta:
        db_table = 'ESTUDIANTES'


class Profesor(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Usuarios, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    asignatura_que_ensena = models.CharField(max_length=255)
    # Tus campos específicos de Profesor aquí

    class Meta:
        db_table = 'PROFESORES'


class Curso(models.Model):
    course_id = models.AutoField(primary_key=True)
    nombre_del_curso = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    asignatura = models.CharField(max_length=100)
    es_pagado = models.IntegerField()
    precio = models.IntegerField(null=True, default=0)
    miniatura = models.ImageField(
        upload_to='media/', default='media/default.jpg')
    teacher = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CURSOS'


class ShoppingSession(models.Model):
    usuario = models.ForeignKey(
        Usuarios, models.DO_NOTHING, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SHOPPING_SESSION'


class Carro(models.Model):
    precio = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    # The composite primary key (products_id, shopping_session_id) found, that is not supported. The first column is selected.
    curso = models.OneToOneField('Curso', models.DO_NOTHING, primary_key=True)
    shopping_session = models.ForeignKey('ShoppingSession', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CARRO'
        unique_together = (('curso_id', 'shopping_session'),)


class Inscripciones(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    course = models.ForeignKey('Curso', on_delete=models.CASCADE)

    class Meta:
        db_table = 'INSCRIPCIONES'


class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    comentario = models.TextField()
    noticia = models.IntegerField(blank=True, null=False)

    class Meta:
        db_table = 'Comentario'
