from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'user',
            'title',
            'message',
            'type',
            'status',
            'is_read',
            'related_session',
            'related_suggestion',
            'related_vehicle',
            'related_parking',
            'sent_at',
            'read_at',
            'created_at'
        ]
        read_only_fields = [
            'id',
            'user',
            'status',
            'sent_at',
            'read_at',
            'created_at'
        ]

    def create(self, validated_data):
        # El usuario se asigna automáticamente
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
