from django.db import models
from .product import Products
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    email=models.EmailField()


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_email(email):
        return Order.objects.filter(email=str(email)).order_by('-date')
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

