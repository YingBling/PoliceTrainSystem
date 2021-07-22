# -*- coding: utf-8 -*-
# @Time : 2021/7/9 14:14
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : urls.py
# @Software: PyCharm
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('lesson', views.LessonViewSet)
urlpatterns = [
]
urlpatterns += router.urls
