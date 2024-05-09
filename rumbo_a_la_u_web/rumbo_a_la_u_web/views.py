from django.shortcuts import render
from .models import Usuarios



def index(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id) if user_id else None
    return render(request, 'index.html', {'user': user})


def about(request):
    return render(request, 'about.html')


def instructor(request):
    return render(request, 'instructor.html')


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


def cart(request):
    return render(request, 'cart.html')


def event2(request):
    return render(request, 'event-2.html')


def eventdetails(request):
    return render(request, 'event-details.html')


def coursefour(request):
    return render(request, 'course-four.html')


def coursethree(request):
    return render(request, 'course-three.html')


def coursetwo(request):
    return render(request, 'course-two.html')


def singlecourse(request):
    return render(request, 'single-course.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registro.html')


def createcourse(request):
    return render(request, 'create-course.html')


def becomeinstructor(request):
    return render(request, 'become-instructor.html')

def error(request):
    return render(request, '404.html')
