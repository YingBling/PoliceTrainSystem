# -*- coding: utf-8 -*-
# @Time : 2021/9/27 17:50
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : urls.py
# @Software: PyCharm
from django.urls import re_path
from . import views
urlpatterns = [
    re_path('upload/',views.UploadFile.as_view())
]
