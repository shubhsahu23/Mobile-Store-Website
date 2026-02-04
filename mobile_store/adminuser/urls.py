from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='admin_dashboard'),
    path('users/', views.view_users, name='admin_users'),
    path('add-product/', views.add_product, name='admin_add_product'),
    path('orders/', views.view_orders, name='admin_orders'),
    path('sales-report/', views.sales_report, name='sales_report'),
    path('logout/', views.admin_logout, name='admin_logout'),
]
