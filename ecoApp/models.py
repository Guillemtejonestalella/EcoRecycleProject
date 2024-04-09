from django.db import models

# Create your models here.
class Category(models.Model):
    CategoryName = models.CharField(verbose_name='Category', max_length=70, null=False, unique=True)
    CategoryPoints = models.IntegerField(verbose_name='Category Points', max_length=500, null = False)
    CategoryImage = models.ImageField(verbose_name="Category Image", upload_to="img/", null=False, blank=False)

    def __str__(self):
        return self.CategoryName
    
    class Meta:
        db_table = 'Categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']    


class Item(models.Model):
    # nom, categoria, fotoReal
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null= True, blank=True)
    ItemName = models.CharField(verbose_name='Item', max_length=70, null=False, unique=False)
    CategoryName = models.CharField(verbose_name= 'Item Category', max_length=70, null=False, unique=False)
    ItemImage = models.ImageField(verbose_name="Item Image", upload_to="img/", null=False, blank=False)

    def __str__(self):
        return self.Category
    
    class Meta:
        db_table = 'Items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['id']  