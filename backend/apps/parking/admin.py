from django.contrib import admin
from .models import Region, City, Parking

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']
    list_filter = ['region']
    search_fields = ['name']

@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'region', 'type', 'price_per_hour', 'available_spaces', 'is_active', 'owner']
    list_filter = ['type', 'region', 'city', 'is_active']
    search_fields = ['name', 'address', 'description']
    ordering = ['-available_spaces']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'address', 'latitude', 'longitude', 'type', 'price_per_hour')
        }),
        ('Ubicación', {
            'fields': ('region', 'city')
        }),
        ('Disponibilidad', {
            'fields': ('total_spaces', 'available_spaces', 'is_active')
        }),
        ('Propietario y fechas', {
            'fields': ('owner', 'created_at', 'updated_at')
        }),
    )