from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PartnersConfig(AppConfig):
    name = 'partners'
    verbose_name = _('partnersManage')
    verbose_name_plural = _('partnersManage')
