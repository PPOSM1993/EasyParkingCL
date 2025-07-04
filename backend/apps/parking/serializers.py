# parkings/serializers.py

from rest_framework import serializers
from .models import Region, City, Parking

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    region_id = serializers.PrimaryKeyRelatedField(
        queryset=Region.objects.all(), write_only=True, source='region'
    )

    class Meta:
        model = City
        fields = ['id', 'name', 'region', 'region_id']


class ParkingSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    region_id = serializers.PrimaryKeyRelatedField(
        queryset=Region.objects.all(), write_only=True, source='region'
    )
    city = CitySerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), write_only=True, source='city'
    )

    class Meta:
        model = Parking
        fields = [
            'id', 'name', 'description', 'address',
            'latitude', 'longitude', 'type', 'price_per_hour',
            'region', 'region_id', 'city', 'city_id',
            'total_spaces', 'available_spaces', 'is_active',
            'owner', 'created_at', 'updated_at'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def validate_available_spaces(self, value):
        total = self.initial_data.get('total_spaces')
        if int(value) < 0:
            raise serializers.ValidationError("Los espacios disponibles no pueden ser negativos.")
        if total and int(value) > int(total):
            raise serializers.ValidationError("Los espacios disponibles no pueden ser mayores que el total.")
        return value



    def validate_price_per_hour(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio por hora no puede ser negativo.")
        return value

    def validate_total_spaces(self, value):
        if value <= 0:
            raise serializers.ValidationError("El número total de espacios debe ser mayor que cero.")
        return value

    def validate(self, data):
        lat = data.get('latitude')
        lon = data.get('longitude')
        name = data.get('name')
        address = data.get('address')

        if lat is not None and (lat < -90 or lat > 90):
            raise serializers.ValidationError({"latitude": "Debe estar entre -90 y 90."})
        if lon is not None and (lon < -180 or lon > 180):
            raise serializers.ValidationError({"longitude": "Debe estar entre -180 y 180."})

        if name and address:
            if Parking.objects.filter(name__iexact=name, address__iexact=address).exists():
                raise serializers.ValidationError("Ya existe un estacionamiento con ese nombre y dirección.")

        return data