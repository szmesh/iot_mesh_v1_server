import xadmin
from .models import Area
from .AreaAdmin import AreaAdmin


# 将设备数据库注册进管理平台
xadmin.site.register(Area, AreaAdmin)