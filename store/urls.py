from django.urls import path
from . import views


urlpatterns = [
    path("products/", views.Productlist.as_view(), name="product_list"),
    path("details/<int:pk>/", views.Productdetail.as_view(), name="product_detail"),
    path("products/woodworking/", views.custom_woodworking, name="woodworking"),
    path("products/3d-printing/", views.custom_printing, name="printing"),
    path("details/<int:pk>/", views.Productdetail.as_view(), name="product_detail"),
    
]