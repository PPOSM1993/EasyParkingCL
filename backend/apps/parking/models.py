from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
from apps.authentication.models import *
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        unique_together = ('name', 'region')
        indexes = [
            models.Index(fields=['region']),
        ]

    def __str__(self):
        return f"{self.name}, {self.region.name}"


class Parking(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'

    TYPE_CHOICES = [
        (PUBLIC, 'Público'),
        (PRIVATE, 'Privado'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=PUBLIC)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='parkings')
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='parkings')
    total_spaces = models.PositiveIntegerField()
    available_spaces = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owned_parkings'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['region']),
            models.Index(fields=['city']),
        ]

    def clean(self):
        if self.available_spaces > self.total_spaces:
            raise ValidationError("Los espacios disponibles no pueden ser mayores al total de espacios.")

    def __str__(self):
        return f'{self.name} - {self.address}'

class RecommendationHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recommendations')
    recommended_parkings = models.ManyToManyField(Parking)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recomendación de {self.user.username} en ({self.latitude}, {self.longitude})"