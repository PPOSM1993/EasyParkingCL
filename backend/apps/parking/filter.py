import django_filters
from .models import Parking

class ParkingFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price_per_hour", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price_per_hour", lookup_expr='lte')
    available = django_filters.BooleanFilter(field_name="available_spaces", lookup_expr='gt')

    class Meta:
        model = Parking
        fields = {
            'region': ['exact'],
            'city': ['exact'],
            'type': ['exact'],
            'available_spaces': ['gt'],  # para filtrar por espacios disponibles mayor a un número
            'is_active': ['exact'],
        }