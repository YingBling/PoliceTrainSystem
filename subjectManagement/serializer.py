# -*- coding: utf-8 -*-
# @Time : 2021/7/16 12:27
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : serializer.py
# @Software: PyCharm
# 序列化类
from user.models import User
from .models import Lesson
from rest_framework.serializers import ModelSerializer


# 课程序列化类
class LessonSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # 序列化所有字段
