from django.contrib import admin

# Register your models here.

from .models import Item, Category, Profile  # Importa el modelo

# Registra tu modelo aquí
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Profile)
