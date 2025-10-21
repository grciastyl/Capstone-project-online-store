from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem

def get_cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return cart
    return None

def add_to_cart(request, product_id):    
    product = get_object_or_404(Product, id=product_id)
    cart = get_cart(request)
    if not cart:
        return redirect('users:login')
    
    item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': 1})
    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart:view_cart')

def view_cart(request):
    cart = get_cart(request)
    items = cart.cartitem_set.all() if cart else []
    total = sum(item.total_price() for item in items)
    return render(request, 'cart/view_cart.html', {'cart': cart, 'items': items, 'total': total})

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart:view_cart')

def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        item.quantity = max(quantity, 1)
        item.save()
    return redirect('cart:view_cart')
