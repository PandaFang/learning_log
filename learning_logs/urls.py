#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018-1-28 15:32
# @File    : urls.py
# @Software: PyCharm Community Edition
__author__ = 'Panda Fang'
''' 定义 learning_logs 的 url 模式'''

from django.urls import path, re_path
from learning_logs import views

app_name  = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    re_path('topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    re_path('new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path('edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

