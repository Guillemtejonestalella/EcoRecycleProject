from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Order(models.Model): 

    ORDER_STATUS = (
        ("Pending aproval", "Pending aproval"),
        ("Accepted", "Accepted"),
        ("Cancelled", "Cancelled")
    )

    OrderUser = models.ForeignKey(User, on_delete=models.CASCADE)   
    OrderPoints = models.IntegerField()
    OrderStatus = models.CharField(max_length=70, choices=ORDER_STATUS, default="Pending approval")
    

    OrderHomePickup = models.BooleanField(null=True, blank=True)
    OrderDelivery = models.BooleanField(null=True, blank=True) #new

    OrderCreationDate = models.DateField() 
    OrderPickupDate = models.DateField(null=True, blank=True)
    
    OrderAddress = models.CharField(max_length=150, null=True, blank=True)
    OrderDeliveryAddress =  models.CharField(max_length=150, null=True, blank=True) #new
    
    def __str__(self): 
        return self.OrderUser.username