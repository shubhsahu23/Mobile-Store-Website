from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='user_register'),
    path('login/', views.login_view, name='user_login'),
    path('products/', views.product_list, name='user_products'),
    path('order/<int:product_id>/', views.place_order, name='place_order'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
