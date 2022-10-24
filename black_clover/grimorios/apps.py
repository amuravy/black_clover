from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GrimoriosConfig(AppConfig):
    name = "black_clover.grimorios"
    verbose_name = _("Grimorios")

    def ready(self):
        try:
            import black_clover.grimorios.signals  # noqa.
        except ImportError as e:
            raise Exception(e)
