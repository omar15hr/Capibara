from django.shortcuts import render, get_object_or_404, redirect
from crud.models import *
from .models import *
from cart.cart import Cart
from django.contrib import messages
import bcrypt
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .email_utils import send_email_via_resend


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



def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Solicitud de restablecimiento de contraseña"
                    email_template_name = "password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'Tu Sitio Web',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    send_email_via_resend(user.email, subject, email)
                return redirect("password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(request, "password_reset.html", {"form": password_reset_form})