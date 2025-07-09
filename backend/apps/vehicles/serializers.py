from rest_framework import serializers
from .models import Vehicle
from datetime import datetime
import re

CURRENT_YEAR = datetime.now().year

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'id',
            'user',
            'license_plate',
            'brand',
            'model',
            'year',
            'vehicle_type',
            'engine_type',
            'color',
            'mileage',
            'insurance_expiration',
            'technical_revision_date',
            'is_electric',
            'image',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at')

    def validate_license_plate(self, value):
        value = value.upper().replace("-", "")
        if not re.match(r'^[A-Z]{2,3}\d{2,3}$', value):
            raise serializers.ValidationError("Formato de patente inválido. Ejemplo válido: ABC123")

        user = self.context['request'].user
        if Vehicle.objects.filter(license_plate=value, user=user).exists():
            raise serializers.ValidationError("Ya tienes un vehículo registrado con esta patente.")

        return value

    def validate_year(self, value):
        if value < 1950 or value > CURRENT_YEAR + 1:
            raise serializers.ValidationError(f"Año fuera de rango permitido (1950 - {CURRENT_YEAR + 1})")
        return value
