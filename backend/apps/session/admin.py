from django.contrib import admin
from .models import ParkingSession

@admin.register(ParkingSession)
class ParkingSessionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'destination_address',
        'parking_space',
        'status',
        'start_time',
        'end_time',
        'created_at',
    )
    list_filter = ('status', 'start_time', 'end_time', 'created_at')
    search_fields = ('user__username', 'user__rut', 'destination_address', 'parking_space__name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Usuario y Destino', {
            'fields': ('user', 'destination_address', 'destination_lat', 'destination_lng')
        }),
        ('Espacio de Estacionamiento', {
            'fields': ('parking_space',)
        }),
        ('Estado de la Sesión', {
            'fields': ('status', 'start_time', 'end_time')
        }),
        ('Fechas del sistema', {
            'fields': ('created_at', 'updated_at')
        }),
    )
