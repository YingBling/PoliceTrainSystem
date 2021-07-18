# -*- coding: utf-8 -*-
# @Time : 2021/7/17 19:17
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : serializer.py
# @Software: PyCharm
from rest_framework.routers import DefaultRouter
from rest_framework.serializers import ModelSerializer, Serializer, HyperlinkedModelSerializer

from . import views
from .models import User


# 序列化器
class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'phoneNumber', 'group']  # 序列化所有字段
