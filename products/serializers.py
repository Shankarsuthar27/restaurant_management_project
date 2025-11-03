from rest_framework import serializers
from .models import Coupon
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        field = ['id','name']

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        field = ['code','discount','is_active','valid_from', 'valid_until']

