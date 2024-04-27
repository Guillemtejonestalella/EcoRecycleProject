from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [   
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('products', views.products, name='products'),
    path('requests', views.requests, name='requests'),
    path('requestsHistory', views.requestsHistory, name='requestsHistory'),
    path('products/<int:category_id>/', views.products, name='products'),
    path('profile', views.profile, name='profile'),
    path('passwordChange', views.PasswordChangeView.as_view(template_name = "registration/passwordChange.html"), name='passwordChange'),
    path('password_succes', views.password_succes, name='passwordChangeSuccess'),
    path('delete_user/<int:pk>/', views.delete_user.as_view(), name='delete_user')
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)