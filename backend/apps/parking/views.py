from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Parking, City, Region
from .serializers import ParkingSerializer, CitySerializer, RegionSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_gis.filters import DistanceToPointFilter
from django.contrib.gis.geos import Point
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ValidationError


class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.filter(is_active=True)
    serializer_class = ParkingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['region', 'city', 'type', 'is_active']
    search_fields = ['name', 'address', 'description']
    ordering_fields = ['price_per_hour', 'available_spaces', 'created_at']
    ordering = ['-available_spaces']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtro adicional por coordenadas (cercanía)
        lat = self.request.query_params.get('latitude')
        lon = self.request.query_params.get('longitude')
        if lat and lon:
            try:
                lat = float(lat)
                lon = float(lon)
                queryset = sorted(
                    queryset,
                    key=lambda x: ((x.latitude - lat) ** 2 + (x.longitude - lon) ** 2)
                )
            except ValueError:
                pass
        return queryset

    @action(detail=False, methods=['get'], url_path='recommend')
    def recommend_parking(self, request):
        """
        Endpoint para recomendar estacionamientos según latitud y longitud.
        Ejemplo: /api/parkings/recommend/?latitude=-38.73&longitude=-72.59
        """
        lat = request.query_params.get('latitude')
        lon = request.query_params.get('longitude')

        if not lat or not lon:
            return Response({'detail': 'Debes proporcionar latitude y longitude.'}, status=400)

        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return Response({'detail': 'Coordenadas inválidas.'}, status=400)

        # Reordenar queryset por cercanía
        queryset = list(Parking.objects.filter(is_active=True))
        queryset.sort(key=lambda x: ((x.latitude - lat) ** 2 + (x.longitude - lon) ** 2))

        top_parkings = queryset[:5]  # Top 5 más cercanos
        serialized = self.get_serializer(top_parkings, many=True)

        # Guardar historial si el usuario está autenticado
        if request.user.is_authenticated:
            history = RecommendationHistory.objects.create(
                user=request.user,
                latitude=lat,
                longitude=lon
            )
            history.recommended_parkings.set(top_parkings)

        return Response(serialized.data)

    @action(detail=False, methods=['get'], url_path='recommend/history')
    def recommendation_history(self, request):
        """
        Endpoint para ver el historial de recomendaciones del usuario autenticado.
        """
        if not request.user.is_authenticated:
            return Response({'detail': 'Autenticación requerida.'}, status=401)

        histories = request.user.recommendations.prefetch_related('recommended_parkings').order_by('-created_at')[:10]
        data = []
        for history in histories:
            data.append({
                'latitude': history.latitude,
                'longitude': history.longitude,
                'created_at': history.created_at,
                'parkings': ParkingSerializer(history.recommended_parkings.all(), many=True).data
            })
        return Response(data)

class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['region']