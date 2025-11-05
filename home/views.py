from rest_framework import generics
from .models import MenuCategory
from .serializers import MenuCategorySerializer
class FeaturedItemView(generics.ListAPIView):
    queryset = MenuCategory.objects.filter(is_featured=True)
    serializer_class = MenuCategorySerializer

