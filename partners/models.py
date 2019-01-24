from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from area.models import CountryArea, ProvinceArea, CityArea, ZoneArea


class Partners(models.Model):
    """
    合作商信息表
    """
    uid = models.AutoField(_('partnersId'), primary_key=True)
    name = models.CharField(_('partnersName'), max_length=512, blank=False, null=False)
    cusc_code = models.CharField(_('cuscCode'), max_length=128, blank=False, null=False)
    legal_person = models.CharField(_('legalPerson'), max_length=128, blank=False, null=False)
    phone_zone = models.CharField(_('phoneZone'), max_length=8, blank=False, null=False)
    phone = models.CharField(_('phone'), max_length=64, blank=False, null=False)
    mobile = models.CharField(_('mobile'), max_length=64, blank=True, null=True)
    email = models.CharField(_('email'), max_length=128, blank=False, null=False)
    country = models.ForeignKey(CountryArea, related_name='country', db_column='country', on_delete=models.CASCADE,
                                verbose_name=_('country'))
    province = models.ForeignKey(ProvinceArea, related_name='province', db_column='province', on_delete=models.CASCADE,
                                 verbose_name=_('province'))
    city = models.ForeignKey(CityArea, related_name='city', db_column='city', on_delete=models.CASCADE,
                             verbose_name=_('city'))
    zone = models.ForeignKey(ZoneArea, related_name='zone', db_column='zone', on_delete=models.CASCADE,
                             verbose_name=_('zone'))
    address = models.CharField(_('address'), max_length=512, blank=False, null=False)
    postal_code = models.IntegerField(_('postalCode'), blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False,
                                    verbose_name=_('user'), editable=False)
    create_time = models.DateTimeField(_('createTime'), auto_now=True, editable=False)
    modify_time = models.DateTimeField(_('modifyTime'), auto_now_add=True, editable=False)

    # 自定义字段
    def get_partners_count(self):
        return 5
    get_partners_count.short_description = _('totalPartnersCount')

    def __str__(self):
        return self.name

    class Meta:
        # 默认排序
        ordering = ['uid']

        verbose_name = _('partners')
        verbose_name_plural = _('partners')
