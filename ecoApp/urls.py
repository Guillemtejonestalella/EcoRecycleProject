from django.urls import path
from . import views

urlpatterns = [   
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('products', views.products, name='products'),
    path('profile', views.profile, name='profile'),
    path('passwordChange', views.PasswordChangeView.as_view(template_name = "registration/passwordChange.html"), name='passwordChange'),
    path('password_succes', views.password_succes, name='passwordChangeSuccess')


]