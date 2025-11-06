import string
import secrets
from .models import Coupon
from django.db.models import Sum
from .models import Order

def generate_coupon_code(length=10):

    characters = string.ascii_uppercase + string.digits

    orders = Order.objects.filter(created_at__date=date)
    total = orders.aggregate(total_sum = Sum('total_price')) ['total_sum']
 

    while True:
        code = ''.join(secrets.choice(characters) for_in range(length))

        if not Coupon.objects.filter(code=code).exists():
            return code

def calculate_tip_amount(total, tip_percentage):
    tip= total*(tip_percentage/100)
    return round(tip, 2)