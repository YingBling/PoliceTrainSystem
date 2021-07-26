# -*- coding: utf-8 -*-
# @Time : 2021/7/17 19:17
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : serializer.py
# @Software: PyCharm
from rest_framework.exceptions import ValidationError
from rest_framework.routers import DefaultRouter
from rest_framework.serializers import ModelSerializer, Serializer, HyperlinkedModelSerializer
import hashlib
from . import views
from .models import User


# 序列化器,不需要重写update和create
class UserSerializer(ModelSerializer):
    def validate_username(self, data):
        if len(data) != 0:
            return data
        else:
            raise ValidationError('用户名不能为空')

    def validate_password(self, data):  # 数据校验函数
        if len(data) >= 8:
            m = hashlib.md5()
            m.update(data.encode())
            data = m.hexdigest()
            return data
        else:
            raise ValidationError('密码长度至少为8位')

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # password设为只写
            'create_time': {'read_only': True},
        }
        # read_only_fields = ['username']
        # write_only_fields = []
        # fields = '__all__'
        # exclude= ('')

    # 局部钩子，主要使用局部钩子
    # def validate_password(self, data):
    # 全局钩子
    # def validate(self, data):
    # # 校验通过则返回数据，否则抛异常
    #     pass
    # def validate_empty_values(self, data):
