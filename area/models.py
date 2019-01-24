from django.db import models
from django.conf import settings
from .AreaAdmin import AreaAdmin
from django.utils.translation import gettext_lazy as _


class Area(models.Model):
  """
  地址管理对象
  """
  LEVEL_CHOICE = (
    (1000, _('continent')),
    (2000, _('country')),
    (3000, _('province')),
    (4000, _('city')),
    (5000, _('zone')),
  )

  name_field_error_message = {
    'null': _('nullEMAreaName'),
    'blank': _('blankEMAreaName'),
    'invalid': _('invalidEMAreaName'),
    'invalid_choice': _('invalidChoiceEMAreaName'),
    'unique': _('uniqueEMAreaName')
  }

  level_field_error_message = {
    'null': _('nullEMLevel'),
    'blank': _('blankEMLevel'),
    'invalid': _('invalidEMLevel'),
    'invalid_choice': _('invalidChoiceEMLevel'),
    'unique': _('uniqueEMLevel')
  }

  uid = models.AutoField(_('areaId'), primary_key=True)
  name = models.CharField(_('areaName'), max_length=512, blank=False, null=False, help_text=_('helpTextAreaName'), error_messages=name_field_error_message)
  code = models.CharField(_('areaCode'), unique=True, max_length=256, blank=False, null=False)
  level = models.IntegerField(_('areaLevel'), default=1000, choices=LEVEL_CHOICE, help_text=_('helpTextLevel'), error_messages=level_field_error_message)
  parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('parent'))
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_('user'), editable=False)
  create_time = models.DateTimeField(_('createTime'), auto_now=True, editable=False)
  modify_time = models.DateTimeField(_('modifyTime'), auto_now_add=True, editable=False)

  def __str__(self):
    return self.name

  class Meta:
    # 默认排序
    ordering = ['uid']

    verbose_name = _('area')
    verbose_name_plural = _('area')


class ContinentArea(Area):
  """
  单独获取洲数据
  """

  class Meta:
    verbose_name = _('continent')
    verbose_name_plural = verbose_name
    proxy = True  # 设置为True 否则会重新注册一张数据表

  def queryset(self):
    qs = super(AreaAdmin, self).queryset()
    qs = qs.filter(level = 1000)
    return qs


class CountryArea(Area):
  """
  单独获取国家数据
  """

  class Meta:
    verbose_name = _('country')
    verbose_name_plural = verbose_name
    proxy = True  # 设置为True 否则会重新注册一张数据表

  def queryset(self):
    qs = super(AreaAdmin, self).queryset()
    qs = qs.filter(level = 2000)
    return qs


class ProvinceArea(Area):
  """
  单独获取省数据
  """

  class Meta:
    verbose_name = _('province')
    verbose_name_plural = verbose_name
    proxy = True  # 设置为True 否则会重新注册一张数据表

  def queryset(self):
    qs = super(AreaAdmin, self).queryset()
    qs = qs.filter(level = 3000)
    return qs


class CityArea(Area):
  """
  单独获取市数据
  """

  class Meta:
    verbose_name = _('city')
    verbose_name_plural = verbose_name
    proxy = True  # 设置为True 否则会重新注册一张数据表

  def queryset(self):
    qs = super(AreaAdmin, self).queryset()
    qs = qs.filter(level = 4000)
    return qs


class ZoneArea(Area):
  """
  单独获取市数据
  """

  class Meta:
    verbose_name = _('zone')
    verbose_name_plural = verbose_name
    proxy = True  # 设置为True 否则会重新注册一张数据表

  def queryset(self):
    qs = super(AreaAdmin, self).queryset()
    qs = qs.filter(level = 5000)
    return qs
