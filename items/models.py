from django.db import models
from categories.models import Category

# Create your models here.
class Item(models.Model):
    # nom, categoria, fotoReal
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null= True, blank=True)
    ItemName = models.CharField(verbose_name='Item', max_length=70, null=False, unique=False) 
    ItemImage = models.ImageField(verbose_name="Item Image", upload_to="ecoApp/static/asstets/img", null=False, blank=False)
    ItemDescription = models.TextField(verbose_name="Item Description", max_length=999, null=False, unique=False)

    def __str__(self):
        return self.ItemName
    
    class Meta:
        db_table = 'Items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['id'] 