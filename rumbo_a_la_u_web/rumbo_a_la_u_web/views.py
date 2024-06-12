import json
import base64
import hmac
import hashlib
import datetime
from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse


def index(request):
    # Código para la vista de la página de inicio
    return render(request, 'index.html')
=======
from .models import Usuarios, Curso, Inscripciones
import datetime as dt
from .views_cart import load_cart
import traceback, os, requests
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import traceback
from django.http import JsonResponse,HttpResponse

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
>>>>>>> e41c06ab1f1ef71bca5b68878c5560f43c820713


def error(request):
    # Código para la vista de la página de error 404
    return HttpResponse("Error 404 - Página no encontrada")


def sobrenosotros(request):
    # Código para la vista de la sección "Sobre Nosotros"
    return render(request, 'sobrenosotros.html')


<<<<<<< HEAD
def carro(request):
    # Código para la vista del carrito de compras
    return render(request, 'carro.html')


def profesores(request):
    # Código para la vista de la sección "Profesores"
    return render(request, 'profesores.html')
=======
def profesores(request):
    return render(request, 'profesores.html')


def pricing(request):
    return render(request, 'pricing.html')


def bloglist(request):
    return render(request, 'blog-list.html')


def blogdetails(request):
    return render(request, 'blog-reuniones.html')


def zoommeeting(request):
    return render(request, 'zoom-meeting.html')


def zoomdetails(request):
    return render(request, 'zoom-reuniones.html')


def event(request):
    return render(request, 'event.html')

@login_required_manual
def carro(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id) if user_id else None
    try: 
        carts, quantities, total, products = load_cart(customer_id=user_id)
    except Exception as ex:
        print(f'Error: {ex}')
        traceback.print_exc()
    buy_order = request.session.get('buy_order')
    context = {
        'user': user,
        'products': products,
        'quantities': quantities,
        'total': total,
        'buy_order': buy_order,
        'session_id': user_id
    }
    print(f'products desde views:{products}')
    print(f'user desde views:{user}')
    print(f'quantities desde views:{quantities}')
    print(f'total desde views:{total}')
    print(f'buy_order desde views:{buy_order}')
    return render(request, 'carro.html', context)


def login(request): 
    return render(request, 'login.html')
>>>>>>> e41c06ab1f1ef71bca5b68878c5560f43c820713


def alumnocalendario(request):
    # Código para la vista del calendario del alumno
    return render(request, 'alumno-calendario.html')

<<<<<<< HEAD

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
=======
def cursocrear(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'curso-crear.html', {'user': user})
>>>>>>> e41c06ab1f1ef71bca5b68878c5560f43c820713


def cursos_biologia_organismoyambiente(request):
    # Código para la vista de cursos de biología sobre organismos y ambiente
    return render(request, 'cursos-biologia-organismoyambiente.html')


<<<<<<< HEAD
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
=======
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
    inscripciones = Inscripciones.objects.filter(student_id=user_id)
    context = {
        'user': user,
        'inscripciones': inscripciones
    }
    return render(request, 'alumno-cursosmatriculados.html', context)

@login_required_manual
def alumnodashboard(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'alumno-dashboard.html', {'user':user})

