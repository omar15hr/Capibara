from django.contrib import admin
from .models import Product, Clasification, ProductType, Shipping, ProductClass




admin.site.register(Product)
admin.site.register(Clasification)
admin.site.register(ProductType)
admin.site.register(ProductClass)
admin.site.register(Shipping)