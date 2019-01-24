class PartnersAdmin(object):
    """
    合作商的控制主类
    """

    # 设置菜单的图标
    model_icon = 'fa fa-home'

    # 默认显示的列
    list_display = ('name', 'cusc_code', 'legal_person', 'phone', 'email', 'address', 'get_partners_count')
    list_display_links = ('cusc_code',)

    # 查询出来的列
    list_filter = ('name', 'cusc_code', 'legal_person', 'phone', 'email', 'address')

    # 过滤查询配置
    search_fields = ('name', 'cusc_code', 'legal_person')

    # 导出的文件类型配置
    list_export = ('xls', 'xml', 'json')

    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (180, 300)

    # 添加记录详情的跳转功能
    show_detail_fields = ['name']

    # 开启数据即时修改功能
    list_editable = ['name']

    # 不显示的字段
    list_exclude = ['uid', 'create_time']

    # 设备下拉选择项通过ajax动态拉取，避免下拉选择项数据过大
    relfield_style = 'fa-ajax'

    # 保存数据的时候，自动添加一些后台数据
    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()
