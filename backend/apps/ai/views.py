from rest_framework import viewsets, permissions, filters
from .models import Suggestion
from .serializers import SuggestionSerializer
from .permissions import IsOwnerOrAdmin
from django_filters.rest_framework import DjangoFilterBackend

class SuggestionViewSet(viewsets.ModelViewSet):
    serializer_class = SuggestionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['method', 'recommended_parking', 'session']
    search_fields = ['destination_address', 'notes']
    ordering_fields = ['score', 'created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or getattr(user, 'role', None) == 'admin':
            return Suggestion.objects.all()
        return Suggestion.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
