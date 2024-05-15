from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from .models import Curso, Carro, ShoppingSession, Usuarios
from .views_cart import load_cart
from django.contrib.auth.hashers import check_password
from datetime import datetime
from django.contrib.auth import login
from django.shortcuts import render

class SellCourseView(View):
    def load_shopping_session(customer_id:int=None):
        print('load_shopping_session')
        try:
            print(f'customer_id: {customer_id}')
            customer = Usuarios.objects.get(pk=customer_id)
            shopping_session = ShoppingSession.objects.get(customers=customer)
            return shopping_session
        except ShoppingSession.DoesNotExist as ex:
            print('Session no encontrada: se procede con su creación.')
            shopping_session = ShoppingSession()
            shopping_session.usuario = customer
            shopping_session.create_at = datetime.now()
            shopping_session.state = 1
            shopping_session.save()
            return shopping_session
        
    def get(self, request):
        print('page building')
        products = []
        quantities = 0
        try:
            products = Curso.objects.all()
            user_id = request.session['user_id']
            carts, quantities, total, products_cart = load_cart(customer_id=user_id)
            #request.session['user_id'] = 1
            try:
                print('Agregar productos al carro de compras.')
                product_id = request.GET.get('course_id')
                print(f'product_id: {product_id}')
                product = Curso.objects.get(pk=product_id)
                print('find product')
                print('hola, voy acá')
                is_not_exist = True
                for cart in carts:
                    
                    if cart.products.name == product.name:
                        cart.cantidad = cart.cantidad + 1
                        cart.save(force_update=True)
                        is_not_exist = False
                if is_not_exist:
                    cart = Carro()
                    cart.shopping_session = self.load_shopping_session(customer_id=user_id)
                    cart.precio = product.precio
                    cart.cantidad = 1
                    cart.products = product
                    cart.save()
                carts, quantities, total, products_cart = load_cart(customer_id=1)
            except Exception as ex:
                print('No agregar productos al carro de compras.')
        except Exception as ex:
            print('Error: al cargar los datos')
        return render(request, 'cursos.html', {'products': products, 'quantities': quantities})
    
    