from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Order(models.Model): 
    OrderUser = models.ForeignKey(User, on_delete=models.CASCADE)   
    OrderPoints = models.IntegerField()
    OrderStatus = models.CharField(max_length=70, default="Pending approval")
    OrderHomePickup = models.BooleanField()
    OrderCreationDate = models.DateField() 
    OrderPickupDate = models.DateField()
    OrderAddress = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self): 
        return self.OrderUser.username