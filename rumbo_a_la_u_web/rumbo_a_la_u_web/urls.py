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
from django.contrib.auth import views as auth_views
from django.urls import path
from rumbo_a_la_u_web.views import index
from .views import *
from django.urls import path, include
from .views_register import RegisterView
from .views_login import LoginView

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    # Error 404
    path('error', error, name="error"),

    # Sobre nosotros
    path('sobrenosotros', sobrenosotros, name="sobrenosotros"),

    # Carro de compras
    path('carro', carro, name="carro"),

    # Seccion Profesores
    path('profesores', profesores, name="profesores"),

    # Seccion Dashboard Alumno
    path('alumno-calendario', alumnocalendario, name="alumnocalendario"),
    path('alumno-configuraciones', alumnoconfiguraciones,
         name="alumnoconfiguraciones"),
    path('alumno-cursosmatriculados',
         alumnocursosmatriculados, name="alumnocursosmatriculados"),
    path('alumno-dashboard', alumnodashboard, name="alumnodashboard"),
    path('alumno-historialpedidos',
         alumnohistorialpedidos, name="alumnohistorialpedidos"),
    path('alumno-listadeseos', alumnolistadeseos, name="alumnolistadeseos"),
    path('alumno-miperfil', alumnomiperfil, name="alumnomiperfil"),
    path('alumno-misevaluaciones', alumnomisevaluaciones,
         name="alumnomisevaluaciones"),
    path('alumno-pregyresp', alumnopregyresp, name="alumnopregyresp"),
    path('alumno-resenas', alumnoresenas name="alumnoresenas"),

    # Seccion Dashboard Profesor
    path('profesor-anuncios', profesor-anuncios, name="profesor-anuncios"),
    path('profesor-asignaciontareas', profesor - \
         asignaciontareas, name="profesor-asignaciontareas"),
    path('profesor-calendario', profesor - \
         calendario, name="profesor-calendario"),
    path('profesor-certificado', profesor - \
         certificado, name="profesor-certificado"),
    path('profesor-configuraciones', profesor - \
         configuraciones, name="profesor-configuraciones"),
    path('profesor-dashboard', profesor-configuraciones,
         name="profesor-configuraciones"),
    path('profesor-evaluaciones', profesor - \
         evaluaciones, name="profesor-evaluaciones"),
    path('profesor-miperfil', profesor-miperfil, name="profesor-miperfil"),
    path('profesor-miperfil', profesor-miperfil, name="profesor-miperfil"),
    path('profesor-miscursos', profesor-miscursos, name="profesor-miscursos"),
    path('profesor-pregyresp', profesor-pregyresp, name="profesor-pregyresp"),
    path('profesor-registro', profesor-registro, name="profesor-registro"),
    path('profesor-reporteria', profesor - \
         reporteria, name="profesor-reporteria"),
    path('profesor-resenas', profesor-resenas, name="profesor-resenas"),
    path('profesor-saldo', profesor-saldo, name="profesor-saldo"),

    # Seccion Perfiles Profesores
    path('profesor-profile-biologia', profesor - \
         profile-biologia, name="profesor-profile-biologia"),
    path('profesor-profile-complectora', profesor - \
         profile-complectora, name="profesor-profile-complectora"),
    path('profesor-profile-fisica', profesor - \
         profile-fisica, name="profesor-profile-fisica"),
    path('profesor-profile-historia', profesor - \
         profile-historia, name="profesor-profile-historia"),
    path('profesor-profile-matematica', profesor - \
         profile-matematica, name="profesor-profile-matematica"),
    path('profesor-profile-quimica', profesor - \
         profile-quimica, name="profesor-profile-quimica"),

    # Seccion blog
    path('blog', blog, name="blog"),
    path('blogdet', blogblogdet, name="blogblogdet"),
    path('blogblogdet01', blogblogdet01, name="blogblogdet01"),
    path('blogblogdet02', blogblogdet02, name="blogblogdet02"),
    path('blogblogdet03', blogblogdet03, name="blogblogdet03"),
    path('blogblogdet04', blogblogdet04, name="blogblogdet04"),
    path('blogblogdet05', blogblogdet05, name="blogblogdet05"),

    # Seccion Cursos
    path('cursos', cursos, name="cursos"),
    path('curso-crear', curso-crear, name="curso-crear"),
    path('cursos-biologia-organismoyambiente', cursos-biologia - \
         organismoyambiente, name="cursos-biologia-organismoyambiente"),
    path('cursos-complectora-evaluar', cursos - \
         complectora-evaluar, name="cursos-complectora-evaluar"),
    path('cursos-complectora-interpretar', cursos - \
         complectora-interpretar, name="cursos-complectora-interpretar"),
    path('cursos-complectora-localizar', cursos - \
         complectora-localizar, name="cursos-complectora-localizar"),
    path('cursos-fisica-mecanica', cursos-fisica - \
         mecanica, name="cursos-fisica-mecanica"),
    path('cursos-historia-ejehistoria', cursos - \
         historia-ejehistoria, name="cursos-historia-ejehistoria"),
    path('cursos-matematicas-algebrayfunciones', cursos - \
         matematicas-algebrayfunciones, name="cursos-matematicas-algebrayfunciones"),
    path('cursos-matematicas-numeros', cursos - \
         matematicas-numeros, name="cursos-matematicas-numeros"),
    path('cursos-quimica-estructuraatomica', cursos - \
         quimica-estructuraatomica, name="cursos-quimica-estructuraatomica"),

    # Seccion Header
    path('header', header, name="header"),

    # Seccion Footer
    path('footer', footer, name="footer"),

    # Seccion Login
    path('login', login, name="login"),

    # Seccion Planes de Membresia
    path('planesdemembresia', planesdemembresia, name="planesdemembresia"),

    # Seccion Registro
    path('registro', registro, name="registro"),
    path('register/', RegisterView.as_view(), name='views_register'),
    path('login/', LoginView.as_view(), name='views_login'),

    # Seccion zoom
    path('zoom-detalles-mat-algebrayfunciones', zoom-detalles-mat - \
         algebrayfunciones, name="zoom-detalles-mat-algebrayfunciones"),
    path('zoom-detalles-mat-geometria', zoom - \
         detalles-mat-geometria, name="zoom-detalles-mat-geometria"),
    path('zoom-detalles-mat-geometria', zoom - \
         detalles-mat-geometria, name="zoom-detalles-mat-geometria"),
    path('zoom-detalles-mat-probabilidadyestadistica', zoom - \
         detalles-probabilidadyestadistica, name="zoom-detalles-probabilidadyestadistica"),
    path('zoom-detalles-quim-estructuraatomica', zoom - \
         detalles-quim-estructuraatomica, name="zoom-detalles-quim-estructuraatomica"),
    path('zoom-detalles-quim-quimicaorganica', zoom - \
         detalles-quim-quimicaorganica, name="zoom-detalles-quim-quimicaorganica"),
    path('zoom-detalles-quim-quimicasyestequiometria', zoom - \
         detalles-quim-quimicasyestequiometria, name="zoom-detalles-quim-quimicasyestequiometria"),
    path('zoom-reuniones', zoomdetails, name="zoom-details"),

]
