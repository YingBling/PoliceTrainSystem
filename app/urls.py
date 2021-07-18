# -*- coding: utf-8 -*-
# @Time : 2021/7/16 14:57
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : urls.py
# @Software: PyCharm
from . import views
from django.urls import path, include

urlpatterns = [
    path('users/', include('user.urls'))
]
