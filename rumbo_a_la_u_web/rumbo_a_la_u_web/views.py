from django.shortcuts import render
from .models import Usuarios



def index(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id) if user_id else None
    return render(request, 'index.html', {'user': user})


def sobrenosotros(request):
    return render(request, 'sobrenosotros.html')


def profesores(request):
    return render(request, 'profesores.html')


def pricing(request):
    return render(request, 'pricing.html')


def bloglist(request):
    return render(request, 'blog-list.html')


def blogdetails(request):
    return render(request, 'blog-details.html')


def zoommeeting(request):
    return render(request, 'zoom-meeting.html')


def zoomdetails(request):
    return render(request, 'zoom-details.html')


def event(request):
    return render(request, 'event.html')


def carro(request):
    return render(request, 'carro.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registro.html')


def cursocrear(request):
    return render(request, 'curso-crear.html')


def becomeinstructor(request):
    return render(request, 'become-instructor.html')


def error(request):
    return render(request, '404.html')

def studentprofile(request):
    return render(request, 'alumno-miperfil.html')

def blog(request):
    return render(request, 'blog.html')

def alumnoconfiguraciones(request):
    return render(request, 'alumno-configuraciones.html')

def alumnocursosmatriculados(request):
    return render(request, 'alumno-cursosmatriculados.html')

def alumnodashboard(request):
    return render(request, 'alumno-dashboard.html')

def alumnohistorialdepedidos(request):
    return render(request, 'alumno-historialdepedidos.html')

def alumnolistadedeseos(request):
    return render(request, 'alumno-listadedeseos.html')

def alumnomisevaluaciones(request):
    return render(request, 'alumno-misevaluaciones.html')

def alumnopregyresp(request):
    return render(request, 'alumno-pregyresp.html')

def alumnoresenas(request):
    return render(request, 'alumno-resenas.html')
