"""import re
from rest_framework import serializers
from datetime import date
from .models import User

# Función para validar el dígito verificador del RUT
def validar_rut(rut: str) -> bool:
    rut = rut.upper().replace("-", "").replace(".", "")
    if len(rut) < 2:
        return False

    cuerpo = rut[:-1]
    dv = rut[-1]

    suma = 0
    multiplo = 2

    for digit in reversed(cuerpo):
        suma += int(digit) * multiplo
        multiplo = 3 if multiplo == 7 else multiplo + 1

    resto = suma % 11
    dv_calculado = 11 - resto

    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado == 10:
        dv_calculado = "K"
    else:
        dv_calculado = str(dv_calculado)

    return dv_calculado == dv

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'rut', 'phone_number',
            'first_name', 'last_name', 'address', 'profile_image',
            'role', 'date_of_birth', 'is_verified',
            'preferences', 'notifications_enabled', 'language'
        ]
        read_only_fields = ['id', 'is_verified']

    def validate_rut(self, value):
        rut_limpio = value.replace(".", "").replace("-", "").upper()
        if not validar_rut(rut_limpio):
            raise serializers.ValidationError("RUT inválido")
        return value

    def validate_phone_number(self, value):
        if value and not re.match(r'^\+?56\d{9}$', value):
            raise serializers.ValidationError("El número de teléfono debe tener formato +569XXXXXXXX")
        return value

    def validate_date_of_birth(self, value):
        if value:
            today = date.today()
            age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
            if age < 18:
                raise serializers.ValidationError("Debe ser mayor de 18 años para registrarse.")
        return value

    def validate_email(self, value):
        user = self.instance
        if User.objects.filter(email=value).exclude(pk=user.pk if user else None).exists():
            raise serializers.ValidationError("El email ya está registrado.")
        return value
"""