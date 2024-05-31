from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from crud.models import Product
from .cart import Cart
from django.urls import reverse

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
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    cantidad_productos = len(cart)
    return render(request, 'detail.html', {'cart': cart, 'cantidad_productos': cantidad_productos})

def get_item_quantity(self, product):
        """
        Retorna la cantidad del producto especificado en el carrito.
        """
        for item in self.cart:
            if item['product_id'] == product.ProductId:
                return item['quantity']
        return 0

def update_quantity(request, product_id):
    product = get_object_or_404(Product, ProductId=product_id)
    cart = Cart(request)
    action = request.POST.get('action')
    if action == 'increase':
        cart.add(product, quantity=1)
    elif action == 'decrease':
        # Verifica que la cantidad actual sea mayor que 1 antes de restar
        if cart.get_item_quantity(product) > 1:
            cart.add(product, quantity=-1)
    return redirect(reverse('cart_detail'))