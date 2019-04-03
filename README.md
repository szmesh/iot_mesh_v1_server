## Mesh iot Platform

### 首次运行代码
1. 安装依赖
```sh
pip install -r requirements.txt
```
2. 在每个子app中添加migrations package，必须带有_init_.py文件，特别是xadmin下面，不然无法创建数据库对象
3. 参照[model后操作数据库]，创建数据库表
4. 参照[参考 -> 国际化](/REFERENCE.md)，创建国际化的本地文件
5. 参照[创建管理员]，添加管理员
6. 运行系统
```sh
python manage.py runserver 8000
```

### 创建管理员
```sh
python manage.py createsuperuser
python manage.py createsuperuser --email admin@example.com --username admin
```

### 创建一个新的app
```sh
python manage.py startapp <app name>
```

### 更新model后操作数据库，更新数据库表
> model里面的属性名字不能和任何一个app名字一样，否则会无法创建数据表
```sh
python manage.py makemigrations
python manage.py migrate
```

### 更改菜单图标
1. 在对应的app中的admin文件，添加xxxAdmin class
2. 添加图标配置：model_icon = 'fa fa-home'
[font更多图标](http://fontawesome.dashgame.com/)
[制作图标](https://fontawesome.com/?from=io#contribute)
3. 注册到xadmin中: xadmin.site.register(Devices, DevicesAdmin)

### 虚拟环境
1. 在当前目录创建
```sh
python -m venv venv
```
2. 激活虚拟环境
```sh
source <venv>/bin/activate
```
3. 退出虚拟环境
```sh
deactivate
```

### [Change Log/Release Note](/CHANGELOG.md)

### [参考](/REFERENCE.md)
