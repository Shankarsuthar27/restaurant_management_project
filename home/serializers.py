from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = MenuCategory
        fields= ['id','name','description','price', 'is_featured']