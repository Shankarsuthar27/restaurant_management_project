from django.db import models
class MenuCategory(models.Model):
    name= models.CharField(max_length=100, unique=True)
    address= models.TextField()
    has_delivery = models.BooleanField(default=False)
    def __str__(self):
        return self.name
# Create your models here.
