#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018-1-28 19:49
# @File    : urls.py
# @Software: PyCharm Community Edition
__author__ = 'Panda Fang'

''' 定义 learning_logs 的 url 模式'''

from django.urls import path, re_path
from django.contrib.auth.views import login
from . import views

app_name  = 'users'

urlpatterns = [
    path('login/', login, {'template_name':'users/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
