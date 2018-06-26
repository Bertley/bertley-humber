"""bertley URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from shop import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), 
    path('admin/', admin.site.urls),
    path('shop/', views.collection, name='collection'), 
    path('shop/', include('shop.urls')),
    path('logout/',views.user_logout, name='logout'), 
    path('admin/dashboard/', views.dashboard, name="dashboard"), 
    path('admin/addproduct/', views.addproduct, name="addproduct"),
    path('admin/myproducts/', views.myproducts, name="myproducts"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
