from rest_framework import serializers
from .models import Payment
from datetime import datetime
from decimal import Decimal

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'user',
            'session',
            'amount',
            'currency',
            'method',
            'status',
            'transaction_id',
            'receipt_url',
            'description',
            'paid_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate_amount(self, value):
        if value <= Decimal('0.00'):
            raise serializers.ValidationError("El monto debe ser mayor a 0.")
        return round(value, 2)

    def validate_currency(self, value):
        if value.upper() not in ['CLP', 'USD', 'EUR']:
            raise serializers.ValidationError("Moneda no soportada. Usa CLP, USD o EUR.")
        return value.upper()

    def validate_status(self, value):
        allowed = ['pending', 'completed', 'failed', 'cancelled']
        if value not in allowed:
            raise serializers.ValidationError(f"Estado inválido. Usa uno de: {allowed}")
        return value

    def validate_paid_at(self, value):
        if value and value > datetime.now():
            raise serializers.ValidationError("La fecha de pago no puede ser en el futuro.")
        return value

    def validate(self, data):
        method = data.get("method")
        receipt = data.get("receipt_url")

        if method in ['webpay', 'mercadopago', 'stripe'] and not receipt:
            raise serializers.ValidationError("Debe proporcionar un comprobante (receipt_url) para pagos online.")

        return data
