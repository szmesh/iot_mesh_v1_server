from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DevicesConfig(AppConfig):
    name = 'devices'
    verbose_name = _('devicesManager')
    verbose_name_plural = _('devicesManager')
