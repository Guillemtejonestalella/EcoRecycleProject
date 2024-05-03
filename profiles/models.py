from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
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