from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingSessionViewSet

router = DefaultRouter()
router.register(r'sessions', ParkingSessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
]
