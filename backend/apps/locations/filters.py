import django_filters
from .models import LocationZone, PointOfInterest

class LocationZoneFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = LocationZone
        fields = ['name']

class PointOfInterestFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    #category = django_filters.CharFilter(lookup_expr='icontains')  # si tienes este campo

    class Meta:
        model = PointOfInterest
        fields = ['name']
