from django.apps import AppConfig

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = 'Замовлення'
    verbose_name_plural = 'Замовлення'

    def ready(self):
        import orders.signals.handlers