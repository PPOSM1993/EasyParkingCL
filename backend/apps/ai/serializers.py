from rest_framework import serializers
from .models import Suggestion
#from parking.models import Parking
#from session.models import ParkingSession
from apps.parking.models import Parking
from apps.session.models import ParkingSession

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = [
            'id',
            'user',
            'destination_address',
            'destination_lat',
            'destination_lng',
            'recommended_parking',
            'method',
            'score',
            'notes',
            'session',
            'created_at'
        ]
        read_only_fields = ('id', 'user', 'created_at')

    def validate_score(self, value):
        if value < 0 or value > 1:
            raise serializers.ValidationError("El score debe estar entre 0.0 y 1.0")
        return value

    def validate(self, data):
        lat = data.get("destination_lat")
        lng = data.get("destination_lng")
        if lat is not None and (lat < -90 or lat > 90):
            raise serializers.ValidationError({"destination_lat": "Latitud inválida"})
        if lng is not None and (lng < -180 or lng > 180):
            raise serializers.ValidationError({"destination_lng": "Longitud inválida"})
        return data

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
