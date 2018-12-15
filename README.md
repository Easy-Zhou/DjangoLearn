# 本项目为第一个django项目
- 创建项目的命令 django-admin startproject project_name
- 创建此项目的app命令 django-admin startapp app_name
- 初始的文件目录以及相关的用处：
```
my_test_web 
├── README.md
├── manage.py
├── my_app1
│   ├── __init__.py
│   ├── admin.py  # 数据库后台
│   ├── apps.py  # django 把项目和app关联起来的文件
│   ├── migrations  # 和数据库相关
│   │   └── __init__.py
│   ├── models.py  # 数据库操作相关
│   ├── tests.py  # 单元测试模块
│   └── views.py  # 业务逻辑代码 -- 主要改动处
└── my_test_web
    ├── __init__.py
    ├── settings.py  # 程序的配置文件
    ├── urls.py  # 程序的路由系统，即：URL和处理其函数的对应关系
    └── wsgi.py  # 指定框架的wsgi
```