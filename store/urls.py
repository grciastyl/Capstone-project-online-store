from django.urls import path
from . import views


urlpatterns = [
    path("products/", views.Productlist.as_view(), name="product_list"),
    path("details/<int:pk>/", views.Productdetail.as_view(), name="product_detail")

    
]