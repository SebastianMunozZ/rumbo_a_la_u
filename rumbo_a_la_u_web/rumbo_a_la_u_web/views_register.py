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
            return redirect('registration', {'error': 'El nombre de usuario ya existe'})
        if Usuarios.objects.filter(correo=correo).exists():
            return redirect('registration', {'error': 'El correo electrónico ya está en uso'})

        
        user = Usuarios(
            nombre=nombre,
            username=username,
            correo_electronico=correo,
            contrasena=make_password(password),
        )

        user.save()

        return redirect('login')