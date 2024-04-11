from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


# Create your models here.
class Category(models.Model):
    CategoryName = models.CharField(verbose_name='Category', max_length=70, null=False, unique=True)
    CategoryPoints = models.IntegerField(verbose_name='Category Points', null = False)
    CategoryImage = models.ImageField(verbose_name="Category Image", upload_to="ecoApp/static/asstets/img", null=False, blank=False)

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
    ItemImage = models.ImageField(verbose_name="Item Image", upload_to="ecoApp/static/asstets/img", null=False, blank=False)
    ItemDescription = models.TextField(verbose_name="Item Description", max_length=999, null=False, unique=False)

    def __str__(self):
        return self.ItemName
    
    class Meta:
        db_table = 'Items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['id']  


class Profile(models.Model):
    ProfileName = models.CharField(max_length=50, blank=True)  # Hacemos que sea opcional
    ProfilePerson = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # Cambiamos el nombre del campo
    ProfilePoints = models.IntegerField(default=0)
    ProfileAdress = models.CharField(max_length=70, blank=True)  # Hacemos que sea opcional

    def __str__(self): 
        return self.ProfileName

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(ProfilePerson=instance, ProfileName="profile")  # Establecemos el ProfileName como el username por defecto

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()