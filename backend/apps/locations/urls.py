# locations/urls.py

from rest_framework.routers import DefaultRouter
from .views import LocationZoneViewSet, PointOfInterestViewSet

router = DefaultRouter()
router.register(r'zones', LocationZoneViewSet)
router.register(r'pois', PointOfInterestViewSet)

urlpatterns = router.urls
