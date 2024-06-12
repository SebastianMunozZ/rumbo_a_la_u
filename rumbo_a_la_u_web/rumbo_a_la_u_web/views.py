from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Código para la vista de la página de inicio
    return render(request, 'index.html')


def error(request):
    # Código para la vista de la página de error 404
    return HttpResponse("Error 404 - Página no encontrada")


def sobrenosotros(request):
    # Código para la vista de la sección "Sobre Nosotros"
    return render(request, 'sobrenosotros.html')


def carro(request):
    # Código para la vista del carrito de compras
    return render(request, 'carro.html')


def profesores(request):
    # Código para la vista de la sección "Profesores"
    return render(request, 'profesores.html')


def alumnocalendario(request):
    # Código para la vista del calendario del alumno
    return render(request, 'alumno-calendario.html')


def alumnoconfiguraciones(request):
    # Código para la vista de las configuraciones del alumno
    return render(request, 'alumno-configuraciones.html')


def alumnocursosmatriculados(request):
    # Código para la vista de los cursos matriculados del alumno
    return render(request, 'alumno-cursosmatriculados.html')


def alumnodashboard(request):
    # Código para la vista del dashboard del alumno
    return render(request, 'alumno-dashboard.html')


def alumnohistorialpedidos(request):
    # Código para la vista del historial de pedidos del alumno
    return render(request, 'alumno-historialpedidos.html')


def alumnolistadeseos(request):
    # Código para la vista de la lista de deseos del alumno
    return render(request, 'alumno-listadeseos.html')


def alumnomiperfil(request):
    # Código para la vista del perfil del alumno
    return render(request, 'alumno-miperfil.html')


def alumnomisevaluaciones(request):
    # Código para la vista de las evaluaciones del alumno
    return render(request, 'alumno-misevaluaciones.html')


def alumnopregyresp(request):
    # Código para la vista de preguntas y respuestas del alumno
    return render(request, 'alumno-pregyresp.html')


def alumnoresenas(request):
    # Código para la vista de las reseñas del alumno
    return render(request, 'alumno-resenas.html')


def profesor_anuncios(request):
    # Código para la vista de la sección de anuncios del profesor
    return render(request, 'profesor-anuncios.html')


def profesor_asignaciontareas(request):
    # Código para la vista de la asignación de tareas del profesor
    return render(request, 'profesor-asignaciontareas.html')


def profesor_calendario(request):
    # Código para la vista del calendario del profesor
    return render(request, 'profesor-calendario.html')


def profesor_certificado(request):
    # Código para la vista del certificado del profesor
    return render(request, 'profesor-certificado.html')


def profesor_configuraciones(request):
    # Código para la vista de las configuraciones del profesor
    return render(request, 'profesor-configuraciones.html')


def profesor_dashboard(request):
    # Código para la vista del dashboard del profesor
    return render(request, 'profesor-dashboard.html')


def profesor_evaluaciones(request):
    # Código para la vista de las evaluaciones del profesor
    return render(request, 'profesor-evaluaciones.html')


def profesor_miperfil(request):
    # Código para la vista del perfil del profesor
    return render(request, 'profesor-miperfil.html')


def profesor_miscursos(request):
    # Código para la vista de los cursos del profesor
    return render(request, 'profesor-miscursos.html')


def profesor_pregyresp(request):
    # Código para la vista de preguntas y respuestas del profesor
    return render(request, 'profesor-pregyresp.html')


def profesor_registro(request):
    # Código para la vista del registro del profesor
    return render(request, 'profesor-registro.html')


def profesor_reporteria(request):
    # Código para la vista de la reportería del profesor
    return render(request, 'profesor-reporteria.html')


def profesor_resenas(request):
    # Código para la vista de las reseñas del profesor
    return render(request, 'profesor-resenas.html')


def profesor_saldo(request):
    # Código para la vista del saldo del profesor
    return render(request, 'profesor-saldo.html')


def profesor_profile_biologia(request):
    # Código para la vista del perfil de biología del profesor
    return render(request, 'profesor-profile-biologia.html')


def profesor_profile_complectora(request):
    # Código para la vista del perfil de complectora del profesor
    return render(request, 'profesor-profile-complectora.html')


def profesor_profile_fisica(request):
    # Código para la vista del perfil de física del profesor
    return render(request, 'profesor-profile-fisica.html')


def profesor_profile_historia(request):
    # Código para la vista del perfil de historia del profesor
    return render(request, 'profesor-profile-historia.html')


def profesor_profile_matematica(request):
    # Código para la vista del perfil de matemática del profesor
    return render(request, 'profesor-profile-matematica.html')


