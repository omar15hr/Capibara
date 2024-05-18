from django.shortcuts import render, get_object_or_404
from crud.models import *

def home(request):
  products = Product.objects.all()
  return render(request, 'home.html', {'products': products})

def category(request):
  products = Product.objects.all()
  return render(request, 'category.html', {'products': products})

def detalleProducto(request, productoId):
  products = Product.objects.all()
  context = {'products': products}
  return render(request, 'detalleProducto.html', context)

def carrito(request):
  
  context = {}
  return render(request, 'cart.html', context)

def checkout(request):
  context = {}
  return render(request, 'cart.html', context)