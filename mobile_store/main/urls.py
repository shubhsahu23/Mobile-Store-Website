from django.urls import path
from . import views
from .auth_views import logout_view
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('collections/', views.collections, name='collections'),
    path('register/', views.register_view, name='main_register'),
    path('login/', views.login_view, name='main_login'),
    path('logout/', logout_view, name='logout'),

]
