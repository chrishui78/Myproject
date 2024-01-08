from django.shortcuts import render , redirect
from django.views import  View
from django.urls import reverse
from store.models.product import Products
from paypal.standard.forms import PayPalPaymentsForm
from store.models.orders import Order
from store.models.customer import Customer

class Process(View):
    
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email= request.POST.get('email')
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        cart = request.session.get('cart')
        customer = request.session.get('customer')
        products = Products.get_products_by_id(list(cart.keys()))
  
        #If have mamber Login , Get Customer id
        if customer:
            for product in products:
                order = Order(customer=Customer(id=customer),
                            email=str(email),
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)),
                            first_name = first_name,
                            last_name = last_name)
            
                order.save()
        else:
            for product in products:
                order = Order(
                            email=str(email),
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)),
                            first_name = first_name,
                            last_name = last_name)
            
                order.save()
        
    
        cart = request.session.get('cart')
        ids = list(request.session.get('cart').keys())
        product = Products.get_products_by_id(ids)
        amount =0

        if ids:
            for id in ids:
                quantity = cart.get (id)

            for i in products.values('price'):
                price_list=list(i.values())
            if price_list != []:
                for price in price_list:
                    amount = price*quantity
                    
        paypal_dict = {
            'business' : 'chrishui78@gmail.com',
            'amount' : amount,
            'currency_code' : 'HKD',
            'item_name' : 'coffee',
            'notify_url' : request.build_absolute_uri(reverse('paypal-ipn')),
            'return' :  request.build_absolute_uri(reverse('done')),
            'cancel_return' : request.build_absolute_uri(reverse('canceled')),
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        context = {
            'products' : product,
            'form' :form,
        }
        request.session['cart'] = {}
        return render(request , 'process.html',context)
    
def payment_done(request):
    return render(request, 'done.html')



def payment_canceled(request):
    return render(request, 'canceled.html')