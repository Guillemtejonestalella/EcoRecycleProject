from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from order.models import Order

@receiver(post_save, sender=Order)
def update_user_points_and_send_email(sender, instance, **kwargs):  #Actualitza els punts de l'usuari i envia correu de confirmacio.
    if instance.OrderStatus == 'Accepted':
        user = instance.OrderUser        
        user.profile.ProfilePoints += instance.OrderPoints
        user.profile.save()

        #Correu electronic automatic 
        send_mail(
            subject='Your order has been ACCEPTED',
            # message= 'Hello user, your order has been accepted!',
            message=f'Dear user,\n\nYour request has been accepted! You have been awarded {instance.OrderPoints} points.\n\nThank you for your order!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
    elif instance.OrderStatus == 'Denied':
        user = instance.OrderUser
        user.profile.save()
        send_mail(
            subject='Your order has been DENIED',
            # message= 'Hello user, your order has been denied!',
            message=f'Dear user,\n\nYour request has been denied!\n\nResend your request!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
    elif instance.OrderStatus == 'Pending approval':
        user = instance.OrderUser
        user.profile.save()
        send_mail(
            subject='Your order has been sended',
            # message= 'Hello user, your request has been submitted successfully. Wait to receive the acceptance or denial email. Thank you so much!',
            message=f'Dear user,\n\nYour request has been submitted successfully. Wait to receive the acceptance or denial email.\n\nThank you for your order!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
