from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'blogit.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import blogit.apps.authentication.signals

default_app_config = 'blogit.apps.authentication.AuthenticationAppConfig'