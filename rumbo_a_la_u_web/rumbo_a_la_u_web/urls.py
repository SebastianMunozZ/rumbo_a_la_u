"""
URL configuration for rumbo_a_la_u_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rumbo_a_la_u_web.views import index
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('about', about, name="about"),
    path('cart', cart, name="cart"),
    path('instructor', instructor, name="instructor"),
    path('become-instructor', becomeinstructor, name="become-instructor"),
    path('pricing', pricing, name="pricing"),
    path('blog-list', bloglist, name="blog-list"),
    path('blog-details', blogdetails, name="blog-details"),
    path('zoom-meeting', zoommeeting, name="zoom-meeting"),
    path('zoom-details', zoomdetails, name="zoom-details"),
    path('event', event, name="event"),
    path('event-2', event2, name="event-2"),
    path('event-details', eventdetails, name="event-details"),
    path('course-four', coursefour, name="course-four"),
    path('course-three', coursethree, name="course-three"),
    path('course-two', coursetwo, name="course-two"),
    path('single-course', singlecourse, name="single-course"),
    path('create-course', createcourse, name="create-course"),
    path('registration', registration, name="registration"),
    path('login', login, name="login"),

]
