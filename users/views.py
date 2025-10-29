from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import SignupForm

# Import cart models
from cart.models import Cart, CartItem
from store.models import Product



"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""


# Create your views here.

class UserLogin(LoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user

        # Merge session cart into user's real cart
        session_cart = self.request.session.get('cart', {})
        if session_cart:
            cart, _ = Cart.objects.get_or_create(user=user)
            for product_id, qty in session_cart.items():
                product = Product.objects.get(id=int(product_id))
                item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': qty})
                if not created:
                    item.quantity += qty
                    item.save()
            # Clear session cart
            del self.request.session['cart']

        # Redirect to cart after login
        return redirect('cart:view_cart')


class UserSignup(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = '/users/login/'  # redirect to login after signup

    def form_valid(self, form):
        # Save the user with hashed password
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        return super().form_valid(form)


# -------------------
# Function-based views
# -------------------

def logout_view(request):
    logout(request)
    request.session.flush()  # Clears session data
    return redirect('home')
