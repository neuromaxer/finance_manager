from django.db import models

class Trade(models.Model):
    symbol = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    purchase_price = models.FloatField()
    current_price = models.FloatField(null=True)
    
