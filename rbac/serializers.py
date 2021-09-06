# -*- coding: utf-8 -*-
# @Time : 2021/8/27 15:12
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : serializers.py
# @Software: PyCharm
from django.db.models import QuerySet
from rest_framework.serializers import (ModelSerializer, SerializerMethodField,
                                        PrimaryKeyRelatedField,
                                        StringRelatedField, ListSerializer
                                        )
from rbac.models import Permission, User, Role, Dept, Post


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

    class Meta:
        # many=True时使用UserListSerializer
        list_serializer_class = UserListSerializer
        model = User
        # fields:序列化的字段
        fields = ['id', 'username', 'dept', 'post', 'roles', 'password', 'create_time']
        # read_only_fields = ['dept', 'post', 'roles']
        extra_kwargs = {'password': {'write_only': True,
                                     'required': False},
                        'create_time': {'read_only': True}}
        depth = 0

    # 获取用户所有权限
    def get_user_permissions(self, obj):
        # 获取用户所有的角色
        roles = obj.roles.all()
        # 权限集合
        permissions = Permission.objects.none()
        for role in roles:
            # 查询该角色下的所有权限
            permission = role.permissions.all()
            permissions = permissions | permission
        permissions = permissions.distinct()
        # 返回用户的权限序列化JSON
        return PermissionSerializer(permissions, many=True).data
