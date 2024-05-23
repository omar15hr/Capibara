from django.shortcuts import render, get_object_or_404, redirect
from crud.models import *
from cart.cart import Cart

def home(request):
  products = Product.objects.all()
  cart = Cart(request)
  cantidad_productos = len(cart)
  return render(request, 'home.html', {'products': products, 'cart': cart, 'cantidad_productos': cantidad_productos})

def category(request):
  products = Product.objects.all()
  cart = Cart(request)
  cantidad_productos = len(cart)
  return render(request, 'category.html', {'products': products, 'cart': cart, 'cantidad_productos': cantidad_productos})

def detalleProducto(request, productoId):
  product = get_object_or_404(Product, pk=productoId)
  tipoProduct = product.tipo.name
  return render(request, 'detalleProducto.html', {'product': product, 'tipoProduct': tipoProduct})
