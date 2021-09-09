# -*- coding: utf-8 -*-
# @Time : 2021/8/30 18:47
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : utils.py.py
# @Software: PyCharm

from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework_simplejwt.views import token_obtain_pair
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


# 登录视图
class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    """
    1.前端输入账号&密码，以POST表单的格式发送到后端
    2.后端验证数据库中账号密码是否正确
    3.如果登录成功，生成JWT以及用户的信息，返回给前端
    4.如果登录失败，返回错误信息
    """

    def post(self, request):
        resp = {
            'code': 200,
            'data': {}
        }
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            resp['msg'] = '登录成功'
            # resp['data'] = UserSerializer(user).data
            refresh = RefreshToken.for_user(user)
            token = {'refresh': str(refresh),
                     'access': str(refresh.access_token)}
            # menu_dict, permission_list = self.get_user_permission(instance=user)
            # resp['data']['menus'] = menu_dict
            # resp['data']['permissions'] = permission_list
            resp['data']['token'] = token
            resp['data']['info'] = UserSerializer(user).data
        else:
            resp['code'] = '400'
            resp['msg'] = '登陆失败，用户名或密码错误！'
        return Response(resp)

    # 获取用户所有权限
    def get_user_permission(self, instance):
        """
        获取用户所有权限，在登陆成功后将权限和菜单返回给前端保存
        :param user:用户实体


        """
        permission_queryset = instance.roles.filter(permissions__url__isnull=False).values('permissions__url',
                                                                                           'permissions__title',
                                                                                           'permissions__menu__id',
                                                                                           'permissions__menu__title',
                                                                                           'permissions__menu__icon').distinct()
        menu_dict = {}  # 菜单与成为菜单的权限
        permission_list = []  # 所有权限

        for row in permission_queryset:
            menu_id = row.get('permissions__menu__id')
            permission_list.append({'permissions__url': row['permissions__url']})
            # 如果有menu_id的话说明是一个菜单,没有的话说明不是菜单
            if not menu_id:
                # 非菜单
                continue
            elif menu_id not in menu_dict:
                # 菜单
                menu_dict[menu_id] = {
                    'title': row['permissions__menu__title'],
                    'icon': row['permissions__menu__icon'],
                    # children:一级菜单下的子菜单列表
                    'children': [
                        {'title': row['permissions__title'],
                         'url': row['permissions__url']}
                    ]
                }
            else:
                permission = {
                    'title': row['permissions__title'],
                    'url': row['permissions__url']
                }
                menu_dict[menu_id]['children'].append(permission)
        # print(menu_dict)
        # print(permission_list)
        return menu_dict, permission_list


# 注销视图
class LogoutView(APIView):
    def get(self, request):
        resp = {
            'code': 200,
            'msg': '用户退出系统'
        }
        user = request.user
        # 修改上次登录时间为注销时间
        user.last_login = timezone.now()
        user.save()  # 这里记得保存一下
        return Response(resp)


# 更新密码视图
class UpdatePasswordView(APIView):
    """

    """

    def post(self, request):
        resp = {
            'code': 200
        }
        username = request.data['username']
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        user = User.objects.filter(username=username).first()
        if user and user.check_password(old_password):
            user.set_password(new_password)
            user.save()  # 这里记得保存一下，不然不会生效
            resp['msg'] = '修改成功'
        else:
            resp['code'] = 400
            resp['msg'] = '修改失败'
        return Response(resp)


class CustomResponse():
    def __init__(self):
        self.status = 100
        self.msg = 'success'

    @property
    def get_dict(self):
        return self.__dict__


class GetUserPermission(APIView):
    #
    pass
