from django.db import models
from django.conf import settings

class Suggestion(models.Model):
    METHOD_CHOICES = (
        ('heuristic', 'Heurístico'),
        ('rule_based', 'Reglas'),
        ('ml', 'Machine Learning'),
        ('ai', 'IA Avanzada'),
        ('manual', 'Manual'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='suggestions'
    )
    destination_address = models.CharField(max_length=255)
    destination_lat = models.FloatField()
    destination_lng = models.FloatField()
    recommended_parking = models.ForeignKey(
        'parking.Parking',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='suggested_for'
    )
    method = models.CharField(max_length=20, choices=METHOD_CHOICES, default='heuristic')
    score = models.FloatField(default=0.0, help_text='Nivel de confianza en la recomendación')
    notes = models.TextField(blank=True, null=True)
    session = models.ForeignKey(
        'session.ParkingSession',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ai_suggestion'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Sugerencia"
        verbose_name_plural = "Sugerencias"

    def __str__(self):
        return f"{self.user.username} → {self.recommended_parking} ({self.method})"
