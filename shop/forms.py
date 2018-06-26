from django import forms 
from django.contrib.auth.models import User 
from shop.models import CustomerInfo, Product
from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect):
       def render(self):
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

# UserForm 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'string optional', 
            'maxlenght':'255', 
            'id':'user-email', 
            'placeholder':'Email', 
            'type':'email', 
            'name':'email', 
        }
    ))

    class Meta():
        model = User 
        fields = ('username', 'email', 'password')

# Customer Info Form  

class CustomerInfoForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'string optional', 
            'maxlength': '255', 
            'placeholder':'First Name', 
            'type':'text', 
            'size':'50', 
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'string optional', 
            'maxlength': '255', 
            'placeholder':'Last Name', 
            'type':'text', 
            'size':'50', 
        }
    ))
    date_of_birth = forms.DateField(input_formats=['%m/%d/%Y',] ,widget=forms.TextInput(
        attrs={
            'class':'form-control', 
            'id':'date_of_birth', 
            'name':'date_of_birth', 
            'placeholder':'MM/DD/YYYY', 
            'type':'text',
        }
    ))
    
    GENDERS = [('Male', 'Male'), ('Female', 'Female')]
    
    gender = forms.ChoiceField(
        choices=GENDERS, 
        initial=0, 
        widget=forms.RadioSelect(
            attrs={
                'class':'ml-1'
            }
        )   
    )
    class Meta():
        model = CustomerInfo
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth']

# Add Product Form 

class AddProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = ('product_type_code','name', 'price', 'color', 'size', 'product_description', 'product_image_1', 'product_image_2', 'product_image_3', 'product_image_4')
