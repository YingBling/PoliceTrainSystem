# -*- coding: utf-8 -*-
# @Time : 2021/10/9 16:00
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : urls.py
# @Software: PyCharm
from django.urls import re_path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('chapter', chapterViewSet)
urlpatterns = [
]
urlpatterns += router.urls
