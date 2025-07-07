from rest_framework.routers import DefaultRouter
from .views import RouteRequestViewSet, RecommendedZoneViewSet

router = DefaultRouter()
router.register(r'route-requests', RouteRequestViewSet, basename='route-requests')
router.register(r'recommended-zones', RecommendedZoneViewSet, basename='recommended-zones')

urlpatterns = router.urls
