from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import LocationZone, PointOfInterest

class LocationZoneSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LocationZone
        geo_field = 'polygon'
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre de la zona debe tener al menos 3 caracteres.")
        return value

    def validate(self, data):
        name = data.get("name", "").lower()
        if "prohibido" in name:
            raise serializers.ValidationError("No se permite usar nombres con 'prohibido'.")
        return data


class PointOfInterestSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PointOfInterest
        geo_field = 'location'
        fields = '__all__'

    def validate_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El nombre del punto de interés debe comenzar con mayúscula.")
        return value

    def validate_location(self, value):
        # Validación de latitud y longitud
        if not (-90 <= value.y <= 90 and -180 <= value.x <= 180):
            raise serializers.ValidationError("Coordenadas fuera del rango válido.")
        return value

    def validate(self, data):
        location = data.get('location')
        if location and PointOfInterest.objects.filter(location=location).exists():
            raise serializers.ValidationError("Ya existe un punto en estas coordenadas.")
        return data
