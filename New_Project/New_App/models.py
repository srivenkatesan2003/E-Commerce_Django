from django.db import models

# Create your models here.

class Mytable(models.Model):
    product_name = models.CharField(max_length=30 , null = True)
    product_code = models.CharField(max_length=30 , null = True)
    price = models.FloatField(default=0)
    gst = models.IntegerField(default=0)
    food_product = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.product_name
    
    