from django.apps import AppConfig


class VehiclesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicles'
    verbose_name = 'Veículos'

    def ready(self):
        import vehicles.signals  # noqa: F401
