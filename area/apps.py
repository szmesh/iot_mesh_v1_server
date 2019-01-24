from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AreaConfig(AppConfig):
    name = 'area'
    verbose_name = _('areaManager')
    verbose_name_plural = _('areaManager')
