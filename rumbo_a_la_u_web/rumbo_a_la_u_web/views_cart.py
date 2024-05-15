import random
from django.shortcuts import render
from .models import Curso, ShoppingSession, Carro,Usuarios
import traceback
from django.utils import timezone

def load(request):
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

    return redirect('login')

def load_cart(customer_id:int=None):
    carts = []
    products = []
    quantities = 0
    total = 0
    try: 
        print(f'customer_id: {customer_id}')
        try:
            customer = Usuarios.objects.get(pk=customer_id)
        except Usuarios.DoesNotExist:
            print('Usuario no encontrado: se procede con su creación.')
            customer = Usuarios()
            customer.user_id = customer_id
            customer.save()
        print(f'customer: {customer.user_id}')
        try:
            shopping_session = ShoppingSession.objects.get(usuario_id=customer.user_id)
        except ShoppingSession.DoesNotExist:
            print('Session no encontrada: se procede con su creación.')
            shopping_session = ShoppingSession()
            shopping_session.usuario = customer
            shopping_session.create_at = timezone.now()
            shopping_session.state = 1
            shopping_session.save()
        carts = Carro.objects.filter(shopping_session=shopping_session)
        for cart in carts:
            product = {
                'name': cart.products.name,
                'description': cart.products.description,
                'quantity': cart.quantity,
                'image': cart.products.image,
                'sale_price': cart.products.sale_price,
                'total': cart.quantity*cart.products.sale_price
            }
            products.append(product)
            quantities = quantities + int(cart.quantity)
            total = total + cart.quantity*cart.products.sale_price
    except Exception as ex:
        print(f'Error: {ex}')
        traceback.print_exc()
    print(f'carts: {carts}')
    print(f'products: {products}')
    print(f'quantities: {quantities}')
    print(f'total: {total}')
    return carts, quantities, total, products