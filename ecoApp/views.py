from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserChangePasswordForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from ecoApp.models import Category, Item


# Create your views here.

def index(request):
    return render(request, 'ecoApp/index.html')

def aboutus(request):
    return render(request, 'ecoApp/aboutus.html')

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()   
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid(): #validació de l'usuari
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            # aqui podria logear directament al user utilitzant: login(request, user)
            return redirect('login')  #el retorno al formulari d'inici de sesio per tal que fagi login
    return render(request, 'registration/register.html', data)

@login_required
def profile(request):   
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes have been saved!')            
    else:
        form = CustomUserChangeForm(instance=request.user)    
    return render(request, 'ecoApp/profile.html', {'form': form})


def products(request):
    categories = Category.objects.all()   
    items = Item.objects.all()
    return render(request, 'ecoApp/products.html', {"categories": categories, "items":items})


class PasswordChangeView(PasswordChangeView):
    form_class = CustomUserChangePasswordForm
    success_url = reverse_lazy('passwordChangeSuccess')
   

def password_succes(request):
    return render(request, "registration/passwordChangeSuccess.html ")

class delete_user(SuccessMessageMixin, generic.DeleteView):
    model = User
    template_name = 'registration/deleteUserConfirm.html'
    # success_message = "User has been deleted!"
    success_url = reverse_lazy('index')




