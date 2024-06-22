from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm): # classe personalitzada que hereda de UserCreationForm (form personalitzat modificat)
    
    class Meta:  #classe que permet modificar el form per tal que demani els camps "fields" especificats, que es troven a model=User
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


# classe personalitzada que hereda de UserChangeForm (form personalitzat modificat)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']


# classe personalitzada que hereda de UserChangePasswordForm (form personalitzat modificat)
class CustomUserChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']




