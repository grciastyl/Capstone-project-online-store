from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem, Order, OrderItem
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required


def get_cart(request):
    """Return the user's cart or a guest cart from session"""
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return cart
    else:
        if 'cart' not in request.session:
            request.session['cart'] = {}  # product_id -> quantity
        return request.session['cart']


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        # Logged-in user
        cart = get_cart(request)
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': 1}
        )
        if not created:
            item.quantity += 1
            item.save()
        return redirect('cart:view_cart')

    else:
        # Guest user: store cart in session
        session_cart = get_cart(request)
        str_id = str(product_id)
        session_cart[str_id] = session_cart.get(str_id, 0) + 1
        request.session['cart'] = session_cart
        return redirect('/users/login/')


def view_cart(request):
    """Display user's cart"""
    cart = get_cart(request) if request.user.is_authenticated else None
    items = cart.items.all() if cart else []
    total = sum(item.total_price() for item in items)
    return render(request, 'cart/view_cart.html', {'cart': cart, 'items': items, 'total': total})


def remove_from_cart(request, item_id):
    """Remove an item from the cart"""
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart:view_cart')


def update_quantity(request, item_id):
    """Change quantity of an item"""
    item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        item.quantity = max(quantity, 1)
        item.save()
    return redirect('cart:view_cart')


@login_required
def checkout(request):
    """Handle checkout process"""
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return redirect('cart:view_cart')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total = cart.total_price()
            order.save()

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product_name=item.product.name,
                    quantity=item.quantity,
                    price=item.product.price,
                )

            # Clear cart after checkout
            cart.items.all().delete()

            return redirect('cart:order_success', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'cart/checkout.html', {'form': form, 'cart': cart})


@login_required
def order_success(request, order_id):
    """Show order confirmation"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'cart/order_success.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'cart/my_orders.html', {'orders': orders})
