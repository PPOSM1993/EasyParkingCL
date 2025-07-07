from rest_framework import viewsets, permissions, filters as drf_filters
from .models import RouteRequest, RecommendedZone
from .serializers import RouteRequestSerializer, RecommendedZoneSerializer
from .permissions import IsOwnerOrAdmin
from .filters import RouteRequestFilter, RecommendedZoneFilter
from .pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend


class RouteRequestViewSet(viewsets.ModelViewSet):
    queryset = RouteRequest.objects.all().order_by('-created_at')
    serializer_class = RouteRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, drf_filters.OrderingFilter]
    filterset_class = RouteRequestFilter
    ordering_fields = ['created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return RouteRequest.objects.all()
        return RouteRequest.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecommendedZoneViewSet(viewsets.ModelViewSet):
    queryset = RecommendedZone.objects.all()
    serializer_class = RecommendedZoneSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, drf_filters.OrderingFilter]
    filterset_class = RecommendedZoneFilter
    ordering_fields = ['created_at', 'is_primary']
