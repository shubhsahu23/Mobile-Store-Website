from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home(request):
    latest_products = Product.objects.all()[:6]
    return render(request, 'main/home.html', {'products': latest_products})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        return redirect('contact')
    return render(request, 'main/contact.html')

def collections(request):
    products = Product.objects.all()
    return render(request, 'main/collections.html', {'products': products})

def register_view(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('main_login')
    return render(request, 'main/register.html')

def login_view(request):
    error = None
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid username or password. Please try again."
    return render(request, 'main/login.html', {'error': error})
