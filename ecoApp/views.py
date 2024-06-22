from asyncio import log
import datetime
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
from order.models import Order
from orderline.models import Orderline
from django.utils import timezone


# views de la web (renderitzacio de les pagines i funcionalitats del backend)

def index(request):
    return render(request, 'ecoApp/index.html')

def aboutus(request):
    return render(request, 'ecoApp/aboutus.html')

def login(request):
    return render(request, 'registration/login.html')


# nomes deixa entrar a requests si l'usuari esta loggejat
@login_required
def requests(request):
    # Gestio de les sol·licituds en progres (si es vol enviar la request o bé es vol eliminar un item de la sol·licitud)
    session_items = request.session.get('session_items', [])

    if request.method == 'POST':
        if 'delete_item_index' in request.POST: #en cas que la solicitud sigui post i tingui l'index delete del item  (solicitud per borrar item)           
             item_index = int(request.POST['delete_item_index'])
             if 0 <= item_index < len(session_items):
                 del session_items[item_index]
                 request.session['session_items'] = session_items
                 request.session.modified = True
             return redirect('requests')   
        else:  # en cas que la solicitud post no tingui l'index delete del item (solicitud per afegir nou item (es guarda a la sessio d'usuari))           
            item_data_json = request.POST.get('item_data')
            item_data = json.loads(item_data_json)
            
            unique_session_items = {tuple(item.items()) for item in session_items}
            new_item_tuple = tuple(item_data.items())

            if new_item_tuple not in unique_session_items:
                session_items.append(item_data)
                request.session['session_items'] = session_items
        # redirecciona a la pagina reqeuests
        return redirect('requests')    
    return render(request, 'ecoApp/requests.html', {'session_items': session_items})


# nomes deixa crear una order si l'usuari esta loggejat
@login_required
def create_order(request):
    if request.method == 'POST':
        # obte tots els items de la sol·licitud de l'usuari
        user = request.user
        session_items = request.session.get('session_items', []) 

        # si no hi ha cap item afegit a la sessio d'usuari, retora a la template de requests
        if not session_items:
            return redirect('requests')    

        # en cas que hi hagin items a la order, es guarda la informacio de la request total
        total_points = int(request.POST.get('total_points', 0))  
        delivery_address = request.POST.get('delivery_address', '') 
        address_delivery = request.POST.get('address_delivery', '')   
        home_pickup = 'home_pickup' in request.POST  
        pick_up_point = 'pick_up_point' in request.POST
        
        # control de atributs en funcio de l'eleccio de l'usuari
        if pick_up_point == False:
            address_delivery = "-"
        else:
            delivery_address = "-"

        pickup_date_str = request.POST.get('pickup_date', '') 
        try:
            pickup_date = timezone.datetime.strptime(pickup_date_str, "%Y-%m-%d").date()
        except ValueError:            
            pickup_date = None     
    
        # Creacio de la Order guardant les caracteristiques d'aquesta
        order = Order(
            OrderUser=user,
            OrderPoints=total_points, 
            OrderHomePickup=home_pickup,   
            OrderDelivery= pick_up_point,       
            OrderCreationDate=timezone.now().date(),
            OrderPickupDate= pickup_date,
            OrderAddress=delivery_address,            
            OrderDeliveryAddress=address_delivery
        )
        order.save()

        # Per cada item guardat a la sessio de l'usuari (que pertanyen a la request total), es guarden les caracteristiques d'aquest
        for item in session_items:
            Orderline.objects.create(
                Order=order,
                OrderlineItem=item['name'],
                OrderlineUnits=item.get('units') or None,
                OrderlineWeight=item.get('weight') or None,
                OrderlineBrand=item.get('brand', '-'),
                OrderlineHeight=item.get('length', None),
                OrderlineDepth=item.get('depth', None),
                OrderlineWidth=item.get('width', None),
                OrderlineStatus=item.get('status', 'None'),
                OrderlineObservations=item.get('observations', ''),
                OrderlinePoints=item['points']
            )     
        # Perultim s'esborren els items de la sessio d'usuari, ja que ja s'ha creat correctament la sol·licitud (es prepara la sessio per a la seguent sol·licitud)
        del request.session['session_items'] 
        request.session.modified = True 
        # Es redirigeix a l'usuari a la pagina requestHistory per tal que aquest pugui veure la sol·licitud que acaba de fer
        return redirect('requestsHistory') 
    
    return redirect('requests')
        

# registre de l'usuari
def register(request):
    # s'agafa la info del formulari
    data = {
        'form': CustomUserCreationForm()   
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid(): #validació de l'usuari
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])            
            return redirect('login')  #el retorno al formulari d'inici de sesio per tal que fagi login
    return render(request, 'registration/register.html', data)


# nomes deixa veure el profile si l'usuari esta loggejat
@login_required
def profile(request):   
    if request.method == 'POST':
        # En cas que l'usuari canvi la info del seu perfil (amb el form CustomUserChangeForm) es guarda la info
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes have been saved!')            
    else:
        form = CustomUserChangeForm(instance=request.user)    
    return render(request, 'ecoApp/profile.html', {'form': form})



def products(request, category_id=None):
    # si s envia un category_id significa que s'esta filtrant per categoria
    if category_id:
         items = Item.objects.filter(Category=category_id)
    else: #sino, mostra tots els items sense filtrar
         items = Item.objects.all()
    categories = Category.objects.all()
    # s'envien les marques per tal de poder-les mostrar en el modal per seleccionar l'item
    brands = [category.CategoryBrands for category in categories]    
    return render(request, 'ecoApp/products.html', {"items": items, "categories": categories, "brands": brands})



def requestsHistory(request):
    # es passa la request de l'usuari per poder-la mostrar
    user_requests = Order.objects.filter(OrderUser=request.user).order_by('-OrderCreationDate').prefetch_related('orderlines')
    return render(request, 'ecoApp/requestsHistory.html', {'user_requests': user_requests})


# Formulari per canviar de contrasenya
class PasswordChangeView(PasswordChangeView):
    form_class = CustomUserChangePasswordForm
    success_url = reverse_lazy('passwordChangeSuccess')
   

def password_succes(request):
    return render(request, "registration/passwordChangeSuccess.html ")


# Eliminar usuari
class delete_user(SuccessMessageMixin, generic.DeleteView):
    model = User
    template_name = 'registration/deleteUserConfirm.html'
    success_url = reverse_lazy('index')




