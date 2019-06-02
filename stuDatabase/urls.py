#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 01:57
# @Author  : zhou
# @File    : urls
# @Software: PyCharm
# @Description: 


from django.urls import path
from . import views

urlpatterns = [
    path('operate_database',views.operate_database),
]