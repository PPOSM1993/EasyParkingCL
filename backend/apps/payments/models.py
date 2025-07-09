from django.db import models
from django.conf import settings

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('completed', 'Completado'),
        ('failed', 'Fallido'),
        ('cancelled', 'Cancelado'),
    ]

    METHOD_CHOICES = [
        ('webpay', 'WebPay'),
        ('mercadopago', 'MercadoPago'),
        ('stripe', 'Stripe'),
        ('cash', 'Efectivo'),
        ('free', 'Gratis'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    session = models.ForeignKey('session.ParkingSession', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, default='CLP')
    method = models.CharField(max_length=20, choices=METHOD_CHOICES, default='webpay')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    receipt_url = models.URLField(blank=True, null=True, help_text="Link al comprobante de pago si aplica")
    description = models.TextField(blank=True, null=True)

    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - ${self.amount} ({self.status})"
