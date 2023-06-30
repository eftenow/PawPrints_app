from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paw_prints_app.accounts'

    def ready(self):
        from paw_prints_app.accounts.signals import create_profile
