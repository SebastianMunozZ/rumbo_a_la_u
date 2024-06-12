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
from .views_register import RegisterView

from django.urls import path
from .views import *

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
    path('alumno-cursosmatriculados', alumnocursosmatriculados,
         name="alumnocursosmatriculados"),
    path('alumno-dashboard', alumnodashboard, name="alumnodashboard"),
    path('alumno-historialpedidos', alumnohistorialpedidos,
         name="alumnohistorialpedidos"),
    path('alumno-listadeseos', alumnolistadeseos, name="alumnolistadeseos"),
    path('alumno-miperfil', alumnomiperfil, name="alumnomiperfil"),
    path('alumno-misevaluaciones', alumnomisevaluaciones,
         name="alumnomisevaluaciones"),
    path('alumno-pregyresp', alumnopregyresp, name="alumnopregyresp"),
    path('alumno-resenas', alumnoresenas, name="alumnoresenas"),  # Corregido

    # Seccion Dashboard Profesor
    path('profesor-anuncios', profesor_anuncios,
         name="profesor_anuncios"),  # Corregido
    path('profesor-asignaciontareas', profesor_asignaciontareas,
         name="profesor_asignaciontareas"),  # Corregido
    path('profesor-calendario', profesor_calendario,
         name="profesor_calendario"),  # Corregido
    path('profesor-certificado', profesor_certificado,
         name="profesor_certificado"),  # Corregido
    path('profesor-configuraciones', profesor_configuraciones,
         name="profesor_configuraciones"),  # Corregido
    path('profesor-dashboard', profesor_dashboard,
         name="profesor_dashboard"),  # Corregido
    path('profesor-evaluaciones', profesor_evaluaciones,
         name="profesor_evaluaciones"),  # Corregido
    path('profesor-miperfil', profesor_miperfil,
         name="profesor_miperfil"),  # Corregido
    path('profesor-miscursos', profesor_miscursos,
         name="profesor_miscursos"),  # Corregido
    path('profesor-pregyresp', profesor_pregyresp,
         name="profesor_pregyresp"),  # Corregido
    path('profesor-registro', profesor_registro,
         name="profesor_registro"),  # Corregido
    path('profesor-reporteria', profesor_reporteria,
         name="profesor_reporteria"),  # Corregido
    path('profesor-resenas', profesor_resenas,
         name="profesor_resenas"),  # Corregido
    path('profesor-saldo', profesor_saldo, name="profesor_saldo"),  # Corregido

    # Seccion Perfiles Profesores
    path('profesor-profile-biologia', profesor_profile_biologia,
         name="profesor_profile_biologia"),  # Corregido
    path('profesor-profile-complectora', profesor_profile_complectora,
         name="profesor_profile_complectora"),  # Corregido
    path('profesor-profile-fisica', profesor_profile_fisica,
         name="profesor_profile_fisica"),  # Corregido
    path('profesor-profile-historia', profesor_profile_historia,
         name="profesor_profile_historia"),  # Corregido
    path('profesor-profile-matematica', profesor_profile_matematica,
         name="profesor_profile_matematica"),  # Corregido
    path('profesor-profile-quimica', profesor_profile_quimica,
         name="profesor_profile_quimica"),  # Corregido

    # Seccion blog
    path('blog', blog, name="blog"),
    path('blogdet', blogdet, name="blogdet"),
    path('blogblogdet01', blogblogdet01, name="blogblogdet01"),
    path('blogblogdet02', blogblogdet02, name="blogblogdet02"),
    path('blogblogdet03', blogblogdet03, name="blogblogdet03"),
    path('blogblogdet04', blogblogdet04, name="blogblogdet04"),
    path('blogblogdet05', blogblogdet05, name="blogblogdet05"),

    # Seccion Cursos
    path('cursos', cursos, name="cursos"),
    path('curso-crear', curso_crear, name="curso_crear"),
    path('cursos-biologia-organismoyambiente', cursos_biologia_organismoyambiente,
         name="cursos_biologia_organismoyambiente"),  # Corregido
    path('cursos-complectora-evaluar', cursos_complectora_evaluar,
         name="cursos_complectora_evaluar"),  # Corregido
    path('cursos-complectora-interpretar', cursos_complectora_interpretar,
         name="cursos_complectora_interpretar"),  # Corregido
    path('cursos-complectora-localizar', cursos_complectora_localizar,
         name="cursos_complectora_localizar"),  # Corregido
    path('cursos-fisica-mecanica', cursos_fisica_mecanica,
         name="cursos_fisica_mecanica"),  # Corregido
    path('cursos-historia-ejehistoria', cursos_historia_ejehistoria,
         name="cursos_historia_ejehistoria"),  # Corregido
    path('cursos-matematicas-algebrayfunciones', cursos_matematicas_algebrayfunciones,
         name="cursos_matematicas_algebrayfunciones"),  # Corregido
    path('cursos-matematicas-numeros', cursos_matematicas_numeros,
         name="cursos_matematicas_numeros"),  # Corregido
    path('cursos-quimica-estructuraatomica', cursos_quimica_estructuraatomica,
         name="cursos_quimica_estructuraatomica"),  # Corregido

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

    # Seccion zoom
    path('zoom-detalles-mat-algebrayfunciones', zoom_detalles_mat_algebrayfunciones,
         name="zoom_detalles_mat_algebrayfunciones"),  # Corregido
    path('zoom-detalles-mat-geometria', zoom_detalles_mat_geometria,
         name="zoom_detalles_mat_geometria"),  # Corregido
    path('zoom-detalles-mat-probabilidadyestadistica', zoom_detalles_mat_probabilidadyestadistica,
         name="zoom_detalles_mat_probabilidadyestadistica"),  # Corregido
    path('zoom-detalles-quim-estructuraatomica', zoom_detalles_quim_estructuraatomica,
         name="zoom_detalles_quim_estructuraatomica"),  # Corregido
    path('zoom-detalles-quim-quimicaorganica', zoom_detalles_quim_quimicaorganica,
         name="zoom_detalles_quim_quimicaorganica"),  # Corregido
    path('zoom-detalles-quim-quimicasyestequiometria', zoom_detalles_quim_quimicasyestequiometria,
         name="zoom_detalles_quim_quimicasyestequiometria"),  # Corregido
    path('zoom-reuniones', zoom_reuniones, name="zoom_reuniones"),  # Corregido
]
