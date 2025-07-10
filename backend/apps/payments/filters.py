import django_filters
from .models import Payment
from django.db.models import Q

class PaymentFilter(django_filters.FilterSet):
    min_amount = django_filters.NumberFilter(field_name="amount", lookup_expr='gte')
    max_amount = django_filters.NumberFilter(field_name="amount", lookup_expr='lte')
    date_from = django_filters.DateFilter(field_name="paid_at", lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name="paid_at", lookup_expr='lte')
    method = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.CharFilter(lookup_expr='iexact')
    currency = django_filters.CharFilter(lookup_expr='iexact')
    transaction = django_filters.CharFilter(field_name="transaction_id", lookup_expr='icontains')

    class Meta:
        model = Payment
        fields = [
            'status',
            'method',
            'currency',
            'transaction',
            'min_amount',
            'max_amount',
            'date_from',
            'date_to',
        ]
