from django.shortcuts import render , redirect
from django.views import  View
from django.urls import reverse
from store.models.product import Products
from store.templatetags import cart
from store.models.customer import Customer
from paypal.standard.forms import PayPalPaymentsForm

class Cart(View):
    def get(self , request):
        cart = request.session.get('cart')
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        amount=0

        if ids:
            for id in ids:
                quantity = cart.get (id)
            for i in products.values('price'):
                price_list=list(i.values())
                print(price_list)
            if price_list != []:
                for price in price_list:
                    amount = price*quantity
                    amount = amount+amount
        if amount:
            paypal_dict = {
                'business' : 'sb-ula2w28569902@business.example.com',
                'amount' : amount,
                'currency' : 'HKD',
                'item_name' : 'coffee',
                'notify_url' : request.build_absolute_uri(reverse('paypal-ipn')),
                'return' :  request.build_absolute_uri(reverse('done')),
                'cancel_return' : request.build_absolute_uri(reverse('canceled')),
            }
            form = PayPalPaymentsForm(initial=paypal_dict)
            context = {
                'products' : products,
                'form' :form
            }
            return render(request , 'cart.html' , context )
        else:
            return render(request , 'cart.html')
    

    

