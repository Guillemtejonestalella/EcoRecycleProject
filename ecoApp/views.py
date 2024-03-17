from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ecoApp/index.html')

def aboutus(request):
    return render(request, 'ecoApp/aboutus.html')

def login(request):
    return render(request, 'ecoApp/login.html')

def register(request):
    return render(request, 'ecoApp/register.html')