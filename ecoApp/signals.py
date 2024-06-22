from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from order.models import Order


@receiver(post_save, sender=Order)
def update_user_points_and_send_email(sender, instance, **kwargs):  #Actualitza els punts de l'usuari i envia correu de confirmacio.
            
    # Creacio dels missatges automatitzats en funcio del canvi de l'estat de la sol·licitud d'usuari (mateix missatge amb diferent info en funcio de l'estat)
    if instance.OrderStatus == 'Accepted':        
        order = instance.OrderUser        
        order.profile.ProfilePoints += instance.OrderPoints
        order.profile.save()     

         #Correu electronic automatic Acceptacio

        message = (
            f'Dear {order.username},\n\n')    

        html_message = (
            f'<p>Dear {order.username},\n\n</p>'
            f'<p>Your request has been accepted! You have been awarded {instance.OrderPoints} points.\n\n</p>'
            f'<p>Thank you for your request!\n\n</p>'
            f'<img src="https://github.com/Guillemtejonestalella/EcoRecycleProject/raw/main/logoRedimensionat-transparent.png" alt="Logo" style="max-width: 20%; margin-top: 30px;">'

        )             
        send_mail(
            subject='Your request has been ACCEPTED',            
            message=message,
            html_message=html_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )
    elif instance.OrderStatus == 'Denied':
        order = instance.OrderUser
        order.profile.save()

        #Correu electronic automatic Denegacio

        message = (
            f'Dear {order.username},\n\n')

        html_message = (
            f'<p>Dear {order.username},\n\n</p>'
            f'<p>Your request has been denied!\n\n</p>'
            f'<p>Resend your request!\n\n</p>'
            f'<img src="https://github.com/Guillemtejonestalella/EcoRecycleProject/raw/main/logoRedimensionat-transparent.png" alt="Logo" style="max-width: 20%; margin-top: 30px;">'
        )

        send_mail(
            subject='Your request has been DENIED',            
            message=message,
            html_message=html_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )
    elif instance.OrderStatus == 'Pending approval':      
        
        order = instance.OrderUser
        order.profile.save()

        #Correu electronic automatic Enviament 

        message= (f'Dear {order.username},\n\n')

        html_message = (
            f'<p>Dear {order.username},\n\n</p>'
            f'<p>Your request has been submitted successfully. Wait to receive the acceptance or denial email.\n\n</p>'
            f'<p>Thank you for your request!\n\n</p>'
            f'<img src="https://github.com/Guillemtejonestalella/EcoRecycleProject/raw/main/logoRedimensionat-transparent.png" alt="Logo" style="max-width: 20%; margin-top: 30px;">'
        )
        
        send_mail(
            subject='Your request has been sended',
            message=message,
            html_message=html_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )

        
