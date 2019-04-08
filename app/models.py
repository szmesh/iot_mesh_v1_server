from django.db import models
from django.conf import settings
from area.models import CountryArea, ProvinceArea, CityArea, ZoneArea
from partners.models import Partners
from django.utils.translation import gettext_lazy as _


# 数据库记录状态选择项
STATUS_RECORD_CHOICE = (
  ('1000', _('activeStatus')),
  ('1001', _('disableStatus')),
  ('1002', _('deleteStatus'))
)


class UserProfile(models.Model):
  """
  用户基本信息
  """
  gender_choices = (
    ('1000', _('male')),
    ('2000', _('female')),
    ('3000', _('secretGender'))
  )

  degrees_choices = (
    (_('Bachelor'), (
      ('1000', _('Bachelor Degree')),
      ('1001', _('Bachelor Degree of Engineering')),
      ('1002', _('Bachelor Degree of Science')),
      ('1003', _('Bachelor Degree of Art')),
      ('1004', _('Bachelor of Education')),
      ('1005', _('Bachelor of Business Adm'))
    )),
    (_('Master'), (
      ('2000', _('Master Eegree')),
      ('2001', _('Master of Science')),
      ('2002', _('Master of Engineering')),
      ('2003', _('Master of Business Administration'))
    )),
    (_('Doctor'), (
      ('3000', _('Doctor Degree')),
      ('3001', _('Doctor of Philosophy'))
    )),
  )

  uid = models.AutoField(_('userProfileId'), primary_key=True)
  alias = models.CharField(_('alias'), max_length=32, default='', null=True, blank=True)
  birthday = models.DateField(null=True, blank=True, verbose_name=_('birthday'))
  gender = models.CharField(max_length=4, choices=gender_choices, default="3000",
                            verbose_name=_('gender'))
  nation = models.CharField(null=True, blank=True, max_length=32, verbose_name=_('nation'), help_text=_('helpTextNation'))
  degrees = models.CharField(choices=degrees_choices, null=True, blank=True, max_length=15, verbose_name=_('degrees'), help_text=_('helpTextDegrees'))
  id_number = models.CharField(null=True, blank=True, max_length=32, verbose_name=_('idNumber'), help_text=_('helpTextIdNumber'))
  phone_zone = models.CharField(null=True, blank=True, max_length=8, verbose_name=_('phoneZone'))
  phone = models.CharField(null=True, blank=True, max_length=16, verbose_name=_('phone'))
  mobile = models.CharField(null=True, blank=True, max_length=17, verbose_name=_('mobile'))
  country = models.ForeignKey(CountryArea, related_name='country_user', on_delete=models.CASCADE,
                              verbose_name=_('country'), null=True, blank=True)
  province = models.ForeignKey(ProvinceArea, related_name='province_user', on_delete=models.CASCADE,
                               verbose_name=_('province'), null=True, blank=True)
  city = models.ForeignKey(CityArea, related_name='city_user', on_delete=models.CASCADE,
                           verbose_name=_('city'), null=True, blank=True)
  zone = models.ForeignKey(ZoneArea, related_name='zone_user', on_delete=models.CASCADE,
                           verbose_name=_('zone'), null=True, blank=True)
  address = models.CharField(null=True, blank=True, max_length=512, verbose_name=_('address'), help_text=_('address'))
  avatar = models.ImageField(max_length=200, upload_to="users/images/headpicture/%Y/%m", null=True,
                                   blank=True, verbose_name=_('Avatar'))
  partners_user = models.ManyToManyField(Partners, verbose_name=_('partners'), null=True, blank=True)

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_('user'), editable=False)
  create_time = models.DateTimeField(_('createTime'), auto_now=True, editable=False)
  modify_time = models.DateTimeField(_('modifyTime'), auto_now_add=True, editable=False)
  status = models.IntegerField(choices=STATUS_RECORD_CHOICE, default=1000, editable=False)

  open_id_wechat = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('openIdWechat'))
  union_id_wechat = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('unionIdWechat'))
  open_id_ali = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('openIdAli'))

  def __str__(self):
    return self.name

  class Meta:
    # 默认排序
    ordering = ['uid']

    verbose_name = _('userProfile')
    verbose_name_plural = _('userProfile')
