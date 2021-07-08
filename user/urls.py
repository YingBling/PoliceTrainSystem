# -*- coding: utf-8 -*-
# @Time : 2021/7/7 11:02
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : urls.py
# @Software: PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_view),  # 注册页面
    path('login', views.login_view),  # 登录页面
    path('logout', views.logout_view)
]
