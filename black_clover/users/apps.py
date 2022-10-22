from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "black_clover.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import black_clover.users.signals  # noqa F401
        except ImportError:
            pass
