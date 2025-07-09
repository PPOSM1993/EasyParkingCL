import django_filters
from .models import Vehicle

class VehicleFilter(django_filters.FilterSet):
    year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label='Año desde')
    year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label='Año hasta')
    is_electric = django_filters.BooleanFilter()

    class Meta:
        model = Vehicle
        fields = {
            'vehicle_type': ['exact'],
            'engine_type': ['exact'],
            'color': ['exact'],
            'is_electric': ['exact'],
        }
