from django.apps import AppConfig

class ArticlesAppConfig(AppConfig):
    name = 'blogit.apps.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import blogit.apps.articles.signals


default_app_config = 'blogit.apps.articles.ArticlesAppConfig'