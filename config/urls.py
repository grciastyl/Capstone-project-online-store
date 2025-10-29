"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include URLs from the users app
    
    path('', include('pages.urls')),  # Include URLs from the pages app

    path('store/', include('store.urls')),  # Include URLs from the store app
    path('cart/', include('cart.urls')),  # Include URLs from the cart app
    path('blog/', include('blog.urls')),  # Include URLs from the blog app
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)