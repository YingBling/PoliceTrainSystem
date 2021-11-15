# -*- coding: utf-8 -*-
# @Time : 2021/8/27 15:12
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : serializers.py
# @Software: PyCharm
# from rest_framework.fields import CharField
from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer, PrimaryKeyRelatedField,
                                        StringRelatedField, ListSerializer
                                        )
from rbac.models import User, Role, Dept, Post, Menu, MenuButton, Button
from django.contrib.auth.hashers import make_password


class ButtonSerializer(ModelSerializer):
    class Meta:
        model = Button
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    parentId = PrimaryKeyRelatedField(source='parent',
                                      label='上级菜单', read_only=True)

    # parent = PrimaryKeyRelatedField(source='parent', write_only=True)

    class Meta:
        model = Menu
        # fields = '__all__'
        exclude = ['parent']


class MenuButtonSerializer(ModelSerializer):
    class Meta:
        model = MenuButton
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class DeptSerializer(ModelSerializer):
    parentID = PrimaryKeyRelatedField(source='parent', queryset=Dept.objects.all(),
                                      label='上级部门', write_only=True, allow_null=True)

    class Meta:
        model = Dept
        fields = ['id', 'title', 'parentID']


class SubDeptSerializer(ModelSerializer):
    # 反向查询，对子部门进行序列化
    children_dept = DeptSerializer(many=True, read_only=True)

    class Meta:
        model = Dept
        fields = ['id', 'title', 'children_dept']


class RoleSerializer(ModelSerializer):
    """
    Role序列化器
    """

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
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    role_list = StringRelatedField(source='role', many=True, read_only=True)

    # create_time = serializers.DateTimeField(read_only=True)

    # roles_list = serializers.SerializerMethodField('get_roles_list')

    class Meta:
        # many=True时使用UserListSerializer
        list_serializer_class = UserListSerializer
        model = User

        # fields:序列化的字段
        fields = ['id', 'username', 'name', 'dept_name', 'post_name',
                  'gender',
                  'role_list', 'password', 'create_time', 'is_active', 'avatar']
        # read_only_fields = ['dept', 'post', 'roles']
        extra_kwargs = {'password': {'write_only': True,
                                     'required': False},
                        'create_time': {'read_only': True}}

    def validate_password(self, data):
        # 密码长度大于6位
        if len(data) >= 6:
            # 将密码通过sha256加密后存到数据库中
            return make_password(data)


class UserInfoSerializer(ModelSerializer):
    roles = StringRelatedField(source='role', many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'name',
                  'roles', 'avatar', 'dept', 'post']
