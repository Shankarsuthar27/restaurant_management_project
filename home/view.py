from 
class MenuCategoryListView(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer