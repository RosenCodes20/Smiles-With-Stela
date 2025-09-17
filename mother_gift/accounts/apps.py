from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mother_gift.accounts'

    def ready(self):
        import mother_gift.accounts.signals