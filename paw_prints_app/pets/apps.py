from django.apps import AppConfig


class PetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paw_prints_app.pets'

    def ready(self):
        from paw_prints_app.pets.signals import set_added_by