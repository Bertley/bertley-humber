from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime

# Create your models here.

class CustomerInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=25)   
    date_of_birth = models.DateField()
    date_account_created = models.DateTimeField(default=datetime.now, blank=True)
    type = models.CharField(max_length=50)

class Address(models.Model):
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    province = models.CharField(max_length=250)
    country = models.CharField(max_length=50)

class Ref_Product_type(models.Model):
    product_type_code = models.AutoField(primary_key=True)
    product_type_description = models.CharField(max_length=1000)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_type_code = models.OneToOneField(Ref_Product_type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=250)
    size = models.CharField(max_length=10)
    product_description  = models.CharField(max_length=600)
    product_image_1 = models.ImageField(upload_to='products',blank=True)
    product_image_2 = models.ImageField(upload_to='products',blank=True)
    product_image_3 = models.ImageField(upload_to='products',blank=True)
    product_image_4 = models.ImageField(upload_to='products',blank=True)

class Ref_Order_Status_Code(models.Model): 
    order_status_code = models.AutoField(primary_key=True)
    order_status_description  = models.CharField(max_length=50)

class Order(models.Model): 
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    order_status_code = models.ForeignKey(Ref_Order_Status_Code, on_delete=models.CASCADE)
    date_of_order = models.DateTimeField
    order_details = models.CharField(max_length=10000)
