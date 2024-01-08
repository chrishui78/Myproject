from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from paypal.standard.forms import PayPalPaymentsForm
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email= request.POST.get('email')
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        cart = request.session.get('cart')
        customer = request.session.get('customer')
        products = Products.get_products_by_id(list(cart.keys()))


        for product in products:
            print(cart.get(str(product.id)))
            orders = Order(email=str(email),
                          customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)),
                          first_name = first_name,
                          last_name = last_name)
            orders.save()
        request.session['cart'] = {}

        return redirect('cart')
