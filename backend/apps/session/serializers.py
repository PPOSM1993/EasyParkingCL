from rest_framework import serializers
from .models import ParkingSession

class ParkingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSession
        fields = [
            'id',
            'user',
            'parking_space',
            'destination_address',
            'start_time',
            'end_time',
            'status',
            'location_snapshot',
            'ai_recommendation_id',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id', 'user', 'start_time', 'created_at', 'updated_at'
        ]

    def validate_status(self, value):
        if value not in ['active', 'completed', 'cancelled']:
            raise serializers.ValidationError("Estado inválido.")
        return value

    def validate(self, data):
        status = data.get('status')
        end_time = data.get('end_time')

        # Si la sesión está marcada como 'completed', debe tener un `end_time`
        if status == 'completed' and not end_time:
            raise serializers.ValidationError({
                'end_time': 'Debes definir la hora de término si finalizas la sesión.'
            })

        return data

    def create(self, validated_data):
        # Asegurar que el usuario autenticado quede asignado
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
