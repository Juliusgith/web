# apps.py

from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'pss'

    def ready(self):
        import pss.signals  # Replace 'your_app' with the name of your app
