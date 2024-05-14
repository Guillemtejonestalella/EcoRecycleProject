from django.db import models

# Create your models here.

from order.models import Order

# Create your models here.
class Orderline(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Cada Orderline debe tener una Order
    OrderlineItem = models.CharField(max_length=70)
    OrderlineUnits = models.IntegerField(null=True, blank=True)
    OrderlineWeight = models.IntegerField(null=True, blank=True)
    OrderlineBrand = models.CharField(max_length=50, null=True, blank=True)
    OrderlineHeight = models.IntegerField(null=True, blank=True)
    OrderlineDepth = models.IntegerField(null=True, blank=True)
    OrderlineWidth = models.IntegerField(null=True, blank=True)
    OrderlineStatus = models.CharField(max_length=70)
    OrderlineObservations = models.CharField(max_length=300, null=True, blank=True)
    OrderlinePoints = models.IntegerField()
    
    def __str__(self): 
        return self.OrderlineItem

    