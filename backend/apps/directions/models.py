from django.contrib.gis.db import models as gis_models
from django.db import models
from django.conf import settings
from apps.locations.models import LocationZone
from django.utils.translation import gettext_lazy as _


class RouteRequest(models.Model):
    """
    Representa una solicitud de ruta generada por el usuario.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='route_requests'
    )
    origin = gis_models.PointField()
    destination = gis_models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Route Request")
        verbose_name_plural = _("Route Requests")

    def __str__(self):
        return f"RouteRequest #{self.id} by {self.user}"


class RecommendedZone(models.Model):
    """
    Representa una zona recomendada como destino de estacionamiento.
    """
    route_request = models.ForeignKey(
        RouteRequest,
        on_delete=models.CASCADE,
        related_name='recommended_zones'
    )
    zone = models.ForeignKey(
        LocationZone,
        on_delete=models.CASCADE,
        related_name='recommendations'
    )
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Recommended Zone")
        verbose_name_plural = _("Recommended Zones")

    def __str__(self):
        return f"Recommendation: Zone #{self.zone_id} for Request #{self.route_request_id}"
