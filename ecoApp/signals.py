from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from order.models import Order

@receiver(post_save, sender=Order)
def update_user_points_and_send_email(sender, instance, **kwargs):  #Actualitza els punts de l'usuari i envia correu de confirmacio.
    if instance.OrderStatus == 'Accepted':        
        order = instance.OrderUser        
        order.profile.ProfilePoints += instance.OrderPoints
        order.profile.save()               

        #Correu electronic automatic Acceptacio
        send_mail(
            subject='Your order has been ACCEPTED',            
            message=f'Dear {order.username},\n\nYour request has been accepted! You have been awarded {instance.OrderPoints} points.\n\nThank you for your order!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )
    elif instance.OrderStatus == 'Denied':
        order = instance.OrderUser
        order.profile.save()
         #Correu electronic automatic Denegacio
        send_mail(
            subject='Your order has been DENIED',            
            message=f'Dear {order.username},\n\nYour request has been denied!\n\nResend your request!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )
    elif instance.OrderStatus == 'Pending approval':      
        
        order = instance.OrderUser
        order.profile.save()
         #Correu electronic automatic Enviament 
        send_mail(
            subject='Your order has been sended',           
            message=f'Dear {order.username},\n\nYour request has been submitted successfully. Wait to receive the acceptance or denial email.\n\nThank you for your order!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )

        