@login_required_manual
def alumnohistorialpedidos(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    inscripciones = Inscripciones.objects.filter(student_id=user_id)
    context = {
        'user': user,
        'inscripciones': inscripciones
    }
    return render(request, 'alumno-historialdepedidos.html', context)

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
    return render(request, 'blogdet01.html')

def blogblogdet02(request):
    return render(request, 'blogdet02.html')

def blogblogdet03(request):
    return render(request, 'blogdet03.html')

def blogblogdet04(request):
    return render(request, 'blogdet04.html')

def blogblogdet05(request):
    return render(request, 'blogdet05.html')

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
    return render(request, 'zoom-detalles-mat-probabilidadyestadistica.html')

def zoomprueba(request):
    user_id = request.session.get('user_id')
    user = Usuarios.objects.get(user_id=user_id)
    return render(request, 'zoom-prueba.html', {'user': user})

def zoomdetallesquimestructuraatomica(request):
    return render(request, 'zoom-detalles-quim-estructuraatomica.html')

def zoomdetallesquimquimicaorganica(request):
    return render(request, 'zoom-detalles-quim-quimicasyestequiometria.html')

def zoomdetallesquimquimicasyestequiometria(request):
    return render(request, 'zoom-detalles-quim-quimicasyestequiometria.html')

def transbankpay_load(request):
    print('METHOD', request.method)

    if  request.method == 'POST':
        course_id = request.POST.get('course_id')
        buy_order = request.POST.get('buy_order')
        session_id = request.POST.get('session_id') # SESSION ID USER
        user = Usuarios.objects.get(user_id=int(session_id))
        course = Curso.objects.get(course_id=int(course_id))
        amount = request.POST.get('amount')
        return_url = 'http://localhost:8000/commit-pay'

        body = {
            "buy_order": buy_order,
            "session_id": session_id,
            "amount": amount,
            "return_url": return_url
            }                        
        response = transbankpay_transbank_create(body)
        print(f'response.status_code: {response.status_code}')        
        if response.status_code == 200 :
            json_response = response.json()
            print('response: ', json_response)
            token = json_response['token']
            print(f'token: ', token)
            url = json_response['url']
            print(f'url: ', url)
            inscription = Inscripciones(student=user, course=course)
            # Guardar la inscripción en la base de datos
            inscription.save()
            return render(request,'send-pay.html', {'token' : token, 'url': url, 'amount': amount})
        else: 
            HttpResponse("Error transacción transbank")
    return HttpResponse("Error transacción transbank")


# MÉTODO QUE CREA LA CABECERA SOLICITADA POR TRANSBANK EN UN REQUEST (SOLICITUD)
def transbankpay_header_request_transbank():
    headers = { # DEFINICIÓN TIPO DE AUTORIZACIÓN Y AUTENTICACIÓN
                "Authorization": "Token",
                # LLAVE QUE DEBE SER MODIFICADA PORQUE ES SOLO DEL AMBIENTE DE INTEGRACIÓN DE TRANSBANK (PRUEBAS)
                "Tbk-Api-Key-Id": "597055555532",
                # LLAVE QUE DEBE SER MODIFICADA PORQUE DEL AMBIENTE DE INTEGRACIÓN DE TRANSBANK (PRUEBAS)
                "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
                # DEFINICIÓN DEL TIPO DE INFORMACIÓN ENVIADA
                "Content-Type": "application/json",
                # DEFINICIÓN DE RECURSOS COMPARTIDOS ENTRE DISTINTOS SERVIDORES PARA CUALQUIER MÁQUINA
                "Access-Control-Allow-Origin": "*",
                'Referrer-Policy': 'origin-when-cross-origin',
                } 
    return headers

def transbankpay_transbank_create(data):
    # CABECERA SOLICITADA POR TRANSBANK
    headers = transbankpay_header_request_transbank()
    # LECTURA DE PAYLOAD (BODY) CON INFORMACIÓN DE TIPO JSON
    print(f'headers: {headers}')
    print(f'data: {data}')
    # DEFINICIÓN DE URL DE TRANSBANK PARA CREAR UNA TRANSACCIÓN
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
    print(f'url: {url}')
    # INVOCACIÓN POR POST A API REST QUE CREA UNA TRANSACCIÓN EN TRANSBANK
    response = requests.post(url=url, json=data, headers=headers, verify=False)
    # RETORNO DE LA RESPUESTA DE TRANSBANK
    return response

# DEFINICIÓN DE RUTA API REST CON UN PARAMETRO DE ENTRADA (tokenws) EN EL PATH, PERMITIENDO SOLO SER LLAMADO POR GET
def transbankpay_transbank_commit(tokenws):
    print('tokenws: ', tokenws)
    # DEFINICIÓN DE URL DE TRANSBANK PARA CONFIRMAR UNA TRANSACCIÓN
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{0}".format(tokenws)
    # CABECERA SOLICITADA POR TRANSBANK
    headers = transbankpay_header_request_transbank()
    # INVOCACIÓN POR GET A API REST QUE CONFIRMA UNA TRANSACCIÓN EN TRANSBANK    
    response = requests.put(url, headers=headers, verify=False)
    print('response: ', response.json())
    # RETORNO DE LA RESPUESTA DE TRANSBANK
    return response.json()

# DEFINICIÓN DE RUTA API REST CON UN PARAMETRO DE ENTRADA (tokenws, amount) EN EL PATH, PERMITIENDO SOLO SER LLAMADO POR POST
def transbankpay_transbank_reverse_or_cancel(tokenws:str="", amount:int=None):
    print('tokenws: ', tokenws)
    # LECTURA DE PAYLOAD (BODY) CON INFORMACIÓN DE TIPO JSON
    data = {
            "amount": amount
            }
    print('data: ', data)
    # DEFINICIÓN DE URL DE TRANSBANK PARA CONFIRMAR UNA TRANSACCIÓN
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{0}/refunds".format(tokenws)
    # CABECERA SOLICITADA POR TRANSBANK
    headers = transbankpay_header_request_transbank()
    # INVOCACIÓN POR GET A API REST QUE CONFIRMA UNA TRANSACCIÓN EN TRANSBANK    
    response = requests.post(url, json = data, headers=headers, verify=False)
    print('response: ', response.json())
    # RETORNO DE LA RESPUESTA DE TRANSBANK
    return response.json() 


@csrf_exempt 
def transbankpay_commitpay(request):
    print('commitpay')
    if request.method == 'GET':
        tokenws = request.GET.get('token_ws')    
    elif request. method == 'POST':
        tokenws = request.POST.get('token_ws')
    #TRANSACCIÓN REALIZADA
    if tokenws is not None:

        #APROBAR TRANSACCIÓN
        response = transbankpay_transbank_commit(tokenws)
        print("response: {}".format(response)) 

        status = response['status']
        print("status: {0}".format(status))
        response_code = response['response_code']
        print("response_code: {0}".format(response_code)) 
        #TRANSACCIÓN APROBADA
        if status == 'AUTHORIZED' and response_code == 0:

            state = ''
            if status == 'AUTHORIZED':
                state = 'ACEPTADO'
            pay_type = ''
            if response['payment_type_code'] == 'VD':
                pay_type = 'Tarjeta de Débito'
            if response['payment_type_code'] == 'VN':
                pay_type = 'Tarjeta de Crédito'
            amount = int(response['amount'])
            amount = f'{amount:,.0f}'.replace(',', '.')
            transaction_date = dt.datetime.strptime(response['transaction_date'], '%Y-%m-%dT%H:%M:%S.%fZ')
            transaction_date = '{:%d-%m-%Y %H:%M:%S}'.format(transaction_date)
            print(response)

            transaction_detail = {  'card_number': response['card_detail']['card_number'],
                                    'transaction_date': transaction_date,
                                    'state': state,
                                    'pay_type': pay_type,
                                    'amount': amount,
                                    'authorization_code': response['authorization_code'],
                                    'buy_order': response['buy_order'], }
            
            carts, quantities, total, products_cart = load_cart(customer_id=int(response['session_id']))
            
            for cart in carts:
                cart.delete()
            carts, quantities, total, products_cart = load_cart(customer_id=int(response['session_id']))
            
            user_id = request.session.get('user_id')
            user = Usuarios.objects.get(user_id=user_id)
            return render(request, 'commit-pay.html', {'transaction_detail': transaction_detail, 'quantities': quantities, 'user': user})
        else:
            #TRANSACCIÓN RECHAZADA
            state = ''
            if status == 'FAILED':
                state = 'RECHAZADO'            
            if response['payment_type_code'] == 'VD':
                pay_type = 'Tarjeta de Débito'
            if response['payment_type_code'] == 'VC':
                pay_type = 'Tarjeta de Crédito'            
            amount = int(response['amount'])
            amount = f'{amount:,.0f}'.replace(',', '.')
            #response = transbank_reverse_or_cancel(tokenws=tokenws, amount=amount)
            print(f'response: {response}')
            transaction_date = dt.datetime.strptime(response['transaction_date'], '%Y-%m-%dT%H:%M:%S.%fZ')
            transaction_date = '{:%d-%m-%Y %H:%M:%S}'.format(transaction_date)
            transaction_detail = {  'card_number': response['card_detail']['card_number'],
                                    'transaction_date': transaction_date,
                                    'state': state,
                                    'pay_type': pay_type,
                                    'amount': amount,
                                    'authorization_code': response['authorization_code'],
                                    'buy_order': response['buy_order'], }
            carts, quantities, total, products_cart = load_cart(customer_id=int(response['session_id']))                              
            return render(request, 'commit-pay.html', {'transaction_detail': transaction_detail, 'quantities': quantities})
    else:
    #TRANSACCIÓN CANCELADA            
        return HttpResponse('ERROR EN LA TRANSACCIÓN, SE CANCELO EL PAGO.')
    
def generate_signature(sdk_key, sdk_secret, meeting_number, role):
    timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
    data = base64.b64encode(
        json.dumps({'meetingNumber': meeting_number, 'role': role}).encode('utf-8')
    ).decode('utf-8').strip()

    message = f'{sdk_key}{data}{timestamp}'
    message_bytes = message.encode('utf-8')
    secret_bytes = sdk_secret.encode('utf-8')
    signature = base64.b64encode(
        hmac.new(secret_bytes, message_bytes, hashlib.sha256).digest()
    ).decode('utf-8').strip()

    return {
        'signature': base64.b64encode(
            f'{sdk_key}.{data}.{timestamp}.{signature}'.encode('utf-8')
        ).decode('utf-8').strip()
    }

def generatesignature(request):
    sdk_key = "dUBoSFQRQmusjyruFMFI7g"
    sdk_secret = "eddeIAwQIAT75RRLqvu7HlAfh0abjR7n"
    meeting_number = request.GET.get('meeting_number')
    role = request.GET.get('role', 0)  # Default to participant (0)

    signature = generate_signature(sdk_key, sdk_secret, meeting_number, role)
    print(signature) 
    return JsonResponse(signature)
>>>>>>> e41c06ab1f1ef71bca5b68878c5560f43c820713
