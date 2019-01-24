"""iot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from xadmin.plugins import xversion
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
xversion.register_models()

urlpatterns = [
    # default system router
    path('', include('app.urls', namespace='app')),

    # system console
    path('console/', xadmin.site.urls, name='console'),

    # js国际化配置
    # path('jsi18n/', JavaScriptCatalog.as_view(), name='jsi18n'),

    # rest framework config
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
