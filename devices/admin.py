import xadmin
from .models import Devices, DevicesType
from .DevicesAdmin import DevicesAdmin
from .DevicesTypeAdmin import DevicesTypeAdmin


# 将设备数据库注册进管理平台
xadmin.site.register(Devices, DevicesAdmin)
xadmin.site.register(DevicesType, DevicesTypeAdmin)
