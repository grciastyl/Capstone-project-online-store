from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

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

class Productlist(ListView):
    model =  Product
    template_name = "store/list.html"

class Productdetail(DetailView):
    model = Product
    template_name = "store/details.html"

def custom_woodworking(request):
    return render(request, "store/custom_woodworking.html")

def custom_printing(request):
    return render(request, "store/custom_printing.html")