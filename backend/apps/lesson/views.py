# -*- coding: utf-8 -*-
# @Time : 2021/10/9 16:17
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : views.py
# @Software: PyCharm
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


class chapterViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
