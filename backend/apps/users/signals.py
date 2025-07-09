"""from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def usuario_creado(sender, instance, created, **kwargs):
    if created:
        # Aquí puedes enviar un correo, crear una notificación, etc.
        print(f"🟢 Usuario creado: {instance.username} ({instance.email})")
"""