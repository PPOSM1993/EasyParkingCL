"""from django_filters import rest_framework as filters
from .models import User

class UserFilter(filters.FilterSet):
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    role = filters.CharFilter(field_name='role', lookup_expr='iexact')
    is_verified = filters.BooleanFilter(field_name='is_verified')

    class Meta:
        model = User
        fields = ['email', 'role', 'is_verified']
"""