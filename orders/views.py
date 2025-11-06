from rest_framework.view import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon
from .serializers import CouponSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import MenuCategory
from .serializers import MenuCategorySerializer



class CouponValidationView(APIView):
    permissions_classes= [IsAuthenticated]
    def get(self, request):
        coupon = Coupon.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

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

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset= MenuCategory.objects.all()
    serializer_class= MenuCategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset= queryset.filter(name__icontains=search_query)
            return queryset
