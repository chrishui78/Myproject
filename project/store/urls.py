from django.contrib import admin
from django.urls import path
from .views.home import home
from .views.about import aboutus
from .views.cart import *
from .views.store import Store,store,product_detail
from .views.contact import Contact
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.signup import Signup
from .views.login import Login , logout
from .middlewares.auth import  auth_middleware
from .views.payment import *
from .views.subscription import Subscription


urlpatterns = [
    path('', home, name='homepage'),
    path('about', aboutus, name='about'),
    path('storepage', Store.as_view() , name='storepage'),
    path('store', store, name='store'),
    path('store/<int:pk>',product_detail,name='product_detail'),
    path('contact', Contact.as_view(), name='about'),
    path('cart', Cart.as_view() , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('orders', auth_middleware(OrderView.as_view()), name='order'),
    path('carts', auth_middleware(Cart.as_view()) , name='carts'),
    path('process', Process.as_view(), name='process'),
    path('done', payment_done , name='done'),
    path('canceled', payment_canceled , name='canceled'),
    path('subscribe',Subscription.as_view(),name="subscribe")
]

