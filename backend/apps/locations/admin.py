from django.contrib import admin
from .models import LocationZone, PointOfInterest
from django.contrib.gis.admin import OSMGeoAdmin

@admin.register(LocationZone)
class LocationZoneAdmin(OSMGeoAdmin):
    list_display = ("name",)
    default_lon = -70.6693   # Santiago (Chile)
    default_lat = -33.4489
    default_zoom = 12

@admin.register(PointOfInterest)
class PointOfInterestAdmin(OSMGeoAdmin):
    pass