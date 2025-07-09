import django_filters
from .models import Suggestion
from django_filters import rest_framework as filters

class SuggestionFilter(filters.FilterSet):
    score_min = filters.NumberFilter(field_name="score", lookup_expr='gte', label="Score desde")
    score_max = filters.NumberFilter(field_name="score", lookup_expr='lte', label="Score hasta")
    created_after = filters.DateTimeFilter(field_name="created_at", lookup_expr='gte', label="Desde fecha")
    created_before = filters.DateTimeFilter(field_name="created_at", lookup_expr='lte', label="Hasta fecha")

    class Meta:
        model = Suggestion
        fields = [
            'method',
            'recommended_parking',
            'session',
        ]
