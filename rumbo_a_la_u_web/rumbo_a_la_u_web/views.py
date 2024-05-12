from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


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
