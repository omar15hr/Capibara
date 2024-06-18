from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarProduct/', views.registrarProduct),
    path('edicionproduct/<ProductId>', views.edicionproduct),
    path('editarproduct/', views.editarproduct),
    path('eliminarproduct/<ProductId>', views.eliminarproduct)
]