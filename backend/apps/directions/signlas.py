from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import RouteRequest, RecommendedZone
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=RouteRequest)
def log_route_request_created(sender, instance, created, **kwargs):
    if created:
        logger.info(f"🚗 Nueva ruta solicitada por {instance.user.email} hacia {instance.destination_address} (ID: {instance.id})")


@receiver(post_delete, sender=RouteRequest)
def log_route_request_deleted(sender, instance, **kwargs):
    logger.info(f"🗑️ Ruta eliminada: ID {instance.id} del usuario {instance.user.email}")


@receiver(post_save, sender=RecommendedZone)
def log_zone_recommendation_created(sender, instance, created, **kwargs):
    if created:
        logger.info(f"📍 Zona recomendada: {instance.zone} para ruta {instance.route_request.id} (Primaria: {instance.is_primary})")


@receiver(post_delete, sender=RecommendedZone)
def log_zone_recommendation_deleted(sender, instance, **kwargs):
    logger.info(f"🗑️ Zona recomendada eliminada para ruta {instance.route_request.id} (Zona: {instance.zone})")
