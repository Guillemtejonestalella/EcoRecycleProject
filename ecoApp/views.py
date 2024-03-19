from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'ecoApp/index.html')

def aboutus(request):
    return render(request, 'ecoApp/aboutus.html')

def login(request):
    return render(request, 'ecoApp/login.html')

def register(request):
    return render(request, 'ecoApp/register.html')

@login_required
def products(request):
    return render(request, 'ecoApp/products.html')