# -*- coding: utf-8 -*-
# @Time : 2021/10/9 16:10
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : serializers.py
# @Software: PyCharm
from rest_framework.serializers import ModelSerializer
from .models import *


class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
