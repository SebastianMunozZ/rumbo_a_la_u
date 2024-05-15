from django.shortcuts import render
from .models import Usuarios, Curso
from .views_cart import load_cart
from django.shortcuts import redirect

def login_required_manual(func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapper



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
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    carts, quantities, total, products = load_cart(request.user.id)
    context = {
        'products': products,
        'quantities': quantities,
        'total': total,
    }
    return render(request, 'carro.html', {'user': user, 'context': context})


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registro.html')

def cursocrear(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'curso-crear.html', {'user': user})


def becomeinstructor(request):
    return render(request, 'become-instructor.html')


def error(request):
    return render(request, '404.html')

@login_required_manual
def alumnomiperfil(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-miperfil.html', {'user': user})

def blog(request):
    return render(request, 'blog.html')

@login_required_manual
def alumnocalendario(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-calendario.html', {'user':user})

@login_required_manual
def alumnoconfiguraciones(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-configuraciones.html', {'user':user})

@login_required_manual
def alumnocursosmatriculados(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-cursosmatriculados.html', {'user':user})

@login_required_manual
def alumnodashboard(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-dashboard.html', {'user':user})

@login_required_manual
def alumnohistorialpedidos(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-historialdepedidos.html', {'user':user})

@login_required_manual
def alumnolistadeseos(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-listadedeseos.html', {'user':user})

@login_required_manual
def alumnomisevaluaciones(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-misevaluaciones.html', {'user':user})

@login_required_manual
def alumnopregyresp(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-pregyresp.html', {'user':user})

@login_required_manual
def alumnoresenas(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-resenas.html', {'user':user})

@login_required_manual
def profesoranuncios(request):
    return render(request, 'profesor-anuncios.html')

@login_required_manual
def profesorasignaciontareas(request):
    return render(request, 'profesor-asignaciontareas.html')

@login_required_manual
def profesorcalendario(request):
    return render(request, 'profesor-calendario.html')

@login_required_manual
def profesorcertificado(request):
    return render(request, 'profesor-certificado.html')

@login_required_manual
def profesorconfiguraciones(request):
    return render(request, 'profesor-configuraciones.html')

@login_required_manual
def profesordashboard(request):
    return render(request, 'profesor-dashboard.html')

@login_required_manual
def profesorevaluaciones(request):
    return render(request, 'profesor-evaluaciones.html')

@login_required_manual
def profesormiperfil(request):
    return render(request, 'profesor-miperfil.html')

@login_required_manual
def profesormiscursos(request):
    return render(request, 'profesor-miscursos.html')

@login_required_manual
def profesorpregyresp(request):
    return render(request, 'profesor-pregyresp.html')

def profesorregistro(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id) if user_id else None
    return render(request, 'profesor-registro.html',{'user':user})

@login_required_manual
def profesorreporteria(request):
    return render(request, 'profesor-reporteria.html')

@login_required_manual
def profesorresenas(request):
    return render(request, 'profesor-resenas.html')

@login_required_manual
def profesorsaldo(request):
    return render(request, 'profesor-saldo.html')


def profesorprofilebiologia(request):
    return render(request, 'profesor-profile-biologia.html')

def profesorprofilecomplectora(request):
    return render(request, 'profesor-profile-complectora.html')

def profesorprofilefisica(request):
    return render(request, 'profesor-profile-fisica.html')

def profesorprofilehistoria(request):
    return render(request, 'profesor-profile-historia.html')

def profesorprofilematematica(request):
    return render(request, 'profesor-profile-matematica.html')

def profesorprofilequimica(request):
    return render(request, 'profesor-profile-quimica.html')

def blogblogdet(request):
    return render(request, 'blogblogdet.html')

def blogblogdet01(request):
    return render(request, 'blogblogdet01.html')

def blogblogdet02(request):
    return render(request, 'blogblogdet02.html')

def blogblogdet03(request):
    return render(request, 'blogblogdet03.html')

def blogblogdet04(request):
    return render(request, 'blogblogdet04.html')

def blogblogdet05(request):
    return render(request, 'blogblogdet05.html')

def cursos(request):
    cursos = Curso.objects.all()
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id) if user_id else None
    return render(request, 'cursos.html', {'cursos': cursos, 'user': user,})

def cursosbiologiaorganismoyambiente(request):
    return render(request, 'cursos-biologia-organismoyambiente.html')

def cursoscomplectoraevaluar(request):
    return render(request, 'cursos-complectora-evaluar.html')

def cursoscomplectorainterpretar(request):
    return render(request, 'cursos-complectora-interpretar.html')

def cursoscomplectoralocalizar(request):
    return render(request, 'cursos-complectora-localizar.html')

def cursosfisicamecanica(request):
    return render(request, 'cursos-fisica-mecanica.html')

def cursoshistoriaejehistoria(request):
    return render(request, 'cursos-historia-ejehistoria.html')

def cursosmatematicasalgebrayfunciones(request):
    return render(request, 'cursos-matematicas-algebrayfunciones.html')

def cursosmatematicasnumeros(request):
    return render(request, 'cursos-matematicas-numeros.html')

def cursosquimicaestructuraatomica(request):
    return render(request, 'cursos-quimica-estructuraatomica.html')

def header(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'header.html', {'user': user})

def footer(request):
    return render(request, 'footer.html')

def planesdemembresia(request):
    return render(request, 'planesdemembresia.html')

def registro(request):
    return render(request, 'registro.html')

def zoomdetallesmatalgebrayfunciones(request):
    return render(request, 'zoom-detalles-mat-algebrayfunciones.html')

def zoomdetallesmatgeometria(request):
    return render(request, 'zoom-detalles-mat-geometria.html')

def zoomdetallesprobabilidadyestadistica(request):
    return render(request, 'zoom-detalles-mat-geometria.html')

def zoomdetallesquimestructuraatomica(request):
    return render(request, 'zoom-detalles-quim-estructuraatomica.html')

def zoomdetallesquimquimicaorganica(request):
    return render(request, 'zoom-detalles-quim-quimicasyestequiometria.html')

def zoomdetallesquimquimicasyestequiometria(request):
    return render(request, 'zoom-detalles-quim-quimicasyestequiometria.html')