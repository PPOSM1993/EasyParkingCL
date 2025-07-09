from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from datetime import datetime

CURRENT_YEAR = datetime.now().year

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = (
        ('car', 'Automóvil'),
        ('motorcycle', 'Motocicleta'),
        ('suv', 'SUV'),
        ('truck', 'Camión'),
        ('van', 'Furgoneta'),
        ('electric', 'Eléctrico'),
        ('other', 'Otro'),
    )

    COLOR_CHOICES = (
        ('white', 'Blanco'),
        ('black', 'Negro'),
        ('gray', 'Gris'),
        ('blue', 'Azul'),
        ('red', 'Rojo'),
        ('silver', 'Plateado'),
        ('green', 'Verde'),
        ('yellow', 'Amarillo'),
        ('other', 'Otro'),
    )

    ENGINE_TYPE_CHOICES = (
        ('gasoline', 'Gasolina'),
        ('diesel', 'Diésel'),
        ('electric', 'Eléctrico'),
        ('hybrid', 'Híbrido'),
        ('other', 'Otro'),
    )

    license_plate_regex = RegexValidator(
        regex=r'^[A-Z]{2,3}-?\d{2,3}$',
        message="La patente debe tener un formato como AB123 o ABC-123"
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vehicles')
    license_plate = models.CharField(max_length=10, unique=True, validators=[license_plate_regex])
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1950),
            MaxValueValidator(CURRENT_YEAR + 1)
        ]
    )
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES, default='car')
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPE_CHOICES, default='gasoline')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='white')
    mileage = models.PositiveIntegerField(default=0, help_text="Kilometraje actual en km")
    insurance_expiration = models.DateField(blank=True, null=True)
    technical_revision_date = models.DateField(blank=True, null=True)
    is_electric = models.BooleanField(default=False)
    image = models.ImageField(upload_to='vehicle_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"

    def __str__(self):
        return f"{self.license_plate} - {self.brand} {self.model}"
