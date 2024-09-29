import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "athletiq_club.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import athletiq_club.users.signals  # noqa: F401
