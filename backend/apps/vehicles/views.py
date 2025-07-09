from rest_framework import viewsets, permissions, filters
from .models import Vehicle
from .serializers import VehicleSerializer
from .permissions import IsOwnerOrAdmin
from .filters import VehicleFilter
from django_filters.rest_framework import DjangoFilterBackend

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = VehicleFilter
    search_fields = ['license_plate', 'brand', 'model']
    ordering_fields = ['year', 'created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or getattr(user, 'role', None) == 'admin':
            return Vehicle.objects.all()
        return Vehicle.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
