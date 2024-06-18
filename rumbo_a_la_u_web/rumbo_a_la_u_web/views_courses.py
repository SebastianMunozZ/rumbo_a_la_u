from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from .models import Usuarios, Profesor, Alumno, Curso
from django.contrib.auth.hashers import make_password

class CourseView(View):
    def post(self, request):
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        asignatura = request.POST.get('asignatura')
        gratis = request.POST.get('gratis')
        pagado = request.POST.get('pagado')
        precio = request.POST.get('precio')
        foto = request.FILES.get('foto')

        es_pagado = 1
        if (gratis == True):
            es_pagado = 0

        try:
            profesor = Profesor.objects.get(user_id=request.session['user_id'])
        except Profesor.DoesNotExist:
            return redirect('cursocrear')
        curso = Curso(
            nombre_del_curso=titulo,
            descripcion=descripcion,
            asignatura=asignatura,
            es_pagado=es_pagado,
            precio=precio,
            miniatura=foto,
            teacher_id=profesor.teacher_id
        )
        curso.save()

        return redirect('cursocrear')
