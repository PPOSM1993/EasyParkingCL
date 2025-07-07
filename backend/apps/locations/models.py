from django.contrib.gis.db import models as gis_models
from django.db import models
from  apps.parking.models import City
from django.contrib.gis.db import models as gis_models

class LocationZone(models.Model):
    ZONE_TYPES = (
        ('residential', 'Residencial'),
        ('commercial', 'Comercial'),
        ('mall', 'Centro Comercial'),
        ('university', 'Universidad'),
        ('airport', 'Aeropuerto'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='zones')
    polygon = gis_models.PolygonField()
    center = gis_models.PointField(null=True, blank=True)
    main_access_point = gis_models.PointField(null=True, blank=True)
    zone_type = models.CharField(max_length=30, choices=ZONE_TYPES, default='commercial')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.polygon:
            self.center = self.polygon.centroid
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    location = gis_models.PointField()
    zone = models.ForeignKey('locations.LocationZone', on_delete=models.CASCADE, related_name='pois')
    type = models.CharField(max_length=50)  # ejemplo: 'restaurante', 'hospital', etc.

    def __str__(self):
        return f"{self.name} ({self.type})"