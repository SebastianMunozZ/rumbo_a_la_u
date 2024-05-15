from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from .models import Usuarios, Profesor, Alumno
from django.contrib.auth.hashers import make_password

class RegisterView(View):
    def post(self, request):
        nombre = request.POST.get('nombre')
        username = request.POST.get('username')
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        if Usuarios.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe')
            return redirect('registration')
        if Usuarios.objects.filter(correo_electronico=correo).exists():
            messages.error(request, 'El correo electrónico ya está en uso')
            return redirect('registration')

        
        user = Usuarios(
            nombre=nombre,
            username=username,
            correo_electronico=correo,
            contrasena=make_password(password),
        )
        user.save()
        alumno = Alumno(user=user)
        alumno.save()

        

        return redirect('login')
    
class RegisterTeacherView(View):
    def post(self, request):
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellidos')
        asignatura = request.POST.get('asignatura')
        username = request.POST.get('username')
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        if Usuarios.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe')
            return redirect('profesorregistro')
        if Usuarios.objects.filter(correo_electronico=correo).exists():
            user = Usuarios.objects.get(correo_electronico=correo)
            user.tipo_usuario = 2
            user.save()
            return redirect('login')

        
        user = Usuarios(
            nombre=nombre,
            username=username,
            correo_electronico=correo,
            contrasena=make_password(password),
        )
        profesor = Profesor(usuario=user, asignatura=asignatura)

        profesor.save()
        user.save()

        return redirect('login')