from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'user', 'brand', 'model', 'year', 'vehicle_type', 'engine_type', 'is_electric', 'insurance_expiration')
    list_filter = ('vehicle_type', 'engine_type', 'is_electric', 'year', 'color')
    search_fields = ('license_plate', 'brand', 'model', 'user__username', 'user__rut')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('user', 'license_plate', 'brand', 'model', 'year')
        }),
        ('Detalles del Vehículo', {
            'fields': ('vehicle_type', 'engine_type', 'color', 'mileage', 'is_electric')
        }),
        ('Documentación', {
            'fields': ('insurance_expiration', 'technical_revision_date')
        }),
        ('Otros', {
            'fields': ('image', 'created_at', 'updated_at')
        }),
    )
