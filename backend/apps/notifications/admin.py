from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'type',
        'status',
        'is_read',
        'created_at',
        'sent_at',
        'read_at'
    )
    list_filter = (
        'type',
        'status',
        'is_read',
        'created_at',
        'sent_at',
        'read_at'
    )
    search_fields = (
        'user__username',
        'title',
        'message',
    )
    readonly_fields = (
        'created_at',
        'sent_at',
        'read_at',
    )
    ordering = ('-created_at',)

    fieldsets = (
        ('Contenido', {
            'fields': ('user', 'title', 'message', 'type', 'status', 'is_read')
        }),
        ('Relaciones', {
            'fields': ('related_session', 'related_suggestion', 'related_vehicle', 'related_parking')
        }),
        ('Tiempos', {
            'fields': ('sent_at', 'read_at', 'created_at')
        }),
    )
