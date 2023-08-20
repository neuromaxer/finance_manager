from django.db import models

class Trade(models.Model):
    symbol = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=18, decimal_places=3)
    current_price = models.DecimalField(null=True, decimal_places=3, max_digits=18)
    type = models.CharField(max_length=4, null=True)
    time = models.CharField(max_length=20, null=True)
    
