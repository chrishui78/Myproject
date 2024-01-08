from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):
    def get(self,request):
        if request.session.get('customer'):
            customer = request.session.get('customer')
            order = Order.get_orders_by_customer(customer)
            context = {
                    'order' : order
            }

            return render(request , 'orders.html',context)
        else:
            return render(request,'askemail.html')
        
    def post(self,request):
        email = request.POST.get('email')
        order = Order.get_orders_by_email(email)
        context = {
                'order' : order
        }

        return render(request , 'orders.html',context)
