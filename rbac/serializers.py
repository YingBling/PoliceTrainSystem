# -*- coding: utf-8 -*-
# @Time : 2021/8/27 15:12
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : serializers.py
# @Software: PyCharm
from django.db.migrations import serializer
from django.db.models import QuerySet
# from rest_framework.fields import CharField
from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer, SerializerMethodField,
                                        PrimaryKeyRelatedField,
                                        StringRelatedField, ListSerializer
                                        )
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from rbac.models import Permission, User, Role, Dept, Post
from django.contrib.auth.hashers import make_password


class PermissionSerializer(ModelSerializer):
    """
    权限序列化器
    """

    class Meta:
        model = Permission
        fields = '__all__'  # 设置序列化字段为所有['title','url']
        # read_only_fields = []  # 设置只读字段
        # extra_kwargs = {}  # 设置每个字段的属性字典，如果字段被显示声明的话，该字典里面的内容将会被忽略


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class DeptSerializer(ModelSerializer):
    """
    Dept序列化器
    """
    parentDept = SerializerMethodField('get_parentDept')

    class Meta:
        model = Dept
        fields = "__all__"
        # depth = 3

    # 获取父部门
    def get_parentDept(self, obj):
        if obj.parentDept:
            return DeptSerializer(obj.parentDept).data
        else:
            return None


class RoleSerializer(ModelSerializer):
    """
    Role序列化器
    """
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = '__all__'


class UserListSerializer(ListSerializer):
    # post请求调用的方法
    def create(self, validated_data):
        return super().create(validated_data)

    # put请求调用的方法
    def update(self, instance, validated_data):
        return [
            self.child.update(attrs, validated_data[i]) for i, attrs in enumerate(instance)
        ]


class UserSerializer(ModelSerializer):
    """
    User序列化器
    roles:一个用户可能对应多个角色
    """
    # 获取用户的所有权限，并将其序列化
    # permissions = SerializerMethodField('get_user_permissions')
    # required=True为反序列化必填
    dept_name = serializers.CharField(source='dept.title', read_only=True)
    post_name = serializers.CharField(source='post.title', read_only=True)
    roles_list = StringRelatedField(source='roles', many=True, read_only=True)

    # create_time = serializers.DateTimeField(read_only=True)

    # roles_list = serializers.SerializerMethodField('get_roles_list')

    class Meta:
        # many=True时使用UserListSerializer
        list_serializer_class = UserListSerializer
        model = User

        # fields:序列化的字段
        fields = ['id', 'username', 'name', 'dept_name', 'post_name',
                  'roles_list', 'password', 'create_time', 'is_active', 'avatar']
        # read_only_fields = ['dept', 'post', 'roles']
        extra_kwargs = {'password': {'write_only': True,
                                     'required': False},
                        'create_time': {'read_only': True}}
        # depth = 0

    # 获取用户所有权限
    def get_user_permissions(self, instance):
        # 获取用户所有的角色
        roles = instance.roles.all()
        # 权限集合
        permissions = Permission.objects.none()
        for role in roles:
            # 查询该角色下的所有权限
            permission = role.permissions.all()
            permissions = permissions | permission
        permissions = permissions.distinct()
        # 返回用户的权限序列化JSON
        return PermissionSerializer(permissions, many=True).data

    def get_roles_list(self, instance):
        roles = instance.roles.all()
        roles_list = Role.objects.none()
        for role in roles:
            roles_list = roles_list | role
        roles_list = roles_list.distinct()
        return RoleSerializer(roles_list, many=True).data

    def validate_password(self, data):
        # 密码长度大于6位
        if len(data) >= 6:
            # 将密码通过sha256加密后存到数据库中
            return make_password(data)


