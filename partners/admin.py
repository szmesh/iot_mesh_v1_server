import xadmin
from .models import Partners
from .PartnersAdmin import PartnersAdmin


# 将合作商数据库注册进管理平台
xadmin.site.register(Partners, PartnersAdmin)
