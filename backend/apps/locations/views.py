from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend

from .models import LocationZone, PointOfInterest
from .serializers import LocationZoneSerializer, PointOfInterestSerializer
from .permissions import IsAdminOrReadOnly
from .filters import PointOfInterestFilter

class LocationZoneViewSet(viewsets.ModelViewSet):
    queryset = LocationZone.objects.all()
    serializer_class = LocationZoneSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Solo administradores pueden crear zonas.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.name.lower() in ['zona central', 'zona protegida']:
            raise PermissionDenied("No puedes eliminar una zona protegida.")
        instance.delete()


class PointOfInterestViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PointOfInterestFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    ordering = ['name']

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Debes estar autenticado para crear puntos de interés.")
        serializer.save()

    def perform_destroy(self, instance):
        if 'hospital' in instance.name.lower():
            raise PermissionDenied("No se puede eliminar un hospital.")
        instance.delete()
