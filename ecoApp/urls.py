from django.urls import path
from . import views

urlpatterns = [   
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('products', views.products, name='products'),
    path('profile', views.profile, name='profile'),


]