from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from .models import Usuarios
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

        return redirect('login')