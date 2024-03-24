from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'ecoApp/index.html')

def aboutus(request):
    return render(request, 'ecoApp/aboutus.html')

def login(request):
    return render(request, 'registration/login.html')

def profile(request):
    return render(request, 'ecoAPp/profile.html')

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
def products(request):
    return render(request, 'ecoApp/products.html')




