from django.db import models
from New_App.models import Mytable

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=30 , null = True)
    customer_since= models.DateField(max_length=30 , null = True)

    def __str__(self) -> str:
        return self.customer_name
    



class Orders(models.Model):
    Customer_reference = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product_reference = models.ForeignKey(Mytable,on_delete=models.SET_NULL,null=True)
    order_number = models.CharField(max_length=20,null=True)
    order_date = models.DateField(null=True)
    quantity = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    gst_amount = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return self.order_number