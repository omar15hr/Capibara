from django.shortcuts import render, get_object_or_404, redirect
from crud.models import *
from .models import *
from cart.cart import Cart
from django.contrib import messages
import bcrypt
from .forms import *

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
  cart = Cart(request)
  cantidad_productos = len(cart)
  tipoProduct = product.tipo.name
  return render(request, 'detalleProducto.html', {'product': product, 'tipoProduct': tipoProduct, 'cart': cart, 'cantidad_productos': cantidad_productos})

def register(request):
    if request.method == 'GET':
        cart = Cart(request)
        cantidad_productos = len(cart)
        return render(request, "register.html", {'cart': cart, 'cantidad_productos': cantidad_productos})
    elif request.method == 'POST':  # Solo necesitas verificar si la solicitud es POST una vez
        request.session['registro_nombre'] = ""
        request.session['registro_apellido'] = ""
        request.session['registro_email'] = ""

        first_name = request.POST.get('firstName', '')  # Utiliza request.POST.get para evitar MultiValueDictKeyError
        last_name = request.POST.get('lastName', '')  # Utiliza request.POST.get para evitar MultiValueDictKeyError
        email = request.POST.get('email', '')  # Utiliza request.POST.get para evitar MultiValueDictKeyError
        password_hash = bcrypt.hashpw(request.POST.get('password', '').encode(), bcrypt.gensalt()).decode()  # Utiliza request.POST.get para evitar MultiValueDictKeyError

        if User.objects.filter(email=email).exists():
            messages.error(request, "El usuario ya está registrado.")
            request.session['level_mensaje'] = 'alert-danger'
            return redirect('register')  # Redirige nuevamente a la página de registro

        obj = User.objects.create(firstName=first_name, lastName=last_name,email=email,password=password_hash)
        messages.success(request, "Usuario registrado con éxito!!!!")
        request.session['level_mensaje'] = 'alert-success'

    return render(request, 'register.html')

def login(request):
    if request.method == 'GET':
        cart = Cart(request)
        cantidad_productos = len(cart)
        return render(request,"login.html", {'cart': cart, 'cantidad_productos': cantidad_productos})
    else:
        if request.method == 'POST':
            
            user = User.objects.filter(email=request.POST['email_login']) #Buscamos el correo ingresado en la BD             
            
            if user : #Si el usuario existe

                usuario_registrado = user[0]
                
                if bcrypt.checkpw(request.POST['password_login'].encode(), usuario_registrado.password.encode()): 
                    usuario = {
                        'id':usuario_registrado.id,
                        'firstName':usuario_registrado.firstName,
                        'lastName':usuario_registrado.lastName,
                        'email':usuario_registrado.email,
                        'rol':usuario_registrado.rol,
                    }

                    request.session['usuario'] = usuario
                    messages.success(request,"Ingreso correcto!!!!")
                    return redirect('/')
                else:
                    messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                    return redirect('/')
            else:
                messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                return redirect('/')
            
def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    return redirect('/')
