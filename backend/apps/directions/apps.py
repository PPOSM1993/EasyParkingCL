from django.apps import AppConfig


class DirectionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.directions'

    def ready(self):
        import apps.directions.signlas