from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from partners.models import Partners


class DevicesType(models.Model):
    """
    设备类型信息表
    """
    uid = models.AutoField(_('deviceTypeId'), primary_key=True)
    name = models.CharField(_('devicesType'), max_length=512, blank=False, null=False)
    des = models.CharField(_('des'), max_length=1024, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False,
                                    verbose_name=_('user'), editable=False)
    create_time = models.DateTimeField(_('createTime'), auto_now=True, editable=False)
    modify_time = models.DateTimeField(_('modifyTime'), auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        # 默认排序
        ordering = ['uid']

        verbose_name = _('devicesType')
        verbose_name_plural = _('devicesType')


class Devices(models.Model):
    """
    设备基本信息表
    """
    uid = models.AutoField(_('deviceId'), primary_key=True)
    name = models.CharField(_('deviceName'), max_length=512, blank=False, null=False)
    code = models.CharField(_('deviceCode'), max_length=256, blank=False, null=False)
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE, verbose_name=_('partner'))
    type = models.ForeignKey(DevicesType, on_delete=models.CASCADE, verbose_name=_('devicesType'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False,
                                    verbose_name=_('user'), editable=False)
    create_time = models.DateTimeField(_('createTime'), auto_now=True, editable=False)
    modify_time = models.DateTimeField(_('modifyTime'), auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        # 默认排序
        ordering = ['uid']

        verbose_name = _('device')
        verbose_name_plural = _('device')
