from django.contrib import admin

# Register your models here.

from .models import Item, Category  # Importa el modelo

# Registra tu modelo aquí
admin.site.register(Item)
admin.site.register(Category)
