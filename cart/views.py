from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from crud.models import Product
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, ProductId=product_id)
    cart.add(product=product)
    return redirect('category')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, ProductId=product_id)
    cart.remove(product)
    return redirect('category')

def cart_detail(request):
    cart = Cart(request)
    cantidad_productos = len(cart)
    return render(request, 'detail.html', {'cart': cart, 'cantidad_productos': cantidad_productos})
