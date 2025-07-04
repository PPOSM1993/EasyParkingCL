from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingViewSet, RegionViewSet, CityViewSet

router = DefaultRouter()
router.register(r'parkings', ParkingViewSet, basename='parkings')
router.register(r'regions', RegionViewSet, basename='regions')
router.register(r'cities', CityViewSet, basename='cities')

urlpatterns = [
    path('', include(router.urls)),
]