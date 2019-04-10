from django.utils.translation import gettext_lazy as _


class DevicesAdmin(object):
    """
    设备管理的控制主类
    """

    # 设置菜单的图标
    model_icon = 'fa fa-suitcase'

    # 默认显示的列
    list_display = ('name', 'code',)
    list_display_links = ('code',)

    # 查询出来的列
    list_filter = ('uid', 'name', 'code', 'modify_time')

    # 过滤查询配置
    search_fields = ('name', 'code')

    # bookmark自定义
    # list_bookmarks = [{
    #     'title': "Female",  # 书签的名称, 显示在书签菜单中
    #     'query': {'name': True, 'code': True},  # 过滤参数, 是标准的 queryset 过滤
    #     'order': "-uid",  # 排序参数
    #     'cols': ('name', 'code'),  # 显示的列
    #     'search': 'name'  # 搜索参数, 指定搜索的内容
    # }]

    # 导出的文件类型配置
    list_export = ('xls', 'xml', 'json')

    # 图表显示
    data_charts = {
        "user_count": {
            'title': _('Devices Type Report'),
            'x-field': 'modify_time',
            'y-field': 'name',
            'order': ('modify_time',)},
        # "avg_count": {
        #     "title": u"Avg Report",
        #     "x-field": "date",
        #     "y-field": ("avg_count",),
        #     "order": ("modify_time",)}
    }

    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (180, 300)

    # 添加记录详情的跳转功能
    show_detail_fields = ['code']

    # 开启数据即时修改功能
    list_editable = ['name', 'code']

    # 不显示的字段
    list_exclude = ['uid', 'create_time']

    # 设备下拉选择项通过ajax动态拉取，避免下拉选择项数据过大
    relfield_style = 'fa-ajax'

    # 保存数据的时候，自动添加一些后台数据
    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()
