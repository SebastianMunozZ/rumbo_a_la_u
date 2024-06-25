import random
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Curso, ShoppingSession, Carro,Usuarios
import traceback
from django.utils import timezone

def load(request, course_id):
    print('page building')
    carts = []
    products =[]
    buy_order = str(random.randrange(1000000, 99999999))
    quantities = 0
    total = 0
    session_id = '' 
    try: 
        customer_id = request.session['user_id']
        print(f'customer_id: {customer_id}')
        session_id = customer_id
        carts, quantities, total, products = load_cart(customer_id=customer_id)
    except Exception as ex:
        print(f'Error: {ex}')
        traceback.print_exc()
    request.session['products'] = products
    request.session['quantities'] = quantities
    request.session['total'] = total
    request.session['buy_order'] = buy_order
    request.session['session_id'] = session_id

    return redirect('carro')

def load_cart(customer_id:int=None):
    carts = []
    products = []
    quantities = 0
    total = 0 
    try: 
        try:
            customer = Usuarios.objects.get(pk=customer_id)
        except Usuarios.DoesNotExist:
            print('Usuario no encontrado: se procede con su creación.')
            customer = Usuarios()
            customer.user_id = customer_id
            customer.save()
        try:
            shopping_session = ShoppingSession.objects.get(usuario_id=customer.user_id)
            print(f'Shopping session: {shopping_session.id}')
        except ShoppingSession.DoesNotExist:
            print('Session no encontrada: se procede con su creación.')
            shopping_session = ShoppingSession()
            shopping_session.usuario = customer 
            shopping_session.create_at = timezone.now()
            shopping_session.state = 1
            shopping_session.save()
        carts = Carro.objects.filter(shopping_session=shopping_session.id)
        for cart in carts:
            precio = cart.curso.precio
            if precio == None:
                precio = 0
            product = {
                'id': cart.curso.course_id,
                'name': cart.curso.nombre_del_curso,
                'description': cart.curso.descripcion, 
                'quantity': cart.cantidad,
                'image': cart.curso.miniatura,
                'sale_price': cart.curso.precio,
                'total': cart.cantidad*int(precio) 
            }
            products.append(product)
            quantities = quantities + int(cart.cantidad)
            total = total + precio
    except Exception as ex:
        print(f'Error: {ex}')
        traceback.print_exc()
    print(f'carts desde load_cart: {carts}')
    print(f'products desde load_cart: {products}')
    print(f'quantities desde load_cart: {quantities}') 
    print(f'total desde load_cart: {total}')
    return carts, quantities, total, products