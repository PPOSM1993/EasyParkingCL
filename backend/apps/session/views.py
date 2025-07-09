from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import ParkingSession
from .serializers import ParkingSessionSerializer
from .permissions import IsOwnerOrAdminSession
from .filters import ParkingSessionFilter

class ParkingSessionViewSet(viewsets.ModelViewSet):
    serializer_class = ParkingSessionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminSession]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParkingSessionFilter

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return ParkingSession.objects.all().order_by('-start_time')
        return ParkingSession.objects.filter(user=user).order_by('-start_time')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
