from django.urls import path
from .views import FeaturedItemVIew

urlpatterns = [
    path('featured-items/', FeaturedItemVIew.as_view(), name='featured-items'),
]