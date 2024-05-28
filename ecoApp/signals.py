from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from order.models import Order

@receiver(post_save, sender=Order)
def update_user_points_and_send_email(sender, instance, **kwargs):
    if instance.OrderStatus == 'Accepted':
        user = instance.OrderUser
        # Actualizar puntos del usuario
        user.profile.ProfilePoints += instance.OrderPoints
        user.profile.save()

        # Enviar correo electrónico
        send_mail(
            subject='Your Order Has Been Accepted',
            message= 'Hello {user.username}, your order has been accepted!',
            # message=f'Dear {user.username},\n\nYour order with ID {instance.id} has been accepted. You have been awarded {instance.OrderPoints} points.\n\nThank you for your order!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
