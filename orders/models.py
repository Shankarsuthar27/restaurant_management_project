from django.db import models
class Coupon(models.Model):
    code= models.CharField(max_length=50, unique=True)
    discount= models.DecimalField(max_digit=5,decimal_place=2)
    is_active= models.BooleanField(default=True)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    def __str__(self):
        return self.code
        
class Order(models.Model):
    customer_name= models.CharField(max_length=100)
    total_price= models.DecimalField(max_length=10, decimal_place=2)
    status= models.ForeignKey(OrderStatus, on_delete = models.SET_NULL, null=True) 

    def __str__(self):
        return f"Order #{self.id}- {self.customer_name}"       
# Create your models here.
