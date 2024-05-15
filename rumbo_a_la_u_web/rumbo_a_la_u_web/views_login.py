from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from .models import Usuarios
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from django.shortcuts import render

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
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

        request.session['user_id'] = user.user_id
        return redirect('index')