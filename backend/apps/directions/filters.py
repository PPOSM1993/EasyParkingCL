from django_filters import rest_framework as filters
from .models import RouteRequest, RecommendedZone


class RouteRequestFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = RouteRequest
        fields = ['user', 'created_at']


class RecommendedZoneFilter(filters.FilterSet):
    is_primary = filters.BooleanFilter()

    class Meta:
        model = RecommendedZone
        fields = ['route_request', 'zone', 'is_primary']
