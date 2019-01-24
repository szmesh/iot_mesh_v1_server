from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('welcome/', views.welcome_info, name='welcome_info'),
]
