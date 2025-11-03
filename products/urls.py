from django.urls import path
from .views import *
from .views import MenuCategoryListView

urlpatterns = [
    path('category/', MenuCategoryListView.as_view(),name='menu-category'),
]