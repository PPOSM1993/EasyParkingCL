from django.contrib import admin
from .models import ParkingSession

@admin.register(ParkingSession)
class ParkingSessionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'vehicle',
        'parking_space',
        'status',
        'destination_address',
        'start_time',
        'end_time',
        'created_at',
    )
    list_filter = ('status', 'created_at', 'start_time', 'end_time')
    search_fields = ('user__username', 'user__rut', 'destination_address', 'parking_space__name')
    ordering = ('-created_at',)

    # 👇 Solo campos editables aquí
    fields = (
        'user',
        'vehicle',
        'parking_space',
        'destination_address',
        'status',
        'location_snapshot',
        'ai_recommendation_id',
    )

    # 👇 Solo lectura para vista de detalle (no los pongas en `fields`)
    readonly_fields = ('start_time', 'end_time', 'created_at', 'updated_at')
