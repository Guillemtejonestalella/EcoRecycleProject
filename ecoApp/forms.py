from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm): # classe personalitzada que hereda de UserCreationForm (form personalitzat modificat)
    
    class Meta:  #classe que permet modificar el form per tal que demani els camps "fields" especificats, que es troven a model=User
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

