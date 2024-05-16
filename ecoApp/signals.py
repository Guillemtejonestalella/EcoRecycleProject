from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from order.models import Order


@receiver(post_save, sender=Order)
def update_user_points(sender, instance, **kwargs):
    if instance.OrderStatus == 'Accepted':
        user = instance.OrderUser
        user.profile.ProfilePoints += instance.OrderPoints
        user.profile.save()
