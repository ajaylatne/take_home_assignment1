from django.apps import AppConfig


class CrudOperationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crud_operations'

    def ready(self):
        import crud_operations.signals  # Import the signals file
