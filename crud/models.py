from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField
from django.db.models.fields import AutoField
from django.db.models.fields import DecimalField
from django.db.models.fields import DateTimeField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey



# Modelo para clasificacion (pino, roble, melamina)
class Clasification(models.Model):
    clasificationId = AutoField(primary_key=True, verbose_name='Id Clasificación')
    name = CharField(max_length=100, verbose_name='Clasificación')
    created_at = DateTimeField(verbose_name='Fecha registro', auto_now_add=True)
    updated_at = DateTimeField(verbose_name='Fecha actualización', auto_now=True)


# Modelo para tipo de producto (cocina, dormitorio, comedor)
class ProductType(models.Model):
    productTypeId = AutoField(primary_key=True, verbose_name='Id Tipo Mueble')
    name = CharField(max_length=100, verbose_name='Tipo de Mueble')
    created_at = DateTimeField(verbose_name='Fecha registro', auto_now_add=True)
    updated_at = DateTimeField(verbose_name='Fecha actualización', auto_now=True)


# Modelo para clase de producto (estante vertical, velador, respaldo cama)
class ProductClass(models.Model):
    productClassId = AutoField(primary_key=True, verbose_name='Id Clase Mueble')
    name = CharField(max_length=100, verbose_name='Clase de Mueble')
    created_at = DateTimeField(verbose_name='Fecha registro', auto_now_add=True)
    updated_at = DateTimeField(verbose_name='Fecha actualización', auto_now=True)


# Modelo para producto 
class Product(models.Model):
    ProductId = AutoField(primary_key=True, verbose_name='Id Producto')
    nombre = CharField(max_length=100)
    clasificacion = ForeignKey(Clasification, on_delete=models.CASCADE, default=0)
    tipo = ForeignKey(ProductType, on_delete=models.CASCADE, default=0)
    clase = ForeignKey(ProductClass, on_delete=models.CASCADE, default=0, null=True)
    stock_disponible = IntegerField()
    image = ImageField(upload_to='capibara/images/')
    precio = DecimalField(max_digits=10, decimal_places=0, default=0)
    largo = DecimalField(max_digits=5, decimal_places=2, default=0)
    ancho = DecimalField(max_digits=5, decimal_places=2, default=0)
    alto = DecimalField(max_digits=5, decimal_places=2, default=0)
    materiales_planchas = IntegerField(default=0)
    materiales_tornillos = IntegerField(default=0)
    pegamento = IntegerField(default=0)
    manillas = IntegerField(default=0)
    bisagras = IntegerField(default=0)
    patas_goma = IntegerField(default=0)
    riel = IntegerField(default=0)
    created_at = DateTimeField(verbose_name='Fecha registro', auto_now_add=True)
    updated_at = DateTimeField(verbose_name='Fecha actualización', auto_now=True)


# Modelo para envíos
class region(models.Model):
    nombre = CharField(max_length=100)
    zona = CharField(max_length=1)

class Shipping(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE)
    zona_1 = DecimalField(max_digits=10, decimal_places=2)
    zona_2 = DecimalField(max_digits=10, decimal_places=2)
    zona_3 = DecimalField(max_digits=10, decimal_places=2)
    zona_4 = DecimalField(max_digits=10, decimal_places=2)
    zona_5 = DecimalField(max_digits=10, decimal_places=2)



class Orden(models.Model):
    nombreCliente = CharField(max_length=100)
    emailCliente = CharField(max_length=100)
    fechaOrden = DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False, null=True, blank=False)
    transactionId = CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
class OrdenItem(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE)
    orden = ForeignKey(Orden, on_delete=models.CASCADE)
    cantidad = IntegerField(default=0, null=True, blank=True)
    fechaAñadido = DateTimeField(auto_now_add=True)


class DireccionEntrega(models.Model):
    nombreCliente = CharField(max_length=100)
    emailCliente = CharField(max_length=100)
    orden = ForeignKey(Orden, on_delete=models.CASCADE)
    direccion  = CharField(max_length=100)
    ciudad = CharField(max_length=100)
    region = CharField(max_length=100)
    codigoPostal = CharField(max_length=100)
    fechaCompra = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.direccion)

