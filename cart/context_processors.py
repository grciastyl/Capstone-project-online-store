from .models import CartItem, Cart

def cart_total(request):
    total_items = 0
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        total_items = sum(item.quantity for item in cart.items.all())
    return {'cart_total_items': total_items}
