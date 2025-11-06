from django.db import models
from django.contrib.auth.models import User
from .models import MenuCategory

class Coupon(models.Model):
    code= models.CharField(max_length=50, unique=True)
    discount= models.DecimalField(max_digit=5,decimal_place=2)
    is_active= models.BooleanField(default=True)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    def __str__(self):
        return self.code
        
class Order(models.Model):
    customer_name= models.ForeignKey(User,on_delete=models.CASCADE, related_name= 'order')
    total_price= models.DecimalField(max_length=10, decimal_place=2)
    status= models.ForeignKey(OrderStatus, on_delete = models.SET_NULL, null=True) 
    coupon= models.ManyToManyField(Coupon)


    def __str__(self):
        return f"Order #{self.id}- {self.customer_name}"       

class NutritionalInformation(models.Model):
    menu_category = models.OneToOneField(MenuCategory, on_delete= models.CASCADE, related_name='nutrition_info')
    calories = models.IntegerField()
    fat = models.DecimalField(max_digit=5, decimal_place=2)
    protein = models.DecimalField(max_digit=5, decimal_place=2)
    carbohydrates = models.DecimalField(max_digit=5, decimal_place=2)

    def __str__(self):
        return f"{self.menu_category.name}- {self.calories} cal"