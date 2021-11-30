from django.apps import AppConfig


class FacesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faces_app'

    def ready(self):
        import faces_app.signals
