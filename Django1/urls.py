"""Django1 URL Configuration

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
from . import settings # 为了加载静态文件
from django.views.static import serve
from django.conf.urls.static import static # 为了加载静态文件
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path, include, register_converter
from my_app1 import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

# 若url中出现重复的部分，可以使用extra_patterns进行聚合
extra_patterns = [
    path('path1/', views.path1),
    path('path2/', views.path2),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuDatabase/', include('stuDatabase.urls')),
    path('l_session/',include('l_session.urls')),
    path('auth/',include('l_auth.urls')),
    path('uploadFile/',include('uploadFile.urls')),
    path('blog/',include('blog.urls')),
    path('polls/', include('polls.urls')),
    # 将匹配到的polls/阶段，并将polls/之后的字符串发送到polls app中的urls.py进行路由匹配 这就支持了
    # 即插即用。因为投票应用有它自己的 URLconf( polls/urls.py )，他们能够被放在 "/polls/" ， "/fun_polls/" ，"/content/polls/"，
    # 或者其他任何路径下，这个应用都能够正常工作。  即将此语句放入其他urls中都能进行匹配
    path('test', views.test_view),  # 编写路由规则 引导到my_app1中views的业务逻辑中
    path('login', views.login_view),
    path('', views.index_view),
    path('articles/<int:year>/<int:month>/<slug:slug>', views.article_archive3),
    # path 中有 str（除/之外的其他字符串） int slug（匹配字母数字下划线等） uuid path（str+/）这几种类型转换
    # path 是在2.0之后使用的方法，不再需要使用正则表达式来写 url中的内容直接表示以xx开始以xx结束
    # re_path是在2.0 之前使用的方法
    re_path(r'articles/2018/$', views.article_2018),  # 未设置开头，因此只要结尾为articles/2018/即可匹配
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.article_archive),  # 通过year=2018 的形式传入函数，因此函数参数必须定义year
    re_path(r'^article/([0-9]{4})/([0-9]{2})/$', views.article_archive2),  # 不通过key=xx的形式传入函数，因此函数的参数名可自定义
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$',views.article_archive3),  # 匹配任意字符

    path('convert/<yyyy:year>/', views.convert_test),  # 使用自定义的格式转换器
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # 配置media路径访问接口
]
# print(urlpatterns)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)  # 为了加载静态文件
# urlpatterns += static(settings.STATIC_URL, document_root='/blog/static')  # 为了加载静态文件
# 这个加在末尾，注意，是末尾，urlpatterns 括号外
# print(urlpatterns)
