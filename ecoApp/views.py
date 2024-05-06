import json
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
from items.models import Item
from categories.models import Category
# from profiles.models import Profile


# Create your views here.

def index(request):
    return render(request, 'ecoApp/index.html')

def aboutus(request):
    return render(request, 'ecoApp/aboutus.html')

def login(request):
    return render(request, 'registration/login.html')


# done
@login_required
def requests(request):
    if request.method == 'POST':        
        item_data_json = request.POST.get('item_data') # Obtinc les dades del JSON   
        item_data = json.loads(item_data_json) #el converteixo a un diccionari        
        session_items = request.session.get('session_items', []) # Obtinc la llista actual de solicituds de la sesio de l usuari        
       
        unique_session_items = {tuple(item.items()) for item in session_items}  # converteixo la llista de solicituds en un conjunt de tuples hashables   
        new_item_tuple = tuple(item_data.items())  # converteixo la nova solicitud en una tupla hashable
        
       
        if new_item_tuple not in unique_session_items:  # contorl de duplicats            
            session_items.append(item_data)        
        
        request.session['session_items'] = session_items # guardo la llista actualitzada       
        print("session_items:", session_items)
        
        return redirect('requests') 

    session_items = request.session.get('session_items', [])
   
    print("session_items:", session_items)    
    return render(request, 'ecoApp/requests.html', {'session_items': session_items})











def requestsHistory(request):
    return render(request, 'ecoApp/requestsHistory.html')

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


def products(request, category_id=None):
    if category_id:
         items = Item.objects.filter(Category=category_id)
    else:
         items = Item.objects.all()
    categories = Category.objects.all()
    brands = [category.CategoryBrands for category in categories]    
    return render(request, 'ecoApp/products.html', {"items": items, "categories": categories, "brands": brands})



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




