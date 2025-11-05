from rest_framework import serializers
from .models import Order,Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id','name','price']

class OrderSerializer(serializers.ModelSerializer):
    coupon= CouponSerializer(many=True)

    class Meta:
        model=Order
        fields=['id','date','total_price','items']