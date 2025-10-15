from django.urls import path
from . import views

urlpatterns = [    # Define your URL patterns here
    path('', views.home_view, name='home'),  # Root URL
    path('home/', views.home_view, name='home'), # Home URL
    path('about/', views.about_view, name='about'), # About URL
    path('contact/', views.contact_view, name='contact'), # Contact URL



]