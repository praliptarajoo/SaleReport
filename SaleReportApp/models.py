from django.db import models
# Create your models here.

class SaleData(models.Model):
    Region = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Item_Type = models.CharField(max_length=150)
    Sales_Channel = models.CharField(max_length=150)
    Order_Priority = models.CharField(max_length=10)
    Order_Date = models.DateField(auto_now=False, auto_now_add=False)
    Order_ID = models.IntegerField(default=0)
    Ship_Date = models.DateField(auto_now=False, auto_now_add=False)
    Units_Sold = models.IntegerField()
    Unit_Price = models.FloatField()
    Unit_Cost = models.FloatField()
    Total_Revenue = models.FloatField()
    Total_Cost = models.FloatField()
    Total_Profit = models.FloatField()