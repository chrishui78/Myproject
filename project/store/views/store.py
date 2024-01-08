from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class Store(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        delete = request.POST.get('delete')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        if cart:
            quantity = cart.get(product)
            if delete:
                cart.pop(product)
        request.session['cart'] = cart
        return redirect(request.META.get('HTTP_REFERER'))


    def get(self , request):
        # print()
        return HttpResponseRedirect(f'{request.get_full_path()[1:]}')

def store(request):
    
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')

    search = request.POST.get('search')
    if search:
        products = Products.objects.filter(name__contains=search)

    elif categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    return render(request, 'store.html', data)

def product_detail(request,pk):
    products = None
    categories = Category.get_all_categories()
    products = Products.objects.filter(pk=pk)
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'store_detail.html', data)


