from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from .models import Usuarios, Profesor, Alumno, Curso, Comentario
from django.contrib.auth.hashers import make_password

class CommentView(View):
    def post(self, request):
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        comentario = request.POST.get('comentario')
        id_noticia = request.POST.get('id_noticia')

        comentario = Comentario(
            nombre=nombre,
            apellido=apellido,
            comentario=comentario,
            noticia=id_noticia
        )
        comentario.save()

        return redirect('blog')
