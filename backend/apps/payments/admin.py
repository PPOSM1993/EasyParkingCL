from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'session',
        'amount',
        'currency',
        'method',
        'status',
        'paid_at',
        'created_at',
    )
    list_filter = ('status', 'method', 'currency', 'created_at')
    search_fields = ('user__username', 'session__id', 'transaction_id')
    ordering = ('-created_at',)

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Información del Usuario y Sesión', {
            'fields': ('user', 'session')
        }),
        ('Detalle del Pago', {
            'fields': (
                'amount', 'currency', 'method', 'status', 'transaction_id', 'receipt_url', 'description'
            )
        }),
        ('Tiempos', {
            'fields': ('paid_at', 'created_at', 'updated_at')
        }),
    )
