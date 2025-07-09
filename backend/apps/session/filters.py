from django_filters import rest_framework as filters
from .models import ParkingSession

class ParkingSessionFilter(filters.FilterSet):
    status = filters.CharFilter(lookup_expr='iexact')
    destination_address = filters.CharFilter(lookup_expr='icontains')
    start_date = filters.DateFilter(field_name='start_time', lookup_expr='date__gte')
    end_date = filters.DateFilter(field_name='start_time', lookup_expr='date__lte')

    class Meta:
        model = ParkingSession
        fields = ['status', 'destination_address', 'start_date', 'end_date']