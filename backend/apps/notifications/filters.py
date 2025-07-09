import django_filters
from django_filters import rest_framework as filters
from .models import Notification

class NotificationFilter(filters.FilterSet):
    created_after = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte', label='Desde fecha de creación')
    created_before = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte', label='Hasta fecha de creación')

    sent_after = filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte', label='Desde fecha de envío')
    sent_before = filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte', label='Hasta fecha de envío')

    read_after = filters.DateTimeFilter(field_name='read_at', lookup_expr='gte', label='Desde fecha de lectura')
    read_before = filters.DateTimeFilter(field_name='read_at', lookup_expr='lte', label='Hasta fecha de lectura')

    class Meta:
        model = Notification
        fields = [
            'type',
            'status',
            'is_read',
            'related_session',
            'related_suggestion',
            'related_vehicle',
            'related_parking',
        ]
