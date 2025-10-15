from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def signup_view(request):
    return render(request, 'users/signup.html')

def contact_view(request):
    return render(request, 'contact.html')