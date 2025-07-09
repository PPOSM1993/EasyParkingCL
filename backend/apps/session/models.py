from django.db import models
from django.conf import settings

class ParkingSession(models.Model):
    STATUS_CHOICES = [
        ('active', 'Activa'),
        ('completed', 'Finalizada'),
        ('cancelled', 'Cancelada'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sessions')
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.SET_NULL, null=True, blank=True)
    parking_space = models.ForeignKey('parking.Parking', on_delete=models.SET_NULL, null=True, blank=True)

    destination_address = models.CharField(max_length=255, help_text="Dirección o destino deseado por el usuario")
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    location_snapshot = models.JSONField(blank=True, null=True, help_text="Datos del espacio recomendado")
    ai_recommendation_id = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} → {self.destination_address} ({self.status})"