def profesor_profile_quimica(request):
    # Código para la vista del perfil de química del profesor
    return render(request, 'profesor-profile-quimica.html')


def blog(request):
    # Código para la vista de la sección de blog
    return render(request, 'blog.html')


def blogdet(request):
    # Código para la vista de la página de detalles del blog
    return render(request, 'blogdet.html')


def blogblogdet01(request):
    # Código para la vista de la página 01 de detalles del blog
    return render(request, 'blogblogdet01.html')


def blogblogdet02(request):
    # Código para la vista de la página 02 de detalles del blog
    return render(request, 'blogblogdet02.html')


def blogblogdet03(request):
    # Código para la vista de la página 03 de detalles del blog
    return render(request, 'blogblogdet03.html')


def blogblogdet04(request):
    # Código para la vista de la página 04 de detalles del blog
    return render(request, 'blogblogdet04.html')


def blogblogdet05(request):
    # Código para la vista de la página 05 de detalles del blog
    return render(request, 'blogblogdet05.html')


def cursos(request):
    # Código para la vista de la sección de cursos
    return render(request, 'cursos.html')


def curso_crear(request):
    # Código para la vista de la creación de curso
    return render(request, 'curso-crear.html')


def cursos_biologia_organismoyambiente(request):
    # Código para la vista de cursos de biología sobre organismos y ambiente
    return render(request, 'cursos-biologia-organismoyambiente.html')


def cursos_complectora_evaluar(request):
    # Código para la vista de cursos de complectora sobre evaluación
    return render(request, 'cursos-complectora-evaluar.html')


def cursos_complectora_interpretar(request):
    # Código para la vista de cursos de complectora sobre interpretación
    return render(request, 'cursos-complectora-interpretar.html')


def cursos_complectora_localizar(request):
    # Código para la vista de cursos de complectora sobre localización
    return render(request, 'cursos-complectora-localizar.html')


def cursos_fisica_mecanica(request):
    # Código para la vista de cursos de física sobre mecánica
    return render(request, 'cursos-fisica-mecanica.html')


def cursos_historia_ejehistoria(request):
    # Código para la vista de cursos de historia sobre el eje historia
    return render(request, 'cursos-historia-ejehistoria.html')


def cursos_matematicas_algebrayfunciones(request):
    # Código para la vista de cursos de matemáticas sobre álgebra y funciones
    return render(request, 'cursos-matematicas-algebrayfunciones.html')


def cursos_matematicas_numeros(request):
    # Código para la vista de cursos de matemáticas sobre números
    return render(request, 'cursos-matematicas-numeros.html')


def cursos_quimica_estructuraatomica(request):
    # Código para la vista de cursos de química sobre estructura atómica
    return render(request, 'cursos-quimica-estructuraatomica.html')


def header(request):
    # Código para la vista de la sección de header
    return render(request, 'header.html')


def footer(request):
    # Código para la vista de la sección de footer
    return render(request, 'footer.html')


def login(request):
    # Código para la vista de la sección de login
    return render(request, 'login.html')


def planesdemembresia(request):
    # Código para la vista de la sección de planes de membresía
    return render(request, 'planesdemembresia.html')


def registro(request):
    # Código para la vista de la sección de registro
    return render(request, 'registro.html')


def zoom_detalles_mat_algebrayfunciones(request):
    # Código para la vista de detalles de zoom para matemáticas - álgebra y funciones
    return render(request, 'zoom-detalles-mat-algebrayfunciones.html')


def zoom_detalles_mat_geometria(request):
    # Código para la vista de detalles de zoom para matemáticas - geometría
    return render(request, 'zoom-detalles-mat-geometria.html')


def zoom_detalles_mat_probabilidadyestadistica(request):
    # Código para la vista de detalles de zoom para matemáticas - probabilidad y estadística
    return render(request, 'zoom-detalles-mat-probabilidadyestadistica.html')


def zoom_detalles_quim_estructuraatomica(request):
    # Código para la vista de detalles de zoom para química - estructura atómica
    return render(request, 'zoom-detalles-quim-estructuraatomica.html')


def zoom_detalles_quim_quimicaorganica(request):
    # Código para la vista de detalles de zoom para química orgánica
    return render(request, 'zoom-detalles-quim-quimicaorganica.html')


def zoom_detalles_quim_quimicasyestequiometria(request):
    # Código para la vista de detalles de zoom para química y estequiometría
    return render(request, 'zoom-detalles-quim-quimicasyestequiometria.html')


def zoom_reuniones(request):
    # Código para la vista de detalles de zoom para reuniones
    return render(request, 'zoom-reuniones.html')
