from django.contrib import admin
from .models import Suggestion

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'destination_address',
        'recommended_parking',
        'method',
        'score',
        'created_at',
    )
    list_filter = ('method', 'created_at')
    search_fields = ('user__username', 'destination_address', 'recommended_parking__name')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    fieldsets = (
        ('Usuario y Destino', {
            'fields': ('user', 'destination_address', 'destination_lat', 'destination_lng')
        }),
        ('Recomendación Generada', {
            'fields': ('recommended_parking', 'method', 'score', 'notes')
        }),
        ('Relación con sesión', {
            'fields': ('session',)
        }),
        ('Tiempos del sistema', {
            'fields': ('created_at',)
        }),
    )
