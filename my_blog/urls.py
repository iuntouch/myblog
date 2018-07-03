# -*- coding: utf-8 -*-
# @ProjectName  : myblog
# @Time    : 2018/7/2 15:18
# @Author  : CHEN HUI   @iuntouch
# @Email   : huch7280@tju.edu.cn
# @File    : urls.py
# @Software: PyCharm


from django.urls import re_path, include
from . import views


urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^register/$', views.register),
    re_path(r'^(.*?)/$', views.blog),
    # re_path(r'^register/$', views.register),
]

