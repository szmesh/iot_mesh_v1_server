import xadmin
from xadmin import views
from django.utils.translation import gettext_lazy as _


class GlobalSetting(object):
    # 设置后台顶部标题
    site_title = _('companyTitle')

    # 设置后台底部标题
    site_footer = _('company')

    # 设置菜单是收缩形式
    menu_style = "accordion"

    # 自定义菜单
    # def get_site_menu(self):
    #     return [
    #         {
    #             'title': '数据统计与分析',
    #             'perm': self.get_model_perm(Service, 'view'),
    #             'icon': 'fa fa-bar-chart-o',
    #             'menu': (
    #                 {
    #                     'title': '区域合作商分布',
    #                     'url': '',
    #                     'perm': self.get_model_perm(Service, 'view'),
    #                     'icon': 'fa fa-cny'
    #                 },
    #                 {
    #                     'title': '区域合作商分布',
    #                     'url': '',
    #                     'perm': self.get_model_perm(Service, 'view'),
    #                     'icon': 'fa fa-cny'
    #                 }
    #             )
    #         }
    #     ]


class ThemeSetting(object):
    """
    主题设置类
    """
    # 启用主题管理器
    enable_themes = True

    # 使用主题
    use_bootswatch = True


# 将配置注入到xadmin
xadmin.site.register(views.CommAdminView, GlobalSetting)
# 注册主题设置
xadmin.site.register(views.BaseAdminView, ThemeSetting)
