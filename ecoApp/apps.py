from django.apps import AppConfig


class EcoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecoApp'


    def ready(self):
        import ecoApp.signals
