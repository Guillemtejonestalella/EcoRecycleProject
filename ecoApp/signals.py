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

        message = (
            f'Dear {order.username},\n\n'
            f'Your request has been accepted! You have been awarded {instance.OrderPoints} points.\n\n'
            f'Thank you for your request!\n\n'
            f'<img src="{settings.MEDIA_URL}ecoApp/static/asstets/img/logoRedimensionat-transparent.png" alt="Logo">'
        )          

        #Correu electronic automatic Acceptacio
        send_mail(
            subject='Your request has been ACCEPTED',            
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )
    elif instance.OrderStatus == 'Denied':
        order = instance.OrderUser
        order.profile.save()
         #Correu electronic automatic Denegacio

        message = (
            f'Dear {order.username},\n\n'
            f'Your request has been denied!\n\n'
            f'Resend your request!\n\n'
            f'<img src="{settings.MEDIA_URL}ecoApp/static/asstets/img/logoRedimensionat-transparent.png" alt="Logo">'
        )
        send_mail(
            subject='Your request has been DENIED',            
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )
    elif instance.OrderStatus == 'Pending approval':      
        
        order = instance.OrderUser
        order.profile.save()
         #Correu electronic automatic Enviament 

        message = (
            f'Dear {order.username},\n\n'
            f'Your request has been submitted successfully. Wait to receive the acceptance or denial email.\n\n'
            f'Thank you for your request!\n\n'
            f'<img src="{settings.MEDIA_URL}ecoApp/static/asstets/img/logoRedimensionat-transparent.png" alt="Logo">'
        )
        message = message
        send_mail(
            subject='Your request has been sended',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )

        
