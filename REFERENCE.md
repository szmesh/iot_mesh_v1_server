## 教程
#### 官方
- [xadmin官方](https://xadmin.readthedocs.io/en/latest/quickstart.html)
- [xadmin github](https://github.com/sshwsfc/xadmin/tree/django2)
##
#### django.utils models
- [models详解](https://www.cnblogs.com/baishuchao/p/9291344.html)
##
#### User model扩展
- [拓展 User 模型](https://www.zmrenwu.com/post/31/)
##
#### xadmin注入参数
- BaseAdminView : 所有 AdminView 的基础类，注册在该 View 上的插件可以影响所有的 AdminView
- CommAdminView : 用户已经登陆后显示的 View，也是所有登陆后 View 的基础类。该 View主要作用是创建了 Xadmin 的通用元素，例如：系统菜单，用户信息等。插件可以通过注册该 View 来修改这些信息。
- ModelAdminView : 基于 Model 的 AdminView 的基础类，注册的插件可以影响所有基于 Model 的 View。
- ListAdminView : Model 列表页面 View。
- ModelFormAdminView : Model 编辑页面 View。
- CreateAdminView : Model 创建页面 View。
- UpdateAdminView : Model 修改页面 View。
- DeleteAdminView : Model 删除页面 View。
- DetailAdminView : Model 详情页面 View。
##
#### xadmin
- [django2使用xadmin - 1](https://www.jianshu.com/p/9b3bfe934511)
- [django2使用xadmin - 2](https://www.jianshu.com/p/4ac3c8e096cb)
---
- [CNBLogs - 2](https://www.cnblogs.com/wumingxiaoyao/p/6945769.html)
---
- [代码规范工具](https://blog.csdn.net/zong596568821xp/article/details/84251616)
---
- [第一章](https://blog.csdn.net/shaququ/article/details/77253198)
- [第二章](https://blog.csdn.net/shaququ/article/details/77253252)
##
#### 国际化
- [官方i18n](https://docs.djangoproject.com/zh-hans/2.1/topics/i18n/translation/)
- [官方js i18n](https://docs.djangoproject.com/en/2.1/topics/i18n/translation/#django.views.i18n.JavaScriptCatalog)
- [配置国际化](https://www.cnblogs.com/fuhuixiang/p/4146861.html)
- 创建国际化文件step
  1. 在对应app目录创建locale目录
  2. 按此格式<language>/LC_MESSAGES/创建好欲支持的语言目录
  3. 转到app目录下执行django-admin.py makemessages --all命令， 把所有标记的翻译符号导出为po文件
  4. 打开各个<language>/LC_MESSAGES/django.po文件，把符号翻译为对应的本地言语
  5. 执行django-admin.py compilemessages把po文件编译为mo文件
  6. 这两个命令一定要在locale所在的app目录下执行。
  7. 错误： Make sure you have GNU gettext tools 0.15 or newer installed
  8. 安装gettext: brew install gettext
  9. 安装gettext后：brew link gettext --force
  10. 提示/usr/local/share/doc is not writable.就赋于当前用户权限：sudo chown -R admin /usr/local/share