#from django.contrib.auth.models import AbstractUser
from django.db import models
"""from django.core.validators import RegexValidator
from django.contrib.postgres.fields import JSONField  # si usas PostgreSQL

class User(AbstractUser):
    rut_regex = RegexValidator(
        regex=r'^\d{7,8}-[\dkK]$',
        message="El RUT debe tener formato 12345678-9 o 12345678-K"
    )
    phone_regex = RegexValidator(
        regex=r'^\+?56\d{9}$',
        message="El número de teléfono debe tener formato +569XXXXXXXX"
    )
    rut = models.CharField(
        max_length=12,
        unique=True,
        validators=[rut_regex],
        help_text="RUT sin puntos, con guion y dígito verificador"
    )
    phone_number = models.CharField(
        max_length=12,
        validators=[phone_regex],
        blank=True,
        null=True
    )
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    ROLE_CHOICES = (
        ('client', 'Cliente'),
        ('operator', 'Operador'),
        ('admin', 'Administrador'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    preferences = JSONField(blank=True, null=True)
    notifications_enabled = models.BooleanField(default=True)
    language = models.CharField(max_length=10, default='es')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.rut})"""
