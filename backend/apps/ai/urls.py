from rest_framework.routers import DefaultRouter
from .views import SuggestionViewSet

router = DefaultRouter()
router.register(r'suggestions', SuggestionViewSet, basename='suggestions')

urlpatterns = router.urls
