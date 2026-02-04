from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import Product
from user.models import Order
from django.db.models import Sum

def admin_login(request):
    error = None
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        elif user:
            error = "You are not authorized to access the admin panel."
        else:
            error = "Invalid username or password. Please try again."
    return render(request, 'adminuser/login.html', {'error': error})

@login_required
def dashboard(request):
    return render(request, 'adminuser/dashboard.html')

@login_required
def view_users(request):
    users = User.objects.filter(is_staff=False)
    return render(request, 'adminuser/users.html', {'users': users})

@login_required
def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            brand=request.POST['brand'],
            name=request.POST['name'],
            price=request.POST['price'],
            description=request.POST['description'],
            image=request.FILES['image']
        )
        return redirect('admin_dashboard')
    return render(request, 'adminuser/add_product.html')

@login_required
def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'adminuser/orders.html', {'orders': orders})

@login_required
def sales_report(request):
    total_sales = Order.objects.aggregate(total=Sum('total_price'))['total']
    orders = Order.objects.all()
    return render(
        request,
        'adminuser/sales_report.html',
        {'total_sales': total_sales, 'orders': orders}
    )

def admin_logout(request):
    logout(request)
    return redirect('admin_login')
