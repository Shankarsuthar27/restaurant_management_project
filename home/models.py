from django.db import models
import random

class MenuCategory(models.Model):
    name= models.CharField(max_length=100, unique=True)
    address= models.TextField()
    has_delivery = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)  
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @staticmethod
    def get_random_special():
        specials = list(DailySpecial.objects.all())
        if specials:
            return random.choice(specials)
            return None      
# Create your models here.
