from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [    # Define your URL patterns here
    path('', views.home_view, name='home'),  # Root URL
    path('home/', RedirectView.as_view(url='/', permanent=True)),
    path('about/', views.about_view, name='about'), # About URL
    path('contact/', views.contact_view, name='contact'), # Contact URL



]