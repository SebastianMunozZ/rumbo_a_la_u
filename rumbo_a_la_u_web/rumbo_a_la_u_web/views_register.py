from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from django.core.mail import send_mail
from .models import Usuarios, Profesor, Alumno
from django.contrib.auth.hashers import make_password, check_password

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

        send_mail(
            'Bienvenido a Rumbo a La U',
            'Gracias por registrarte en nuestra plataforma.',
            'rumboalau@outlook.com',
            [correo],
            fail_silently=False,
        )

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
        if 'user_id' in request.session:
            user = Usuarios.objects.get(user_id=request.session['user_id'])
            nombre = user.nombre
        else:
            nombre = request.POST.get('nombre')

        nombre_parts = nombre.split()

        if len(nombre_parts) >= 3:
            apellido = ' '.join(nombre_parts[1:3])
        else:
            apellido = ' '.join(nombre_parts[1:]) if len(nombre_parts) > 1 else ''

        asignatura = request.POST.get('asignatura')

        if 'user_id' in request.session:
            user = Usuarios.objects.get(user_id=request.session['user_id'])
            username = user.username
        else:
            username = request.POST.get('username')

        if 'user_id' in request.session:
            user = Usuarios.objects.get(user_id=request.session['user_id'])
            correo = user.correo_electronico
        else:
            correo = request.POST.get('correo')

        if 'user_id' in request.session:
            user = Usuarios.objects.get(user_id=request.session['user_id'])
            password = user.contrasena
        else:
            password = request.POST.get('password')
        
        
        if not 'user_id' in request.session:
            if Usuarios.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya existe')
                return redirect('profesorregistro')
        if Usuarios.objects.filter(correo_electronico=correo).exists():
            user = Usuarios.objects.get(correo_electronico=correo)
            user.tipo_usuario = 2
            user.save()
            profesor = Profesor(user_id=request.session['user_id'],
                            nombre=nombre,
                            apellido=apellido,
                            asignatura_que_ensena=asignatura)

            profesor.save()
            return redirect('login')

        
        user = Usuarios(
            nombre=nombre,
            username=username,
            correo_electronico=correo,
            contrasena=make_password(password),
        )
        
        user.save()
        profesor = Profesor(user_id=request.session['user_id'],
                            nombre=nombre,
                            apellido=apellido,
                            asignatura_que_ensena=asignatura)

        profesor.save()

        return redirect('login')
    
class ChangePasswordView(View):
    def post(self, request):
        if request.method == 'POST':
            user_id = request.session.get('user_id')
            user = Usuarios.objects.get(user_id=user_id)
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if not check_password(current_password, user.contrasena):
                # La contraseña actual es incorrecta
                messages.error(request, 'La contraseña actual es incorrecta')
                return redirect('alumnoconfiguraciones')

            if new_password != confirm_password:
                # La nueva contraseña y la confirmación no coinciden
                messages.error(request, 'Las contraseñas no coinciden')
                return redirect('alumnoconfiguraciones')

            # Todo está bien, cambiar la contraseña
            user.contrasena = make_password(new_password)
            user.save()

            return redirect('login')

        return redirect('alumnoconfiguraciones')