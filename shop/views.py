from django.shortcuts import render
from shop.models import CustomerInfo,Product
from shop.forms import CustomerInfoForm,UserForm,AddProductForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def home(request): 
    return render(request, 'shop/index.html')

def collection(request): 
    products = Product.objects.all()
    args = {'products':products}
    return render(request, 'shop/collection.html', args)

def product(request):
    product = Product.objects.get(id=1)
    args = {'product':product}
    return render(request, 'shop/product.html', args)

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        customer_form = CustomerInfoForm(data=request.POST)

        if customer_form.is_valid() and user_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            customer = customer_form.save(commit=False)
            customer.user = user

            customer.save()
            registered = True

        else:
            print(customer_form.errors,user_form.errors)
    else:
        user_form = UserForm()
        customer_form = CustomerInfoForm()

    return render(request, 'shop/login.html', 
                            {
                                'user_form':user_form,
                                'customer_form':customer_form, 
                                'registered':registered
                            })

def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('collection'))

            else:
                return HttpResponse("Account not active")
        else: 
            print("Someone tried to login anf failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'shop/login.html',{})

@staff_member_required
def dashboard(request):
    return render(request, 'shop/dashboard.html')

@staff_member_required
def addproduct(request):
    
    product_added = False

    if request.method == 'POST':
        
        addproduct_form = AddProductForm(data=request.POST)
        
        if addproduct_form.is_valid():
            product = addproduct_form.save(commit=False)

            if 'product_image_1' in request.FILES: 
                product.product_image_1 = request.FILES['product_image_1']
            if 'product_image_2' in request.FILES: 
                product.product_image_1 = request.FILES['product_image_2']
            if 'product_image_3' in request.FILES: 
                product.product_image_1 = request.FILES['product_image_3']
            if 'product_image_4' in request.FILES: 
                product.product_image_1 = request.FILES['product_image_4']

            product.save()
            product_added = True
            # return redirect('dashboard')
        else: 
            print(addproduct_form.errors)
    else:
        addproduct_form = AddProductForm()


    return render(request, 'shop/addproduct.html',
                    {
                        'addproduct_form':addproduct_form,
                        'product_added':product_added
                    })

def myproducts(request):
    products = Product.objects.all()
    args = {'products':products}
    return render(request, 'shop/myproducts.html', args)