from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from store.models.orders import Order
from django.db.models import Q, Sum



# Create your views here.
def home(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();
    
    item = Order.objects.all().values('product_id').annotate(quantity_sum=Sum('quantity')).order_by('-quantity_sum')[:3]
    hot_item=[]
    for i in item:
        hot_item.append(Products.objects.get(id=i['product_id']))   


    data = {}
    data['products'] = products
    data['categories'] = categories
    data['hot_item'] = hot_item
    return render(request, 'index.html',data)


