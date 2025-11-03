from django.db import models
class OrderStatus(models.Model):
    name= models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
        
class Order(models.Model):
    customer_name= models.CharField(max_length=100)
    total_price= models.DecimalField(max_length=10, decimal_place=2)
    status= models.ForeignKey(OrderStatus, on_delete = models.SET_NULL, null=True) 

    def __str__(self):
        return f"Order #{self.id}- {self.customer_name}"       
# Create your models here.
