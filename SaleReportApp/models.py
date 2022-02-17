from django.db import models
# Create your models here.

class SaleData(models.Model):
    CHOICES = (
        ('Online','Online'),
        ('Offline','Offline'),
    )
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    item_type = models.CharField(max_length=150)
    sales_channel = models.CharField(max_length=150, choices= CHOICES)
    order_priority = models.CharField(max_length=10)
    order_date = models.DateField(auto_now=False, auto_now_add=False)
    order_id = models.IntegerField(default=0)
    ship_date = models.DateField(auto_now=False, auto_now_add=False)
    units_sold = models.IntegerField()
    unit_price = models.FloatField()
    unit_cost = models.FloatField()
    total_revenue = models.FloatField()
    total_cost = models.FloatField()
    total_profit = models.FloatField()