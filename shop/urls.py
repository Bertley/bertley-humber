from django.urls import path
from shop import views

# Template Urls 
app_name = 'shop'

urlpatterns = [
    path('product/', views.product, name='product'), 
    path('register/', views.register, name='register'), 
    path('signin/', views.signin, name='signin'),
]