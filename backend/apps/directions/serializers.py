from rest_framework import serializers
from .models import RouteRequest, RecommendedZone


class RouteRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = RouteRequest
        geo_field = 'geometry'
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        origin = data.get('origin_address')
        destination = data.get('destination_address')
        if origin == destination:
            raise serializers.ValidationError("Origen y destino no pueden ser iguales.")
        return data


class RecommendedZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecommendedZone
        geo_field = 'zone'
        fields = '__all__'
        read_only_fields = ['created_at']

    def validate(self, data):
        route_request = data.get('route_request')
        zone = data.get('zone')
        if RecommendedZone.objects.filter(route_request=route_request, zone=zone).exists():
            raise serializers.ValidationError("Esta zona ya ha sido recomendada para esta ruta.")
        return data
