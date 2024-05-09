from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from .models import Usuarios
from django.contrib.auth.hashers import check_password

class LoginView(View):
    def post(self, request):
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
            user = Usuarios.objects.get(correo_electronico=correo)
        except Usuarios.DoesNotExist:
            messages.error(request, 'Correo electrónico o contraseña incorrectos')
            return redirect('login')

        if not check_password(password, user.contrasena):
            messages.error(request, 'Correo electrónico o contraseña incorrectos')
            return redirect('login')

        return redirect('index')