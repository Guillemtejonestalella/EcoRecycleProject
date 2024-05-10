import json
from django.http import JsonResponse
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

# Create your views here.

def index(request):
    return render(request, 'ecoApp/index.html')

def aboutus(request):
    return render(request, 'ecoApp/aboutus.html')

def login(request):
    return render(request, 'registration/login.html')


@login_required
def requests(request):
    session_items = request.session.get('session_items', [])

    if request.method == 'POST':
        if 'delete_item_index' in request.POST: #en cas que la solicitud sigui post i tingui l'index delete del item  (solicitud per borrar item)           
             item_index = int(request.POST['delete_item_index'])
             if 0 <= item_index < len(session_items):
                 del session_items[item_index]
                 request.session['session_items'] = session_items
                 request.session.modified = True
             return redirect('requests')   
        else:  # en cas que la solicitud post no tingui l'index delete del item (solicitud per afegir nou item)           
            item_data_json = request.POST.get('item_data')
            item_data = json.loads(item_data_json)
            
            unique_session_items = {tuple(item.items()) for item in session_items}
            new_item_tuple = tuple(item_data.items())

            if new_item_tuple not in unique_session_items:
                session_items.append(item_data)
                request.session['session_items'] = session_items

        return redirect('requests')    
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




