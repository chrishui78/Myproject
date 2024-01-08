from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.orders import Order
from .models.customer import Customer
from .models.contact import Contact
from .models.subscribe import Subscribe
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Subscribe)