from django.shortcuts import render

from product.models import Product

def indexpage(request):
    newest_products = Product.objects.all()[0:8]

    return render(request, 'core/indexpage.html', {'newest_products': newest_products})

def clogin(request):

    return render(request, 'core/clogin.html' )
