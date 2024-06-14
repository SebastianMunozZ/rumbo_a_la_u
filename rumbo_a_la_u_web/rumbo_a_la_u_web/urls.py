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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import index
from .views import *
from django.urls import path, include
from .views_register import RegisterView, RegisterTeacherView
from .views_courses import CourseView
from .views_login import LoginView
from .views_sell_course import SellCourseView
from .views_cart import load as load_viewcart
from .views_sell_course import SellCourseView
from .views_blogcomments import CommentView
from .views import transbankpay_load, transbankpay_commitpay
from .views import error
from .views import sobrenosotros  # Import the missing view function
from .views import carro

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    # Error 404
    path('404', error, name="error"),

    # Sobre nosotros
    path('sobrenosotros', sobrenosotros, name="sobrenosotros"),

    # Carro de compras
    path('carro', carro, name="carro"),
    path('webpay-plus-create', transbankpay_load),
    path('commit-pay', transbankpay_commitpay),

    # Seccion Profesores
    path('profesores', profesores, name="profesores"),

    # Seccion Dashboard Alumno
    path('alumno-calendario', alumnocalendario, name="alumnocalendario"),
    path('alumno-configuraciones', alumnoconfiguraciones, name="alumnoconfiguraciones"),
    path('alumno-cursosmatriculados', alumnocursosmatriculados, name="alumnocursosmatriculados"),
    path('alumno-dashboard', alumnodashboard, name="alumnodashboard"),
    path('alumno-historialpedidos', alumnohistorialpedidos, name="alumnohistorialpedidos"),
    path('alumno-listadeseos', alumnolistadeseos, name="alumnolistadeseos"),
    path('alumno-miperfil', alumnomiperfil, name="alumnomiperfil"),
    path('alumno-misevaluaciones', alumnomisevaluaciones, name="alumnomisevaluaciones"),
    path('alumno-pregyresp', alumnopregyresp, name="alumnopregyresp"),
    path('alumno-resenas', alumnoresenas, name="alumnoresenas"),

    # Seccion Dashboard Profesor
    path('profesor-anuncios', profesoranuncios, name="profesor-anuncios"),
    path('profesor-asignaciontareas', profesorasignaciontareas, name="profesor-asignaciontareas"),
    path('profesor-calendario', profesorcalendario, name="profesor-calendario"),
    path('profesor-certificado', profesorcertificado, name="profesor-certificado"),
    path('profesor-configuraciones', profesorconfiguraciones, name="profesor-configuraciones"),
    path('profesor-dashboard', profesorconfiguraciones, name="profesor-dashboard"),
    path('profesor-evaluaciones', profesorevaluaciones, name="profesor-evaluaciones"),
    path('profesor-miperfil', profesormiperfil, name="profesor-miperfil"),
    path('profesor-miperfil', profesormiperfil, name="profesor-miperfil"),
    path('profesor-miscursos', profesormiscursos, name="profesor-miscursos"),
    path('profesor-pregyresp', profesorpregyresp, name="profesor-pregyresp"),
    path('profesor-registro', profesorregistro, name="profesorregistro"),
    path('profesor-reporteria', profesorreporteria, name="profesor-reporteria"),
    path('profesor-resenas', profesorresenas, name="profesor-resenas"),
    path('profesor-saldo', profesorsaldo, name="profesor-saldo"),

    # Seccion Perfiles Profesores
    path('profesor-profile-biologia', profesorprofilebiologia, name="profesor-profile-biologia"),
    path('profesor-profile-complectora', profesorprofilecomplectora, name="profesor-profile-complectora"),
    path('profesor-profile-fisica', profesorprofilefisica, name="profesor-profile-fisica"),
    path('profesor-profile-historia', profesorprofilehistoria, name="profesor-profile-historia"),
    path('profesor-profile-matematica', profesorprofilematematica, name="profesor-profile-matematica"),
    path('profesor-profile-quimica', profesorprofilequimica, name="profesor-profile-quimica"),

    # Seccion blog
    path('blog', blog, name="blog"),
    path('blogdet', blogblogdet, name="blogblogdet"),
    path('blogblogdet01', blogblogdet01, name="blogblogdet01"),
    path('blogblogdet02', blogblogdet02, name="blogblogdet02"),
    path('blogblogdet03', blogblogdet03, name="blogblogdet03"),
    path('blogblogdet04', blogblogdet04, name="blogblogdet04"),
    path('blogblogdet05', blogblogdet05, name="blogblogdet05"),
    path('comentario/', CommentView.as_view(), name='comentario'),

    # Seccion Cursos
    path('cursos', cursos, name="cursos"),
    path('agregarcurso/<int:course_id>', SellCourseView.as_view()),
    path('sell-courses', SellCourseView.as_view(), name="views_sell_course"),
    path('sell-courses', SellCourseView.as_view(), name="views_sell_course"),
    path('curso-crear', cursocrear, name="cursocrear"),
    path('cursos-biologia-organismoyambiente', cursosbiologiaorganismoyambiente, name="cursos-biologia-organismoyambiente"),
    path('cursos-complectora-evaluar', cursoscomplectoraevaluar, name="cursos-complectora-evaluar"),
    path('cursos-complectora-interpretar', cursoscomplectorainterpretar, name="cursos-complectora-interpretar"),
    path('cursos-complectora-localizar', cursoscomplectoralocalizar, name="cursos-complectora-localizar"),
    path('cursos-fisica-mecanica', cursosfisicamecanica, name="cursos-fisica-mecanica"),
    path('cursos-historia-ejehistoria', cursoshistoriaejehistoria, name="cursos-historia-ejehistoria"),
    path('cursos-matematicas-algebrayfunciones', cursosmatematicasalgebrayfunciones, name="cursos-matematicas-algebrayfunciones"),
    path('cursos-matematicas-numeros', cursosmatematicasnumeros, name="cursos-matematicas-numeros"),
    path('cursos-quimica-estructuraatomica', cursosquimicaestructuraatomica, name="cursos-quimica-estructuraatomica"),
    path('course/', CourseView.as_view(), name='views_course'),

    # Seccion Header
    path('header', header, name="header"),

    # Seccion Footer
    path('footer', footer, name="footer"),

    # Seccion Login
    path('login', login, name="login"),

    # Seccion Planes de Membresia
    path('planesdemembresia', planesdemembresia, name="planesdemembresia"), 

    # Seccion Registro
    path('registration/', registration, name="registration"),
    path('register/', RegisterView.as_view(), name='views_register'),
    path('registerteacher/', RegisterTeacherView.as_view(), name='views_teacher_register'),
    path('login/', LoginView.as_view(), name='views_login'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Seccion zoom
    path('zoom-detalles-mat-algebrayfunciones', zoomdetallesmatalgebrayfunciones, name="zoom-detalles-mat-algebrayfunciones"),
    path('zoom-detalles-mat-geometria', zoomdetallesmatgeometria, name="zoom-detalles-mat-geometria"),
    path('zoom-detalles-mat-probabilidadyestadistica', zoomdetallesprobabilidadyestadistica, name="zoom-detalles-probabilidadyestadistica"),
    path('zoom-detalles-quim-estructuraatomica', zoomdetallesquimestructuraatomica, name="zoom-detalles-quim-estructuraatomica"),
    path('zoom-detalles-quim-quimicaorganica', zoomdetallesquimquimicaorganica, name="zoom-detalles-quim-quimicaorganica"),
    path('zoom-detalles-quim-quimicasyestequiometria', zoomdetallesquimquimicasyestequiometria, name="zoom-detalles-quim-quimicasyestequiometria"),
    path('zoom-reuniones', zoomdetails, name="zoom-reuniones"),
    path('zoom-prueba', zoomprueba, name="zoom-prueba"),
    path('generate_signature/', generatesignature, name='generate_signature'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
