# locations/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import LocationZone, PointOfInterest
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=LocationZone)
def location_zone_created(sender, instance, created, **kwargs):
    if created:
        logger.info(f"🟢 Zona creada: {instance.name} (ID: {instance.id})")
    else:
        logger.info(f"🟡 Zona actualizada: {instance.name} (ID: {instance.id})")

@receiver(post_delete, sender=LocationZone)
def location_zone_deleted(sender, instance, **kwargs):
    logger.warning(f"🔴 Zona eliminada: {instance.name} (ID: {instance.id})")

@receiver(post_save, sender=PointOfInterest)
def poi_created(sender, instance, created, **kwargs):
    if created:
        logger.info(f"🟢 POI creado: {instance.name} (ID: {instance.id})")
    else:
        logger.info(f"🟡 POI actualizado: {instance.name} (ID: {instance.id})")

@receiver(post_delete, sender=PointOfInterest)
def poi_deleted(sender, instance, **kwargs):
    logger.warning(f"🔴 POI eliminado: {instance.name} (ID: {instance.id})")
