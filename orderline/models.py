# models.py
from django.db import models
from order.models import Order

class Orderline(models.Model):
    Order = models.ForeignKey(Order, related_name='orderlines', on_delete=models.CASCADE)  
    OrderlineItem = models.CharField(max_length=70)
    OrderlineUnits = models.IntegerField(null=True, blank=True)
    OrderlineWeight = models.IntegerField(null=True, blank=True)
    OrderlineBrand = models.CharField(max_length=50, null=True, blank=True)
    OrderlineHeight = models.IntegerField(null=True, blank=True)
    OrderlineDepth = models.IntegerField(null=True, blank=True)
    OrderlineWidth = models.IntegerField(null=True, blank=True)
    OrderlineStatus = models.CharField(max_length=70, null=True, blank=True)
    OrderlineObservations = models.CharField(max_length=300, null=True, blank=True)
    OrderlinePoints = models.IntegerField()
    
    def __str__(self): 
        return self.OrderlineItem

    