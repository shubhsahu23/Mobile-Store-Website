from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from main.models import Product
from .models import Order, Cart, CartItem

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('user_login')
    return render(request, 'user/register.html')

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
            next_url = request.GET.get('next', 'user_products')
            return redirect(next_url)
        else:
            error = "Invalid username or password. Please try again."
    return render(request, 'user/login.html', {'error': error})

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'user/product_list.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = cart.get_total()
    return render(request, 'user/cart.html', {'cart': cart, 'items': items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('view_cart')

@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        item = CartItem.objects.get(id=item_id)
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    
    if request.method == 'POST':
        for item in items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                total_price=item.get_subtotal()
            )
        # Clear cart
        items.delete()
        return redirect('my_orders')
    
    total = cart.get_total()
    return render(request, 'user/checkout.html', {'items': items, 'total': total})

@login_required
def place_order(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        qty = int(request.POST['quantity'])
        total = qty * product.price
        Order.objects.create(
            user=request.user,
            product=product,
            quantity=qty,
            total_price=total
        )
        return redirect('my_orders')
    return render(request, 'user/place_order.html', {'product': product})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user/my_orders.html', {'orders': orders})
