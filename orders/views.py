from rest_framework.view import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon
from .serializers import CouponSerializer

class CouponValidationView(APIView):
    def post(self , response):
        code = request.data.get('code')

        if not code:
            return Response({"error": "Coupon code is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            coupon = Coupon.objects.get(code=code)
        expect Coupon.DoesNotExist:
        return Response({"error": "Invalid coupon code"}, status=status.HTTP_400_BAD_REQUEST)

        now  = timezone.now()
            if not coupon.is_active or coupon.valid_from > now or coupon.valid_until < now:
                return Response({"error": "Coupon is not valid or has expired"}, status=status.HTTP_400_BAD_REQUEST)

                serializer = CouponSerializer(coupon)
                return Response({"success": True, "coupon": serializer.data}, status=status.HTTP_200_OK)