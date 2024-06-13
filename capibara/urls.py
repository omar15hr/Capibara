"""
URL configuration for capibara project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


from core import views


urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    # PAGINA PROYECTO
    path('accounts/profile/', views.home, name='home'),
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('reparationForm/', views.reparationForm, name='reparationForm'),
    path('detalleProducto/<int:productoId>', views.detalleProducto, name='detalleProducto'),
    # CARRITO
    path('cart/', include('cart.urls')),
    # AUTENTICACION
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # # RECUPERACION DE CONTRASEÑA
    path('accounts/', include('allauth.urls')),
    # ENVIO
    path('envio',views.envio, name='envio'),
    #admin
    path('editadministrador',views.editadministrador, name='editadministrador'),
    path('administrador',views.administrador, name='administrador'),
    path('editproducto',views.editproducto, name='editproducto'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
